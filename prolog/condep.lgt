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

actorOfEvent(_ActorOfEvent,_Event).
objectOfEvent(_ObjectOfEvent, _Event).

% Physical definitions
inside(Food,Eater,T) :-
    ::isTime(T),
    ::injestEvent(InjEvent),
    ::justAfter(T,InjEvent),
    ::actorOfEvent(Eater, InjEvent),
    ::objectOfEvent(Food, InjEvent).

inside(Food,Eater,T) :-
    ::isTime(T),
    ::expelEvent(InjEvent),
    ::justBefore(T,InjEvent),
    ::actorOfEvent(Eater, InjEvent),
    ::objectOfEvent(Food, InjEvent).


outside(Food,Container,T) :-
    ::isTime(T),
    ::expelEvent(InjEvent),
    ::justAfter(T,InjEvent),
    ::actorOfEvent(Container, InjEvent),
    ::objectOfEvent(Food, InjEvent).

outside(Food,Container,T) :-
    ::isTime(T),
    ::injestEvent(InjEvent),
    ::justBefore(T,InjEvent),
    ::actorOfEvent(Container, InjEvent),
    ::objectOfEvent(Food, InjEvent).
 
% partOf(_Part,_Thing).
% ptrans(_).

% move(Thing, Part) :- isPartOf(Part,Thing), ptransEvent(Part).
:- end_object.