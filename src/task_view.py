from pprint import pprint
from InquirerPy import inquirer
import re

import task_controller

class DrawUtils:
    """Dependencies:
    - task_controller"""
    controller = None
    model = None

    def set_controller(self, controller: task_controller):
        self.controller = controller

    def add_new_task(self):
        self.model = self.controller.create_new_task()
        print("add new task")
        self.input_name()
        self.input_urgency()
        self.input_date()
        self.input_finish_date()
        self.save_task()
        
    def input_name(self):
        name = inquirer.text(message='Enter task name').execute()
        self.model.set_name(name)

    def input_urgency(self):
        urgency = inquirer.select(message='Select urgency', choices= ["low", "medium", "high"]).execute()
        self.model.set_urgency(urgency)

    def input_date(self):
        date = inquirer.text(message='Enter starting date\n Example 2023.01.01\n',
                             validate=lambda result: re.search("^\d{4}[.]\d{2}[.]\d{2}$", result)).execute()
        self.model.set_date(date)

    def input_finish_date(self):
        finish_date =  inquirer.text(
            message='Enter finishing date\n Example 2023.01.01\n',
            validate=lambda result: re.search("^\d{4}[.]\d{2}[.]\d{2}$", result)
            ).execute()
        self.model.set_finish_date(finish_date)

    def save_task(self):
        pprint(self.controller.save_task(self.model))

    def delete_task(self):
        self.list_tasks()
        # TODO actually make some filtering
        task_id = inquirer.text(message='Enter task id').execute()
        task_id = int(task_id)
        self.controller.delete_task(task_id)
        pprint("Task deleted successfully")

    def list_tasks(self):
        pprint("All tasks saved:")
        pprint(self.controller.get_all_tasks())


class DrawUI:
    """Dependencies:
    - DrawUtils"""

    run = True
    utils = None
    action = None

    def set_utils(self, utils: DrawUtils):
        self.utils = utils

    def draw(self):
        while self.run is True:
            self.action = inquirer.select(
                message='What do you want to do?', 
                choices=["Add new task", 
                        "List all tasks", 
                        "Delete task", 
                        "Exit"]).execute()
            
            match self.action:
                case "Add new task":
                    self.utils.add_new_task()
                case "List all tasks":
                    self.utils.list_tasks()
                case "Delete task":
                    self.utils.delete_task()
                case "Exit":
                    self.run = False
