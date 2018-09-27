% :- module(general,
%     [expelEvent/1,
%     injestEvent/1]
% ).

% Event defintions
% event(_).
% injestEvent(_).
event(B) :- expelEvent(B).
event(B) :- injestEvent(B).


isTime(_).
% justAfter(_time,_event).

% subject(_Event, _subject).
% object(_event,_subject).

% Physical definitions
% inside(_food,_eater,_time).
inside(Food,Eater,T) :-
    isTime(T),
    injestEvent(InjEvent),
    justAfter(T,InjEvent),
    subject(InjEvent, Eater),
    object(InjEvent, Food).


outside(Food,Container,T) :-
    isTime(T),
    expelEvent(InjEvent),
    justAfter(T,InjEvent),
    subject(InjEvent, Container),
    object(InjEvent, Food).

% throw :- 
%     inside(A,B,T),
%     outside(A,B,T).

% partOf(_Part,_Thing).
% ptrans(_).

% move(Thing, Part) :- isPartOf(Part,Thing), ptransEvent(Part).



