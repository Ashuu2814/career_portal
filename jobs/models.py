from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):

    JOB_TYPES = (
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Internship', 'Internship'),
    )

    title = models.CharField(max_length=200)

    company = models.CharField(max_length=200)

    location = models.CharField(max_length=200)

    salary = models.CharField(max_length=100)

    job_type = models.CharField(
        max_length=20,
        choices=JOB_TYPES
    )

    description = models.TextField()

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title