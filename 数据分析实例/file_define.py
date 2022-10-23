"""
和文件相关的类定义
"""
from data_define import Record
import json


# 定义一个抽象类来做顶层设计，确认功能实现
class FileReader:

    def read_data(self) -> list[Record]:
        """读取文件数据，读到的每一条数据都转化为record对象，将其封装进list内返回即可"""
        pass


class TextFileReader(FileReader):

    def __init__(self, path):
        self.path = path  # 记录成员变量记录文件的路径

    # 复写（实现抽象方法）父类的方法
    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")
        record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip()  # 去除数据中每一行\n
            data_list = line.split(",")
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)

        f.close()
        return record_list


class JsonFileReader(FileReader):
    def __init__(self, path):
        self.path = path  # 记录成员变量记录文件的路径

    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")
        record_list: list[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["data"], data_dict["order_id"], int(data_dict["money"]), data_dict["province"])
            record_list.append(record)

        f.close()
        return record_list
