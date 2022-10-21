from django.contrib import admin
from .models import IT, ITAnswer, ITQuestion, ITLearning, ITRequirement
from .models import IT_eng, ITAnswer_eng, ITQuestion_eng
from .models import IT_ch, ITAnswer_ch, ITQuestion_ch

# Register your models here.
admin.site.register(IT)
admin.site.register(ITAnswer)
admin.site.register(ITQuestion)

admin.site.register(IT_eng)
admin.site.register(ITAnswer_eng)
admin.site.register(ITQuestion_eng)

admin.site.register(IT_ch)
admin.site.register(ITQuestion_ch)
admin.site.register(ITAnswer_ch)

admin.site.register(ITRequirement)
admin.site.register(ITLearning)
