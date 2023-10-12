from pprint import pprint
from InquirerPy import inquirer
import re

from src import task_controller


class DrawUI:
    """Dependencies:
    - task_controller"""

    run = True
    action = None
    controller = None
    model = None

    def set_controller(self, controller: task_controller):
        self.controller = controller

    def draw(self):
        while self.run is True:
            self.action = inquirer.select(
                message="What do you want to do?",
                choices=[
                    "Add new task",
                    "List all tasks",
                    "List tasks by due date",
                    "Delete task",
                    "Exit",
                ],
            ).execute()

            match self.action:
                case "Add new task":
                    self.add_new_task()
                case "List all tasks":
                    self.list_tasks()
                case "List tasks by due date":
                    self.list_tasks_by_due_date()
                case "Delete task":
                    self.delete_task()
                case "Exit":
                    self.run = False

    def add_new_task(self):
        self.model = self.controller.create_new_task()
        print("add new task")
        self.input_name()
        self.input_urgency()
        self.input_date()
        self.input_finish_date()
        self.save_task()

    def input_name(self):
        name = inquirer.text(message="Enter task name").execute()
        self.model.set_name(name)

    def input_urgency(self):
        urgency = inquirer.select(
            message="Select urgency", choices=["low", "medium", "high"]
        ).execute()
        self.model.set_urgency(urgency)

    def input_date(self):
        date = inquirer.text(
            message="Enter starting date\n Example 2023.01.01\n",
            validate=lambda result: self.validate_date(result),
        ).execute()
        self.model.set_date(date)

    def input_finish_date(self):
        # FIXME repeating logic here
        finish_date = inquirer.text(
            message="Enter finishing date\n Example 2023.01.01\n",
            validate=lambda result: self.validate_date(result),
        ).execute()
        self.model.set_finish_date(finish_date)

    def save_task(self):
        pprint(self.controller.save_task(self.model))

    def delete_task(self):
        self.list_tasks()
        # TODO actually make some filtering
        task_id = inquirer.text(message="Enter task id").execute()
        task_id = int(task_id)
        self.controller.delete_task(task_id)
        pprint("Task deleted successfully")

    # TODO redo it, looks awful
    def list_tasks(self):
        pprint("All tasks saved:")
        pprint(self.controller.get_all_tasks())

    def list_tasks_by_due_date(self):
        query_model = self.controller.create_new_query_model()

        # TODO implement this long fucking function
        # all_finish_dates = self.controller.get_all_saved_finish_dates_for_auto_completeion()
        finish_date = inquirer.text(
            message="Enter task due date\n Example 2023.01.01\n",
            # FIXME hacky way of doing this
            validate=lambda result: self.validate_date(result),
            # completer=all_finish_dates
        ).execute()
        query_model.set_finish_date(finish_date)

        urgency = inquirer.select(
            message="Select urgency\n To select multiple press space",
            # FIXME this should be a class variable
            choices=["low", "medium", "high", "all"],
            default="all",
            multiselect=True,
        ).execute()
        query_model.set_urgency(urgency)

        pprint(self.controller.get_task_by_query_model(query_model))

    # BUG this will let through non existent dates such as: 8888.99.99
    def validate_date(self, date):
        return re.search("^\d{4}[.]\d{2}[.]\d{2}$", date)
