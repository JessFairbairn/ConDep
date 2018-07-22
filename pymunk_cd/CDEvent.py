from .EventType import EventType

class CDEvent:
    def __init__(self, subject:str, event_type:EventType, event_object = None):
        "Takes CDEntity and event type as arguments"
        self.subject = subject
        self.event_type = event_type

        # 'Object' in logical sense
        self.event_object = event_object
        self.direction = None
        
        return


    def __str__(self):
        if(self.event_object):
            if(hasattr(self.event_object, 'name')):
                object_str = self.event_object.name
            else:
                object_str = str(type(self.event_object))
        else:
            object_str = ''
        return self.subject.name + " " + self.event_type.name + "s " + object_str
