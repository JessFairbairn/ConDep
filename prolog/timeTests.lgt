:- object(timeTests, extends(condep)).

	:- discontiguous(afterEvent/2).
	:- discontiguous(beforeEvent/2).

	betweenEvents(A,B,C) :- ^^betweenEvents(A,B,C).
	afterEvent(A,B) :- ^^afterEvent(A,B).
	beforeEvent(A,B) :- ^^beforeEvent(A,B).
	movingAwayFrom(A, B, C) :- ^^movingAwayFrom(A, B, C).

	afterEvent(newEvent,eventA).
	beforeEvent(newEvent,eventB).

:- end_object.