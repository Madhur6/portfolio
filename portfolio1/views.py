from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Contact
from markdown2 import Markdown
from . import util

# Create your views here.
def index(request):
    getInTouch = request.session.pop('getInTouch', None)
    return render(request, "portfolio1/index.html", {
        "getInTouch": getInTouch,
    })

def contact(request):
    if request.method == "GET":
        return render(request, "portfolio1/contact.html")
    
    elif request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        telephone = request.POST['telephone']
        comment = request.POST['comment']

        contact = Contact(name=name, email=email, phone=telephone, feedback=comment)
        contact.save()

        request.session['getInTouch'] = "Thank you for getting in touch! I will reach out to you soon!"
        return HttpResponseRedirect(reverse("index"))


def project(request):
    return render(request, "portfolio1/project.html", {
        "entries": util.list_entries()
    })
    
def detail(request, TITLE):
    title = util.get_entry(TITLE)

    redirect_url = reverse("project")
    
    if title is None:
        return render(request, "portfolio1/error.html", {
            "message": "request not found!",
            "redirect_url": redirect_url
        })
    
    return render(request, "portfolio1/detail.html", {
        "title": TITLE,
        "content": markdown(title),
        "redirect_url": redirect_url
        })

def markdown(content):
    markdowner = Markdown()
    return markdowner.convert(content)