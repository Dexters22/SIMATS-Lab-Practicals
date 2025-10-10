% Prolog program to implement Towers of Hanoi

% Base case: Move one disk directly
towers_of_hanoi(1, Source, Destination, _) :-
    write('Move disk from '), write(Source), write(' to '), write(Destination), nl.

% Recursive case
towers_of_hanoi(N, Source, Destination, Auxiliary) :-
    N > 1,
    M is N - 1,
    towers_of_hanoi(M, Source, Auxiliary, Destination),
    write('Move disk from '), write(Source), write(' to '), write(Destination), nl,
    towers_of_hanoi(M, Auxiliary, Destination, Source).
