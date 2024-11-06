from django.contrib import admin

# Register your models here.

from app.models import *

class WebpageAdminview(admin.ModelAdmin):
    list_display=['Topic_name','name','url','email']
    #list_editable=('name',)
    #list_per_page=4
    #list_display_links=['url']
    #search_fields=['name','url']
    list_filter=['Topic_name','name','url','email']

admin.site.register(Topic)
admin.site.register(Webpage,WebpageAdminview)
admin.site.register(Accessrecord) 



