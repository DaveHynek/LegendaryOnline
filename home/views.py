from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name=None)
def home(request):
    template = loader.get_template('home/home.html')

    context = {}
    return HttpResponse(template.render(context, request))
