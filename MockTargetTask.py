import luigi
import luigi from MockTarget

class MockTargetTask(luigi.Task):

    """
    Luigi mandatorily requires an output for each task. In case you do not need
    file output you can use MockTarget as an output
    """
    def output(self):
        return luigi.MockTarget('out.txt')

    def run(self):
        print("Hello from mock target task")

        with output().open("w") as f:
            f.writeline("Hello from mock target task")
