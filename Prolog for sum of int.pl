% Prolog program to find the sum of integers from 1 to N

% Base case
sum(1, 1).

% Recursive case
sum(N, Result) :-
    N > 1,
    N1 is N - 1,
    sum(N1, PartialSum),
    Result is PartialSum + N.
