from django.shortcuts import render
from apps.vadmin.op_drf.viewsets import CustomModelViewSet
from apps.vadmin.staticdata.models.data import Country,Category,Projectinfo,SiteArea,Region,Company
from apps.vadmin.permission.models.users import UserProfile
from apps.vadmin.permission.models.dept import Dept
from apps.vadmin.staticdata.serializers import CountrySerializer,CategorySerlizer,ProjectinfoSerlizer,CountrySerlizer,SiteAreaSerlizer,RegionSerlizer
from apps.vadmin.staticdata.serializers import DeptSerlizer,ProjectinfoPostSerlizer
from apps.vadmin.staticdata.serializers import CountryPostSerializer,Project1infoSerlizer,CompanyModelSerlizer
from rest_framework.request import Request
from apps.vadmin.op_drf.response import SuccessResponse,ErrorResponse
from apps.vadmin.staticdata.serializers import ProjectModelSerlizer,ProjectPostModelSerlizer,ReserveModelSerlizer,Project1infoSerlizer
from rest_framework import status
from apps.vadmin.staticdata.models.data import CheckList
from apps.vadmin.staticdata.models.project import ProjectModel,Reserve,Kpimodel
from apps.vadmin.staticdata.filters import ProjectFilter
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class DictDataModelViewSet(CustomModelViewSet):
    """
    数据模型的CRUD视图
    """
    queryset = UserProfile.objects.all()
    serializer_class = CountrySerializer
    # retrieve_serializer_class = CountryPostSerializer

    def get_serializer_class(self):
        print(self.action)
        if self.action == "retrieve":
            return CountryPostSerializer
        return CountrySerializer




class CategoryModelViewSet(CustomModelViewSet):
    """
    项目类别
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerlizer



class ProjectinfoModelViewset(CustomModelViewSet):
    """
    项目子公司管理
    """
    queryset = Projectinfo.objects.all()
    serializer_class = ProjectinfoSerlizer
    def get_serializer_class(self):
        print(self.action)
        if self.action == "list":
            return Project1infoSerlizer
        if self.action == "retrieve":
            return ProjectinfoPostSerlizer
        if self.action == "update":
            return ProjectinfoSerlizer
        else:
            return ProjectinfoSerlizer


class Project1infoModelViewset(CustomModelViewSet):
    """
    项目子公司管理
    """
    queryset = Projectinfo.objects.all()
    serializer_class = Project1infoSerlizer


class CountryModelViewset(CustomModelViewSet):
    """
    国家名称模型
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerlizer


class SiteAreaViewset(CustomModelViewSet):
    """
    工厂所属基地
    """
    queryset = SiteArea.objects.all()
    serializer_class = SiteAreaSerlizer


class RegionViewset(CustomModelViewSet):
    """
    区域名称
    """
    queryset = Region.objects.all()
    serializer_class = RegionSerlizer



class DeptViewset(CustomModelViewSet):
    queryset = Dept.objects.all()
    serializer_class = DeptSerlizer


class DeptbackViewset(CustomModelViewSet):
    queryset = Dept.objects.all()
    serializer_class = DeptSerlizer

    def list(self, request: Request, *args, **kwargs):
        if hasattr(self, 'handle_logging'):
            self.handle_logging(request, *args, **kwargs)
        queryset = self.filter_queryset(self.get_queryset().filter(parentId__deptName="RCP/OA"))
        page = self.paginate_queryset(queryset)
        if page is not None:
            if getattr(self, 'values_queryset', None):
                return self.get_paginated_response(page)
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        if getattr(self, 'values_queryset', None):
            return SuccessResponse(page)
        serializer = self.get_serializer(queryset, many=True)
        return SuccessResponse(serializer.data)




from rest_framework.views import APIView


class ComnameAPiview(APIView):
    def post(self,request,*args,**kwargs):
        # comname = request
        print(request.data.get("comname"))
        money = request.data.get("comname")
        s = int(money) % 5
        print(s)
        return SuccessResponse(status=200)
