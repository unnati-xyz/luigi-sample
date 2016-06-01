import luigi
from helloworld_task import HelloWorldTask


class DependantTask(luigi.Task):

    # requires method defines the dependencies of this Task
    def requires(self):
        return HelloWorldTask()

    def output(self):
        return luigi.LocalTarget('out-dependant.txt')

    def run(self):
        print("Hello from dependant task")

        with self.output().open("w") as f:
            f.write("Hello from dependant task")
