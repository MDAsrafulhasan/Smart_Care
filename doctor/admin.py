from django.contrib import admin

# Register your models here.
from .models import Review, Designation,Specialization,Doctor,AvailableTime

admin.site.register(Doctor)
admin.site.register(AvailableTime)
admin.site.register(Review)

class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',),}
admin.site.register(Designation,DesignationAdmin)

class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',),}
admin.site.register(Specialization,SpecializationAdmin)
