from .EventType import EventType

class CDEvent:
    def __init__(self, subject:str, event_type:EventType, object = None):
        "Takes CDEntity and event type as arguments"
        self.subject = subject
        self.event_type = event_type

        # 'Object' in logical sense
        self.object = object
        self.direction = None
        
        return


    def __str__(self):
        if(self.object):
            if(hasattr(self.object, 'name')):
                object_str = self.object.name
            else:
                object_str = str(type(self.object))
        else:
            object_str = ''
        return self.subject.name + " " + self.event_type.name + "s " + object_str
