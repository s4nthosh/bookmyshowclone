from django.contrib import admin
from .models import *


class moviesAdmin(admin.ModelAdmin):
    list_display=['name','movie','id']


class theaterAdmin(admin.ModelAdmin):
    list_display=['theater_name','movie','id']


class timeAdmin(admin.ModelAdmin):
    list_display=['time','movie','theater_name','id']
    

admin.site.register(movies,)
admin.site.register(list_mov,moviesAdmin)
admin.site.register(main)
admin.site.register(theaters,theaterAdmin)
admin.site.register(theater)
admin.site.register(cast_crew)
admin.site.register(seats)
admin.site.register(save_details)
admin.site.register(date_time,timeAdmin)
