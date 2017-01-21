from django.db import models

class CardSet(models.Model):
    name = models.CharField(max_length=30)

class HeroClass(models.Model):
    class_name = models.CharField(max_length=50, db_column='Name')
    description = models.CharField(max_length=200)

class HeroicTeam(models.Model):
    team_name = models.CharField(max_length=50, db_column='Name')
    description = models.CharField(max_length=200)

class Hero(models.Model):
    name = models.CharField(max_length=30)
    static_folder = models.CharField(max_length=20)
    hero_team = models.ForeignKey(HeroicTeam, models.SET_NULL, null=True)
    card_set = models.ForeignKey(CardSet)

class HeroCard(models.Model):
    major_text = models.CharField(max_length=50)
    cost = models.PositiveSmallIntegerField()
    base_recruit = models.PositiveSmallIntegerField()
    base_attack = models.PositiveSmallIntegerField()
    quantity = models.PositiveSmallIntegerField()
    card_file_name = models.CharField(max_length=20)
    hero = models.ForeignKey(Hero)
    hero_class = models.ManyToManyField(HeroClass, db_table='cards_herocard_heroclass')
