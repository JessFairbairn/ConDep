from ..cd_event import CDEvent
from condep.primitives import Primitives

def convert_to_prolog(event:CDEvent):
    'Returns an array of prolog predicates describing the event'

    predicates = []

    eventName = 'eve' + str(id(event))

    pred = '' + event.primitive.name.lower() + 'Event(' + eventName + ').'
    predicates.append(pred)

    if event.subject:
        actorPred = 'actorOfEvent(' + event.subject + ',' + eventName + ').'
        predicates.append(actorPred)

    if event.event_object:
        objectPred = 'objectOfEvent(' + event.event_object + ',' + eventName + ').'
        predicates.append(objectPred)

    return predicates

def output_logtalk_file(predicates: list):
    header = ''':- object(state, extends(condep)).
:- discontiguous(actorOfEvent/2).
:- discontiguous(objectOfEvent/2).
:- discontiguous(justBefore/2).
:- discontiguous(justAfter/2).

actorOfEvent(A,B) :- ^^actorOfEvent(A,B).
objectOfEvent(A,B) :- ^^objectOfEvent(A,B).
justBefore(A,B) :- ^^justBefore(A,B).
justAfter(A,B) :- ^^justAfter(A,B).

'''

    footer = '\n:- end_object.'

    output = header + '\n' + '\n'.join(predicates) + '\n'+footer
    return output