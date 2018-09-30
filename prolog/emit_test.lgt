% :- include(condep).

:- object(state, extends(condep)).

expelEvent(myEvent).

actorOfEvent(myEvent, blackHole).
objectOfEvent(myEvent, barbara).

justBefore(timeBeforeEvent, myEvent).
justAfter(timeAfterEvent, myEvent).


inside(bill, box, t).

inside(A,B,C) :- ^^inside(A,B,C).
		% outside(bill, box, t).

:- end_object.