import sound
from sound.filters.vocoder import voc
from sound.effects import *
from sound.effects.echo import echofilter
from sound.effects import echo
import math
import fibo  # Import a file name from same directory
import fibo as fib  # Alias for import
from fibo import fibonacci_series, print_fibonacci_series
from fibo import fibonacci_series as fibonacci
import sys
import builtins

# In most cases Python programmers do not use facility of import *
# since it introduces an unknown set of names into the interpreter,
# possibly hiding some things that are already defined.
# from fibo import *  #

fibo.print_fibonacci_series(100)
print(fibo.fibonacci_series(100))
print(fibo.__name__)  # fibo

print_fibonacci_series(100)
print(fibonacci_series(100))

print(fib.fibonacci_series(100))
print(fibonacci(100))

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        # [0] is '06_modules.py' (file name)
        print_fibonacci_series(int(sys.argv[1]))

# Names of all modules that are compiled into this Python interpreter
print(sys.builtin_module_names)

# List of directories that Python interpreter can search for modules
print(sys.path)

# If there would be 'math.py' file in this directory, it would "override"
# original math module
# Same thing with compiled 'math.pyc'

math.sqrt(2)

# Modifying sys path (where to search for Python modules)
sys.path.append('/tmp/project/python')

# dir - list of all names that module defines

# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
#  '__package__', '__spec__', 'fibonacci_series', 'print_fibonacci_series']
dir(fibo)

# A lot of names :)
dir(sys)

# No arguments in dir - names from current module
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__',
#  '__loader__', '__name__', '__package__', '__spec__', 'fib', 'fibo', 'fibonacci',
#  'fibonacci_series', 'math', 'print_fibonacci_series', 'sys']
dir()

# Built-in functions, exceptions, and other objects, which are "always" available.
dir(builtins)

echo.echofilter('input', 'output', delay=0.7, atten=4)

echofilter('input', 'output', delay=0.7, atten=4)

# ImportError: cannot import name 'non_existing_effect' from 'sound.effects'
# from sound.effects import non_existing_effect

# When using syntax like import item.subitem.subsubitem, each item except for the last
# must be a package; the last item can be a module or a package but can’t be
# a class or function or variable defined in the previous item.

# ModuleNotFoundError: No module named 'sound.effects.echo.echofilter
# import sound.effects.echo.echofilter

print(surround.__doc__)

voc()

# __path__ - list containing the name of the directory holding the package’s __init__.py before the code in that file is executed
print(sound.filters.__path__)
