from django.contrib import admin
from .models import Society, SocietyAnswer, SocietyQuestion, SocietyLearning, SocietyRequirement
from .models import Society_ENG, SocietyAnswer_ENG, SocietyQuestion_ENG
from .models import Society_CN, SocietyAnswer_CN, SocietyQuestion_CN

# Register your models here.
admin.site.register(Society)
admin.site.register(SocietyAnswer)
admin.site.register(SocietyQuestion)

admin.site.register(Society_ENG)
admin.site.register(SocietyAnswer_ENG)
admin.site.register(SocietyQuestion_ENG)

admin.site.register(Society_CN)
admin.site.register(SocietyQuestion_CN)
admin.site.register(SocietyAnswer_CN)

admin.site.register(SocietyLearning)
admin.site.register(SocietyRequirement)