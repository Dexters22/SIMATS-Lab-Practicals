% stack(Stack) defines a sample stack
stack([apple, banana, cherry, date]).

% pop(Stack, Element, RestStack) pops the top element
pop([Top|Rest], Top, Rest).

% Non-deterministic POP demonstration
pop_demo :-
    stack(Stack),
    pop(Stack, Element, Rest),
    write('Popped Element: '), write(Element), nl,
    write('Remaining Stack: '), write(Rest), nl.
