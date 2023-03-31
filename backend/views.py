from rest_framework.generics import ListAPIView
from .serializers import (
        EmployeeSerializer,
        NewsSerializer,
        AnoncSerializer,
        photoUrlSerializer,
        VideoUrlSerializer,
        CentralHardwareUrlSerializer,
        VacancyUrlSerializer,
        EventUrlSerializer,
        TenderUrlSerializer,
        AutobiUrlSerializer,
        LectureUrlSerializer,
        StatisticsUrlSerializer,
        AdultNewsUrlSerializer,
        # OpenBudgetNamesSerializer,
        OpenBudgetFilesSerializer,
)
from .models import (
            Employee,
            NewsUrl,
            AnoncUrl,
            photoUrl,
            VideoUrl,
            CentralHardwareUrl,
            VacancyUrl,
            EventUrl,
            TenderUrl,
            AutobiUrl,
            LectureUrl,
            StatisticsUrl,
            AdultNewsUrl,
            # OpenBudgetNames,
            OpenBudgetFiles,
)


class EmployeeListAPIView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class NewsUrlListAPIView(ListAPIView):
    queryset = NewsUrl.objects.all()
    serializer_class = NewsSerializer


class AnoncUrlListAPIView(ListAPIView):
    queryset = AnoncUrl.objects.all()
    serializer_class = AnoncSerializer


class photoUrlListAPIView(ListAPIView):
    queryset = photoUrl.objects.all()
    serializer_class = photoUrlSerializer


class VideoUrlListAPIView(ListAPIView):
    queryset = VideoUrl.objects.all()
    serializer_class = VideoUrlSerializer


class CentralHardwareUrlListAPIView(ListAPIView):
    queryset = CentralHardwareUrl.objects.all()
    serializer_class = CentralHardwareUrlSerializer


class VacancyUrlListAPIView(ListAPIView):
    queryset = VacancyUrl.objects.all()
    serializer_class = VacancyUrlSerializer


class EventUrlListAPIView(ListAPIView):
    queryset = EventUrl.objects.all()
    serializer_class = EventUrlSerializer


class TenderUrlListAPIView(ListAPIView):
    queryset = TenderUrl.objects.all()
    serializer_class = TenderUrlSerializer


class AutobiUrlListAPIView(ListAPIView):
    queryset = AutobiUrl.objects.all()
    serializer_class = AutobiUrlSerializer


class LectureUrlListAPIView(ListAPIView):
    queryset = LectureUrl.objects.all()
    serializer_class = LectureUrlSerializer


class StatisticsUrlListAPIView(ListAPIView):
    queryset = StatisticsUrl.objects.all()
    serializer_class = StatisticsUrlSerializer


class AdultNewsUrlListAPIView(ListAPIView):
    queryset = AdultNewsUrl.objects.all()
    serializer_class = AdultNewsUrlSerializer


# class OpenBudgetNamesListAPIView(ListAPIView):
#     queryset = OpenBudgetNames.objects.all()
#     serializer_class = OpenBudgetNamesSerializer


class OpenBudgetFilesListAPIView(ListAPIView):
    queryset = OpenBudgetFiles.objects.all()
    serializer_class = OpenBudgetFilesSerializer

    # def get_queryset(self):
    #     objs = OpenBudgetFiles.objects.all()
    #     print("1 => ", objs[1].categoryName)
    #     # print(objs)
    #     # data = {}
    #     # for obj in objs:
    #     #     data = {
    #     #         # "categoryName": OpenBudgetNames.objects.get(id=obj.categoryName.id),
    #     #         "categoryName": obj.categoryName,
    #     #         "title": obj.title,
    #     #         "files": obj.files,
    #     #     }           
    #     #     print(data) 
    #     return objs
    
    
