
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from common.utils import log
from django.core.mail import mail_admins

from . models import Account
from . forms import AccountAvatarForm

@login_required
def avatar(request, template_name = 'account/general/avatar.html'):

    user = User.objects.get( pk = request.user.id )

    account = ''

    try:
        account = Account.objects.get(user=user)
    except Account.DoesNotExist:
        pass

    if account:
        form = AccountAvatarForm(initial={'user': user}, instance=account)
    else:
        form = AccountAvatarForm(initial={'user': user})

    if request.method == "POST":
        if account:
            form = AccountAvatarForm(request.POST, request.FILES, initial={'user': user}, instance=account)
        else:
            form = AccountAvatarForm(request.POST, request.FILES, initial={'user': user})

        if form.is_valid():
            form.save()
            if settings.IN_PRODUCTION:
#                mail_admins('user updated avatar', 'user %(user)s uploaded avatar %(avatar)r' % {'user': user.id, 'avatar': account.x150.url})
                mail_admins('user updated avatar', 'user %(user)s uploaded avatar' % {'user': user.id,})

            return redirect('account:general-avatar')

    data = {
        'form':form,
        'account':account,
    }

    return render(request, template_name, data)

@login_required
def password(request, template_name='account/general/password.html'):

    user = get_object_or_404(User, pk=request.user.id)



#    try:
#        account = Account.objects.get(user=user)
#    except Account.DoesNotExist:
#        pass


    data = {
        'form':form,
    }
    return render(request, template_name, data)