from django.contrib import admin
from backend import models

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["id", "fio", "rank", "mobile_phone_number", "email"]
    ordering=["-id"]
    search_fields = ["fio", "rank"]

class PhotoGallery(admin.ModelAdmin):
    list_display = ["name", "image1", "created_at"]
    search_fields = ["name"]


class VideoGallery(admin.ModelAdmin):
    list_display = ["name", "detail", "created_at"]
    search_fields = ["name"]
    
class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "content"]
    search_fields = ["title", "content"]

class AnoncUrlAdmin(admin.ModelAdmin):
    list_display = ["title", "note", "content"]
    search_fields = ["title", "content"]

class VacancyUrlAdmin(admin.ModelAdmin):
    list_display = ["name", "education", "work_experience"]
    search_fields = ["name", "education"]

class EventUrlAdmin(admin.ModelAdmin):    
    def decade_born_in(self):
        return '%d s' % (self.start_date.year // 10 * 10)

    list_display = ["title", "organizer", decade_born_in]
    search_fields = ["title", "organizer"]

class AutobiUrlAdmin(admin.ModelAdmin):
    list_display = ["fio", "email", "phone_number"]
    search_fields = ["fio", "email", "phone_number"]

class AdultNewsUrlAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "author"]
    search_fields = ["title", "content", "author"]

class OpenBudgetFilesAdmin(admin.ModelAdmin):
    list_display = ["title", "files"]
    search_fields = ["title", "files"]

class JournalFilesAdmin(admin.ModelAdmin):
    list_display = ["title", "image", "files"]
    search_fields = ["title", "image", "files"]

# admin.site.register(models.YoshlargsOidYangiliklar)
admin.site.register(models.Employee, EmployeeAdmin)
admin.site.register(models.JournalFilesUrl, JournalFilesAdmin)
admin.site.register(models.CentralHardwareUrl, EmployeeAdmin)
admin.site.register(models.NewsUrl, NewsAdmin)
admin.site.register(models.AnoncUrl, AnoncUrlAdmin)
admin.site.register(models.VacancyUrl, VacancyUrlAdmin)
admin.site.register(models.EventUrl, EventUrlAdmin)
admin.site.register(models.AutobiUrl, AutobiUrlAdmin)
admin.site.register(models.AdultNewsUrl, AdultNewsUrlAdmin)
admin.site.register(models.photoUrl, PhotoGallery)
admin.site.register(models.VideoUrl, VideoGallery)
admin.site.register(models.OpenBudgetFiles, OpenBudgetFilesAdmin)
 