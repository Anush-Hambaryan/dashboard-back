from django.db import models
from accounts.models import CustomUser


class GenericJob(models.Model):

    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class StandardJob(GenericJob):

    JOB_TYPE_CHOICES = (
        (1, 'Job 1'),
        (2, 'Job 2'),
        (3, 'Job 3'),
        (4, 'Job 4'),
    )
    job_type = models.CharField(max_length=1, choices=JOB_TYPE_CHOICES, blank=False, null=False)

    address = models.CharField(max_length=500, blank=False, null=False)

    STATUS_CHOICES = (
        ('sold', 'Sold'),
        ('available', 'Available'),
    )
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, blank=False, null=False)

    def __str__(self):
        return str(self.id)


class Job5(GenericJob):
    SHAPE_CHOICES = (
        ('polygon', 'Polygon'),
        ('circle', 'Circle'),
    )
    shape = models.CharField(max_length=7, choices=SHAPE_CHOICES, blank=False, null=False)
    radius = models.DecimalField(max_digits=15, decimal_places=6, blank=True, null=True) #blank for polygon

class Coords(models.Model):
    standard_owner = models.ForeignKey(StandardJob, on_delete=models.CASCADE, related_name='coords_stantdard_job', blank=True, null=True)
    job5_owner = models.ForeignKey(Job5, on_delete=models.CASCADE, related_name='coords_job5', blank=True, null=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, blank=False, null=False)
    lng = models.DecimalField(max_digits=9, decimal_places=6, blank=False, null=False)



