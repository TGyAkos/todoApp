import task_view, task_service

class Controller:
    """Dependencies:
    - task_service
    - task_view"""
    service = None
    view = None

    # Needs to be set before use
    def set_view(self, view: task_view.DrawUtils):
        self.view = view

    # Needs to be set before use
    def set_service(self, service: task_service.TaskService):
        self.service = service

    def create_new_task(self):
        return self.service.create_new_task()
    
    def create_new_query_model(self):
        return self.service.create_new_query_model()
    
    def get_task(self, task):
        """Get task by task id or name"""
        return self.service.get_task(task)
    
    def delete_task(self, task_id):
        return self.service.delete_task(task_id)
    
    def save_task(self, model):
        return self.service.save_task(model)
    
    def get_all_tasks(self):
        return self.service.get_all_tasks()
    
    def get_task_by_query_model(self, query_model):
        return self.service.get_task_by_query_model(query_model)

    # TODO implement will cause errors when called
    def get_all_saved_finish_dates_for_auto_completeion(self):
        return self.service.get_all_saved_finish_dates_for_auto_completeion()
         