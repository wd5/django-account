
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from common.utils import log
from django.contrib.auth import get_user_model
from . models import Account
from . forms import AccountAvatarForm

@login_required
def avatar(request, template_name = 'account/settings/avatar.html'):

    user = User.objects.get( pk = request.user.id )

    form = AccountAvatarForm(initial={'user':user})

    if request.method == "POST":
        form = AccountAvatarForm( request.POST, request.FILES )
        if form.is_valid():
            form.save()

    account = ''
    try:
        account = Account.objects.get(user=user)
    except:
        pass

    log('account')
    log(str(account))

    data = {
        'form':form,
        'account':account,
    }

    return render(request, template_name, data)