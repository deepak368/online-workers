from datetime import datetime

from django.db import models

class feedbackmodel(models.Model):
    username=models.CharField(max_length=120)
    Feedback=models.CharField(max_length=300)


class userRequest(models.Model):
    choices=[
        ("carpenter","carpenter"),
        ("plumber","plumber"),
        ("mechanic","mechanic"),
        ("construction","construction"),
        ("mining", "mining"),
        ("cook", "cook"),
        ("teacher", "teacher"),
    ]
    Work_type=models.CharField(max_length=50,choices=choices)
    user=models.CharField(max_length=120)
    start_date=models.DateField()
    end_date=models.DateField()
    Place=models.CharField(max_length=120)
    Description=models.TextField(blank=True)
    def __str__(self):
        return self.user

class workerRequest(models.Model):
    Clint=models.ForeignKey(userRequest,on_delete=models.CASCADE)
    Name=models.CharField(max_length=120)
    Mobile=models.CharField(max_length=12)
    description=models.CharField(max_length=200)
    def __str__(self):
        return self.Name


class Book(models.Model):
    Username=models.CharField(max_length=120)
    worker_name=models.ForeignKey(workerRequest,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    time=models.TimeField(auto_now_add=True)
    status = models.CharField(max_length=10, default="booked")
    def __str__(self):
        return self.worker_name

