import requests

from django.core.management.base import BaseCommand, CommandError
from tags.models import Tag

class Command(BaseCommand):

	def handle(self, *args, **options):
		payload = {'order':'desc', 'sort':'popular', 'site':'stackoverflow', 'pagesize':50}
		tag_objects = []
		try:
			response = requests.get('https://api.stackexchange.com/2.2/tags', params=payload)
			tag_items = response.json()['items']

			for tag in tag_items:
				payload = {'order':'desc', 'sort':'activity', 'tagged':tag['name'], 'site':'stackoverflow', 'filter':'total'}
				response = requests.get('https://api.stackexchange.com/2.2/questions/unanswered', params=payload)
				unanswered_questions = response.json()['total']
				percentage = round(unanswered_questions/tag['count']*100, 2)
				tag_objects.append(Tag(name=tag['name'],asked_questions=tag['count'],unanswered_questions=unanswered_questions,percentage=percentage))
		except Exception as e:
			raise


		Tag.objects.bulk_update_or_create(tag_objects, ['asked_questions', 'unanswered_questions', 'percentage'], match_field='name')

		self.stdout.write(self.style.SUCCESS('Successfully updated the database'))
