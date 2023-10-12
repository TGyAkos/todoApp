import pytest
from src import task_view


class Test_TaskView:
    @pytest.fixture(scope="module", autouse=True)
    def task_view_fixture():
        print("INIT")

        yield
        print("TEARDOWN")
