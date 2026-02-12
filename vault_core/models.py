from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

files = CloudinaryField(
    resource_type="auto",
    blank=True,
    null=True
)

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=20, null=True)
    
class Resources(models.Model):
    # this helps in creating architecture of a table like how our database table looks like
    # ORM converts to real table 
    owner = models.ForeignKey(User , on_delete=models.CASCADE, related_name='resources',null=True,
    blank=True)
    RESOURCE_TYPE = [
        ('png','PNG'),
        ('image','Screenshot'),
        ('link','Link'),
        ('notes','Notes')
    ] # this is list of data type a user will opt to upload 
    
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, null=True)
    
    resource_type = models.CharField(max_length=10,
                                    choices=RESOURCE_TYPE,
                                    null = True
                                    )
    
    files = models.FileField(
        upload_to = 'resources/',
        # in disk the uploaded file is stored as media/resources/screenshot.png
        blank=True,
        null=True
    )
    
    current_url = models.URLField(
        blank=True,
        null=True
    )
    
    created_at = models.DateTimeField(auto_now_add = True)
    tag = models.ManyToManyField(Tag)
    # django automatically creats an additional table where it itself create joins 
    # one resource have many tags , many resources have one tag : many to many relationship
