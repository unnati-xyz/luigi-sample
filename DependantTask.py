import luigi
from HelloWorldTask import HelloWorldTask

class DependantTask(luigi.Task):

    """
    `requires` method defines the dependencies of this Task
    """
    def requires(self):
        return HelloWorldTask()

    # Let us use a mock target
    def output(self):
        return luigi.LocalTarget('out.txt')

    def run(self):
        print("Hello from dependant task")

        with output().open("w") as f:
            f.writeline("Hello from dependant task")
