from django.contrib import admin
from .models import MediaContent, MediaContentAnswer, MediaContentQuestion
from .models import MediaContent_ENG, MediaContentAnswer_ENG, MediaContentQuestion_ENG
from .models import MediaContent_CN, MediaContentAnswer_CN, MediaContentQuestion_CN
from .models import MediaContentRequirement, MediaContentLearning
# Register your models here.
admin.site.register(MediaContent)
admin.site.register(MediaContentAnswer)
admin.site.register(MediaContentQuestion)

admin.site.register(MediaContent_ENG)
admin.site.register(MediaContentAnswer_ENG)
admin.site.register(MediaContentQuestion_ENG)

admin.site.register(MediaContent_CN)
admin.site.register(MediaContentQuestion_CN)
admin.site.register(MediaContentAnswer_CN)

admin.site.register(MediaContentRequirement)
admin.site.register(MediaContentLearning)