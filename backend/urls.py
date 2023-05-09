from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
            EmployeeListAPIView,
            NewsUrlListAPIView,
            AnoncUrlListAPIView,
            photoUrlListAPIView,
            VideoUrlListAPIView,
            CentralHardwareUrlListAPIView,
            VacancyUrlListAPIView,
            EventUrlListAPIView,
            TenderUrlListAPIView,
            AutobiUrlListAPIView,
            LectureUrlListAPIView,
            StatisticsUrlListAPIView,
            AdultNewsUrlListAPIView,
            # OpenBudgetNamesListAPIView,
            OpenBudgetFilesListAPIView,
            JournalFilesListAPIView
        )

urlpatterns = [
    path("employee/",  EmployeeListAPIView.as_view()),
    path("news/",  NewsUrlListAPIView.as_view()),
    path("announcement/",  AnoncUrlListAPIView.as_view()),
    path("photo-gallery/",  photoUrlListAPIView.as_view()),
    path("video-gallery/",  VideoUrlListAPIView.as_view()),
    path("central-hardware/",  CentralHardwareUrlListAPIView.as_view()),
    path("vacancy/",  VacancyUrlListAPIView.as_view()),
    path("event/",  EventUrlListAPIView.as_view()),
    path("tender/",  TenderUrlListAPIView.as_view()),
    path("autobiography/",  AutobiUrlListAPIView.as_view()),
    path("lecture/",  LectureUrlListAPIView.as_view()),
    path("dynamic-static/",  StatisticsUrlListAPIView.as_view()),
    path("adult-news/",  AdultNewsUrlListAPIView.as_view()),
    path("open-budget-files/",  OpenBudgetFilesListAPIView.as_view()),
    path("journal-files/",  JournalFilesListAPIView.as_view()),
] 