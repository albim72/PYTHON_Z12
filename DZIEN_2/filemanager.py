class FileManager:
    def __init__(self,filename,mode,encod):
        self.filename = filename
        self.mode = mode
        self.encod = encod
        self.file = None

    def __enter__(self):
        self.file = open(self.filename,self.mode,encoding=self.encod)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()



with FileManager('test.txt',"a",'utf-8') as fm:
    fm.write('to jest plik utworzony za pomocą FileManager\n')

print(fm.closed)


with FileManager('test.txt',"r",'utf-8') as fm:
    print(fm.read())
