from collections import namedtuple
from dataclasses import dataclass, field
from typing import Optional

# Represents a pattern of bits with a mask and a value
class BitPattern(namedtuple("BitPattern", ["mask", "pattern"])):
    def merge(self, other: "BitPattern") -> Optional["BitPattern"]:
        """
        Attempts to merge two BitPatterns by checking compatibility.
        If compatible, returns a new BitPattern; otherwise, returns None.
        """
        common_mask = self.mask & other.mask
        if (self.pattern & common_mask) == (other.pattern & common_mask):
            return BitPattern(self.mask | other.mask, self.pattern | other.pattern)
        return None

    def __lshift__(self, shift_by: int):
        """Shifts the bit pattern and mask to the left by the specified number of bits."""
        return BitPattern(self.mask << shift_by, self.pattern << shift_by)

    def __repr__(self):
        """
        Generates a string representation where constrained bits are 0/1,
        and unconstrained bits are represented as '.'.
        """
        mask_bin = f"{self.mask:010b}"
        pattern_bin = f"{self.pattern:0{len(mask_bin)}b}"
        return "BitPattern(" + "".join(
            "." if m == "0" else p for m, p in zip(mask_bin, pattern_bin)
        ) + ")"

@dataclass
class VirtualMachine:
    program: list[int]  # Sequence of operations and operands
    register_a: int  # Register A
    register_b: int  # Register B
    register_c: int  # Register C
    pointer: int = 0  # Current position in the program
    output: list[int] = field(default_factory=list, init=False)  # Output log

    def __post_init__(self):
        """Initialize the operation methods for the virtual machine."""
        self.operations = [
            self.shift_a, self.xor_b_with_value, self.store_b_remainder,
            self.jump_if_a_nonzero, self.xor_b_with_c, self.output_value,
            self.shift_b, self.shift_c
        ]

    def __repr__(self):
        """
        Provides a representation of the program with the current pointer position.
        """
        program_repr = [
            f"{'>' if self.pointer == i else ' '} {self.operations[opcode].__name__} {operand}"
            for i, (opcode, operand) in enumerate(zip(self.program[::2], self.program[1::2]))
        ]
        return (
            f"{' ; '.join(program_repr)}\n"
            f"   {self.register_a=}, {self.register_b=}, {self.register_c=}, {self.output=}"
        )

    def resolve_operand(self, operand: int) -> int:
        """
        Resolves the value of an operand based on its encoding.
        Values 4, 5, and 6 correspond to registers A, B, and C, respectively.
        """
        if operand < 0 or operand > 6:
            raise ValueError(f"Invalid operand {operand}")
        return [operand, operand, operand, operand, self.register_a, self.register_b, self.register_c][operand]

    def right_shift_a(self, operand: int) -> int:
        """Performs a right shift operation on register A by the resolved operand."""
        return self.register_a >> self.resolve_operand(operand)

    def run(self, initial_a: Optional[int] = None, debug: bool = False) -> bool:
        """
        Executes the program, optionally starting with an initial value for register A.
        Outputs debug information if requested.

        Returns True if the output matches the program itself, False otherwise.
        """
        self.output.clear()
        self.pointer = 0
        saved_registers = (self.register_a, self.register_b, self.register_c)

        if initial_a is not None:
            self.register_a = initial_a

        while self.pointer < len(self.program):
            next_pointer = self.operations[self.program[self.pointer]](self.program[self.pointer + 1])
            self.pointer = next_pointer if next_pointer is not None else self.pointer + 2

            if debug:
                print(self)

        self.register_a, self.register_b, self.register_c = saved_registers
        return self.output == self.program

    # Operations

    def shift_a(self, operand: int):
        self.register_a = self.right_shift_a(operand)

    def shift_b(self, operand: int):
        self.register_b = self.right_shift_a(operand)

    def shift_c(self, operand: int):
        self.register_c = self.right_shift_a(operand)

    def xor_b_with_value(self, operand: int):
        self.register_b ^= operand

    def store_b_remainder(self, operand: int):
        self.register_b = self.resolve_operand(operand) % 8

    def jump_if_a_nonzero(self, operand: int):
        if self.register_a != 0:
            return operand

    def xor_b_with_c(self, operand: int):
        self.register_b ^= self.register_c

    def output_value(self, operand: int):
        self.output.append(self.resolve_operand(operand) % 8)

def generate_base_patterns(vm: VirtualMachine) -> list[set[BitPattern]]:
    """
    Generates base bit patterns from the program in the virtual machine.

    Each number in the program is associated with a set of BitPatterns that
    constrain the possible initial state of register A.
    """
    k1, k2 = vm.program[3], vm.program[7]  # Magic constants from the input program
    patterns = []

    for digit in range(8):
        digit_patterns = set()
        for temp_b in range(8):
            b_pattern = BitPattern(7, temp_b ^ k1 ^ k2)
            c_pattern = BitPattern(7, digit ^ temp_b) << (temp_b ^ k2)
            merged = b_pattern.merge(c_pattern)
            if merged:
                digit_patterns.add(merged)
        patterns.append(digit_patterns)

    return patterns

def find_minimum_quine_seed(vm: VirtualMachine) -> int:
    """
    Finds the smallest seed for register A such that the program is a quine.
    """
    base_patterns = generate_base_patterns(vm)

    candidates = set(base_patterns[vm.program[0]])
    for i, target_digit in enumerate(vm.program[1:], start=1):
        shifted_patterns = {p << (3 * i) for p in base_patterns[target_digit]}
        candidates = {
            merged for existing_pattern in candidates for new_pattern in shifted_patterns
            if (merged := existing_pattern.merge(new_pattern))
        }

        if not candidates:
            raise ValueError("This program cannot generate itself")

    return min(p.pattern for p in candidates)

def load_vm_data(file_path: str) -> VirtualMachine:
    """Loads program and initial register values from a file."""
    with open(file_path, "r") as file:
        register_a = int(file.readline()[12:])
        register_b = int(file.readline()[12:])
        register_c = int(file.readline()[12:])
        file.readline()  # Skip blank line
        program = list(map(int, file.readline()[9:].split(",")))

    return VirtualMachine(program=program, register_a=register_a, register_b=register_b, register_c=register_c)

def main():
    vm = load_vm_data("../data/17.txt")

    # Part 1: Run the program and print its output
    vm.run(debug=True)
    print("Output:", "".join(map(str, vm.output)))

    # Part 2: Find and print the minimum quine seed
    print(f"Minimum quine seed: {find_minimum_quine_seed(vm)}")

if __name__ == "__main__":
    main()
