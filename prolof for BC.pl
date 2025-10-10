% Facts
parent(mary, john).
parent(susan, mary).
parent(tom, susan).
parent(alice, tom).

% Rules
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).

% Example query:
% ?- ancestor(mary, tom).
