from django.forms.models import inlineformset_factory
from django.shortcuts import render,redirect
from .models import Programmer, Language
from django.forms import modelformset_factory,inlineformset_factory

# modelformset_factory
# def indexView(request, programmer_id):
# 	programmer =Programmer.objects.get(pk=programmer_id)

# 	LanguageFormset = modelformset_factory(Language, fields=('name',))

# 	if request.method == 'POST':
# 		print("aaa:",request.POST)
# 		formset = LanguageFormset(request.POST, queryset=Language.objects.filter(programmer_id=programmer.id))
# 		if formset.is_valid():
# 			instances = formset.save(commit=False)
# 			for instance in instances:
# 				instance.programmer_id =programmer.id
# 				instance.save()
# 			return redirect('index-view', programmer_id=programmer.id)

# 	formset = LanguageFormset(queryset=Language.objects.filter(programmer_id=programmer.id))

# 	return render(request, 'modelformset/index.html', {'formset': formset})
	
# inlineformset_factory

def indexView(request, programmer_id):
	programmer =Programmer.objects.get(pk=programmer_id)

	LanguageFormset = inlineformset_factory(Programmer,Language, fields=('name',))

	if request.method == 'POST':
		formset =LanguageFormset(request.POST, instance=programmer)
		if formset.is_valid():
			formset.save()
		return redirect('index-view', programmer_id=programmer.id)

	formset = LanguageFormset(instance=programmer)

	return render(request, 'modelformset/index.html', {'formset': formset})

