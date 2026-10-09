from django.db import models

# Create your models here.
class ResumeModel(models.Model):
    # 1. Personal Details
    full_name = models.CharField(max_length =100)
    profile_picture = models.ImageField(upload_to ='profiles/', blank = True, null = True)
    email = models.EmailField()
    phone = models.CharField(max_length = 15)
    address = models.TextField()
    summary = models.TextField(help_text = "Short personal objective")

    # 2. Education Details
    degree = models.CharField(max_length =100)
    institute_name = models.CharField(max_length =150)
    year_of_graduation = models.IntegerField()

    # 3. Experience Details
    

