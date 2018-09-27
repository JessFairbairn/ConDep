ensure_loaded('general.pl').

% :- discontiguous(subject).
% :- discontiguous(object).

expelEvent(myEvent).

subject(myEvent, blackHole).
object(myEvent, barbara).

% isTime(timeAfterEvent).
justAfter(timeAfterEvent, myEvent).

