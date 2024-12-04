import abc
import json
from json.decoder import JSONDecodeError


class DataReader(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def read(filepath: str):
        json.dump


class DataWriter(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def write(filepath: str, data: dict):
        pass

    @staticmethod
    @abc.abstractmethod
    def add(filepath: str, data: dict):
        pass


class JSONIO(DataReader, DataWriter):
    def read(filepath: str) -> dict:
        with open(filepath, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
            except JSONDecodeError:
                data = {}
        return data

    def write(filepath: str, data: dict) -> None:
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(data, file)

    def add(filepath: str, data: dict) -> None:
        with open(filepath, "a", encoding="utf-8") as file:
            json.dump(data, file)
