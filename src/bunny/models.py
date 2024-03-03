from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator

class Bunny(models.Model):
    tg_id = fields.IntField(pk = True)
    invited = fields.IntField(null = True)
    coins = fields.IntField(default = 0)
    productivity = fields.IntField(default = 1)
    experience = fields.IntField(default = 1)
    endurance = fields.IntField(default = 1)
    

class Productivity(models.Model):
    value = models.IntField()
    cost = models.IntField()

class Experience(models.Model):
    value = models.IntField()
    cost = models.IntField()

class Endurance(models.Model):
    value = models.IntField()
    cost = models.IntField()

Bunny_Schema = pydantic_model_creator(Bunny, name="Bunny")