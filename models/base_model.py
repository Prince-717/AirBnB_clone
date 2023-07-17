#!/usr/bin/python3
"""
BaseModel module
"""
from datetime import datetime
import uuid


class BaseModel():
    """
    Public instance attributes:
    id: string - assign with an uuid when an instance is created:
        uuid.uuid4(): generate unique id but dont forget to convert to a string
        the goal is to have unique id for each BaseModel
    created_at: assign current date to insstance created
   
    updated_at: datetime - assign current date and time to when the instance
    	is updated
    """
    def __init__(self, *args, **kwargs):
        """
        initializer
        id (int): public instance attribute
        """
        from models import storage
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    value = datetime.strptime(value, time_format)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            storage.new(self)

    def __str__(self):
        """
        Human readable format
        __str__ method should print: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        The initial step in the serialization/deserialization process
        involves creating a dictionary representation of our BaseModel object.
        This method returns a dictionary that contains all the keys and values
        from the object's __dict__ attribute, effectively converting the instance
        into a dictionary format.

        """
        basemodel_dict = dict(self.__dict__)
        basemodel_dict["created_at"] = basemodel_dict["created_at"].isoformat()
        basemodel_dict["updated_at"] = basemodel_dict["updated_at"].isoformat()
        basemodel_dict["__class__"] = self.__class__.__name__
        return basemodel_dict
