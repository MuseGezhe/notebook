from django.db import models

# Create your models here.
class Grade(models.Model):
    name     = models.CharField(max_length=20)
    boyNum   = models.IntegerField()
    girlNum  = models.IntegerField()
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    class Meta():
        db_table = "grades"



class StudentManager(models.Manager):
    def get_queryset(self):
        return super(StudentManager, self).get_queryset().filter(isDelete=False)

class Student(models.Model):
    #自定义模型管理器
    objects = StudentManager()

    name     = models.CharField(max_length=20)
    sex      = models.BooleanField()
    age      = models.IntegerField()
    contend = models.CharField(max_length=40)
    #                            关联类名的小写
    grade    = models.ForeignKey("grade")
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    class Meta():
        db_table = "students"
        ordering = ["-id"]
    @classmethod
    def create(cls, name, sex, age, contend, grade):
        return cls(name=name, sex=sex, age=age, contend=contend, grade=grade)
