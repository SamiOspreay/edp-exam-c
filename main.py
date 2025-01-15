class Event:
    def __init__(self, payload):
        self.timestamp = datetime.now()
        self.payload = payload

    def __str__(self):
        return f"{self.__class__.__name__} at {self.timestamp} with payload: {self.payload}"



class ApplicationSentEvent(Event):
    name = "application_submitted"


class ApplicationRejectedEvent(Event):
    name = "application_rejected"


class ApplicationAcceptedEvent(Event):
    name = "application_accepted"



class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.event = event

    def send_application(self,university):
        
        event = ApplicationSentEvent(f"Application sent to:  {university.name} by {self.name}")
        self.events.append(event)
        university.handle_event(event)

    def __str__(self):
        
        return f"Student: {self.name}, ID: {self.student_id}"


class University:
    def __init__(self, name):
        self.name = name
        self.communication_queue = degue()
    
    def handle_event(self, event):
        
        print(f"University {self.name} processing event: {event}")
        if isinstance(event, ApplicationSentEvent):
            self.application_review(event)
    
    def application_review(self.event):
        pass



        