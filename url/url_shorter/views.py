from django.shortcuts import get_object_or_404, render

from .models import Shorter
from .form import ShorterForm
# Create your views here.


from django.http import Http404, HttpResponse, HttpResponseRedirect

def home_view(request):

    template = 'home.html'
    context = {}
    context['form'] = ShorterForm

    if request.method == "GET":
        return render(request,template,context)
    
    elif request.method =="POST":
        used_form =ShorterForm(request.POST)

        if used_form.is_valid():
            shorter_obj = used_form.save()
            new_url = request.build_absolute_uri('/') + shorter_obj.short_url
            long_url = shorter_obj.long_url

            context['new_url'] = new_url
            context['long_url'] =long_url

            return render(request,template,context)

        context['errors'] = used_form.errors

        return render(request,template,context)


def redirect_url_view(request ,shorter_part):
    try:
        shorter = Shorter.objects.get(short_url=shorter_part)
        shorter.times_followed +=1

        shorter.save()

        return HttpResponseRedirect(shorter.long_url)

    except:
        raise Http404('Sorry this link is broken :(')
        
        
