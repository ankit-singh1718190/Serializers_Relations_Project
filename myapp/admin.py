from django.contrib import admin
from .models import Singer,Song
@admin.register(Singer)
class singhAdmin(admin.ModelAdmin):
    list_display=['id','name','gender']
@admin.register(Song)
class songAdmin(admin.ModelAdmin):
    list_display=['id','title','singer','duration']    
