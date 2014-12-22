import logging
import json

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from predict.models import EmailAddress
from predict.forms import EmailPredictForm
from predict.predict_email import predict_email, create_all_possible_emails, get_all_patterns
from predict.parse_dataset import parse_dataset, update_patterns_probability

logger = logging.getLogger(__name__)


def index(request):
    return predict_email_address(request)


def predict_email_address(request):
    context = {}
    no_matching_domain_pattern = ''
    if request.method == 'POST':
        form = EmailPredictForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name'].strip()
            last_name = form.cleaned_data['last_name'].strip()
            domain = form.cleaned_data['domain'].strip()

            predicted_emails = predict_email(
                first_name=first_name, last_name=last_name, domain=domain)

            if not predicted_emails:
                predicted_emails = create_all_possible_emails(
                    first_name=first_name, last_name=last_name, domain=domain, patterns=get_all_patterns())
                no_matching_domain_pattern = 'No Matching Domain Patterns In Database!'

            context['predicted_emails'] = predicted_emails
            context['no_matching_domain_pattern'] = no_matching_domain_pattern
    else:
        form = EmailPredictForm()

    return render_to_response('predict/predict_email_address.html', {'form': form, 'context': context}, RequestContext(request))


def verify_email_ajax(request):
    verified = False

    if request.is_ajax():
        full_name = request.GET.get('full_name', '').strip()
        email = request.GET.get('email', '').strip()

        try:
            name = full_name.split(' ')
            first_name = name[0]
            last_name = name[1]
            domain = email.split('@')[1]

            try:
                email_address_record = EmailAddress.objects.get(
                    first_name__iexact=first_name, last_name__iexact=last_name, email__iexact=email)
                email_address_record.verified = True
                email_address_record.save()

                predicted_email_address_records = EmailAddress.objects.filter(
                    first_name__iexact=first_name, last_name__iexact=last_name, domain__iexact=domain, verified=False)
                for predicted_email_address_record in predicted_email_address_records:
                    predicted_email_address_record.delete()
                    update_patterns_probability(
                        domain=domain, pattern=predicted_email_address_record.pattern.pattern, add=False)
            except EmailAddress.DoesNotExist:
                parse_dataset({full_name: email})

            verified = True
        except Exception as error:
            logger.debug('Not able to verify email address, error: %s' % error)

    data = json.dumps({'verified': verified})
    return HttpResponse(data, content_type='application/json')
