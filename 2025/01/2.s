# Advent of Code 2025 - Day 1: Secret Entrance (Part Two)
# Assembly solution (ARM64, macOS)
# Counts how many times the dial points at 0 during rotations

.section __DATA,__data
filename:
    .asciz "../data/1.txt"
mode:
    .asciz "r"
format:
    .asciz "%lld\n"

.section __BSS,__bss
buffer:
    .space 256

.section __TEXT,__text
.globl _main
.align 2

_main:
    # Prologue
    stp x29, x30, [sp, #-16]!
    mov x29, sp
    sub sp, sp, #32
    
    # Initialize: position = 50, count = 0
    mov x19, #50
    mov x20, #0
    
    # Open file
    adrp x0, filename@PAGE
    add x0, x0, filename@PAGEOFF
    adrp x1, mode@PAGE
    add x1, x1, mode@PAGEOFF
    bl _fopen
    cbz x0, error_exit
    mov x21, x0
    
read_loop:
    # Read a line from file
    adrp x0, buffer@PAGE
    add x0, x0, buffer@PAGEOFF
    mov x1, #256
    mov x2, x21
    bl _fgets
    cbz x0, file_done
    
    # Parse the line: L/R followed by number
    adrp x22, buffer@PAGE
    add x22, x22, buffer@PAGEOFF
    ldrb w23, [x22]
    
    cmp w23, #76
    b.eq parse_left
    cmp w23, #82
    b.eq parse_right
    b read_loop
    
parse_left:
    # Skip 'L' and parse number
    add x0, x22, #1
    bl _atoi
    sxtw x0, w0
    neg x0, x0
    b apply_rotation
    
parse_right:
    # Skip 'R' and parse number
    add x0, x22, #1
    bl _atoi
    sxtw x0, w0
    
apply_rotation:
    # x0 = rotation amount (can be positive or negative)
    # x19 = current position
    # x20 = total count
    
    # Store rotation in x24, and get absolute value in x25
    mov x24, x0
    cmp x0, #0
    b.ge rotation_positive
    neg x25, x0
    b rotation_abs_done
    
rotation_positive:
    mov x25, x0
    
rotation_abs_done:
    # x25 = absolute value of rotation
    # x24 = rotation (signed)
    # x19 = current position
    
    # Step through each position in the rotation
    mov x26, #0
    mov x27, x19
    
step_loop:
    cmp x26, x25
    b.ge step_done
    
    # Move one step
    cmp x24, #0
    b.gt step_right
    b.lt step_left
    b step_done
    
step_right:
    add x27, x27, #1
    b modulo_check
    
step_left:
    sub x27, x27, #1
    b modulo_check
    
modulo_check:
    # Normalize position to [0, 99]
modulo_neg:
    cmp x27, #0
    b.ge modulo_pos
    add x27, x27, #100
    b modulo_neg
    
modulo_pos:
    cmp x27, #99
    b.le check_zero_step
    sub x27, x27, #100
    b modulo_pos
    
check_zero_step:
    # Check if current position is 0
    cmp x27, #0
    b.ne step_continue
    add x20, x20, #1
    
step_continue:
    add x26, x26, #1
    b step_loop
    
step_done:
    # Update position to final value
    mov x19, x27
    b read_loop
    
file_done:
    # Close file
    mov x0, x21
    bl _fclose
    
    # Print result
    str x20, [sp]
    adrp x0, format@PAGE
    add x0, x0, format@PAGEOFF
    ldr x1, [sp]
    bl _printf
    
    # Exit
    mov x0, #0
    bl _exit
    
error_exit:
    mov x0, #1
    bl _exit

