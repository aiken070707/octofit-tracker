from django.db import models
from django.conf import settings


class Activity(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	activity_type = models.CharField(max_length=100)
	duration_minutes = models.PositiveIntegerField()
	distance_km = models.FloatField(null=True, blank=True)
	calories = models.PositiveIntegerField(null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return f"{self.user} — {self.activity_type} ({self.duration_minutes} min)"
