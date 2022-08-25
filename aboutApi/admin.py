from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .models import Degree, ProfileInfo, Universities, Bachelor, Master, Doctorate, Course, UserUndergraduate, Employment, JobPosition, PersonalInfo, Education, ContactForm, Language, PhoneModel, TechnologyUsed

admin.site.unregister(Group)
admin.site.register(Education)
admin.site.register(Employment)
admin.site.register(JobPosition)
admin.site.register(ProfileInfo)
admin.site.register(PersonalInfo)
admin.site.register(Universities)
admin.site.register(Degree)
admin.site.register(Bachelor)
admin.site.register(Master)
admin.site.register(Doctorate)
admin.site.register(Course)
admin.site.register(UserUndergraduate)
admin.site.register(ContactForm)
admin.site.register(Language)
admin.site.register(PhoneModel)
admin.site.register(TechnologyUsed)