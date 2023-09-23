import datetime
import re
from pprint import pprint

import task_orm, task_model, task_query_model

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
    
    def get_task_by_query_model(self, query_model: task_query_model.TaskQueryModel):
        query_model.set_finish_date(self.convert_string_to_datetime(query_model.get_finish_date()))

        # FIXME it works but its hacky me no like
        if query_model.get_urgency() == ['all']:
            query_model.set_urgency(["low", "medium", "high"])
        
        pprint(query_model.get_urgency())
        return self.model_orm.get_task_by_query_model(query_model)

    # bleh i hate it here
    def save_task(self, task_model: task_model.TaskModel):
        task_model.set_date(
            self.convert_string_to_datetime(task_model.get_date()))

        task_model.set_finish_date(
            self.convert_string_to_datetime(task_model.get_finish_date()))
        
        self.model_orm.save_task(task_model)
        return "Task created successfully"
    
    def delete_task(self, task_id):
        self.model_orm.delete_task_by_id(task_id)
        return "Task deleted successfully"  

    def convert_string_to_datetime(self, date: str) -> datetime:
        date_list = date.split('.')

        # HACK Cleaning date from leading 0's to convert to datetime
        for value in date_list:
            if value[0] is 0:
                value.replace('0', '', 1)

        date_list = [int(value) for value in date_list]
        date = datetime.datetime(*date_list)

        return date 
    
    def clean_date(self, date_list: list):

        return date_list

    
    def create_new_task(self):
        return task_model.TaskModel()

    def create_new_query_model(self):
        return task_query_model.TaskQueryModel()