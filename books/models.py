from django.db import models

class Book(models.Model):
  title = models.CharField(max_length=250) 
  subtitle = models.CharField(max_length=250) 
  author = models.CharField(max_length=100) 
  isbn = models.CharField(max_length=13)
  publication_date = models.DateField()
  status = models.BooleanField()
  created_at = models.DateField()
  updated_at = models.DateField()
  
def __str__(self): 
  return self.title