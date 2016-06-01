# Luigi Sample Repository

There are lot of resources online explaining the use cases of Luigi, but not
a lot of them explain how to setup and configure Luigi. Here, we have different
Luigi tasks explaining the use cases and setup

## Installation

Only package we need is luigi

```$ pip install luigi```

## Tasks

#### Each task is a unit of work. Tasks can be independant or can have dependancies

* [Simple Hello World task](helloworld_task.py) - Simple example to show the structure of a Luigi task
* [Task with dependecy](dependant_task.py) - Example to show how to add dependencies to current task
* [Task with mock target](mock_target_task.py) - *I really do not have an output, but still want some task dependency*
* [PySpark Task](pyspark_task.py) - Example pyspark task with JDBC connection

##### Note:
Every task mandatorily needs to have an output, else luigi does not know if the task is completed or not. It is more like a book keeping for Luigi to find out the status of the task.

If you remove `output()` method from any of the dependant task, the dependant task will run infinitely. So make sure you have the output method specified and is used to write output in all tasks.

## Running the tasks
To run any task, we follow the below command pattern

```
$ luigi --module mymodule MyTask --local-scheduler
```

**Example:**
```
$ luigi --module dependant_task DependantTask --local-scheduler
```

## Configuration

Luigi looks for config files in:

* `/etc/luigi/client.cfg`
* `luigi.cfg` in the current working directory
* `LUIGI_CONFIG_PATH` environment variable

Most important part of the configuration is setting up a spark job or a pyspark job. Luigi config has sections `[spark]` and `[pyspark]` to specify extra JARs and drivers required to run the spark job.

## Central Scheduler

The `--local-scheduler` param to run the luigi module must be used only during
development. Once deployed, we need to use the central scheduler.

Running the central scheduler:
```
$ luigid
```
When luigid starts up, it looks for the config file in previously mentioned locations.

Running a luigi task with the central scheduler
```
$ luigi --module pyspark_task PySparkTableSchema
```

## Web Dashboard

Luigi comes with a web dashboard for task history and statuses. The dashboard can
be accessed via `http://localhost:8082` for local instance. The central server's
dashboard can be accessed via `http://<central-scheduler-host>:8082`
