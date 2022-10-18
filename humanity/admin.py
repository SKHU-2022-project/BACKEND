from django.contrib import admin
from humanity.models import HumanityQuestion, Humanity, HumanityAnswer
from .models import Humanity_ENG, Humanity_CN, HumanityAnswer_CN, HumanityAnswer_ENG, HumanityQuestion_CN, HumanityQuestion_ENG
# Register your models here.
admin.site.register(Humanity)
admin.site.register(HumanityQuestion)
admin.site.register(HumanityAnswer)

admin.site.register(Humanity_ENG)
admin.site.register(HumanityQuestion_ENG)
admin.site.register(HumanityAnswer_ENG)

admin.site.register(Humanity_CN)
admin.site.register(HumanityQuestion_CN)
admin.site.register(HumanityAnswer_CN)
