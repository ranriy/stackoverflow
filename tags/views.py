from django.shortcuts import render

from .models import Tag

def display(request):
	tags = Tag.objects.all()
	labels = []
	data = []
	for tag in tags:
		labels.append(tag.name)
		data.append(float(tag.percentage))
	return render(request, 'display.html', {'labels':labels, 'data':data})