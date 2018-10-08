:- object(condep).

:- public(
    [
    inside/3, outside/3,
    isTime/1, injestEvent/1, expelEvent/1, isEvent/1,
    betweenEvents/3, beforeEvent/2, afterEvent/2,
    missingEventBetween/2,
    justBefore/2, justAfter/2,
    actorOfEvent/2, objectOfEvent/2,
    movingAwayFrom/3
    ]
).

%%% Event defintions %%%
isEvent(B) :- ::expelEvent(B).
isEvent(B) :- ::injestEvent(B).

justBefore(_Time,_Event).
justAfter(_Time,_Event).

isTime(Time) :-
    ::justAfter(Time,Event),
    ::isEvent(Event).

isTime(Time) :-
    ::justBefore(Time,Event),
    ::isEvent(Event).

actorOfEvent(_ActorOfEvent,_Event).
objectOfEvent(_ObjectOfEvent, _Event).


betweenEvents(EventBetween, Event1, Event2) :-
    ::isEvent(EventBetween);isTime(EventBetween),
    ::afterEvent(EventBetween,Event1),
    ::beforeEvent(EventBetween, Event2).

afterEvent(LaterTime, JustAfter) :-
    not(isEvent(JustAfter)),
    ::isTime(JustAfter),
    ::justAfter(JustAfter, Event),
    ::isEvent(Event),
    afterEvent(LaterTime, Event).

% if an object is moving away from something, and later moving towards it, then there was an event inbetween
missingEventBetween(ExpEvent, InjEvent) :-
    % ::isEvent(ExpEvent),
    ::injestEvent(InjEvent),
    ::actorOfEvent(Mass, InjEvent),
    ::objectOfEvent(Obj, InjEvent),

    ::justAfter(T1, ExpEvent),
    ::movingAwayFrom(Obj, Mass, T1),
    ::beforeEvent(T1,InjEvent) ; ::afterEvent(InjEvent, T1).
    % not((::isEvent(MiddleEvent),::betweenEvents(MiddleEvent, T1, InjEvent))).

    


%%% Physical definitions %%%
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

%%%% Relative Movement %%%
movingAwayFrom(Actor, MovingFrom, T) :-
        ::expelEvent(ExpEvent),
        ::justAfter(T,ExpEvent),
        ::actorOfEvent(MovingFrom, ExpEvent),
        ::objectOfEvent(Actor, ExpEvent).
        
:- end_object.