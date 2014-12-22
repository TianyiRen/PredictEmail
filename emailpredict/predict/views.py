from django.shortcuts import render_to_response
from django.template import RequestContext

from predict.forms import EmailPredictForm
from predict.predict_email import predict_email, create_all_possible_emails, get_all_patterns


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
