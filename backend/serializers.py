from rest_framework import serializers
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
            JournalFilesUrl,
            AutobiUrl,
            LectureUrl,
            StatisticsUrl,
            AdultNewsUrl,
            # OpenBudgetNames,
            OpenBudgetFiles,
            )

class JournalFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalFilesUrl
        fields = "__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsUrl
        fields = "__all__"

class AnoncSerializer(serializers.ModelSerializer):
    class Meta:
        models = AnoncUrl
        fields = "__all__"

class photoUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = photoUrl
        fields = "__all__"

class VideoUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoUrl
        fields = "__all__"

class CentralHardwareUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentralHardwareUrl
        fields = "__all__"

class VacancyUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacancyUrl
        fields = "__all__"

class EventUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventUrl
        fields = "__all__"

class TenderUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenderUrl
        fields = "__all__"

class AutobiUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutobiUrl
        fields = "__all__"

class LectureUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = LectureUrl
        fields = "__all__"

class StatisticsUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatisticsUrl
        fields = "__all__"

class AdultNewsUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdultNewsUrl
        fields = "__all__"


class OpenBudgetFilesSerializer(serializers.ModelSerializer):
    # categName = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = OpenBudgetFiles
        fields = "__all__"

    # def get_categName(self, obj):
    #     return obj.categoryTitle