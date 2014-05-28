from django.shortcuts import render
from django.http import HttpResponse,HttpResponsePermanentRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, Context, loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login,logout

from register.forms import RegisterForm,RegistrationForm

def _render_to_response(page, request, args=None):
    return render_to_response(page, RequestContext(request, args))

def index_view(request):
    return render(request,'register/index.html')

def enrollment(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = RegisterForm()
    return render(request,'enrollment/create.html',{'form':form,})

#@login_required
def contact_view(request):
    return render(request,'register/contact.html')

def account_create_view(request, **args):
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data['username'], # XXX: this will get truncated
                password = form.cleaned_data['password'],
                email    = form.cleaned_data['username'],
            )

            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()

            if settings.SEND_EMAIL:

                template = loader.get_template('e-mails/user/create.txt')
                body = template.render(Context({'user': user, 'conf_name_upper': settings.CONF_NAME_UPPER, 'conf_year': settings.CONF_YEAR, 'conf_web': settings.CONF_WEB}))

                user.email_user("[%(conf_name_upper)s %(conf_year)s] Account Creation Notification" % {'conf_name_upper': settings.CONF_NAME_UPPER, 'conf_year': settings.CONF_YEAR}, body)

                template = loader.get_template('e-mails/admin/create.txt')
                body = template.render(Context({'user': user}))

                mail_admins("[ADMIN] New Account", body)

            return HttpResponsePermanentRedirect('/account/create/success/')
    else:
        form = RegistrationForm()

    local_args = {'form': form }

    return _render_to_response('account/create.html', request, local_args)

def account_login_view(request):
    next = request.path
    
    login(request)
    return render(request,'account/login.html',{'next':next})

@login_required
def account_logout_view(request, **args):
    logout(request)

    return HttpResponsePermanentRedirect('/')

def about_view(request):
    return render(request,'courses/karel.html')

def nclab_view(request):
    return render(request,'nclab/results.html')

def handler404(request):
    return _render_to_response('errors/404.html', request)

def handler500(request):
    return _render_to_response('errors/500.html', request)