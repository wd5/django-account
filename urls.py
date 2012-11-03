from django.conf.urls import patterns, include, url

# (?P<year>\d{4})
urlpatterns = patterns( 'account',
    url( r'^$', 'views.home', name = 'account-home' ),
 )

