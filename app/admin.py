from django.contrib import admin

# Register your models here.
from app.models import CV, Project, Person, SkillGroup, Skill
admin.site.register(Project)
admin.site.register(Person)

admin.site.register(SkillGroup)

admin.site.register(Skill)
