from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

MOTHER_STATUS_CHOICES = (('P', 'Pregnant'),
			 ('PP', 'Postpartum'),
			 ('DC', 'Deceased'))

BABY_STATUS_CHOICES = (('U', 'Unborn'),
			('LB', 'Live birth'),
			('SB', 'Still birth'),
			('DC', 'Deceased'))

EVENT_TYPE_CHOICES = (('RC', 'Record Created'),
			('N', 'Note'),
			('V', 'Visit'),
			('DL', 'Delivered'),
			('DC', 'Deceased'))

class Mother(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=200)	
	last_name = models.CharField(max_length=200)
	status = models.CharField(max_length=2, choices=MOTHER_STATUS_CHOICES)
	date_of_birth = models.DateField(null=True, blank=True)
	height = models.IntegerField(max_length=3, null=True, blank=True)	
	picture = models.FileField(upload_to='/images/', null=True, blank=True)

	def full_name(self):
		return '%s %s' % (self.first_name, self.last_name)

	def __unicode__(self):
		return self.full_name()

class MotherForm(ModelForm):
	class Meta:
		model = Mother
		exclude = ['created_at']

class Baby(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	due_date = models.DateField(null=True)
	date_of_birth = models.DateField(null=True)
	mother = models.ForeignKey('Mother', null=True)
	status = models.CharField(max_length=2, choices=BABY_STATUS_CHOICES)

class BabyForm(ModelForm):
	class Meta:
		model = Baby
		exclude = ['created_at']

class Visit(models.Model):
	visit_date = models.DateField(null=True)
	temperature = models.IntegerField(max_length=3, blank=True)
	weight = models.IntegerField(max_length=3, blank=True)
	blood_pressure = models.CharField(max_length=50, blank=True)
	mother = models.ForeignKey('Mother')

class VisitForm(ModelForm):
	class Meta:
		model = Visit
		fields = '__all__'

class EventLog(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, null=True)
	mother = models.ForeignKey('Mother') 
	event_type = models.CharField(max_length=2, choices=EVENT_TYPE_CHOICES)
	description = models.TextField()
	
	def __unicode__(self):
		return unicode(self.mother.full_name + ': ' + self.event_type)
