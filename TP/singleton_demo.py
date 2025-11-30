#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

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


class DatabaseSingleton:
    instance = None

    def __new__(cls, dbname):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.conn = sqlite3.connect(dbname)
        return cls.instance

    def execute(self, query):
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()

    def close(self):
        self.conn.close()


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


def test_file_writer_singleton():
    fw1 = FileWriterSingleton("file_singleton.txt")
    fw2 = FileWriterSingleton("autre.txt")
    fw1.write("ligne 1 via fw1\n")
    fw2.write("ligne 2 via fw2\n")
    print("FileWriterSingleton même instance:", fw1 is fw2)
    fw1.close()


def test_database_singleton():
    db1 = DatabaseSingleton("singleton.db")
    db2 = DatabaseSingleton("autre.db")
    db1.execute("CREATE TABLE IF NOT EXISTS demo(id INTEGER);")
    db1.execute("INSERT INTO demo(id) VALUES (1);")
    print("DatabaseSingleton même instance:", db1 is db2)
    db1.close()


def test_file_access_pool():
    a = FileAccessPool("pool.txt")
    b = FileAccessPool("pool.txt")
    c = FileAccessPool("pool.txt")
    d = FileAccessPool("pool.txt")
    print("Taille du pool:", len(FileAccessPool.instances))
    print("a is b:", a is b)
    print("a is c:", a is c)
    print("a is d:", a is d)
    for inst in FileAccessPool.instances:
        inst.close()


if __name__ == "__main__":
    test_file_writer_singleton()
    test_database_singleton()
    test_file_access_pool()
