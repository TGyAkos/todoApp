import re
from pprint import pprint

import task_orm, task_model

class TaskService:
    """Dependencies: 
    - task_orm 
    - task_model"""
    model_orm = None

    def set_model_orm(self, model_orm: task_orm.Orm):
        self.model_orm = model_orm

    def get_all_tasks(self):
        return self.model_orm.get_all_tasks()

    def get_task(self, task):
        """Get task by id or name."""

        if type(task) is int:
            self.model_orm.get_task_by_id(task)

        if type(task) is str:
            self.model_orm.get_task_by_name(task)
    

    def save_task(self, task_model: task_model.TaskModel):
        self.model_orm.save_task(task_model)
        return "Task created successfully"
    
    def delete_task(self, task_id):
        self.model_orm.delete_task_by_id(task_id)
        return "Task deleted successfully"  
    
    def create_new_task(self):
        return task_model.TaskModel()