% Advent of Code 2025 - Day 2: Gift Shop
% SWI Prolog solution
% Finds invalid product IDs (numbers made of a sequence repeated twice)

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

% Find invalid IDs in a range by generating patterns
% An invalid number is formed by repeating a pattern twice
invalid_ids_in_range(Start-End, InvalidIDs) :-
    End >= Start,
    % Calculate the square root bounds to limit pattern search
    % If pattern P creates number PP, we need Start <= PP <= End
    % So we can limit P to roughly sqrt(Start) to sqrt(End)
    StartSqrt is integer(sqrt(Start)),
    EndSqrt is integer(sqrt(End)) + 1,
    findall(Num, (
        between(1, EndSqrt, PatternNum),
        number_string(PatternNum, PatternStr),
        string_concat(PatternStr, PatternStr, CombinedStr),
        number_string(Num, CombinedStr),
        Num >= Start,
        Num =< End
    ), InvalidIDs).

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
    sum_list(AllInvalid, Sum),
    format('Invalid IDs: ~w~n', [AllInvalid]),
    format('Sum: ~d~n', [Sum]).

% Main entry point
main :-
    solve(Sum),
    format('~d~n', [Sum]).
