from django.shortcuts import render

from django.shortcuts import render
from django.forms import modelformset_factory
from .models import Example

def index(request):
	ExampleFormSet = modelformset_factory(Example, fields=('name','location',), extra=3,)

	if request.method == 'POST':
		form =ExampleFormSet(request.POST)
		form.save()
		# save individually
		#instances = form.save(commit=False)

		#for instance in instances:
		#	instance.save()


	#form =ExampleFormSet(queryset=Example.objects.none())

	form =ExampleFormSet()
	return render(request, 'index.html',{'form': form})
