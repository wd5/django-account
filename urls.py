from django.conf.urls import patterns, include, url

# (?P<year>\d{4})
urlpatterns = patterns( 'account',
    url( r'^$', 'views.home', name = 'account-home' ),

    url( r'^blogs/$', 'blog.blogs', name = 'account-blogs' ),
    url( r'^addblogpost/$', 'blog.addblogpost', name = 'account-addblogpost' ),
    url( r'^editblogpost/(?P<id>\d+)$', 'blog.editblogpost', name = 'account-editblogpost' ),
    url( r'^deleteblogpost/(?P<id>\d+)$', 'blog.deleteblogpost', name = 'account-deleteblogpost' ),

    url( r'^addblog/$', 'blog.addblog', name = 'account-addblog' ),
    url( r'^editblog/(?P<id>\d+)$', 'blog.editblog', name = 'account-editblog' ),
    url( r'^deleteblog/(?P<id>\d+)$', 'blog.deleteblog', name = 'account-deleteblog' ),
 )

