# Create your views here.
from zokiguide.decorators import render_to

@render_to( 'account/home.html' )
def home( request ):
    data = {}
    return data
