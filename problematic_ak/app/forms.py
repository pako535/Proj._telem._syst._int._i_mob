from django import forms


class PollsForm(forms.Form):
	choices_list =[("", " --- "),
	               ("amk1", "Arytmetyka komputerów 1"),
	               ("ak1", "Architektura komputerów 1"),
	               ("oiak", "Organizacja i archit. komp."),
	               ("ak2", "Architektura komputerów 2")]

	name = forms.CharField(label = 'Imię',
	                       initial = "Paweł",
	                       max_length = 20,
	                       widget = forms.TextInput(attrs = {'class': 'inputs'}))

	second_name = forms.CharField(label = 'Drugie imię (opcjonalnie)',
	                              required = False,
	                              initial = "Karol",
	                              max_length = 20,
	                              widget = forms.TextInput(attrs = {'class': 'inputs'}))

	last_name = forms.CharField(label = 'Nazwisko',
	                            initial = "Biel",
	                            max_length = 20,
	                            widget = forms.TextInput(attrs = {'class': 'inputs'}))

	index = forms.CharField(label = 'Numer albumu',
	                        initial = "225949",
	                        max_length = 11,
	                        widget = forms.TextInput(attrs = {"class": "inputs bfh-phone",
	                                                          "data-format": "ddddddddddd"}))

	date_of_birth = forms.DateField(label = "Data urodzenia",
	                                initial = "1996-06-07",
	                                widget = forms.DateInput(attrs = {
		                                'id': 'datetimepicker1',
		                                'class': 'form-control datetimepicker-input',
		                                'type': 'text',
		                                'data-target': '#datetimepicker1'}))

	email = forms.EmailField(label = 'Email',
	                         initial = "pako-96@o2.pl",
	                         max_length = 45,
	                         widget = forms.TextInput(attrs = {'class': 'inputs'}))

	phone_number = forms.CharField(label = "Telefon kom.",
	                               initial = "535226885",
	                               max_length = 11,
	                               widget = forms.TextInput(attrs = {"class": "inputs bfh-phone",
	                                                                 "data-format": "ddd ddd ddd"}))

	city = forms.CharField(label = "Miejscowość",
	                       initial = "Zielona Góra",
	                       max_length = 25,
	                       widget = forms.TextInput(attrs = {'class': 'inputs'}))

	address = forms.CharField(label = "Ulica, numer domu/numer mieszkania",
	                          initial = "św.Cyryla-Met 8/10",
	                          max_length = 50,
	                          widget = forms.TextInput(attrs = {'class': 'inputs'}))

	subject = forms.ChoiceField(label = "Kurs",
	                            choices = choices_list,
	                            widget = forms.Select(attrs = {'class': 'inputs'}))

	pulse = forms.IntegerField(label = "Twoje tętno",
	                           initial = 0,

	                           widget = forms.NumberInput(attrs = {'class': 'inputs'}))