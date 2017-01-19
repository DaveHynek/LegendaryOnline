from django.db import models

class Set(models.Set):
	name = models.CharField(max_length=50)

class Hero(models.Model):
	name = models.CharField(max_length=50)
	set = models.ForeignKey(Set)

class HeroCard(models.Model):
	major_text = models.CharField(max_length=100)
	cost = models.PositiveSmallIntegerField()
	base_recruit = models.PositiveSmallIntegerField()
	base_attack = models.PositiveSmallIntegerField()
	quantity = models.PositiveSmallIntegerField()
	hero = models.ForeignKey(Hero)
	hero_team = models.ForeignKey(HeroicTeam)
	hero_class = models.ManyToManyField(HeroClass)

class HeroClass(models.Model):
    class_name = models.CharField(max_length=50, db_column='Name')

class HeroicTeam(models.Model):
    team_name = models.CharField(max_length=50, db_column='Name')