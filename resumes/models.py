from django.db import models

class ResumeModel(models.Model):
    # 1. Personal Details
    full_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    summary = models.TextField(help_text="Short personal objective")

    # 2. Education Details
    degree = models.CharField(max_length=100)
    institute_name = models.CharField(max_length=150)
    year_of_graduation = models.IntegerField()

    # 3. Experience Details
    company_name = models.CharField(max_length=150)
    position = models.CharField(max_length=100)
    years_of_experience = models.IntegerField()

    # 4. Skills & Additional Info (comma-separated)
    skills = models.TextField(help_text="Comma-separated skills (e.g. Python, Django, SQL)")
    hobbies = models.TextField(help_text="Comma-separated hobbies")
    achievements = models.TextField(help_text="Comma-separated achievements")

    # Optional metadata: stores when this resume was created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name