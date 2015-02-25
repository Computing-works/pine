from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    
    user = models.ForeignKey(User, unique=True)

    affiliation = models.CharField(max_length=100)

    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    speaker = models.CharField(max_length=1)
    student = models.CharField(max_length=1)
    postconf = models.CharField(max_length=1)
    vegeterian = models.CharField(max_length=1)

    arrival = models.DateField()
    departure = models.DateField()

    accompanying = models.IntegerField()

    tshirt = models.CharField(max_length=3)

    payment = models.CharField(max_length=30, blank=True)
    remark = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return u"Profile for %s" % self.user.get_full_name()
    
class Kid(models.Model):
    user = models.OneToOneField(User)
    
    def __unicode__(self):
        return self.name
    


