class CDEvent:
    def __init__(self, object, type):
        "Takes object and event type as arguments"
        self.object = object
        self.type = type

        self.part = None
        self.direction = None
        return