% Facts about animal features
has_feathers(tweety).
can_fly(tweety).
lays_eggs(tweety).
has_fur(tom).
can_fly(tom).

% Rules to classify animals
bird(X) :- has_feathers(X), lays_eggs(X).
mammal(X) :- has_fur(X), \+ lays_eggs(X).

% Query examples:
% ?- bird(tweety).
% ?- mammal(tom).
