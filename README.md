# full-profiler
A simple Python wrapper to profile both memory and time of python scripts in Linux or MacOS.
Quickly built with Typer 🚀💣

## Installation
You need to clone the repo and install in your environment:

```
git clone git@github.com:faviasono/full-profiler.git
cd full_profiler 
pip install .
```

n.b. It's not yet available as wheel package in PyPi.

## Usage
You must run as python module in the following way:

```
python -m full_profiler [ARGS] [OPTIONS]
```

In order to collect in-line memory information using `memory_profiler` you'll need to decorate your function with `memory_profiler.profile` function.
Take a look at the `example/example.py` or to the [official page](https://github.com/pythonprofilers/memory_profiler) of the tool 

Use the ` --help`  flag to see the available commands. For instance, the command `python -m full_profiler --help` will generate the following output:


![example](example/help_example.png "Example when using --help flag")




## TODO

[ ] Get Metrics from  program.prof (e.g., max usage, peak usage)

[ ] Automatically parse information from text referring to `model.predict` or `session.run` codes.

[ ] Add results in common folder (handle paths)
