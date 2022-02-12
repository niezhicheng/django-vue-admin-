from django.db.models import CharField, BooleanField, TextField
from django.db import models
from apps.vadmin.permission.models.users import UserProfile
from apps.vadmin.staticdata.models.data import Category
from apps.vadmin.permission.models.dept import Dept
from apps.vadmin.op_drf.models import CoreModel,BaseModel
from datetime import datetime

class ProjectModel(BaseModel):
    # 甲方信息
    userid = models.IntegerField(verbose_name="创建人所属id")
    leader = models.CharField(max_length=64,verbose_name="所属项目经理")
    mobile = models.CharField(max_length=64,verbose_name="电话")
    deptName = models.CharField(max_length=64,verbose_name="项目组")
    category = models.ForeignKey("Category", on_delete=models.CASCADE, verbose_name="项目类别")
    proname = models.CharField(max_length=64,verbose_name="项目名称")
    pronum = models.CharField(max_length=64,verbose_name="项目号")
    # 乙方信息
    name = models.CharField(max_length=64,verbose_name="姓名")
    number = models.CharField(max_length=64,verbose_name="电话")
    divison = models.CharField(max_length=64,verbose_name="部门")
    code = models.CharField(max_length=64,verbose_name="组织代码")
    plant = models.CharField(max_length=64,verbose_name="工厂")
    compayname = models.CharField(max_length=64,verbose_name="公司名称")
    area = models.CharField(max_length=64,verbose_name="基地/区域")
    country = models.CharField(max_length=64,verbose_name="国家")
    region = models.CharField(max_length=64,verbose_name="地区")
    spanr = models.CharField(max_length=64,verbose_name="成本中心/SAP 号")
    coutroller = models.CharField(max_length=64,verbose_name="客户公司财务人员")
    email = models.CharField(max_length=64,verbose_name="客户公司财务人员邮箱")
    money = models.CharField(max_length=64,verbose_name="预计净服务费(不含税)RMB")
    moneymark = models.CharField(max_length=64,verbose_name="预计净服务费(含5% mark-up) RMB")
    zongmoney = models.CharField(max_length=64,verbose_name="预计总服务费(含税)")
    projectname = models.CharField(max_length=64,verbose_name="项目名称")
    start_time = models.DateField(verbose_name="开始时间")
    end_time = models.DateField(verbose_name="截止时间")
    checkList = models.TextField(max_length=64,verbose_name="项目概述")
    package = models.CharField(max_length=64,verbose_name="项目范围/工作包")
    content = models.CharField(max_length=64,verbose_name="交付内容")
    overview = models.CharField(max_length=64,verbose_name="电话")
    material = models.CharField(max_length=64,verbose_name="该项目涉及双重用途物质清单中的物质")

    class Meta:
        verbose_name = "项目信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.proname


class Reserve(BaseModel):
    projectid = models.IntegerField(verbose_name="申请的项目id")
    applicant = models.IntegerField(verbose_name="申请人id")
    money = models.CharField(max_length=64,verbose_name="金钱数额")

    class Meta:
        verbose_name = "项目信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}".format(self.projectid)


class Kpimodel(BaseModel):
    choice_check = (
        (1,'年度'),
        (2,'月度')
    )
    kpiname = models.IntegerField(verbose_name="部门名称id")
    mubiao = models.CharField(max_length=32,verbose_name="目标金额")
    category = models.CharField(choices=choice_check,default="1",max_length=16)
    datatime = models.CharField(max_length=32,verbose_name="时间")

    class Meta:
        verbose_name = "kpi指数"
        verbose_name_plural = verbose_name

    def __int__(self):
        return self.kpiname

