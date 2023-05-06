class CSVSticker:
    def __init__(self, id_, name, content) -> None:
        self.id = id_
        self.name = name
        self.content = content
        
    def __str__(self):
        return f"| id: {self.id} | name: {self.name} | content: {self.content} |"