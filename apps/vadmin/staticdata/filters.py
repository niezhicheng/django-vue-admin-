import django_filters
from apps.vadmin.staticdata.models import ProjectModel
from apps.vadmin.system.models import LoginInfor, OperationLog, CeleryLog


class ProjectFilter(django_filters.rest_framework.FilterSet):
    """
    字典管理 简单过滤器
    """
    pronum = django_filters.CharFilter(lookup_expr='icontains')
    proname = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.CharFilter()

    class Meta:
        model = ProjectModel
        fields = '__all__'