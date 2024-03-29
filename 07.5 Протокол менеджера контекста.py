#  7.5 Протокол менеджера контекста
""""""

#  Собственный класс FileManager для работы с файлами,
#  который закрывает файл после окончания работы и обрабатывает ошибки при открытии файла
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
            return self.file
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found")
            # raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


with FileManager("test.txt", "r") as f:
    if f:
        print(f.read())  # Error: File 'test.txt' not found