from enum import Enum

class MyJson:
    pass

class MyXML:
    pass

class Serializer(Enum):
    Json = 1,
    Xml = 2


class Factory:
    
    @staticmethod
    def create_serializer(serialized : Serializer):
        if Serializer.Json:
            return MyJson()
        
        elif Serializer.Xml:
            return MyXML()
        