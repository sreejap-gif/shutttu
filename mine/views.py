from django.shortcuts import render
from django.http import HttpResponse

# def sh(request):
#     return HttpResponse("hiiii")

# def color(request):
#     return render(request, 'index.html')


# 💖 Home Page
def home(request):
    return render(request, 'home.html')


# 📖 Story Page
def story(request):
    return render(request, 'story.html')


# 🖼 Gallery Page
def gallery(request):
    return render(request, 'gallery.html')


# 💕 Reasons Page
def reasons(request):
    return render(request, 'reasons.html')


# 🎁 Surprise Page
def surprise(request):
    return render(request, 'surprise.html')


# 💘 Finale Page
def finale(request):
    return render(request, 'finale.html')
