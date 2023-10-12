class TaskQueryModel:
    finish_date = None
    urgency = None

    # Getters
    def get_finish_date(self):
        return self.finish_date
    
    def get_urgency(self):
        return self.urgency
    
    # Setters
    def set_finish_date(self, finish_date):
        self.finish_date = finish_date

    def set_urgency(self, urgency):
        self.urgency = urgency

    
