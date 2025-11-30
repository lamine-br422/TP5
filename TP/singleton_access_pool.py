class FileAccessPool:
    max_instances = 3
    instances = []
    
    def __new__(cls, filename):
        if len(cls.instances) < cls.max_instances:
            obj = super().__new__(cls)
            obj.file = open(filename, "a")
            cls.instances.append(obj)
            return obj
        return cls.instances[0]

    def write(self, text):
        self.file.write(text)

    def close(self):
        self.file.close()
