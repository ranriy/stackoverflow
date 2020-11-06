import requests

from django.shortcuts import render

from .models import Tag

def index(request):
	payload = {'order':'desc', 'sort':'popular', 'site':'stackoverflow', 'limit':50}
	response = requests.get('https://api.stackexchange.com/2.2/tags', params=payload)
	tag_items = response.json()['items']
	tag_objects = []
	print("HER")
	for tag in tag_items:
		payload = {'order':'desc', 'sort':'activity', 'tagged':tag['name'], 'site':'stackoverflow', 'filter':'total'}
		response = requests.get('https://api.stackexchange.com/2.2/questions/unanswered', params=payload)
		unanswered_questions = response.json()['total']
		print(unanswered_questions)
		tag_objects.append(Tag(name=tag['name'],asked_questions=tag['count'],unanswered_questions=unanswered_questions,percentage=0))
	Tag.objects.bulk_update_or_create(tag_objects, ['asked_questions', 'unanswered_questions'], match_field='name')
	print(tag_items)
	return "ahs"#tag_items

def display(request):
	tags = Tag.objects.all()
	labels = []
	data = []
	for tag in tags:
		labels.append(tag.name)
		data.append(float(tag.percentage))
	return render(request, 'display.html', {'labels':labels, 'data':data})