import json
import os.path
from dataclasses import asdict
from typing import Type, TypeVar


class SettingsStorage:
    @classmethod
    def save(cls, data, filename):
        with open(filename, 'w') as file:
            json.dump(asdict(data), file)

    @classmethod
    def load(cls, filename):
        with open(filename) as file:
            return json.load(file)

    SettingsType = TypeVar('SettingsType')

    @classmethod
    def try_load(cls, filename, type_class: Type[SettingsType]) -> SettingsType:
        if not os.path.isfile(filename):
            return type_class()
        return type_class(**cls.load(filename))
