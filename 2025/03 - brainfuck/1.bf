>>>>>>>>>>>>>>>>>>>
Memory layout:
0-9: work area
10-109: digit storage (up to 100 per line)
110: digit count
111: max tens
112: max after (for current position)
113: line max value
114-116: sum (3 bytes)
200+: output buffer

Initialize and read first char
,

Main loop while not EOF
[
  Subtract 10 to check newline
  ----------

  If not zero then digit
  [
    Add 10 back subtract 48 for digit value
    ++++++++++
    ------------------------------------------------

    Save digit to storage (cell 10+count)
    Go to count at 110
    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    >>>>>>>>>>

    Get count add 10 to find storage position
    [->+>+<<]>>[-<<+>>]
    ++++++++++
    [-<+>]<

    Go to that position and store
    [->+<]

    Back to start
    <[<]

    Increment count
    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    >>>>>>>>>>+

    Back to cell 0 and read next
    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    <<<<<<<<<<

    Clear and read
    [-],----------
  ]

  Was newline process line
  +[
    -
    Find max pair for this line
    
    Go to digit storage
    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    >>>>>>>>>>

    For each digit find max after it
    [
      Copy current digit as tens candidate
      [->+>+<<]>>[-<<+>>]

      Save position scan right for max
      >[
        Compare with running max
        [->+>+<<]>>[[-]<<+>>]<
        [[-<+>]>]<
        >
      ]<

      Calculate 10*tens + max_after
      Multiply tens by 10
      [-<++++++++++>]

      Add max after
      >[-<+>]<

      Compare with line max update if bigger
      [->+>+<<]>>
      [-<<+>>]
      <<[->>-<<]>>
      [[-]<<[-]>>]
      <<

      Move to next digit
      >
    ]

    Add line max to sum
    Go to sum at 114
    >>>>
    [-<+<+>>]<<[->>+<<]>
    Add with carry
    [
      -<+>
      <[->+<[->+<[->+<]]]>
    ]

    Clear digits and count
    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    <<<<<<<<<<<<<<
    [[-]>]
    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    <<<<<<<<<<<<<<

  ]

  Read next char
  [-],
]

Output sum as decimal
Go to sum
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>>>>

Division loop for decimal output
Get sum value
[->+<]>

Store digits in reverse
>>>>>

[
  Divide by 10
  >++++++++++<
  [->-[>+>>]>[+[-<+>]>+>>]<<<<<]

  Remainder plus 48 is digit
  >>>>++++++++++++++++++++++++++++++++++++++++++++++++

  Store move to next
  [->>+<<]>>

  Check quotient continue if nonzero
  <<<<<<<
  [->+<]>[-<+>]
  <
]

Print digits backwards
>>>[.>>>]
