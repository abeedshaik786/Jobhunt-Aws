from django.contrib import admin
from .models import Fresher,FresherData,FresherQualification,Qualification,Qualification_Course,JobRequirments,ProfileImg,Notifications

# Register your models here.
admin.site.register(Fresher)
admin.site.register(FresherData)
admin.site.register(FresherQualification)
admin.site.register(Qualification)
admin.site.register(Qualification_Course)
admin.site.register(JobRequirments)
admin.site.register(ProfileImg)
admin.site.register(Notifications)


