from django.db import models


class Person(models.Model):
	name = models.CharField(max_length = 45,  verbose_name = 'Imię')
	second_name = models.CharField(max_length = 45, blank = True, verbose_name = 'Drugie imię')
	last_name = models.CharField(max_length = 45, verbose_name = 'Nazwisko')
	index = models.CharField(max_length = 11)
	date_of_birth = models.DateField(verbose_name = 'Data urodzenia')
	name_day = models.DateField(verbose_name = 'Data imienin')
	email = models.EmailField(max_length = 45, verbose_name = 'E-mail')

	city = models.CharField(max_length = 45, verbose_name = 'Miasto')
	address = models.CharField(max_length = 100, verbose_name = 'Adres')


class SubjectPulse(models.Model):
	subject = models.CharField(max_length =150)
	pulse = models.IntegerField()
