from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class JobDescription(models.Model):
    job_id = models.CharField(primary_key=True, max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    role = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    primary_skills = models.CharField(max_length=200)
    secondary_skills = models.CharField(max_length=200)
