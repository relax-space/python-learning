

class FruitDto:
    def __init__(self):
        self.name =""
        self.value =""
    
    def __eq__(self,other):
        return self.name == other.name \
        and self.value == other.name
    
    @classmethod
    def toDict(self,obj):
        dict = obj.__dict__
        return dict

    @classmethod
    def fromDict(self,dict):
        obj = FruitDto()
        obj.__dict__.update(dict)
        return obj
