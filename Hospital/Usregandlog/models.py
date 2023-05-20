from django.db import models


# Create your models here.
Sex = (
    ("1", "Male"),
    ("2", "Female"),
    ("3", "Others"),
)

class Register(models.Model):
    name = models.CharField(max_length=50)
    Father_name = models.CharField(max_length=200)
    DOB = models.DateField()
    sex = models.CharField(max_length=6,choices=Sex)
    phone_num = models.CharField(max_length=10)
    finger_print = models.ImageField(max_length=10000)
    created = models.DateTimeField(auto_now_add=True) # snap when it was created

    def __str__(self):
        return self.name
