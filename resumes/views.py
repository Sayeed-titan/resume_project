from django.shortcuts import redirect
from resumes.forms import ResumeForm
from resumes.models import ResumeModel
from django.shortcuts import render

# Create your views here.
def resume_list(request):
    # 1. Fetch all resumes from the database
    resumes = ResumeModel.objects.all()

    # 2. Send that data to the HTML Template
    return render(request, 'resumes/resume_list.html', {'resumes':resumes})


    # --- NEW CREATE VIEW ---
def resume_create(request):
    # If the user clicked the "Submit" button...
    if request.method == 'POST':
        # Grab the text data (request.POST) AND the image file (request.FILES)
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() # Save it to the SQLite database
            return redirect('resume_list') # Send them back to the homepage
    else:
        # If they just visited the page normally, show a blank form
        form = ResumeForm()
        
    return render(request, 'resumes/resume_form.html', {'form': form})