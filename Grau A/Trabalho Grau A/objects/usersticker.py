from .csvsticker import CSVSticker


class UserSticker:
    def __init__(self, id_, number, name, content):
        self.__id = id_
        self.__number = number
        self.__name = name
        self.__content = content
        self.__status = 0  #0 = In the colletion, 1 = pasted in the album, 2 = available for trade

    def get_id(self):
        return self.__id
    
    def __add__(self, other):
        if isinstance(other, UserSticker):
            if other.get_id() == self.__id:
                self.__number += 1
            else:
                raise Exception("Cannot add stickers of different ids!")
        else:
            raise TypeError('Cannot combine different types with UserSticker!')
        
        return self
        
    def __str__(self):
        return f"| id: {self.__id} | number: {self.__number} | name: {self.__name}"
    
    @staticmethod
    def from_csvsticker(csvsticker: CSVSticker):
        return UserSticker(csvsticker.id, 1, csvsticker.name, csvsticker.content)