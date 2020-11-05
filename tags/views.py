import requests

from django.shortcuts import render

def index(request):
	payload = {'order':'desc', 'sort':'popular', 'site':'stackoverflow'}
	response = requests.get('https://api.stackexchange.com/2.2/tags', params=payload)
	tag_items = response.json()["items"]
	print(tag_items)
	return "ahs"#tag_items