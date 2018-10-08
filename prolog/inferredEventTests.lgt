:- logtalk_load(condep, [reload(skip)]).

:- object(inferTests, extends(condep)).

	:- discontiguous(afterEvent/2).
	:- discontiguous(beforeEvent/2).
	:- discontiguous(actorOfEvent/2).
	:- discontiguous(objectOfEvent/2).
	:- discontiguous(isEvent/1).
	

	betweenEvents(A,B,C) :- ^^betweenEvents(A,B,C).
	afterEvent(A,B) :- ^^afterEvent(A,B).
	beforeEvent(A,B) :- ^^beforeEvent(A,B).
	movingAwayFrom(A, B, C) :- ^^movingAwayFrom(A, B, C).
	actorOfEvent(A,B) :- ^^actorOfEvent(A,B).
	objectOfEvent(A,B) :- ^^objectOfEvent(A,B).
	missingEventBetween(A,B) :- ^^missingEventBetween(A,B).
	isEvent(A) :- ^^isEvent(A).

	expelEvent(exEvent).
	injestEvent(injEvent).

	actorOfEvent(exEvent, mass).
	objectOfEvent(exEvent, obj).
	actorOfEvent(injEvent, mass).
	objectOfEvent(injEvent, obj).

	beforeEvent(exEvent, injEvent).

	isEvent(sillyEvent).
	beforeEvent(sillyEvent, injEvent).
	afterEvent(sillyEvent, exEvent).
	

:- end_object.