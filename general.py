
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from common.utils import log
from django.core.mail import mail_admins

from . models import Account
from . forms import AccountAvatarForm

@login_required
def avatar(request, template_name = 'account/settings/avatar.html'):

    user = User.objects.get( pk = request.user.id )

    account = ''
    try:
        account = Account.objects.get(user=user)
    except Account.DoesNotExist:
        pass

    form = AccountAvatarForm(initial={'user':user}, instance=account)

    if request.method == "POST":
        form = AccountAvatarForm( request.POST, request.FILES, initial={'user':user}, instance=account )
        if form.is_valid():
            form.save()
            if settings.IN_PRODUCTION:
                mail_admins('user updated avatar', 'user %(user)s uploaded avatar %(avatar)s' % {'user': user.id, 'avatar': account.x150.url})

            return redirect('account:settings-avatar')

    data = {
        'form':form,
        'account':account,
    }

    return render(request, template_name, data)