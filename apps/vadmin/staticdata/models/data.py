from django.db.models import CharField, BooleanField, TextField
from django.db import models
from apps.vadmin.op_drf.models import CoreModel,BaseModel


class Country(BaseModel):
    """
    国家名称模型
    """
    country = models.CharField(max_length=64,verbose_name="国家名字")

    class Meta:
        verbose_name = "国家名字"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.country

class SiteArea(BaseModel):
    """
    工厂所属基地模型
    """
    sitearea = models.CharField(max_length=64,verbose_name="工厂所属基地")

    class Meta:
        verbose_name = "工厂所属基地"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sitearea


class Region(BaseModel):
    """
    区域名称模型
    """
    region = models.CharField(max_length=64,verbose_name="区域名称")

    class Meta:
        verbose_name = "区域名称模型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.region


class Company(BaseModel):
    compname = models.CharField(max_length=64,verbose_name="分公司名称")

    class Meta:
        verbose_name = "分公司管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.compname


class Projectinfo(BaseModel):
    """
    项目所属子公司管理
    """
    company_name = models.ForeignKey("Company",on_delete=models.CASCADE,verbose_name="分公司名称")
    site_area = models.ForeignKey("SiteArea",on_delete=models.CASCADE,verbose_name="工厂所属基地")
    country = models.ForeignKey("Country",on_delete=models.CASCADE,verbose_name="国家")
    region = models.ForeignKey("Region",on_delete=models.CASCADE,verbose_name="区域")

    class Meta:
        verbose_name = "项目所属子公司管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}".format(self.company_name.id)



class Category(BaseModel):
    """
    项目类别
    """
    category = models.CharField(max_length=64,verbose_name="项目类别")

    class Meta:
        verbose_name = "项目类别模型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.category


class CheckList(BaseModel):
    """
    checkList
    """
    checkList = models.CharField(max_length=64,verbose_name="选项个")

    class Meta:
        verbose_name = "项目类别模型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.checkList
