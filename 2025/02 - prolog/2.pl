% Advent of Code 2025 - Day 2: Gift Shop (Part Two)
% SWI Prolog solution - Precise bounds optimization
% Finds invalid product IDs (numbers made of a sequence repeated at least twice)

% Read input from file
read_input(String) :-
    read_file_to_string('../data/2.txt', String, []).

% Parse ranges from input string
parse_ranges(String, Ranges) :-
    split_string(String, ",", "", RangeStrings),
    maplist(parse_range, RangeStrings, Ranges).

parse_range(RangeString, Start-End) :-
    split_string(RangeString, "-", "", [StartStr, EndStr]),
    number_string(Start, StartStr),
    number_string(End, EndStr).

% Calculate the multiplier for pattern P of length L repeated R times
% Result = P * (10^(L*(R-1)) + 10^(L*(R-2)) + ... + 10^L + 1)
% This is a geometric series: (10^(L*R) - 1) / (10^L - 1)
multiplier(PatternLen, RepeatCount, Mult) :-
    Base is 10^PatternLen,
    Mult is (Base^RepeatCount - 1) // (Base - 1).

% Find invalid IDs in a range with precise pattern bounds
invalid_ids_in_range(Start-End, InvalidIDs) :-
    End >= Start,
    number_string(Start, StartStr),
    number_string(End, EndStr),
    string_length(StartStr, StartLen),
    string_length(EndStr, EndLen),
    findall(Num, (
        % Try each possible result length
        between(StartLen, EndLen, ResultLen),
        ResultLen >= 2,
        % Try each divisor of ResultLen as pattern length
        between(1, ResultLen, PatternLen),
        ResultLen mod PatternLen =:= 0,
        RepeatCount is ResultLen // PatternLen,
        RepeatCount >= 2,
        % Calculate the multiplier for this (PatternLen, RepeatCount) pair
        multiplier(PatternLen, RepeatCount, Mult),
        % Calculate precise pattern bounds from range bounds
        MinPatternVal is 10^(PatternLen - 1),
        MaxPatternVal is 10^PatternLen - 1,
        % From Start <= Pattern * Mult <= End, we get:
        % Start/Mult <= Pattern <= End/Mult
        MinPatternFromRange is (Start + Mult - 1) // Mult,  % ceiling
        MaxPatternFromRange is End // Mult,  % floor
        % Intersect with valid pattern range
        ActualMinPattern is max(MinPatternVal, MinPatternFromRange),
        ActualMaxPattern is min(MaxPatternVal, MaxPatternFromRange),
        ActualMinPattern =< ActualMaxPattern,
        % Now iterate only over valid patterns
        between(ActualMinPattern, ActualMaxPattern, PatternNum),
        % Verify pattern has correct length (no leading zeros issue)
        number_string(PatternNum, PatternStr),
        string_length(PatternStr, PatternLen),
        % Calculate result
        Num is PatternNum * Mult,
        % Verify result is in range (should be, but double-check)
        Num >= Start,
        Num =< End
    ), InvalidIDsList),
    sort(InvalidIDsList, InvalidIDs).

% Sum invalid IDs in a range
sum_invalid_in_range(Start-End, Sum) :-
    invalid_ids_in_range(Start-End, InvalidIDs),
    sum_list(InvalidIDs, Sum).

% Main predicate: solve the problem
solve(Sum) :-
    read_input(String),
    parse_ranges(String, Ranges),
    maplist(sum_invalid_in_range, Ranges, Sums),
    sum_list(Sums, Sum).

% Test with example
test_example :-
    Ranges = [11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
               1698522-1698528,446443-446449,38593856-38593862,565653-565659,
               824824821-824824827,2121212118-2121212124],
    maplist(invalid_ids_in_range, Ranges, InvalidLists),
    flatten(InvalidLists, AllInvalid),
    sort(AllInvalid, SortedInvalid),
    sum_list(SortedInvalid, Sum),
    format('Invalid IDs: ~w~n', [SortedInvalid]),
    format('Expected: [11,22,99,111,999,1010,1188511885,222222,446446,38593859,565656,824824824,2121212121]~n'),
    format('Sum: ~d~n', [Sum]),
    format('Expected sum: 4174379265~n').

% Main entry point
main :-
    solve(Sum),
    format('~d~n', [Sum]).
