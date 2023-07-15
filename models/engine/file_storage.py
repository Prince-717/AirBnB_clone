#!/usr/bin/python3
""" FileStorage class """
import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """Serializes airbnb_instances to a JSON file and deserializes

    ATTRIBUTES:
    __file_pathh is a private class attribute (str) path to the JSON file

     __objects is a private class attribute (dict) that is empty but will
    store all objects by <class name>.id ex: to store a BaseModel object
    with id=12121212, the key will be BaseModel.12121212)

    """
    __file_path = "file.json"
    __objects = {}

    class_for_airbnb = {"BaseModel": BaseModel,
                      "User": User,
                      "State": State,
                      "City": City,
                      "Amenity": Amenity,
                      "Place": Place,
                      "Review": Review}

    def all(self):
        """
        [all] methods

        Returns:
            [dict]: [dictionary containing objects]
        """
        return self.__objects

    def new(self, value):
        """
        [new] new method sets in __objects the value with
        key <value class name>.id

        Args:
            value ([object]): [object to be created]
        """
        _id = value.id
        key = str(value.__class__.__name__) + "." + _id
        self.__objects[key] = value

    def save(self):
        """
        [save] save method serializes __objects to the JSON file
        (path: __file_path)
        """
        basemodel_dict = {}
        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            for key, value in self.__objects.items():
                basemodel_dict[key] = value.to_dict()
            json.dump(basemodel_dict, file)

    def reload(self):
        """
        [reload] deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesnt exist,
        no exception should be raised)
        """
        if path.isfile(self.__file_path):
            with open(self.__file_path, mode="r") as file:
                value = json.load(file)
                basemodel_dict = {}
                for key, val in value.items():
                    basemodel_dict[key] = self.class_for_airbnb[val["__class__"]](**val)
                self.__objects = basemodel_dict
        else:
            return
