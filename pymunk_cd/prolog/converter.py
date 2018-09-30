from ..cd_event import CDEvent
from pymunk_cd.primitives import Primitives

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
    header = ':- object(state, extends(condep)).'

    footer = ':- end_object.'

    output = header + '\n' + '\n'.join(predicates) + '\n'+footer
    return output