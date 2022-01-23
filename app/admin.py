from django.contrib import admin
from app.models import Exercise, Workout, User
# Register your models here.
admin.site.register(Exercise)
admin.site.unregister(User)
admin.site.register(User)
admin.site.register(Workout)