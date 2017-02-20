from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import hashers
from django.template import loader
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User

from .forms.userForm import UserForm


def register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST, prefix='user')
        if uf.is_valid():
            user = uf.save(commit=False)
            user.password = hashers.make_password(uf.cleaned_data['password'])
            user.save()
            return HttpResponseRedirect('sent')
        else:
            template = loader.get_template('users/registerUser.html')
            context = {'user_form': uf}
            return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template('users/registerUser.html')
        context = {'user_form': UserForm(prefix='user')}
        return HttpResponse(template.render(context, request))


def sent(request):
    template = loader.get_template('users/confirmSent.html')
    return HttpResponse(template.render({}, request))


