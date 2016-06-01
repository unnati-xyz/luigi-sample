# Luigi Sample Repository

There are lot of resources online explaining the use cases of Luigi, but not
a lot of them explain how to setup and configure Luigi. Here, we have different
Luigi tasks explaining the use cases and setup

## Installation

Only package we need is luigi

```$ pip install luigi```

## Tasks

#### Each task is a unit of work. Tasks can be independant or can have dependancies

* [Simple Hello World task](HelloWorldTask.py) - Simple example to show the structure of a Luigi task
* [Task with dependecy](DependantTask.py) - Example to show how to add dependencies to current task
* [Task with mock target](MockTargetTask.py) - *I really do not have an output, but still want some task dependency*

#### NOTE:
Every task mandatorily needs to have an output, else luigi does not know if the task is completed or not. It is more like a book keeping for Luigi to find out the status of the task.

If you remove `output()` method from any of the dependant task, the dependant task will run infinitely. So make sure you have the output method specified and is used to write output in all tasks.

## Running the tasks
