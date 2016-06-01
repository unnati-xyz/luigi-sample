import luigi

class HelloWorldTask(luigi.Task):

    def output(self):
        return luigi.LocalTarget('out.txt')

    def run(self):
        print("Hello World")

        with output().open("w") as f:
            f.writeline("Hello from luigi task")
