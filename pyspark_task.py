import luigi
from pyspark.sql import SQLContext
from luigi.contrib.spark import PySparkTask, SparkSubmitTask
import logging
from helloworld_task import HelloWorldTask


class PySparkTableSchema(PySparkTask):

    def requires(self):
        return HelloWorldTask()

    def output(self):
        return luigi.LocalTarget('pysparkout.csv')

    def main(self, sc, *args):
        logging.info("=======SPARK JOB=========")
        sqlContext = SQLContext(sc)

        df = (sqlContext.load(source="jdbc",
            url="jdbc:postgresql://localhost:2222/mydatabase?user=dbuser&password=dbpassword",
                dbtable="tablename"))

        print(df.show())
        logging.info(df.printSchema())

        with self.output().open('w') as outFile:
            outFile.write(str(result))
