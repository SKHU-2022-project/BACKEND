from django.contrib import admin
from .models import IT, ITAnswer, ITQuestion

# Register your models here.
admin.site.register(IT)
admin.site.register(ITQuestion)
admin.site.register(ITAnswer)