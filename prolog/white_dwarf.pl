myStar.

% read_term_from_atom('2.765E30', cLimit, []).
% cLimit is 3.

overChandrasekharLimit(Obj) :-
    mass(Obj, ObjMass),
    ObjMass > 3;

% mass(Obj, ObjMass).

isWhiteDwarf(Star) :-
    mass(Star, Mass),
    dif(true,overChandrasekharLimit(Mass)).