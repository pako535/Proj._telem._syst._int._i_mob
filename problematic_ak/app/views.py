from django.shortcuts import render
from django.http import HttpResponseBadRequest
from .forms import PollsForm
from .models import Person, SubjectPulse
# Create your views here.

def polls_view(request):
	if request.method == 'POST':
		form = PollsForm(request.POST)
		request.session['log_in'] = 'cycki'
		if form.is_valid():
			subject_pulse = create_subject_pulse(form.cleaned_data)
			subject_pulse.save()
			person = create_person(form.cleaned_data)
			person.save()
			return render(request, 'congratulation.html')
		else:
			return render(request, 'polls.html', {'form': form})
	elif request.method == 'GET':
		form = PollsForm()
		return render(request, 'polls.html', {'form': form})
	else:
		return HttpResponseBadRequest()


def create_person(cleaned_data, subject_pulse):
	return Person(name = cleaned_data['name'],
	              second_name = cleaned_data['second_name'],
	              last_name = cleaned_data['last_name'],
	              index = cleaned_data['index'],
	              date_of_birth = cleaned_data['date_of_birth'],
	              email = cleaned_data['email'],
	              phone_number = cleaned_data['phone_number'],
	              city = cleaned_data['city'],
	              address = cleaned_data['address'],
	              subject_pulse = subject_pulse)

def create_subject_pulse(cleaned_data):
	return SubjectPulse(subject = cleaned_data['subject'],
	                    pulse = cleaned_data['pulse'])