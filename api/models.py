from django.db import models

STATUS_CHOICES = (
  ('pending', "Pendiente"),
  ('in_progress', "En Progreso"),
  ('completed', "Completada"),
)

class Task(models.Model):
  id =  models.AutoField(primary_key=True)
  title = models.CharField(max_length=100)
  description = models.TextField()
  status = models.CharField(max_length=30,choices=STATUS_CHOICES)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  due_date = models.DateField(blank=True, null=True)
  owner = models.IntegerField()
  class Meta:
    db_table = 'Task'

class Users(models.Model):
  id =  models.AutoField(primary_key=True)
  userName = models.CharField(max_length=100)
  password = models.TextField()
  created_at = models.DateTimeField()
  class Meta:
    db_table = 'Users'
