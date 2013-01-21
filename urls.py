from django.conf.urls import patterns, include, url

# (?P<year>\d{4})
urlpatterns = patterns( 'account',
    url( r'^$', 'views.home', name = 'home' ),

    url( r'^blogs/$', 'blog.blogs', name = 'blogs' ),
    url( r'^addblogpost/$', 'blog.addblogpost', name = 'blog-add-post' ),
    url( r'^editblogpost/(?P<id>\d+)$', 'blog.editblogpost', name = 'blog-edit-post' ),
    url( r'^deleteblogpost/(?P<id>\d+)$', 'blog.deleteblogpost', name = 'blog-delete-post' ),

    url( r'^addblog/$', 'blog.addblog', name = 'blog-add' ),
    url( r'^editblog/(?P<id>\d+)$', 'blog.editblog', name = 'blog-edit' ),
    url( r'^deleteblog/(?P<id>\d+)$', 'blog.deleteblog', name = 'blog-delete' ),

    url(r'^general/avatar/', 'general.avatar', name='general-avatar'),
#    url(r'^general/password/', 'django.contrib.auth.views.password_change', {'template_name': 'account/general/password.html'}, name='general-password'),
 )

