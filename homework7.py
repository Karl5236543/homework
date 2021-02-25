import contextlib
import sys, os
import time


class cd:
    def __init__(self, path, suppress_exc=None):
        if not os.path.exists(path):
            raise ValueError("директория не найдена")
        self._is_suppress = True if suppress_exc else False
        self._suppress_exc = suppress_exc or Exception
        self._path = path
        self._current_dir = os.getcwd()

    def __enter__(self):
        try:
            os.chdir(self._path)
            raise IndexError()
        except self._suppress_exc:
            if not self._is_suppress:
                raise
    
    def __exit__(self, exc_type, exc_value, tb):
        os.chdir(self._current_dir)


@contextlib.contextmanager
def cd_decorator(path, suppress_exc=None):
    if not os.path.exists(path):
        raise ValueError("директория не найдена")
    is_suppress = True if suppress_exc else False
    suppress_exc = suppress_exc or Exception
    current_dir = os.getcwd()
    try:
        os.chdir(path)
        raise IndexError()
    except suppress_exc:
        if not is_suppress:
            raise
    try:
        yield
    except Exception:
        pass
    finally:
        os.chdir(current_dir)


class timeit(contextlib.ContextDecorator):
    def __init__(self, handle=sys.stdout):
        self._handle = handle
        self._start = None

    def __enter__(self):
        self._start = time.time()

    def __exit__(self, *exc_info):
        print(f'time: {time.time() - self._start}', file=self._handle)


project_path = os.getcwd()
other_path = os.path.join(project_path, 'tests')


@cd_decorator(other_path, IndexError)
def foo():
    print(f'current dir: {os.getcwd()}')
    [][0]


@timeit()
def bar():
    time.sleep(2)


if __name__ == '__main__':

    print('------------------1-------------------')
    print(f'current dir: {os.getcwd()}')
    with cd(other_path, IndexError):
        print(f'current dir: {os.getcwd()}')
    print(f'current dir: {os.getcwd()}')

    print('------------------2-------------------')
    print(f'current dir: {os.getcwd()}')
    foo()
    print(f'current dir: {os.getcwd()}')

    print('------------------3-------------------')
    bar()








    