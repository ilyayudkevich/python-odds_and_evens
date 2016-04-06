from django.db import models

class Action(models.Model):
  name = models.CharField(max_length = 10)
  iname = models.IntegerField()
  def __iname__(self):
    return self.iname
  def __str__(self):
    return self.name
    

class Result(models.Model):
  name = models.CharField(max_length = 10)
  iname = models.IntegerField()
  def __str_(self):
    return self.name

class Player1Action(models.Model):
  actionid = models.ForeignKey(Action, on_delete = models.CASCADE)
  iname = models.IntegerField()
  def __actionid__(self):
    return self.actionid

class Player2Action(models.Model):
  actionid = models.ForeignKey(Action, on_delete = models.CASCADE)
  iname = models.IntegerField()
  def __actionid__(self):              
      return self.actionid

class GameResultsDisplay(models.Model):
  action1 = models.CharField(max_length = 10)
  result1 = models.CharField(max_length = 10)
  action2 = models.CharField(max_length = 10)
  result2 = models.CharField(max_length = 10)

  def __str__(self):
    return self.action1
  def __str__(self):
    return self.result1
  def __str__(self):
    return self.action1
  def __str__(self):
    return self.result1

  def save(self, *args, **kwargs):
    super(GameResultsDisplay, self).save(*args, **kwargs)


