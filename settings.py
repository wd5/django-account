from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

@login_required
def avatar(request, template_name = 'account/settings/avatar.html'):

    data = {}

    return render(request, template_name, data)