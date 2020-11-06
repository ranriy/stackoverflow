from django.db import models
from bulk_update_or_create import BulkUpdateOrCreateQuerySet

class Tag(models.Model):
	name = models.CharField(max_length=50, primary_key=True)
	unanswered_questions = models.IntegerField()
	asked_questions = models.IntegerField()
	percentage = models.DecimalField(max_digits=10,decimal_places=3)
	
	objects = BulkUpdateOrCreateQuerySet.as_manager()