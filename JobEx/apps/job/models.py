from django.db import models
from apps.payment_period.models import PaymentPeriod

# Create your models here.
class Job(models.Model):
    company_name = models.CharField(max_length=200, blank=True, null=True)
    company_website = models.URLField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()
    responsibilities = models.TextField()
    qualifications = models.TextField()
    salary = models.PositiveBigIntegerField(blank=True, null=True)
    payment_period = models.ForeignKey(PaymentPeriod, on_delete=models.SET_NULL, null=True, blank=True)
    location = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    posted_date = models.DateTimeField(auto_now_add=True)
    application_deadline = models.DateTimeField()

    def __str__(self):
        return str(self.title) + " - " + str(self.location)

    class Meta:
        ordering = ['-posted_date']
        verbose_name = "Job"
        verbose_name_plural = "Jobs"