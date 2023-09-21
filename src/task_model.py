class TaskModel:
    name = None
    urgency = None
    date = None
    finish_date = None

    # Getters
    def get_name(self):
        return self.name

    def get_urgency(self):
        return self.urgency

    def get_date(self):
        return self.date

    def get_finish_date(self):
        return self.finish_date

    # Setters
    def set_name(self, name):
        self.name = name
    
    def set_urgency(self, urgency):
        self.urgency = urgency

    def set_date(self, date):
        self.date = date

    def set_finish_date(self, finish_date):
        self.finish_date = finish_date
        