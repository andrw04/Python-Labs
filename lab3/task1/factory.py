from constants import Serializer

class MyJson:
    pass

class MyXML:
    pass


class Factory:
    
    @staticmethod
    def create_serializer(serialized : Serializer):
        if Serializer.Json:
            return MyJson()
        
        elif Serializer.Xml:
            return MyXML()
        