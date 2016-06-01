import luigi

class HelloWorldTask(luigi.Task):

    def output(self):
        return luigi.LocalTarget('out.txt')

    def run(self):
        print("Hello World")

        with self.output().open("w") as f:
            f.write("Hello from luigi task")
