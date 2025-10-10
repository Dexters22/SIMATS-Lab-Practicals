% Prolog program to store and retrieve Name and Date of Birth

% Facts: Database of names with their DOB
dob(john, 15, march, 1998).
dob(mary, 22, july, 2000).
dob(alex, 5, january, 1995).
dob(sophia, 10, december, 2002).
dob(david, 3, june, 1999).

% Rule to display DOB of a given person
show_dob(Name) :-
    dob(Name, Day, Month, Year),
    write(Name), write(' was born on '),
    write(Day), write(' '), write(Month), write(' '), write(Year), write('.'), nl.

% Rule for unknown names
show_dob(Name) :-
    \+ dob(Name, _, _, _),
    write('No record found for '), write(Name), write('.'), nl.
