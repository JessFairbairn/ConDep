:- object(state, extends(condep)).

:- discontiguous(actorOfEvent/2).
:- discontiguous(objectOfEvent/2).
:- discontiguous(justBefore/2).
:- discontiguous(justAfter/2).

actorOfEvent(A,B) :- ^^actorOfEvent(A,B).
objectOfEvent(A,B) :- ^^objectOfEvent(A,B).
justBefore(A,B) :- ^^justBefore(A,B).
justAfter(A,B) :- ^^justAfter(A,B).

expelEvent(myEvent).

actorOfEvent(myEvent, blackHole).
objectOfEvent(myEvent, barbara).

justBefore(timeBeforeEvent, myEvent).

justAfter(timeAfterEvent, myEvent).


% inside(bill, box, t).

% inside(A,B,C) :- ^^inside(A,B,C).

:- end_object.