from django.contrib import admin

# Register your models here.
from myApp.models import Student,Grade

# 创建班级时关联添加学生
class StudentInLine(admin.TabularInline):
    model = Student
    # 添加学生数量
    extra = 2

class GradeAdmin(admin.ModelAdmin):
    inlines = [StudentInLine]
    list_display = ['pk','name','boyNum','girlNum','isDelete']
admin.site.register(Grade,GradeAdmin)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    #设置执行动作的位置
    actions_on_top = False
    actions_on_bottom = True

    # 设置布尔属性
    def sex(self):
        if self.sex:
            return '男'
        else:
            return '女'
    #设置页面列的名称
    sex.short_description = '性别'
    def isDelete(self):
        if self.isDelete:
            return '是'
        else:
            return '否'

    #列表页属性
    list_display = ['pk','name','age',sex,'contend','grade',isDelete]
    list_filter = ['grade']
    search_fields = ['contend']
    list_per_page = 3

    #添加、修改页属性
    # fields = ['name','age','sex','contend','grade','isDelete']
    fieldsets = [
        ('base',{'fields':['name','age','grade']}),
        ('more',{'fields':['sex','contend','isDelete']}),
    ]
# admin.site.register(Student,StudentAdmin)

