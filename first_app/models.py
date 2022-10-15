from django.db import models
import re
import datetime
from django import forms

# ------------------------------
#   > Vaildation of Driver <
# ------------------------------


class DriverManager(models.Manager):
     def basic_validator(self, postData):
        errors = {}
        if len(postData['fullname']) < 10:
            errors["fullname"] = "Your name should be at least 10 characters"
        if postData['birthday'] > str(datetime.date(2004, 1, 1)):  
            errors["birthday"] = "Your Age Must be more than  or equal 18"
        if postData['cpassword']!=postData['password']:
            errors["cpassword"] = "The Password doesnt match"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):            
            errors['email'] = "Invalid email format"
        if len(postData['password']) < 8:
            errors["password"] = "The Password should be at least 8 characters"
        PHONE_REGEX=re.compile(r'^05(9[987542]|6[982])\d{6}$')
        if not PHONE_REGEX.match(postData['phonenumber']):
            errors['phonenumber'] = "Invalid Number"
        if postData['nid'] == "":
            errors['nid'] = "nid required"


        return errors

class Driver(models.Model):
    full_name=models.CharField(max_length=30)
    birthday=models.DateField()
    notional_id=models.IntegerField(null=True)
    city=models.CharField(max_length=30)
    blood_type=models.CharField(max_length=4)
    email=models.CharField(max_length=40)
    password=models.CharField(max_length=20)
    phone_number=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='images',blank=True,null=True)
    objects=DriverManager()

    
# ------------------------------
#   > Vaildation of Police <
# ------------------------------

class PoliceManager(models.Manager):
     def basic_validator2(self, postData):
        errors = {}
        if len(postData['fullname']) < 10:
            errors["fullname"] = "Your name should be at least 10 characters"
        if postData['cpassword']!=postData['password']:
            errors["cpassword"] = "The Password doesnt match"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):            
            errors['email'] = "Invalid email format"
        if len(postData['password']) < 8:
            errors["password"] = "The Password should be at least 8 characters"
        PHONE_REGEX=re.compile(r'^05(9[987542]|6[982])\d{6}$')
        if not PHONE_REGEX.match(postData['phonenumber']):
            errors['phonenumber'] = "Invalid Number"
        return errors

class Police(models.Model):
    full_name=models.CharField(max_length=30)
    birthday=models.DateField()
    city=models.CharField(max_length=30)
    email=models.CharField(max_length=40)
    password=models.CharField(max_length=20)
    phone_number=models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=PoliceManager()

# ------------------------------
#   > Vaildation of Violation <
# ------------------------------

class ViolationManager(models.Manager):
    def basic_validator3(self, postData):
        errors = {}
        if len(postData['location']) > 60:
            errors["location"] = "Your location character should be no more 60 characters"

        if int(postData['fees']) > 5000 or postData['fees'] == "":
            errors["fees"] = "Your fees  should be no more than 5000 shekal"

        if len(postData['reason']) > 100:
            errors["reason"] = "Your reason should not exceeded it more than 100 character"

        if postData['ex_date'] < str(datetime.date.today()):
            errors["ex_date"] = "The date should be at modern"

        if postData['violation_date'] > str(datetime.date.today()):
            errors["violation_date"] = "The date should be at past"
        return errors

class Violation(models.Model):
    location=models.CharField(max_length=60)
    violation_date=models.DateField(null=True)
    fees=models.IntegerField()
    expierd_date_violation=models.DateField(null=True)
    resson=models.CharField(max_length=120)
    driver=models.ForeignKey(Driver,related_name="dviolations", on_delete=models.CASCADE)
    police=models.ForeignKey(Police,related_name="pviolations", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20,default="Not paid",null=True)
    objects=ViolationManager()

