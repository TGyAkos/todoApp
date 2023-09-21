import task_controller, task_model, task_service, task_view, task_model, task_orm

class Main:
    model = None
    orm = None
    service = None
    view_utils = None
    view = None
    controller = None

    def __init__(self):
        self.initialize_classes()
        self.wire_dependencies()

    def start(self):
        self.view.draw()

    def initialize_classes(self):        
       self.model = task_model.TaskModel()
       self.orm = task_orm.Orm()
       self.view_utils = task_view.DrawUtils()
       self.view = task_view.DrawUI()
       self.service = task_service.TaskService()
       self.controller = task_controller.Controller()

    def wire_dependencies(self):
       self.view_utils.set_controller(self.controller)
       self.view.set_utils(self.view_utils)
       self.service.set_model_orm(self.orm)
       self.controller.set_service(self.service)
       self.controller.set_view(self.view)
    
def run_app():
    app = Main()
    app.start()

if __name__ == "__main__":
    run_app()