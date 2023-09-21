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
    
    def get_task(self, task):
        """Get task by task id or name"""
        return self.service.get_task(task)
    
    def delete_task(self, task_id):
        return self.service.delete_task(task_id)
    
    def save_task(self, model):
        return self.service.save_task(model)
    
    def get_all_tasks(self):
        return self.service.get_all_tasks()
         