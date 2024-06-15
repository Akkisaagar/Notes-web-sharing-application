from django.db import models
from django.contrib.auth.models import User



class Signup(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    contact = models.IntegerField(null=True)
    year = models.CharField(max_length=10,null=True)
    stream = models.CharField(max_length=30,null=True)
    role = models.CharField(max_length=7,null=True)
    roll = models.IntegerField(null=True)
    
    def __str__(self):
        return self.user.username
    
class Notes(models.Model):
 user = models.ForeignKey(User,on_delete=models.CASCADE)
 uploadingdate = models.DateField(max_length=30,null=True)
 stream = models.CharField(max_length=30,null=True)
 year = models.CharField(max_length=10,null=True)
 subject = models.CharField(max_length=30,null=True)
 notesfile = models.FileField(null=True)
 filetype = models.CharField(max_length=30,null=True)
 description = models.CharField(max_length=300,null=True)
 status = models.CharField(max_length=15,null=True)
 
    
 def __str__(self):
      return self.user.username+ " "+self.status
    
    