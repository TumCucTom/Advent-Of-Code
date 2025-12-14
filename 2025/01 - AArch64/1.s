
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
    # atoi returns int in w0, sign-extend to x0, then negate
    sxtw x0, w0
    neg x0, x0
    b apply_rotation
    
parse_right:
    # Skip 'R' and parse number
    add x0, x22, #1
    bl _atoi
    # atoi returns int in w0, sign-extend to x0
    sxtw x0, w0
    
apply_rotation:
    # Apply rotation: position = (position + rotation) mod 100
    add x19, x19, x0
    
    # Handle modulo 100 (circular dial)
    # Normalize to [0, 99] range
modulo_neg:
    cmp x19, #0
    b.ge modulo_pos
    add x19, x19, #100
    b modulo_neg
    
modulo_pos:
    cmp x19, #99
    b.le check_zero
    sub x19, x19, #100
    b modulo_pos
    
check_zero:
    # Check if position is 0
    cmp x19, #0
    b.ne read_loop
    # Increment count if position is 0
    add x20, x20, #1
    b read_loop
    
file_done:
    # Close file
    mov x0, x21
    bl _fclose
    
    # Print result
    # Store count on stack (16-byte aligned)
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
