import typer
import os
import subprocess
import matplotlib
import datetime as dt
from contextlib import redirect_stdout

MPROF_RUN_COMMAND = "mprof run {} > output"
MPROF_PLOT_COMMAND = "mprof plot --flame --slope --title {} --output {}.png"
MPROFILE_MEM_COMMAND = "python -m memory_profiler {} > output_profiler"
CPROFILE_COMMAND = "python -m cProfile -o program.prof {}"
SNAKEVIZ_COMMAND = "snakeviz program.prof"

app = typer.Typer()


def create_output_file(path):
    file_name = "full_profiler_out_{}_{}.txt".format(path.split('.')[-2], dt.datetime.now().timestamp())
    return file_name

@app.command()
def file_size(path: str):
    """
    Return file size of the script
    """
    if not os.path.exists(path):
        raise ValueError
    size_ = f"{os.path.getsize(path)} bytes"
    print(size_) 

@app.command()
def inline_memory(path: str):
    """
    Use memory_profiler to generate statistics and save in full_profiler_out_{filename}.txt file
    """
    if not os.path.exists(path):
        raise ValueError
    if not path.endswith('.py'):
        raise ValueError('It must be a Python scipt')
    try:
        with open(create_output_file(path), 'x') as f:
            subprocess.call(MPROFILE_MEM_COMMAND.format(path).split(), stdout=f)
    except OSError as e:
        print('Error' + str(e))


@app.command()
def time_memory(path: str):
    """
    Use memory_profiler to generate statistics and plot results in file_name.png file
    """
    if not os.path.exists(path):
        raise typer.Abort()
    if not path.endswith('.py'):
        print('It must be a Python scipt')
        typer.Abort()
    try:
        with open(create_output_file(path), 'x') as f:
            subprocess.call(MPROF_RUN_COMMAND.format(path).split(), stdout=f)
            title = input('Insert title plot\n')
            os_put = title.replace(' ','_').strip().lower()
            subprocess.call(MPROF_PLOT_COMMAND.format(title, os_put).split(), stdout=f)
    except OSError as e:
        print('Error' + str(e))
        typer.Abort()

@app.command()
def cpu_time(path: str, plot: bool = False):
    """
    Use cProfile to generate statistics program.prof and plot results using snakeviz in browser
    """
    if not os.path.exists(path):
        raise typer.Abort()
    if not path.endswith('.py'):
        raise  typer.Abort()
       
    try:
        with open(create_output_file(path), 'x') as f:
            subprocess.call(CPROFILE_COMMAND.format(path).split(), stdout= f)
            if plot:
                subprocess.call(SNAKEVIZ_COMMAND.split(), stdout= f)
    except OSError as e:
        typer.Abort()


if __name__ == "__main__":
    app()