class FileWriterSingleton:
    instance = None

    def __new__(cls, filename):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.file = open(filename, "w")
        return cls.instance

    def write(self, text):
        self.file.write(text)

    def close(self):
        self.file.close()
