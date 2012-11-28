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
def addblogpost( request ):
    from blogs.models import BlogsPost

    if request.session.get( 'blogs-post-draft-id', '' ) and int( request.session['blogs-post-draft-id'] ) > 0:
        return redirect( 'account-editblogpost', id = request.session['blogs-post-draft-id'] )
    else:
        post = BlogsPost( status = 'draft', author = User.objects.get( pk = request.user.id ) )
        post.save()
        request.session['blogs-post-draft-id'] = post.id
        return redirect( 'account-editblogpost', id = post.id )

@login_required
def editblogpost( request, id ):
    from blogs.models import BlogsBlog, BlogsPost
    from blogs.forms import BlogsPostEditForm, BlogsImageUploadForm

    id = int( id )

    try:
        post = BlogsPost.objects.get( pk = id )
    except BlogsPost.DoesNotExist:
        raise Http404

    user = User.objects.get( pk = request.user.id )

    form = BlogsPostEditForm( instance = post )

    data = {
        'post':post,
        'image_upload_form':BlogsImageUploadForm( initial = {'post':post} ),
        'form':form,
    }
    return render( request, 'account/edit-post.html', data )


@login_required
def deleteblogpost( request, id ):
    data = {}
    return render( request, 'account/list-blogs.html', data )

@login_required
def addblog( request ):
    from blogs.models import BlogsBlog

    if request.session.get( 'blogs-blog-draft-id', '' ) and int( request.session['blogs-blog-draft-id'] ) > 0:
        return redirect( 'account-editblog', id = request.session['blogs-blog-draft-id'] )
    else:
        blog = BlogsBlog( 
            author = User.objects.get( 
                pk = request.user.id
            )
        )
        blog.save()
        request.session['blogs-blog-draft-id'] = blog.id
        return redirect( 'account-editblog', id = blog.id )

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

