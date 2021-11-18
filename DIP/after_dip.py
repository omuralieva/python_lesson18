# перезаписали все по принципу "dependency inversion", принцип которого заключается в том, что более высокоуровневые
# не должны зависеть от более низкоуровневых модулей, а желательно они должны зависеть от абстракций, а абстракции не
# не должны зависеть от деталей ( детали должны зависеть от абстракций)


import sys
import time


class TerminalPrinter:
    def write(self, msg):
        sys.stderr.write(f"{msg}\n")


class FilePrinter:
    def write(self, msg):
        with open('log.txt', 'a+', encoding='UTF8') as f:
            f.write(f"{msg}\n")


class Logger:
    def __init__(self):
        self.format = '%Y-%b-%d %H:%M:%S'

    def log(self, message, notifier):                               # создали отдельный метод, который принимает
        prefix = time.strftime(self.format, time.localtime())       # в аргументы "notifier"(абстракция) и
        notifier().write(f"{prefix} {message}")                     # и реализовывает метод "write"

                    # удалили ненужные методы, которые принцип DIP нарушали


logger = Logger()
logger.log("Starting the program...", TerminalPrinter)              # вызвали метод задав в него нужный нам класс
logger.log("An error!", FilePrinter)                                # и сообщение
