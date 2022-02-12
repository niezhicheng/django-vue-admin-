from apps.vadmin.op_drf.serializers import CustomModelSerializer
from apps.vadmin.permission.models.users import UserProfile
from apps.vadmin.permission.models.dept import Dept
from apps.vadmin.permission.models.post import Post
from apps.vadmin.permission.models.role import Role
from apps.vadmin.staticdata.models.data import Category,Projectinfo,Country,SiteArea,Region,Company
from apps.vadmin.staticdata.models.project import ProjectModel,Reserve
from rest_framework import serializers
import json
class CountrySerializer(CustomModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("username","id","name",)

class DeptSerizlier(CustomModelSerializer):
    class Meta:
        model = Dept
        fields = "__all__"

class PostSerizlier(CustomModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

class CountryPostSerializer(CustomModelSerializer):
    post = PostSerizlier(many=True)
    class Meta:
        model = UserProfile
        fields = ("dept","id","role","post","mobile")


class CategorySerlizer(CustomModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProjectinfoSerlizer(CustomModelSerializer):
    class Meta:
        model = Projectinfo
        fields = "__all__"


class ProjectinfoPostSerlizer(CustomModelSerializer):
    class Meta:
        model = Projectinfo
        fields = "__all__"



class CountrySerlizer(CustomModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"



class SiteAreaSerlizer(CustomModelSerializer):
    class Meta:
        model = SiteArea
        fields = "__all__"


class RegionSerlizer(CustomModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"


class DeptSerlizer(CustomModelSerializer):
    class Meta:
        model = Dept
        fields = "__all__"

class CompanyModelSerlizer(CustomModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"

class Project1infoSerlizer(CustomModelSerializer):
    company_name = CompanyModelSerlizer()
    site_area = SiteAreaSerlizer()
    country = CountrySerlizer()
    region = RegionSerlizer()

    class Meta:
        model = Projectinfo
        fields = "__all__"


class ProjectModelSerlizer(CustomModelSerializer):
    userid = serializers.IntegerField()
    leader = serializers.SerializerMethodField()
    shengyu = serializers.SerializerMethodField()
    # deptName = serializers.SerializerMethodField()
     # = serializers.SerializerMethodField()

    def get_leader(self,obj):
        s = UserProfile.objects.filter(id=obj.leader).first()
        return s.name if s.name else s.username

    def get_shengyu(self,obj):
        s = int(obj.money)
        a = 0
        for i in Reserve.objects.filter(projectid=obj.id):
            a += int(i.money)
        return s - a

    # def get_deptName(self,obj):
    #     print(obj.deptName)
    #     # m = Dept.objects.filter(deptName=obj.deptName).first()
    #     return obj.leader
    class Meta:
        model = ProjectModel
        fields = "__all__"


# 上面的是get 请求

# 下面是post
import datetime
class ProjectPostModelSerlizer(CustomModelSerializer):
    def validate(self, attrs):
        attrs['userid'] = self.request.user.id
        s = datetime.date
        x = s.today().year
        a = '1'
        b = int(a)
        print('%03d' % b)
        s = "%03d" % b
        m = ("%s") % x + "{}".format(s)
        obj2 = ProjectModel.objects.filter(pronum=m).first()
        if obj2:
            s = ProjectModel.objects.all().order_by('-create_datetime').first()
            num1 = int(s.pronum) + 1
            attrs['pronum'] = num1
            print(self.request.data)
        else:
            attrs['pronum'] = m
        return attrs
    class Meta:
        model = ProjectModel
        fields = "__all__"


class ReserveModelSerlizer(CustomModelSerializer):
    class Meta:
        model = Reserve
        fields = "__all__"


class ReserveModelsSerlizer(CustomModelSerializer):
    projectid = serializers.SerializerMethodField()
    applicant = serializers.SerializerMethodField()
    pronum = serializers.SerializerMethodField()
    shengyu = serializers.SerializerMethodField()

    def get_shengyu(self,obj):
        # Reserve.objects.filter()
        return 1

    def get_projectid(self, obj):
        s = ProjectModel.objects.filter(id=obj.projectid).first()
        return s.proname

    def get_applicant(self,obj):
        s = UserProfile.objects.filter(id=obj.applicant).first()
        return s.username

    def get_pronum(self,obj):
        s = ProjectModel.objects.filter(id=obj.projectid).first()
        return s.pronum
    class Meta:
        model = Reserve
        fields = "__all__"



from apps.vadmin.staticdata.models.project import ProjectModel
class ProjectModelExport(CustomModelSerializer):
    """
    导出 项目字典管理 简单序列化器
    """
    class Meta:
        model = ProjectModel
        # fields = ('id', 'leader', 'mobile','deptName','category','proname','name','number','divison','code','plant','compayname','area','deptName','content','start_time', 'end_time', 'overview', 'material',)
        fields = "__all__"
