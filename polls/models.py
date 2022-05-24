from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.Charfield(_MAX_LENGTH-200)
    pub_date = models.DateTimeField('Date Published')
