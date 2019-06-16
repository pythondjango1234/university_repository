from django.db import models
from multiselectfield import MultiSelectField

class Feedbackdata(models.Model):
    name=models.CharField(max_length=100)
    rating=models.IntegerField()
    date=models.DateField()
    feedback=models.TextField(max_length=1000)

class ContactData(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.BigIntegerField()

    COURSES_CHOICES=(
        ('py','Python'),
        ('dj','Django'),
        ('ui','UI'),
        ('rest','REST API')
    )

    courses=MultiSelectField(max_length=200, choices=COURSES_CHOICES)

    SHIFTS_CHOICES=(
        ('mrg','Morning'),
        ('aftrn','Afternoon'),
        ('evng','Evening'),
        ('night','Night')
    )
    shifts=MultiSelectField(max_length=200,choices=SHIFTS_CHOICES)

    LOCATIONS_CHOICES=(
        ('hyd','Hyderbad'),
        ('bang','Banglore'),
        ('pune','pune'),
        ('chn','Chennai')

    )
    locations= MultiSelectField(max_length=200,choices=LOCATIONS_CHOICES)

    gender=models.CharField(max_length=50)
    start_date=models.DateField(max_length=100)

class CoursesData(models.Model):
    course_id=models.IntegerField()
    course_name=models.CharField(max_length=100)
    course_dur=models.IntegerField()
    course_fee=models.IntegerField()
    start_date=models.DateField(max_length=100)
    start_time=models.TimeField(max_length=100)
    trainer_name=models.CharField(max_length=100)
    trainer_exp=models.IntegerField()

