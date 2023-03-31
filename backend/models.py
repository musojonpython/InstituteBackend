from django.db import models

class Employee(models.Model):
    fio = models.CharField(max_length=120)
    image = models.FileField(upload_to="employee/")
    rank = models.CharField(max_length=30)
    mobile_phone_number = models.CharField(max_length=30)
    home_phone_number = models.CharField(max_length=30)
    short_bio = models.TextField()
    division_of_responsibility = models.TextField()
    email = models.EmailField()
    reception_days = models.CharField(max_length=60)

    
class NewsUrl(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    image = models.ImageField(upload_to="newsphoto/")
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title

class AnoncUrl(models.Model):
    title = models.CharField(max_length=120)
    note = models.CharField(max_length=250)
    content = models.TextField()
    image = models.FileField(upload_to="annonc/")
    created_at = models.DateTimeField(auto_now_add=True)

class photoUrl(models.Model):
    name = models.CharField(max_length=150, blank=True)
    image = models.FileField(upload_to="photos/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class VideoUrl(models.Model):
    name = models.CharField(max_length=150, blank=True)
    detail = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class CentralHardwareUrl(models.Model):
    fio = models.CharField(max_length=120)
    short_bio = models.TextField()
    image = models.FileField(upload_to="centralHard/")
    rank = models.CharField(max_length=30)
    mobile_phone_number = models.CharField(max_length=30)
    home_phone_number = models.CharField(max_length=30)
    email = models.EmailField()
    reception_days = models.CharField(max_length=60)

class VacancyUrl(models.Model):
    name =  models.CharField(max_length=120)
    education = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    work_experience = models.CharField(max_length=300)
    general = models.CharField(max_length=400)

class EventUrl(models.Model):
    title = models.CharField(max_length=200) 
    image = models.FileField(upload_to="events/") 
    organizer = models.CharField(max_length=200) 
    start_date = models.DateField()
    end_date = models.DateField()

class TenderUrl(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    image = models.FileField(upload_to="tenders/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class AutobiUrl(models.Model):
    fio = models.CharField(max_length=150)
    email = models.EmailField()
    phone_number = models.CharField(max_length=120) 
    comment = models.CharField(max_length=300)
    file = models.FileField(upload_to="autobiFiles/")

class LectureUrl(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="lecture/")

    def __str__(self):
        return self.title

class StatisticsUrl(models.Model):
    statistics = models.FileField(upload_to="statistics/")
    statistics2 = models.FileField(upload_to="statistics/")
    statistics3 = models.FileField(upload_to="statistics/")

class AdultNewsUrl(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    author = models.CharField(max_length=160)
    created_at = models.DateTimeField(auto_now_add=True)

# class OpenBudgetNames(models.Model):
#     name = 

#     def __str__(self):
#         return self.name

class OpenBudgetFiles(models.Model):
    categoryName = models.CharField(max_length=600)
    title = models.CharField(max_length=300)
    files = models.FileField(upload_to="openbudget/")
    created_at = models.DateTimeField(auto_now_add=True)

    # @property
    # def categoryTitle(self):
    #     return self.categoryName


# class YoshlargsOidYangiliklar(models.Model):
#     title = models.CharField(max_length=120)
#     content = models.TextField()


