% isPartOf(_Part,_Thing).
% ptrans(_).

move(Thing, Part) :- isPartOf(Part,Thing), ptrans(Part).

collapse(Thing, Radius) :- .