:- object(condep).

:- public(
    [
    inside/3, outside/3,
    isTime/1, injestEvent/1, expelEvent/1, isEvent/1,
    justBefore/2, justAfter/2,
    actorOfEvent/2, objectOfEvent/2
    ]
).

% Event defintions
% event(_).
% injestEvent(_A).
expelEvent(_A).
% :- multifile(expelEvent).

% justAfter(Time,Event).
% isEvent(_).
isEvent(B) :- ::expelEvent(B).
isEvent(B) :- ::injestEvent(B).


isTime(Time) :-
    ::justAfter(Time,Event),
    ::isEvent(Event).

isTime(Time) :-
    ::justBefore(Time,Event),
    ::isEvent(Event).

actorOfEvent(_Event, _ActorOfEvent).
objectOfEvent(_Event,_ActorOfEvent).

% Physical definitions
inside(Food,Eater,T) :-
    ::isTime(T),
    ::injestEvent(InjEvent),
    ::justAfter(T,InjEvent),
    ::actorOfEvent(InjEvent, Eater),
    ::objectOfEvent(InjEvent, Food).

inside(Food,Eater,T) :-
    ::isTime(T),
    ::expelEvent(InjEvent),
    ::justBefore(T,InjEvent),
    ::actorOfEvent(InjEvent, Eater),
    ::objectOfEvent(InjEvent, Food).


outside(Food,Container,T) :-
    ::isTime(T),
    ::expelEvent(InjEvent),
    ::justAfter(T,InjEvent),
    ::actorOfEvent(InjEvent, Container),
    ::objectOfEvent(InjEvent, Food).

outside(Food,Container,T) :-
    ::isTime(T),
    ::injestEvent(InjEvent),
    ::justBefore(T,InjEvent),
    ::actorOfEvent(InjEvent, Container),
    ::objectOfEvent(InjEvent, Food).
 
% partOf(_Part,_Thing).
% ptrans(_).

% move(Thing, Part) :- isPartOf(Part,Thing), ptransEvent(Part).
:- end_object.