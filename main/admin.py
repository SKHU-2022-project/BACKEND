from django.contrib import admin
from humanity.models import HumanityQuestion, Humanity, HumanityAnswer
# Register your models here.
admin.site.register(Humanity)
admin.site.register(HumanityQuestion)
admin.site.register(HumanityAnswer)