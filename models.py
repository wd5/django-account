import uuid
from django.db import models
from django.contrib.auth.models import User

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Adjust, SmartResize, ResizeToFit

def image_upload_to( instance, filename ):
    ext = filename.split( '.' )[-1]
    filename = "%s.%s" % ( uuid.uuid4(), ext.lower() )
    id = str( instance.user.id )
    return 'account/%s/%s/%s' % ( id[:1], id, filename )


class Account(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField( upload_to = image_upload_to, blank=True, null=True, default=None )
    x50 = ImageSpecField( [
            Adjust( contrast = 1.2, sharpness = 1.1 ),
            ResizeToFit( 50, 50 )
        ],
        image_field = 'avatar',
        options = {
            'quality': 90,
            'progressive':True,
        },
    )
    x100 = ImageSpecField( [
            Adjust( contrast = 1.2, sharpness = 1.1 ),
            ResizeToFit( 100, 100 )
        ],
        image_field = 'avatar',
        options = {
            'quality': 90,
            'progressive':True,
        },
    )
    x150 = ImageSpecField( [
            Adjust( contrast = 1.2, sharpness = 1.1 ),
            ResizeToFit( 150, 150 )
        ],
        image_field = 'avatar',
        options = {
            'quality': 90,
            'progressive':True,
        },
    )