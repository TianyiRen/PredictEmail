from django.db import models

# Create your models here.


class EmailAddress(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    domain = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(
        max_length=256, blank=True, null=True)
    pattern = models.ForeignKey('predict.Pattern', blank=True, null=True)
    verified = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Email Address'
        verbose_name_plural = 'Email Addresses'

    def __unicode__(self):
        return '"{first_name} {last_name}" => "{email}"'.format(first_name=self.first_name, last_name=self.last_name, email=self.email)

    @property
    def full_name(self):
        return '{first_name} {last_name}'.format(first_name=self.first_name, last_name=self.last_name)

    def save(self, *args, **kwargs):
        if not self.domain:
            self.domain = self.email.split('@')[1]
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()
        self.email = self.email.lower()
        super(EmailAddress, self).save(*args, **kwargs)


class Pattern(models.Model):

    FIRST_NAME_DOT_LAST_NAME = 'first_name_dot_last_name'
    FIRST_NAME_DOT_LAST_INITIAL = 'first_name_dot_last_initial'
    FIRST_INITIAL_DOT_LAST_NAME = 'first_initial_dot_last_name'
    FIRST_INITIAL_DOT_LAST_INITIAL = 'first_initial_dot_last_initial'

    PATTERN_CHOICES = (
        (FIRST_NAME_DOT_LAST_NAME, 'FirstName.LastName'),
        (FIRST_NAME_DOT_LAST_INITIAL, 'FirstName.LastInitial'),
        (FIRST_INITIAL_DOT_LAST_NAME, 'FirstInitial.LastName'),
        (FIRST_INITIAL_DOT_LAST_INITIAL, 'FirstInitial.LastInitial'),
    )

    domain = models.CharField(max_length=100, blank=True, null=True)
    pattern = models.CharField(
        max_length=50, choices=PATTERN_CHOICES, blank=True, null=True)
    probability = models.FloatField(default=0.00)

    class Meta:
        verbose_name = 'Pattern'
        verbose_name_plural = 'Patterns'

    def __unicode__(self):
        return '{domain} => {pattern} {probability}'.format(domain=self.domain, pattern=self.pattern, probability=self.probability)

    @property
    def display_probability(self):
        return "{:.0%}".format(self.probability)
