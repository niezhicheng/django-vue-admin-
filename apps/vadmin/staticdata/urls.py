from django.urls import re_path,path
from rest_framework.routers import DefaultRouter

from apps.vadmin.staticdata.views import DictDataModelViewSet,CategoryModelViewSet,ProjectinfoModelViewset,CountryModelViewset,RegionViewset,SiteAreaViewset
from apps.vadmin.staticdata.views import DeptViewset,Project1infoModelViewset,ComnameAPiview,FormdataApiview,ReserveModel,CompanyModelViewset
from apps.vadmin.staticdata.views import Gongsiviewset,ProjecFilterApiview,StatsicAPiview,KpimodelApiview,DeptbackViewset,Kpimodelapview,Pkimodelapview
from apps.vadmin.staticdata.views import ReservesModel
router = DefaultRouter()
router.register(r'dict/user', DictDataModelViewSet)
router.register(r'dict/category',CategoryModelViewSet)
router.register(r'dict/comname',ProjectinfoModelViewset)
# router.register(r'dict/comname1',Project1infoModelViewset)
router.register(r'dict/country',CountryModelViewset)
router.register(r'dict/region',RegionViewset)
router.register(r'dict/siteaxrea',SiteAreaViewset)
router.register(r'dict/dept',DeptViewset)
router.register(r'dict/deptbak',DeptbackViewset)
router.register(r'dict/form',FormdataApiview)
router.register(r'dict/reserve',ReserveModel)
router.register(r'dict/reservers',ReservesModel)
router.register(r'dict/company',CompanyModelViewset)
router.register(r'dict/gongsi',Gongsiviewset)



urlpatterns = [
    path('dict/money/',ComnameAPiview.as_view()),
    path('filt/',ProjecFilterApiview.as_view()),
    path('statistics/',StatsicAPiview.as_view()),
    path('kpi/',KpimodelApiview.as_view()),
    path('init/',Kpimodelapview.as_view()),
    path('getdename/',Pkimodelapview.as_view()),
    # path('export/',FormdataApiview.as_view({"get","export"}))
    re_path('export/', FormdataApiview.as_view({'get': 'export'})),
    # path('dict/form/',FormdataApiview.as_view()),
    # re_path('dict/get/type/(?P<pk>.*)/', DictDetailsModelViewSet.as_view({'get': 'dict_details_list'})),
    # re_path('config/configKey/(?P<pk>.*)/', ConfigSettingsModelViewSet.as_view({'get': 'get_config_key'})),
]
urlpatterns += router.urls
