from django.db import models
from django.utils import timezone
# models.py

from django.db import models
class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=100)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=15)

    def __str__(self):
        return "%s " %(self.ename)
    class Meta:
        db_table = "employee"
class Appointment(models.Model):
    parent_name = models.CharField(max_length=255)
    child_name = models.CharField(max_length=50)
    appointment_date = models.DateField()
    appointment_type = models.CharField(max_length=50, choices=[
        ('home_babysitter', 'Home Babysitter'),
        ('home_tutor', 'Home Tutor'),
        ('school_babysitter', 'School Babysitter'),
        ('school_tutor', 'School Tutor'),
        ('home_playbuddy', 'Home Playbuddy'),
        ('course_program', 'Course/Program'),
       ],
        default='home_babysitter'  # Choose the default value you prefer
    )
    duration = models.PositiveIntegerField()
    payment_option = models.CharField(max_length=20, choices=[
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('cash', 'Cash'),
    ],
                                      default='credit_card'
                                      )
    amount_to_pay = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.parent_name} - {self.appointment_type}"





class Child(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()



class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    image = models.ImageField(upload_to='images', default='profile.png')

    def __str__(self):
        return self.name

class Hero(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    button1_text = models.CharField(max_length=50)
    button1_link = models.URLField()
    button2_text = models.CharField(max_length=50)
    button2_link = models.URLField()

    def __str__(self):
        return self.title




class About(models.Model):
    video_url = models.URLField()
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Service(models.Model):
    icon_class = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Program(models.Model):
    image = models.ImageField(upload_to='program_images/')
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    title = models.CharField(max_length=255)
    description = models.TextField()
    teacher_name = models.CharField(max_length=255)
    teacher_role = models.CharField(max_length=255)
    seats = models.IntegerField()
    lessons = models.IntegerField()
    hours = models.IntegerField()

    def __str__(self):
        return self.title

class Event(models.Model):
        image = models.ImageField(upload_to='event_images/')
        date = models.DateField()
        time = models.CharField(max_length=255)
        location = models.CharField(max_length=255)
        title = models.CharField(max_length=255)
        description = models.TextField()

        def __str__(self):
            return self.title

class Blog(models.Model):
    image = models.ImageField(upload_to='blog_images/')
    date = models.DateField()
    author_name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()
    comments_count = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    image = models.ImageField(upload_to='team_images/')
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    image = models.ImageField(upload_to='testimonial_images/')
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    rating = models.PositiveIntegerField()
    content = models.TextField()

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name="Student Name")
    email = models.EmailField(max_length=277, verbose_name="Student Email")


    def __str__(self):
        return str(self.id)