from apps.vadmin.staticdata.serializers import ProjectModelExport
class FormdataApiview(CustomModelViewSet):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectModelSerlizer
    filter_class = ProjectFilter
    ordering = '-create_datetime'
    search_fields = ('pronum','proname','category',)
    export_field_data = ['主键id','创建人所属id', '所属项目经理', '电话', '项目组', '项目类别', '项目名称', '项目号', '姓名', '电话', '部门', '部门', '组织代码', '工厂', '公司名称', '基地/区域', '国家', '地区','成本中心/SAP 号','客户公司财务人员','客户公司财务人员邮箱','预计净服务费(不含税)RMB','预计净服务费(含5% mark-up) RMB','预计总服务费(含税)','项目名称','开始时间','截止时间','项目概述','项目范围/工作包','交付内容','电话','该项目涉及双重用途物质清单中的物质',]
    export_serializer_class = ProjectModelExport

    def get_serializer_class(self):
        if self.action == "create":
            return ProjectPostModelSerlizer
        elif self.action == "list":
            print(self.request.query_params)
            print("这边是list")
            return ProjectModelSerlizer
        else:
            print("没有选择的话")
            return ProjectModelSerlizer



    def create(self, request: Request, *args, **kwargs):
        print(request.user.id)
        print(request.data.get("dateRange"))
        print(request.data.get("end_time"))
        request.data["end_time"] = request.data.get("dateRange")[1]
        request.data["start_time"] = request.data.get("dateRange")[0]
        request.data["checkList"] = request.data.get("checkList")[0]
        # print(self.request.methods)
        request.data["userid"] = request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        if hasattr(self, 'handle_logging'):
            self.handle_logging(request, instance=serializer.instance, *args, **kwargs)
        headers = self.get_success_headers(serializer.data)
        return SuccessResponse(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    def list(self, request: Request, *args, **kwargs):
        if hasattr(self, 'handle_logging'):
            self.handle_logging(request, *args, **kwargs)
        dept = UserProfile.objects.filter(id=self.request.user.id).first()
        obj = Dept.objects.filter(deptName=dept.dept).first()
        daterange1 = self.request.query_params.get("dateRange[0]")
        datarange2 = self.request.query_params.get("dateRange[1]")
        datarange1 = str(daterange1) + ".000000"
        datarange2 = str(datarange2) + ".000000"
        # 时间第一模块
        if obj.parentId is None:
            if daterange1 and datarange2 is not None:
                queryset = self.filter_queryset(self.get_queryset().filter(create_datetime__range=(datarange1,datarange2)))
            else:
                queryset = self.filter_queryset(self.get_queryset().filter())
        elif obj.parentId.id == 1:
            queryset = self.filter_queryset(self.get_queryset())
        else:
            queryset = self.filter_queryset(self.get_queryset().filter(deptName=dept.dept))
        page = self.paginate_queryset(queryset)
        if page is not None:
            if getattr(self, 'values_queryset', None):
                return self.get_paginated_response(page)
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        if getattr(self, 'values_queryset', None):
            return SuccessResponse(page)
        serializer = self.get_serializer(queryset, many=True)
        return SuccessResponse(serializer.data)



class ReserveModel(CustomModelViewSet):
    queryset = Reserve.objects.all()
    serializer_class = ReserveModelSerlizer

from apps.vadmin.staticdata.serializers import ReserveModelsSerlizer
class ReservesModel(CustomModelViewSet):
    queryset = Reserve.objects.all()
    serializer_class = ReserveModelsSerlizer


class CompanyModelViewset(CustomModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanyModelSerlizer


class Gongsiviewset(CustomModelViewSet):
    queryset = Projectinfo.objects.all()
    serializer_class = Project1infoSerlizer

    def retrieve(self, request: Request, *args, **kwargs):
        print("请求过来了")
        print(self.request.query_params)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if hasattr(self, 'handle_logging'):
            self.handle_logging(request, instance=instance, *args, **kwargs)
        return SuccessResponse(serializer.data)




class ProjecFilterApiview(APIView):
    def post(self,request,*args,**kwargs):
        print("收到了请求")
        print(request.data)
        userid = request.user.id
        id = request.data.get("id")
        money = request.data.get("money")
        obj = Reserve.objects.filter(applicant=userid,projectid=id)
        if obj:
            return SuccessResponse(data={"message": "已经申请过了"})
        moneypay = 0
        reser = Reserve.objects.filter(projectid=id)
        for i in reser:
            moneypay+=int(i.money)
        print(moneypay)
        s = ProjectModel.objects.filter(id=id).first()
        if int(s.money) <= int(money):
            return SuccessResponse(data={"message":"项目资金没有那么多了"})
        if int(s.money) <= int(moneypay):
            return SuccessResponse(data={"message":"项目资金没有那么多了"})
        else:
            Reserve.objects.create(applicant=userid,projectid=id,money=money).save()
            return SuccessResponse(data={"message": "项目申请资金成功"})

    def get(self,request,*args,**kwargs):
        # id = request.query_parmas()
        id = request.query_params.get("id")
        userid = request.user.id
        reser = Reserve.objects.filter(projectid=id,applicant=userid).first()
        if reser:
            money = reser.money
            print(money)
            return SuccessResponse(status=200,data=money)
        else:
            return SuccessResponse(status=201,data=0)


class StatsicAPiview(APIView):
    def get(self,request,*args,**kwargs):
        dept = Dept.objects.all()
        b = []
        a = []
        c = []
        d = []
        procount = ProjectModel.objects.count()
        zong = 0
        yong = 0
        mon = 0
        for i in ProjectModel.objects.all():
            zong += int(i.money)
        for ss in Reserve.objects.all():
            yong += int(ss.money)
        for i in dept:
            b.append(i.deptName)
            count = ProjectModel.objects.filter(deptName=i.deptName).count()
            s = ProjectModel.objects.filter(deptName=i.deptName)
            for x in s:
                mon += int(x.money)
            a.append({"name": i.deptName, "value": count})
            c.append(i.deptName)
            d.append(mon)
            mon = 0
        return SuccessResponse(data={"datas":a,"datass":b,"c":c,"d":d,"procount":procount,"zong":zong,"yong":yong,"shengyu":zong-yong})


class KpimodelApiview(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        kpiname = request.data.get("kpiname")
        # 组别id
        mubiao = request.data.get("mubiao")
        # 金额金钱
        category = str(request.data.get("category")).replace(" ","")
        # 时间
        datatime = str(request.data.get("datatime")).replace(" ","")
        # 类型
        ifex = Kpimodel.objects.filter(kpiname=kpiname,datatime=datatime,category=category).first()
        if ifex:
            ifex.mubiao = mubiao
            ifex.save()
            SuccessResponse(data={"data":"存在了"})
        else:
            Kpimodel.objects.create(kpiname=kpiname,mubiao=mubiao,category=int(category),datatime=datatime).save()
        return SuccessResponse()


    def get(self,request,*args,**kwargs):
        kpiname = request.query_params.get("status")
        mubiao = request.query_params.get("mubiao")
        datatime = request.query_params.get("value2")
        obj = Kpimodel.objects.filter(kpiname=kpiname,mubiao=mubiao).first()
        if obj:
            return SuccessResponse(data={"data":obj.mubiao})
        else:
            return SuccessResponse()


import datetime
class Kpimodelapview(APIView):
    def get(self,request,*args,**kwargs):
        year = datetime.datetime.now().year
        yue = datetime.datetime.now().month
        if len(str(yue)) == 1:
            a = "{}-0{}-0100:00".format(year, yue)
        else:
            a = "{}-{}-0100:00".format(year, yue)
        # 这是后面的逻辑
        ibj1 = Dept.objects.filter(parentId__deptName="RCP/OA")
        for i in ibj1:
            isexit = Kpimodel.objects.filter(kpiname=i.id,category=2, datatime=a)
            if isexit:
                pass
            else:
                Kpimodel.objects.create(kpiname=i.id, mubiao=5000000, category=2, datatime=a).save()
        x = []
        for sas in ibj1:
            nas = Kpimodel.objects.filter(datatime=a, category="2", kpiname=sas.id).first()
            x.append({"depName": nas.kpiname, "money": nas.mubiao})
        shuju = []
        for shudui in x:
            dept = Dept.objects.filter(id=int(shudui['depName'])).first()
            pik = Kpimodel.objects.filter(kpiname=dept.id).first()
            asia = Dept.objects.filter(id=pik.kpiname).first()
            objs = ProjectModel.objects.filter(deptName=asia)
            he = 0
            for n in objs:
                he += int(n.money)
            jine = int(pik.mubiao)
            rcpoa = "{:.2%}".format(he / jine)
            baifnebi = rcpoa.replace("%", " ")
            shuju.append({"depName": asia.deptName, "baifenbi": baifnebi, "money": pik.mubiao, "he": he})
        a = 0
        hias = 0
        for i in shuju:
            a += int(i.get("money"))
            hias += int(i.get("he"))
        rcpoa = "{:.2%}".format(hias / a)
        baifnebi = rcpoa.replace("%", " ")
        he12 = {"depName": "RCP/OA", "baifenbi": baifnebi, "money": a, "he": hias}
        return SuccessResponse(data={"data": shuju, "he": he12})



class Pkimodelapview(APIView):
    def get(self,request,*args,**kwargs):
        print(request.query_params)
        kpiname = request.query_params.get("kpiname")
        datatime = str(request.query_params.get("datatime")).replace(" ","")
        category = request.query_params.get("category")
        print(datatime)
        s = Kpimodel.objects.filter(kpiname=kpiname,category=category,datatime=datatime).first()
        if s:
            return SuccessResponse(data={"data":s.mubiao})
        else:
            return SuccessResponse(data={"data":5000000})