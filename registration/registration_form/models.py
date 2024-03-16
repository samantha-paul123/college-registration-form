# from django.db import models

# class UserDetails(models.Model):
#     Name = models.CharField(max_length=100)
#     Email = models.CharField(max_length=100)
#     Gender = models.CharField(max_length=10)
#     Lang = models.CharField(max_length=50)  # Renamed to Lang to follow PEP8 naming convention
#     Ph_no = models.CharField(max_length=10)  
#     Age = models.IntegerField()  

#     class Meta:
#         db_table = "User_info";

from django.db import models

# Create your models here.


class userdetails(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Gender=models.CharField(max_length=10)
    lang=models.CharField(max_length=50)
    ph_no=models.IntegerField(max_length=10)
    age=models.IntegerField(max_length=2)

    class Meta:
        db_table="User_info"
