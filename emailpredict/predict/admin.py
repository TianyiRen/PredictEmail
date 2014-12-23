from django.contrib import admin
from predict.models import EmailAddress, Pattern

# Register your models here.


class EmailAddressAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name', 'email', )
    list_display = ('domain', 'first_name', 'last_name', 'email', )
    ordering = ('domain', 'first_name', 'last_name', )

admin.site.register(EmailAddress, EmailAddressAdmin)


class PatternAdmin(admin.ModelAdmin):
    search_fields = ('domain', )
    list_display = ('domain', 'pattern', 'probability', )
    ordering = ('domain', 'pattern', )

admin.site.register(Pattern, PatternAdmin)
