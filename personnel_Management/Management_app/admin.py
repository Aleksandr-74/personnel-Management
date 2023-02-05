from django.contrib import admin

class WorkerAdmin(admin.ModelAdmin):
    list_display = ('id', 'roles', 'name_worker')
    # prepopulated_fields = {"slug": ("name_worker")}


class BrigadeAdmin(admin.ModelAdmin):
    pass