import json


class Commit:

    def __init__(self, hash, author, date, message):
        self.hash = hash
        self.author = author
        self.date = date
        self.message = message

    def toJson(self):
        data = self.toDictionary()
        return json.dumps(data)

    def toDictionary(self):
        data = {}
        data['hash'] = self.hash
        data['author'] = self.author
        data['date'] = self.date
        data['message'] = self.message
        return data

    def __str__(self):
        return f"{self.hash} - {self.author} {self.date} : {self.message}"
