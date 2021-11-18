# переделали все по принципу "Single responsibility", принцип которого заключается в том, что один класс
# должен иметь одну зону ответственности ( не надо мешать все в одну кучу)


class FormatData:                           # Создали класс, в котором будут хранится сырые данные
    def __init__(self, raw_data):
        self.raw_data = raw_data

    def prepare(self):                      # создали метод, который будет подготавливать эти сырые данные и выводить
        result = ''                         # имя, фамилию и профессию каждого в отдельной строке, через запятую
        for item in self.raw_data:
            new_line = ','.join(
                (
                    item['name'],
                    item['surname'],
                    item['occupation']
                )
            )
            result += f"{new_line}\n"
        return result


class FileWriter:                           # создали класс, который перезаписывает файлы в csv
    def __init__(self, filename):
        self.filename = filename

    def write(self, data):
        with open(self.filename, 'w', encoding='UTF8') as f:
            f.write(data)


row_data = [
    {
        'name': 'Sherlock',
        'surname': 'Holmes',
        'occupation': 'private detective'
    },
    {
        'name': 'John',
        'surname': 'Watson',
        'occupation': 'doctor'
    }
]                             # записали данные, которые надо подготовить и перезаписать в csv

formatter = FormatData(row_data)             # присвоили  класс, передав в аргументы данные
formatted_data = formatter.prepare()         # запустили метод в классе для подготовки данных

writer = FileWriter('out.csv')               # присвоили класс, указав куда перезаписывать
writer.write(formatted_data)                 # запустили метод для перезаписи, передав в аргументы подготовленные данные
