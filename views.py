from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.db.models import ObjectDoesNotExist
from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
@login_required
def home( request ):
    data = {}
    return render( request, 'account/home.html', data )


@login_required
def blogs( request ):
    from blogs.models import BlogsBlog

    blogs = BlogsBlog.objects.filter( 
        author = User.objects.get( 
            pk = request.user.id
        )
    )

    data = {
        'blogs':blogs
    }
    return render( request, 'account/list-blogs.html', data )

@login_required
def addblog( request ):
    from blogs.models import BlogsBlog

    if request.session.get( 'blogs-blog-draft-id', '' ) and int( request.session['blogs-blog-draft-id'] ) > 0:
        return redirect( 'account:blog-edit', id = request.session['blogs-blog-draft-id'] )
    else:
        blog = BlogsBlog( 
            author = User.objects.get( 
                pk = request.user.id
            )
        )
        blog.save()
        request.session['blogs-blog-draft-id'] = blog.id
        return redirect( 'account:blog-edit', id = blog.id )

@login_required
def editblog( request, id ):
    from blogs.models import BlogsBlog
    from blogs.forms import BlogsBlogEditForm

    id = int( id )

    try:
        blog = BlogsBlog.objects.get( pk = id )
    except BlogsBlog.DoesNotExist:
        raise Http404

    form = BlogsBlogEditForm( instance = blog )

    if request.method == "POST":
        form = BlogsBlogEditForm( request.POST, instance = blog )

        if form.is_valid():
            form.save()
            blog.status = 'active'
            blog.save()

            try:
                del request.session['blogs-blog-draft-id']
            except:
                pass

            return redirect( 'blogs-blog', id = id )

    data = {
        'form':form
    }
    return render( request, 'account/edit-blog.html', data )

@login_required
def deleteblog( request, id ):
    from blogs.models import BlogsBlog

    data = {}

    return render( request, 'account/delete-blog.html', data )

