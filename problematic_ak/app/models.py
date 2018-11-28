from django.db import models


class SubjectPulse(models.Model):
    subject = models.CharField(max_length=150)
    pulse = models.IntegerField()


    def __str__(self):
        return "{}: {}".format(self.pulse, self.subject)

class Person(models.Model):
    name = models.CharField(max_length=45, verbose_name='Imię')
    second_name = models.CharField(max_length=45, blank=True, verbose_name='Drugie imię')
    last_name = models.CharField(max_length=45, verbose_name='Nazwisko')
    index = models.CharField(max_length=11)
    date_of_birth = models.DateField(verbose_name='Data urodzenia')
    phone_number = models.CharField(max_length=12, verbose_name='Numer telefonu')
    email = models.EmailField(max_length=45, verbose_name='E-mail')
    
    city = models.CharField(max_length=45, verbose_name='Miasto')
    address = models.CharField(max_length=100, verbose_name='Adres')
    subject_pulse = models.ForeignKey(SubjectPulse, on_delete=models.CASCADE)
    
    def __str__(self):
        return "{} {} {}".format(self.name, self.last_name, self.index)