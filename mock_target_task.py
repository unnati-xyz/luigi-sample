import luigi
from luigi.mock import MockTarget

class MockTargetTask(luigi.Task):

    # Luigi mandatorily requires an output for each task. In case you do not need
    # file output you can use MockTarget as an output
    def output(self):
        return MockTarget('out-mock.txt')

    def run(self):
        print("Hello from mock target task")

        with self.output().open("w") as f:
            f.write("Hello from mock target task")
