from __future__ import division

from predict.models import EmailAddress, Pattern
from predict.parse_dataset import update_patterns_probability


def predict_email(first_name, last_name, domain):
    existing_email_records = EmailAddress.objects.filter(
        first_name__iexact=first_name, last_name__iexact=last_name, domain__iexact=domain).order_by('-pattern__probability')
    if existing_email_records:
        return existing_email_records

    domain_patterns = Pattern.objects.filter(domain__iexact=domain)
    predicted_emails = []
    for domain_pattern in domain_patterns:
        pattern = domain_pattern.pattern
        email = create_email(
            first_name=first_name, last_name=last_name, domain=domain, pattern=pattern)
        if email:
            email_record = EmailAddress.objects.create(
                first_name=first_name, last_name=last_name, domain=domain, email=email, pattern=domain_pattern)
            update_patterns_probability(domain=domain, pattern=pattern)
            predicted_emails.append(email_record)

    return predicted_emails


def create_email(first_name, last_name, domain, pattern):
    first_initial = first_name[0]
    last_initial = last_name[0]
    email = ''
    if pattern == Pattern.FIRST_NAME_DOT_LAST_NAME:
        email = '{first_name}.{last_name}@{domain}'.format(
            first_name=first_name, last_name=last_name, domain=domain)
    elif pattern == Pattern.FIRST_INITIAL_DOT_LAST_NAME:
        email = '{first_initial}.{last_name}@{domain}'.format(
            first_initial=first_initial, last_name=last_name, domain=domain)
    elif pattern == Pattern.FIRST_NAME_DOT_LAST_INITIAL:
        email = '{first_name}.{last_initial}@{domain}'.format(
            first_name=first_name, last_initial=last_initial, domain=domain)
    elif pattern == Pattern.FIRST_INITIAL_DOT_LAST_INITIAL:
        email = '{first_initial}.{last_initial}@{domain}'.format(
            first_initial=first_initial, last_initial=last_initial, domain=domain)

    return email.lower()


def create_all_possible_emails(first_name, last_name, domain, patterns):
    emails = []
    probability = 1 / len(patterns)
    for pattern in patterns:
        email = create_email(
            first_name=first_name, last_name=last_name, domain=domain, pattern=pattern)
        if email:
            emails.append({'full_name': '{first_name} {last_name}'.format(first_name=first_name.title(
            ), last_name=last_name.title()), 'email': email, 'pattern': {'display_probability': "{:.0%}".format(probability)}})
    return emails


def get_all_patterns():
    return [Pattern.FIRST_NAME_DOT_LAST_NAME, Pattern.FIRST_NAME_DOT_LAST_INITIAL,
            Pattern.FIRST_INITIAL_DOT_LAST_NAME, Pattern.FIRST_INITIAL_DOT_LAST_INITIAL]
