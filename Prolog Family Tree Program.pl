% Family Tree Program

% Facts
male(john). male(david). male(mike). male(ron).
female(lisa). female(susan). female(anna). female(kate).

father(john, david). father(john, susan).
father(david, mike). father(david, anna).

mother(lisa, david). mother(lisa, susan).
mother(susan, mike). mother(susan, anna).

% Rules
parent(X, Y) :- father(X, Y).
parent(X, Y) :- mother(X, Y).

grandparent(X, Y) :- parent(X, Z), parent(Z, Y).

sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

brother(X, Y) :- sibling(X, Y), male(X).
sister(X, Y) :- sibling(X, Y), female(X).
