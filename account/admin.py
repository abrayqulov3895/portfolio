from django.contrib import admin

from account.models import Brend, Contact, Fair_price, IconInformation, Information, Language, Love_to, SpecialistInformation, Thoughts, Work

# Register your models here.

admin.site.register(Information)
admin.site.register(IconInformation)
admin.site.register(SpecialistInformation)
admin.site.register(Work)
admin.site.register(Thoughts)
admin.site.register(Fair_price)
admin.site.register(Love_to)
admin.site.register(Language)
admin.site.register(Brend)
admin.site.register(Contact)


