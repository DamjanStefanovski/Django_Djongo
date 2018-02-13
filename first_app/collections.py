from mongoengine import *
class Persons(Document):
    name = StringField(required=True)
    age = IntField()
