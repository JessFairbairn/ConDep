class CDManager:
    def __init__(self):
        self.objects = []
        return


    def tick(self):
        for obj in self.objects:
            events = obj.tick()
            #if events:
                #TODO: do something clever with any events

        return