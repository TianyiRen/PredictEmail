from __future__ import division

from predict.models import EmailAddress, Pattern


def parse_dataset(dataset):
    parsed_emails = []
    for name, email in dataset.items():
        name = name.split(' ')
        first_name = name[0]
        last_name = name[1]

        email = email.lower()
        email_address = email.split('@')
        email_prefix = email_address[0]
        domain = email_address[1]

        patterns = check_pattern(
            first_name=first_name, last_name=last_name, email_prefix=email_prefix)

        for pattern in patterns:
            email_address_record, created = EmailAddress.objects.get_or_create(
                first_name=first_name, last_name=last_name, email=email, verified=True)
            parsed_emails.append(email_address_record)
            if created:
                pattern_record, success = Pattern.objects.get_or_create(
                    domain=domain, pattern=pattern)
                email_address_record.pattern = pattern_record
                email_address_record.save()

                update_patterns_probability(domain=domain, pattern=pattern)
            else:
                break
    return parsed_emails


def check_pattern(first_name, last_name, email_prefix):
    first_initial = first_name[0]
    last_initial = last_name[0]

    # Create four possible patterns
    first_name_dot_last_name = '{first_name}.{last_name}'.format(
        first_name=first_name, last_name=last_name)
    first_name_dot_last_initial = '{first_name}.{last_initial}'.format(
        first_name=first_name, last_initial=last_initial)
    first_initial_dot_last_name = '{first_initial}.{last_name}'.format(
        first_initial=first_initial, last_name=last_name)
    first_initial_dot_last_initial = '{first_initial}.{last_initial}'.format(
        first_initial=first_initial, last_initial=last_initial)

    # Check possible patterns
    # May have multiple patterns if first_name/last_name only has 1 character
    patterns = []
    if first_name_dot_last_name.lower() == email_prefix.lower():
        patterns.append(Pattern.FIRST_NAME_DOT_LAST_NAME)

    if first_name_dot_last_initial.lower() == email_prefix.lower():
        patterns.append(Pattern.FIRST_NAME_DOT_LAST_INITIAL)

    if first_initial_dot_last_name.lower() == email_prefix.lower():
        patterns.append(Pattern.FIRST_INITIAL_DOT_LAST_NAME)

    if first_initial_dot_last_initial.lower() == email_prefix.lower():
        patterns.append(Pattern.FIRST_INITIAL_DOT_LAST_INITIAL)

    return patterns


def update_patterns_probability(domain, pattern, add=True):
    ''' Update pattern probability in database '''
    domain_patterns = Pattern.objects.filter(domain__iexact=domain)

    total_emails_in_domain = EmailAddress.objects.filter(
        domain__iexact=domain, verified=True).count()

    for domain_pattern in domain_patterns:
        probability = domain_pattern.probability
        if domain_pattern.pattern == pattern:
            if add:
                probability = (
                    (total_emails_in_domain - 1) * probability + 1) / (total_emails_in_domain)
            else:
                probability = (
                    (total_emails_in_domain + 1) * probability - 1) / (total_emails_in_domain)
            domain_pattern.probability = probability
        else:
            if add:
                probability = (
                    (total_emails_in_domain - 1) * probability) / (total_emails_in_domain)
            else:
                probability = (
                    (total_emails_in_domain + 1) * probability) / (total_emails_in_domain)
            domain_pattern.probability = probability
        domain_pattern.save()
