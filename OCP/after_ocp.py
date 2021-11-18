# перделали все по принципу "open - closed", принцип которого заключается в том, что классы можно расширять,
# но не модифицировать


import sys
import time


class Logger:                                                  # перзаписали класс логгер, задав в него формат даты и вр
    def __init__(self):
        self.format = '%Y-%b-%d %H:%M:%S -->'

    def log(self, message):                                    # задали метод для записи даты и сообщения
        prefix = time.strftime(self.format, time.localtime())
        sys.stderr.write(f"{prefix} {message}\n")


class CustomerLogger(Logger):                                  # создали подкласс, наследуемый от класса "Logger"
    def __init__(self):
        super().__init__()
        self.format = '%Y-%b-%d ::'


logger = Logger()                                             # присвоили класс "Logger"
logger.log('An error has happened!')                          # запустили метод, передав сообщение

c_logger = CustomerLogger()                                   # присвоили подкласс "CustomerLogger"
c_logger.log('Custom logged message!')                        # запустили метод, передав сообщение
