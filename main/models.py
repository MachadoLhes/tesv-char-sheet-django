from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Character(models.Model):
    personality_validators = [MinValueValidator(0),MaxValueValidator(10)]

    player = models.OneToOneField(User, on_delete=models.CASCADE)

    # Characteristics
    name = models.CharField(max_length=40,blank=False,null=False)
    race = models.CharField(max_length=30,blank=False,null=False)
    sex = models.CharField(max_length=10,blank=False,null=False)
    age = models.IntegerField(blank=True,null=True)
    birthsign = models.CharField(max_length=10,blank=True,null=True)
    char_class = models.CharField(max_length=20,blank=True,null=True)
    hometown = models.CharField(max_length=30,blank=True,null=True)
    backstory = models.TextField(max_length=560,blank=True,null=True)
    disposition = models.CharField(max_length=30,blank=True,null=True)

    # Personality
    violence = models.IntegerField(blank=False,null=False,default=5,validators=personality_validators)
    passivity = models.IntegerField(blank=False,null=False,default=5,validators=personality_validators)
    selfishness = models.IntegerField(blank=False,null=False,default=5,validators=personality_validators)
    compliance = models.IntegerField(blank=False,null=False,default=5,validators=personality_validators)
    trust = models.IntegerField(blank=False,null=False,default=5,validators=personality_validators)
    empathy = models.IntegerField(blank=False,null=False,default=5,validators=personality_validators)
    likes = models.TextField(max_length=280,blank=True,null=True)
    deslikes = models.TextField(max_length=280,blank=True,null=True)

    # Combat
    weapons = models.TextField(max_length=280,blank=True,null=True)
    spells = models.TextField(max_length=280,blank=True,null=True)
    armor = models.TextField(max_length=280,blank=True,null=True)
    forbidden_equip = models.TextField(max_length=280,blank=True,null=True)
    forbidden_magic = models.TextField(max_length=280,blank=True,null=True)

    # Affiliations
    worship = models.TextField(max_length=280,blank=True,null=True)
    factions = models.TextField(max_length=280,blank=True,null=True)
    forbidden_factions = models.TextField(max_length=280,blank=True,null=True)

    # Afflictions
    deseases = models.TextField(max_length=280,blank=True,null=True)
    handicaps = models.TextField(max_length=280,blank=True,null=True)

    def __str__(self):
        return self.name