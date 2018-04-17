#!/usr/bin/python3
'''
    Define class FileStorage
'''
import json
import models


class FileStorage:
    '''
        Serializes instances to JSON file and deserializes to JSON file.
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        '''
            Return the dictionary
        '''
        if cls is not None:
            cls_dict = []
            for key, obj in self.__objects.items():
                if obj.__class.__name__ == cls or obj.__class.__ == cls:
                    cls_dict[key] = obj
            return cls_dict
        else:
            return self.__objects

    def new(self, obj):
        '''
            Set in __objects the obj with key <obj class name>.id
            Aguments:
                obj : An instance object.
        '''
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj
        self.__objects[key] = value_dict

    def save(self):
        '''
            Serializes __objects attribute to JSON file.
        '''
        objects_dict = {}
        for key, val in self.__objects.items():
            objects_dict[key] = val.to_dict()

        with open(self.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(objects_dict, fd)

    def reload(self):
        '''
            Deserializes the JSON file to __objects.
        '''
        try:
            with open(self.__file_path, encoding="UTF8") as fd:
                self.__objects = json.load(fd)
            for key, val in self.__objects.items():
                class_name = val["__class__"]
                class_name = models.classes[class_name]
                self.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        '''
            Delete an object from __objects.
        '''
        if obj is not None:
            key = str(obj.__class__.__name__) + "." + str(obj.id)
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        '''
            Call reload() to deserialize JSON file
        '''
        self.reload()
