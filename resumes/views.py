from resumes.models import ResumeModel
from django.shortcuts import render

# Create your views here.
def resume_list(request):
    # 1. Fetch all resumes from the database
    resumes = ResumeModel.objects.all()

    # 2. Send that data to the HTML Template
    return render(request, 'resumes/resume_list.html', {'resumes':resumes})