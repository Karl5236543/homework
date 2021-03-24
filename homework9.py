from functools import wraps

# Задача-1
# У вас есть файл из нескольких строк. Нужно создать генератор который будет построчно выводить строки из вашего файла.
# При вызове итерировании по генератору необходимо проверять строки на уникальность.
# Если строка уникальна, тогда ее выводим на экран, если нет - скипаем
def read_line(file):
    all_lines = []
    while True:
        next_line = file.readline()
        if not next_line:
            break
        if next_line in all_lines:
            continue
        yield next_line
        all_lines.append(next_line)



# Задача-2 (оригинальный вариант и его делать не обязательно):
# представим есть файл с логами, его нужно бессконечно контролировать
# на предмет возникнования заданных сигнатур.
#
# Необходимо реализовать пайплайн из корутин, который подключается к существующему файлу
# по принципу команды tail, переключается в самый конец файла и с этого момента начинает следить
# за его наполнением, и в случае возникнования запиcей, сигнатуры которых мы отслеживаем -
# печатать результат
#
# Архитектура пайплайна

#                    --------
#                   /- grep -\
# dispenser(file) <- - grep - -> pprint
#                   \- grep -/
#                    --------

# Структура пайплайна:
# ```

def coroutine(func):
    def wrap(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return wrap


@coroutine
def grep(*args):
    pattern, target = args
    while True:
        line = yield
        if pattern in line:
            target.send(line)


@coroutine
def printer():
    while True:
        line = yield
        print(line)


@coroutine
def dispenser(*args):
    while True:
        item = yield
        for target in list(*args):
            target.send(item)


def follow(file, disp):
    while True:
        line = file.readline().rstrip()
        if not line:
            continue
        disp.send(line)