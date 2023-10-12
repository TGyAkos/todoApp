from src import (
    task_controller,
    task_model,
    task_service,
    task_view,
    task_model,
    task_orm,
)


class Main:
    model = None
    orm = None
    service = None
    view = None
    view_utils = None
    controller = None

    def __init__(self):
        self.initialize_classes()
        self.wire_dependencies()

    def start(self):
        self.view.draw()

    def initialize_classes(self):
        self.model = task_model.TaskModel()
        self.orm = task_orm.Orm()
        self.view = task_view.DrawUI()
        self.service = task_service.TaskService()
        self.controller = task_controller.Controller()
        return

    def wire_dependencies(self):
        self.view.set_controller(self.controller)
        self.service.set_model_orm(self.orm)
        self.controller.set_service(self.service)
        return


def run_app():
    app = Main()
    app.start()


if __name__ == "__main__":
    run_app()
