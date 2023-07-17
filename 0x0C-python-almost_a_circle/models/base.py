#!/usr/bin/python3
"""base.py"""
import json
import csv


class Base:
    """Base class for managing id attribute."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of a list of dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        json_list = []
        if list_objs is not None:
            json_list = [obj.to_dictionary() for obj in list_objs]
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list represented by a JSON string."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances loaded from a JSON file."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_data = file.read()
                data = cls.from_json_string(json_data)
                instances = [cls.create(**obj) for obj in data]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes a list of instances to a CSV file.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            if list_objs is None:
                writer.writerows([])
            else:
                rows = [obj.to_dictionary() for obj in list_objs]
                writer.writerows(rows)

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes a CSV file into a list of instances.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                rows = list(reader)
                if cls.__name__ == "Rectangle":
                    keys = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    keys = ["id", "size", "x", "y"]
                data = []
                for row in rows:
                    values = [int(val) for val in row]
                    instance_data = dict(zip(keys, values))
                    data.append(instance_data)
                instances = [cls.create(**obj) for obj in data]
                return instances
        except FileNotFoundError:
            return []
