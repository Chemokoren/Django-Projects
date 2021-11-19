from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm, SnippetForm


# formsets 
from django.forms import modelformset_factory
from .models import FormsetExample

def contact(request):
	# form =None

	if request.method == 'POST':
		form = ContactForm(request.POST)

		if form.is_valid():

			name = form.cleaned_data['name']
			email = form.cleaned_data['email']

			print(name, email)
		else:
			form = ContactForm()
		return render(request,'form.html', {'form':form})

def snippet_detail(request):

	if request.method == 'POST':

		form = SnippetForm(request.POST)

		if form.is_valid():
			print("VALID")
			name = form.cleaned_data['name']
			body = form.cleaned_data['body']
			print(name, ":" ,body)
			form.save()
			

	form = SnippetForm()
	return render(request, 'form.html',{'form':form})

def formset_example(request):

	ExampleFormSet = modelformset_factory(FormsetExample, fields=('name','location'), extra=4)

	# returns nothing
	# form = ExampleFormSet(queryset=FormsetExample.objects.none()) 

	# save all the values
	if request.method == 'POST':
		form = ExampleFormSet(request.POST)
		form.save()

	# save them individually
	# if request.method == 'POST':
	# 	form = ExampleFormSet(request.POST)
	# 	instances = form.save(commit=False)

	# 	for instance in instances:
	# 		instance.save()


	form = ExampleFormSet()

	context={
	'form':form
	}

	return render(request, 'index.html', context)

