from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from ckeditor.fields import RichTextField

# Create your models here.
TITLE_CHOICES = [
    ('male', 'Male.'),
    ('female', 'Female.'),
    ('other', 'Other'),
]
Qualification_CHOICES = [
    ('Doctorate/PhD', 'Doctorate/PhD'),
    ('Masters/Post-Graduation', 'Masters/Post-Graduation'),
    ('Graduation/Diploma', 'Graduation/Diploma'),
    ('12th','12th'),
    ('12th','10th'),
    ('below 10th','Below 10th')
]
Min_lacks = [
    ('50,000','50000'),
    ('100,000','100,000'),
    ('200,000','200,000'),
    ('300,000','300,000'),
    ('400,000','400,000'),
    ('500,000','500,000'),
    ('600,000','600,000'),
    ('700,000','700,000'),
    ('800,000','800,000'),
    ('900,000','900,000'),
    ('10,00,000','10,00,000'),
]
Max_lacks = [
    ('50,000','50000'),
    ('100,000','100,000'),
    ('200,000','200,000'),
    ('300,000','300,000'),
    ('400,000','400,000'),
    ('500,000','500,000'),
    ('600,000','600,000'),
    ('700,000','700,000'),
    ('800,000','800,000'),
    ('900,000','900,000'),
    ('10,00,000','10,00,000'),
]
Min_Experience = [
    ('0','0'),
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10'),


]
Max_Experience = [
    ('0','0'),
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10'),
]
Range =[
    ('10','10'),
    ('20','20'),
    ('30','30'),
    ('40','40'),
    ('50','50'),
    ('60','60'),
    ('70','70'),
    ('80','80'),
    ('90','90'),
    ('100','100'),
]
dummy=[
     ('0','0'),
 ]
status = [
    ('Read','Read'),
    ('Unread','Unread'),
]
# class User(AbstractUser):
#     is_student = models.BooleanField(default=False)
#     is_teacher = models.BooleanField(default=False)
class Qualification(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Qualification_Course(models.Model):
    country = models.ForeignKey(Qualification, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
class Fresher(models.Model):
    FirstName = models.CharField(max_length=100,blank=False)
    SecondName = models.CharField(max_length=100,blank=False)
    Email = models.EmailField()
    PhoneNumber = models.IntegerField()
    UserName = models.CharField(blank=False,max_length=100)
    Password = models.CharField(blank=False,max_length=100)
    def __str__(self):
        return self.UserName
class FresherData(models.Model):
    Gender = models.CharField(max_length=6,choices=TITLE_CHOICES)
    Nationality = models.CharField(max_length=100,blank=False)
    Religion = models.CharField(max_length=100,blank=False)
    Age = models.CharField(max_length=2,blank=True)
    Address = models.CharField(max_length=500,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True )
    def __str__(self):
        return self.Nationality
class FresherQualification(models.Model):  
    Highest_Qualification= models.ForeignKey(Qualification,on_delete=models.SET_NULL, null=True,max_length=100)
    SubQualification = models.CharField(max_length=100)
    Specialization = models.CharField(max_length=100,null=True,blank=True)
    Skills1 = models.CharField(max_length=100,blank=True)
    Range1 = models.CharField(max_length=100,choices=Range,blank=True)
    Skills2 = models.CharField(max_length=100,blank=True)
    Range2 = models.CharField(max_length=100,choices=Range,blank=True)
    Skills3 = models.CharField(max_length=100,blank=True)
    Range3 = models.CharField(max_length=100,choices=Range,blank=True)
    Skills4 = models.CharField(max_length=100,blank=True)
    Range4 = models.CharField(max_length=100,choices=Range,blank=True)
    Skills5 = models.CharField(max_length=100,blank=True)
    Range5 = models.CharField(max_length=100,choices=Range,blank=True)
    Skills6 = models.CharField(max_length=100,blank=True)
    Range6 = models.CharField(max_length=100,choices=Range,blank=True)
    Course_Type = models.CharField(max_length=100)
    Passing_Year = models.CharField(max_length=100)
    Phone = models.CharField(max_length=10,blank=True)
    Resume = models.FileField(upload_to = 'Resume')
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True )
    
    def __str__(self):
        return self.Specialization
class ProfileImg(models.Model):
    Profile = models.FileField(upload_to='profile')
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True )
class profilesummary(models.Model):
    StudentInfo = models.CharField(max_length=500,blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True )
class JobRequirments(models.Model):
    CompanyName = models.CharField(max_length=100)
    Company_Description = models.CharField(max_length=100)
    Skills = models.CharField(max_length=100)
    Roles_and_Responsabulity = models.CharField(max_length=100)
    Iterview_Date = models.DateField()
    Interview_Location = models.CharField(max_length=100)
    Min_Salary = models.CharField(max_length=100,blank=True,choices=Min_lacks)
    Max_Salary = models.CharField(max_length=100,blank=True,choices=Max_lacks)
    Min_Exp = models.CharField(max_length=10,blank=True,choices=Min_Experience)
    Max_Exp = models.CharField(max_length=10,blank=True,choices=Max_Experience)
    First_HrName = models.CharField(max_length=100)
    Second_HrName = models.CharField(max_length=100)
    First_HrNumber = models.IntegerField()
    Second_HrNumber = models.IntegerField()
    manager = models.ForeignKey(User,on_delete=models.CASCADE)
    fresherqualification = models.ManyToManyField(FresherQualification, blank=True)
    class Meta:
            ordering = ['CompanyName']
    def __str__(self):
        return self.CompanyName
class Notifications(models.Model):
    Status = models.CharField(choices=status,max_length=100,blank=True,null=True)
    Name = models.CharField(max_length=100,blank=True,null=True)
    Subject = models.CharField(max_length=100,blank=True,null=True)
    Message = RichTextField(max_length=10000,blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True )
    sender = models.CharField(max_length=100,blank=True,null=True)
    Profile = models.FileField(upload_to='profile',null= True)

    def __str__(self):
        return self.Name

# creating chatting process for this application



