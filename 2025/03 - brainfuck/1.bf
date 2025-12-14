Cell 0: input
Cell 1: flag
Cells 2 to 101: digit storage (max 100 digits per line)
Cell 102: digit count
Cell 103: outer index i
Cell 104: inner index j
Cell 105: tens digit value
Cell 106: units digit value
Cell 107: current pair value
Cell 108: line max
Cell 109: temp
Cells 110 to 112: sum (3 bytes for values up to 16M)
Cells 120+: output digits

Initialize
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[-]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

Read first character
,

Main input loop
[
  Check for newline (ASCII 10) vs digit (ASCII 49 to 57)
  Copy char to cell 1 for testing
  [->+>+<<]>>[-<<+>>]<<
  
  >
  ----------  Subtract 10
  
  [
    Not newline so process as digit
    Restore by adding 10 then subtract 48 for value
    ++++++++++
    ------------------------------------------------
    
    Now cell has digit value 1 to 9
    Move to storage array at position [digit count + 2]
    
    Increment count in cell 102 and store digit
    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    <<<<<<<<<<<<
    
    At cell 102 increment count
    +
    
    Go to position [count + 1] in storage starting at cell 2
    [>>]+<<
    
    Store digit value from cell 1
    Back to input position and read next
    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    >>>>>>>>>>>>
    
    [-]
    ,
    [->+>+<<]>>[-<<+>>]<<
    >----------
  ]
  
  If was newline cell is now 0
  [<+>[-]]
  <
  
  [
    Process line: find max pair
    
    Navigate to storage start cell 2
    <[-]>[-]
    
    Get count from cell 102
    For i from 0 to count minus 2
      For j from i plus 1 to count minus 1
        Calculate 10 times digit[i] plus digit[j]
        Compare with max update if larger
    
    Add final max to sum cells 110 to 112
    Handle carry: if cell 110 > 255 carry to 111 etc
    
    Clear storage cells 2 to 101 and count
    Reset for next line
    -
  ]
  
  Read next character  
  >[-]<
  ,
]

End of input convert sum to decimal and print

Navigate to sum at cells 110 to 112
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
<<<<<<<<<

Build decimal digits via repeated division by 10

[
  While sum not zero
  
  Divide by 10 store remainder plus 48 as ASCII digit
  
  >++++++++++  divisor in next cell
  
  Division algorithm
  [->-[>+>>]>[+[-<+>]>+>>]<<<<<]
  
  Remainder is digit add 48
  >>>>
  ++++++++++++++++++++++++++++++++++++++++++++++++
  
  Store digit move to next output position
  [->+<]>
  
  Move quotient back check if zero
  <<<<<
  [->+<]>
  [-<+>]<
]

Print digits in reverse
Navigate to last digit and print backwards
>>[>]<[.<]

Done
