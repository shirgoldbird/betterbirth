from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import logging
from django.template import Template, Context
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from betterbirthapp.models import Mother, Baby, EventLog, MOTHER_STATUS_CHOICES

class MotherListView(ListView):
    def get_queryset(self, **kwargs):
        category = self.kwargs['category']
        mapping = {
            'all': Mother.objects.all(),
            'pregnant': Mother.objects.filter(status__in=('P')),
            'postpartum': Mother.objects.filter(status__in=('PP')),
            'deceased': Mother.objects.filter(status__in=('DC')),
        }
        return mapping[category] if category in mapping else None
    
    def get_context_data(self, **kwargs):
        context = super(MotherListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['category'] = self.kwargs['category']
        return context
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MotherListView, self).dispatch(*args, **kwargs)

class MotherDetailView(DetailView):
    pk_url_kwarg = 'id'
    model = Mother
    
    #def get_queryset(self, **kwargs):
    #    return Application.objects.filter(id=self.kwargs['id'])
    
    def get_context_data(self, **kwargs):
        context = super(MotherDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        
        """
        # massage responses into format that's good for rendering
        qresponses = QResponse.objects.filter(application=self.kwargs['id']).order_by('question')
        questions = Question.objects.all().order_by('id')
        logging.debug(questions)
        response_dict = dict([(qr.question.id, qr.response) for qr in qresponses])
        logging.debug(response_dict)
        responses = []
        for q in questions:
            logging.debug(q.id)
            if q.id in response_dict:
                resp = response_dict[q.id]
            else:
                resp = ''
            responses.append((q.question_text, resp))
        logging.debug(responses)
        context['responses'] = responses
        """
        
        # get event log for user
        events = EventLog.objects.filter(application=self.kwargs['id']).order_by('created_at')
        context['events'] = events
        
        # get acceptable transitions for user
        # YAY STATE MACHINES
        transitions_map = {
            'P': ('PP', 'DC'),
            'PP': ('DC'),
            'DC': (),
        }
        transitions_abbr = transitions_map[Mother.objects.filter(id=self.kwargs['id']).first().status]
        logging.debug(transitions_abbr)
        transitions = [(abbr, dict(MOTHER_STATUS_CHOICES)[abbr]) for abbr in transitions_abbr]
        context['transitions'] = transitions

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MotherDetailView, self).dispatch(*args, **kwargs)

@login_required
def do_action(request):
    if request.method != 'POST':
        return HttpResponseNotFound()
    action = request.POST['action']
    mother_id = request.POST['mother_id']
    mother = Mother.objects.filter(id=mother_id).first()
    user = request.user
    note = request.POST['note']
    log_entry = EventLog(user=user, mother=mother, event_type=action, description=note)
    log_entry.save()
    if action in [x[0] for x in MOTHER_STATUS_CHOICES]:
        mother.status = action
        mother.save()
    return HttpResponse('Great success!')

