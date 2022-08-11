from django.contrib import admin
from siteapp.models import *
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    pass
admin.site.register(Blog,BlogAdmin)


class TeacherAdmin(admin.ModelAdmin):
    pass
admin.site.register(Teacher,TeacherAdmin)


class AshiqsabaqAdmin(admin.ModelAdmin):
    pass
admin.site.register(Ashiqsabaq,AshiqsabaqAdmin)


class CalculateAdmin(admin.ModelAdmin):
    pass
admin.site.register(Calculate,CalculateAdmin)


class PostAdmin(admin.ModelAdmin):
    pass
admin.site.register(Post,PostAdmin)



class GalleryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Gallery,GalleryAdmin)



class ContactAdmin(admin.ModelAdmin):
    pass
admin.site.register(Contact,ContactAdmin)


class GosAdmin(admin.ModelAdmin):
    pass

admin.site.register(Gos,GosAdmin)