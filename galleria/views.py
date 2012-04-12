from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from galleria.models import Gallery
from galleria.forms import CreateForm


def home(request):
    context = RequestContext(request)
    return render(request, 'home.html', context_instance=context)

def gallery_list(request):
    context = RequestContext(request, { 'galleries': Gallery.objects.all()})
    return render(request, 'list.html', context_instance=context)
    
def my_galleries(request):
    context = RequestContext(request, { 'galleries': Gallery.objects.all().filter(user=request.user)})
    return render(request, 'my_galleries.html', context_instance=context)

def create(request):
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("my_galleries"))
        else:
            print form.__errors
            return redirect(reverse("create_gallery"))
    else:
        form = CreateForm()
    context = RequestContext(request, { 'form': form})
    return render(request, 'create.html', context_instance=context)

def add_image(request):
    pass