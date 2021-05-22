from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,Http404
from .forms import  FresherModel,FresherDataModel,FresherQualificationModel,Qualification_Course,JobRequirmentsModel,ProfileImgModel,NotificationModel
from .models import FresherQualification,JobRequirments,FresherData,Notifications,profilesummary
from django.core.files.storage import FileSystemStorage
from .functions import handle_uploaded_file
from .models import Fresher,FresherData,JobRequirments,ProfileImg,Qualification
from django.conf import settings
from django.core import serializers
from django.http import JsonResponse
import json
import datetime
from django.views.generic import ListView,DetailView
from django.db.models import Q
import sys
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import requires_csrf_token
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.urls import reverse
from django.contrib import messages
from django.db.models import Count
from django.core.paginator import Paginator
from django.urls import path
from django.http import FileResponse
from django.utils.encoding import force_text, smart_str
import pdb;
import os
from django.conf import settings


@requires_csrf_token

@csrf_exempt

@cache_page(60 * 15)
@csrf_protect





# Create your views here.
# def Home_of_jobkarle(Listview):
#     model = JobRequirments
#     template_name = jobkarleapp/ba
def FresherRigister(request):
    
    # import pdb;pdb.set_trace()
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.info(request,'!That username is already taken.')
            return render(request,'FresherRigister.html')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'!That email is already taken.')
            return render(request,'FresherRigister.html')
        else:
            obj = User(first_name = firstname , last_name = lastname ,email = email , username = username ,password = password)
            obj.set_password(password)
            obj.is_student = True
            obj.save()
            # import pdb;pdb.set_trace()
            user_data = User.objects.get(username = username)
            return HttpResponseRedirect(reverse('jobkarlepro:fresherdata', args={user_data.id}))
           
    forms = FresherModel()
    # latest_updates = JobRequirments.objects.latest('id')
    temp = JobRequirments.objects.all()
    count = JobRequirments.objects.all().count()
    dump= count - 5
    latest_updates = temp[dump:count]
    return render(request,'FresherRigister.html',{ 'forms':forms,'latest_updates':latest_updates})

def CompanyRegister(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('secondname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.info(request,'!That username is already taken.')
            return render(request,'FresherRigister.html')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'!That email is already taken.')
            return render(request,'FresherRigister.html')
        obj = User(first_name = firstname , last_name = lastname ,email = email , username = username ,password = password)
        obj.set_password(password)
        obj.is_staff = True
        obj.save()
        user_data = User.objects.get(username = username )
        return HttpResponseRedirect(reverse('jobkarlepro:fresherdata', args={user_data.id}))
def profileimg(request):
    pass
def ProfileData(request,User_id):
    user_data = User.objects.get(id=User_id)
    student_jobs = JobRequirments.objects.all()
    paginator=Paginator(student_jobs, 10)
    page_obj = paginator.get_page(1)

    # import pdb;pdb.set_trace()
    user_personal_data = FresherData.objects.get(user_id=user_data.id)
    user_qualification = FresherQualification.objects.get(user_id=user_data.id)
    # import pdb; pdb.set_trace()
    forms = FresherQualificationModel()
    profilepic = ProfileImg.objects.get(user_id=user_data.id)
    notifications=Notifications.objects.filter(user_id = user_data.id)
    notification_count=Notifications.objects.filter(Status = 'Unread',user_id = user_data.id).count()
    notification_unread=Notifications.objects.filter(user_id = user_data.id,Status = 'Unread')
    notification_read=Notifications.objects.filter(Status = 'Read')
    return render(request,'userpage.html',{
        'user_data':user_data,
        'student_jobs':page_obj,
        'user_personal_data':user_personal_data,
        'profilepic':profilepic,
        'user_qualification':user_qualification,
        'forms':forms,
        'notifications':notifications,
        'notification_count':notification_count,
        'notification_unread':notification_unread, 
        'notification_read':notification_read, })
    
def Companyprofile_data(request,User_id):
    user_data = User.objects.get(id=User_id)
    user_personal_data = FresherData.objects.get(user_id = user_data.id)
    jobs_data = JobRequirments.objects.all()
    obj1 = JobRequirments.objects.filter(manager__id=User_id)
    # obj2 = FresherQualification.objects.filter(jobrequirments__fr)
    # import pdb;pdb.set_trace()
    # user_personal_data = FresherData.objects.get(user_id=user_data.id)
    profilepic = ProfileImg.objects.get(user_id=user_data.id)
    notifications=Notifications.objects.filter(user_id = user_data.id)
    notification_count=Notifications.objects.filter(Status = 'Unread',user_id = user_data.id).count()
    notification_unread=Notifications.objects.filter(user_id = user_data.id,Status = 'Unread')
    notification_read=Notifications.objects.filter(Status = 'Read')
    return render(request,'companypage.html',{
        'user_data':user_data,
        'jobs_data':jobs_data,
        'obj1':obj1,
        'user_personal_data':user_personal_data,
        'profilepic':profilepic,
        'notifications':notifications,
        'notification_count':notification_count,
        'notification_unread':notification_unread, 
        'notification_read':notification_read,

    })

@ensure_csrf_cookie
@csrf_exempt
@cache_page(60 * 15)
@csrf_protect
@requires_csrf_token
def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == "":
            messages.info(request,'!That username is should not be empty.')
            return render(request,'FresherRigister.html')
        elif password == "":
            messages.info(request,'!That password should not be empty.')
            return render(request,'FresherRigister.html')
        if authenticate(request,username = username , password = password):
            validation = User.objects.get(username=username)
            users = authenticate(request,username = username , password = password)
            if validation.is_staff == False:
                if users is not None:
                    login(request,users)
                    user_data = User.objects.get(username=username)
                    return HttpResponseRedirect(reverse('jobkarleapp:ProfileData', args={user_data.id}))
            else:
                    if  validation.is_staff == True:
                        if users is not None:
                            # import pdb;pdb.set_trace()
                            login(request,users)
                            user_data = User.objects.get(username=username)
                            return HttpResponseRedirect(reverse('jobkarleapp:Companyprofile_data', args={user_data.id}))
        else:
            messages.info(request,'Login With Valid Username and Password.')
            return render(request,'FresherRigister.html')   
@ensure_csrf_cookie
@cache_page(60 * 15)                
@csrf_protect
def Logout(request):
    logout(request)
    return HttpResponseRedirect('FresherRigister')
def mulltisearch(request,idd):
    if request.method == "GET":

        Role = request.GET.get('role')
        Location = request.GET.get('location')
        Experiance = request.GET.get('experiance')
        Salary = request.GET.get('salary')
        # sys.setrecursionlimit(10**6)
        student_jobs = JobRequirments.objects.filter(Q(Interview_Location__iexact = Location) | Q(Skills__iexact = Role) ).order_by()
        # sys.setrecursionlimit(10**6)
        # import pdb;pdb.set_trace()
        user_data = User.objects.get(id=idd)
        # import pdb;pdb.set_trace()
        user_personal_data = FresherData.objects.get(user_id=user_data.id)
        user_qualification = FresherQualification.objects.get(user_id=user_data.id)
        # import pdb; pdb.set_trace()
        forms = FresherQualificationModel()
        profilepic = ProfileImg.objects.get(user_id=user_data.id)
        notifications=Notifications.objects.filter(user_id = user_data.id)
        notification_count=Notifications.objects.filter(Status = 'Unread',user_id = user_data.id).count()
        notification_unread=Notifications.objects.filter(user_id = user_data.id,Status = 'Unread')
        notification_read=Notifications.objects.filter(Status = 'Read')
        return render(request,'userpage.html',{
        'user_data':user_data,
        'student_jobs':student_jobs,
        'user_personal_data':user_personal_data,
        'profilepic':profilepic,
        'user_qualification':user_qualification,
        'forms':forms,
        'notifications':notifications,
        'notification_count':notification_count,
        'notification_unread':notification_unread, 
        'notification_read':notification_read, })
def FreshExtradata(request):
     if request.method == "POST":
            # import pdb;pdb.set_trace()
        forms = FresherDataModel(request.POST)
        id = request.POST.get('user_id')
        user = User.objects.get(id = id)
        #import pdb;pdb.set_trace()
        if forms.is_valid():
            data = forms.save()
            obj = FresherData.objects.get(id=data.id)
            obj.user = user
            obj.save()
            # import pdb;pdb.set_trace()
            user_data =  User.objects.get(id = user.id)
            print(user_data)
            if user_data.is_staff == True:
                return HttpResponseRedirect(reverse('jobkarleapp:Profiledef', args={user_data.id}))
            else:
                return HttpResponseRedirect(reverse('jobkarleapp:fresherqualification', args={user_data.id}))

        return render(request,'Fresherdata.html',{'forms':forms,})

def fresherdata(request,User_id):
    forms = FresherDataModel()
    user_id = User.objects.get(id = User_id)
    return render(request,'Fresherdata.html',{'forms':forms,'user_id':user_id})

def fresherqualification(request,User_id):
    forms = FresherQualificationModel()
    user_id = User.objects.get(id= User_id)
    return render(request,'FresherQualification.html',{'forms':forms,'user_id':user_id})
def fresherqualificationextra(request):
     if request.method == 'POST':
            #import pdb;pdb.set_trace()
        forms = FresherQualificationModel(request.POST, request.FILES)
        # import pdb;pdb.set_trace()
        if forms.is_valid():
            data = forms.save()
            dump = request.POST.get('course')
            id = request.POST.get('user_id')
            profileimg = request.POST.get('profile')
            user = User.objects.get(id = id)
            obj = FresherQualification.objects.get(id = data.id)
            obj.SubQualification = dump
            obj.user = user
            obj.save()
            return HttpResponseRedirect(reverse('jobkarleapp:Profiledef', args={user.id}))
        else:
              return render(request,'FresherQualification.html',{'forms':forms})
def Profiledef(request,User_id):
    user_data = User.objects.get(id = User_id)
    forms = ProfileImgModel()
    return render(request,'profileimg.html',{'user_data':user_data,'forms':forms})
def Profileextradef(request):
    if request.method == "POST":
        dump = request.FILES.get('Profile')
        # import pdb;pdb.set_trace()
        id = request.POST.get('user_id')
        user = User.objects.get(id = id)
        tempobj = ProfileImg()
        tempobj.Profile = dump
        tempobj.user = user
        tempobj.save()
        return HttpResponseRedirect(reverse('jobkarleapp:Logout'))
def country_list(request):
    country_data1 = []
    # import pdb;pdb.set_trace()
    if request.method == 'POST':
        # to read the data from COUNTRIES2.json in this project
        country_data = json.loads(open(settings.COUNTRIES2[0], 'r').read())
        return HttpResponse(json.dumps(country_data))
    else:
        pass
def Support_Course(request,Highest_Qualification_id):
    data_list = Qualification_Course.objects.filter( country__id = Highest_Qualification_id).order_by()
    return JsonResponse({'data':json.dumps(data_list)})
def load_Course(request):
    Highest_Qualification_id = request.POST.get('Highest_Qualification_id')
    # import pdb;pdb.set_trace()
    #data = Qualification_Course.objects.filter( country_id = Highest_Qualification_id).order_by('name')
    # courses_data = Qualification_Course.objects.filter( country_id = Highest_Qualification_id).order_by()
    # courses_data = Qualification_Course.objects.filter( country__id = Highest_Qualification_id).order_by()
    courses_data = Qualification_Course.objects.filter(country=Highest_Qualification_id)
    data = courses_data.values_list('name',flat=True)
    data_list = [name for name in data]
    # import pdb;pdb.set_trace()
    return JsonResponse({'data':json.dumps(data_list)})
    # return HttpResponseRedirect(reverse('jobkarleapp:Support_Course',kwargs={'Highest_Qualification_id.id'}))
    
    #return HttpResponse(json.dumps(data))
    #return render(request, 'FresherQualification.html', {'data':data})
# def Users_Login(request):
#     if request.method =="POST":
#         Username = request.POST.get('username')
#         Password = request.POST.get('password')
#         user = auth
#         if Username and Password:
def room(request, room_name):
    return render(request, 'multifilter.html', {
        'room_name': room_name
    })
def job_postview(request):
    if request.method == "POST":
        Company_id = request.POST.get('user_id')
        Dump = User.objects.get(id = Company_id)
        copmanyname = request.POST.get('companyname')
        skills = request.POST.get('skills')
        company_description = request.POST.get('Company_description')
        min_experience = request.POST.get('min_experience')
        max_experience = request.POST.get('max_experience')
        min_sal = request.POST.get('min_salary')
        max_sal = request.POST.get('max_salary')
        fisrthrname = request.POST.get('firsthrname')
        firsthrnumber = request.POST.get('firsthrnumber')
        secondhrname = request.POST.get('secondhrname')
        secondhrnumber = request.POST.get('secondhrnumber')
        roledescription = request.POST.get('roledescription')
        interviewdate = request.POST.get('interviewdate')
        interviewlocation = request.POST.get('interviewlocation')
        obj = JobRequirments()
        obj.CompanyName = copmanyname
        obj.Skills = skills
        obj.Company_Description = company_description
        obj.Min_Exp = min_experience 
        obj.Max_Exp = max_experience
        obj.Min_Salary = min_sal
        obj.First_HrName = fisrthrname
        obj.Second_HrName = secondhrname
        obj.First_HrNumber = firsthrnumber
        obj.Second_HrNumber = secondhrnumber
        obj.Roles_and_Responsabulity = roledescription 
        obj.Interview_Location = interviewlocation
        obj.Iterview_Date = interviewdate
        obj.manager = Dump
        obj.save()  
        return render(request,'post_jobs.html',{'obj':obj})
    else:
        forms = JobRequirmentsModel()
        return render(request,'post_jobs.html',{'forms':forms})
def Apply_Click(request,idd):
    data = FresherQualification.objects.get(id=idd)
    job= request.POST.get('job_id')
    user_id= request.POST.get('user_id')
    user_data = User.objects.get(fresherqualification__id=data.id)
    student_jobs = JobRequirments.objects.all()
    user_qualification = FresherQualification.objects.get(user_id=user_data.id)
    user_personal_data = FresherData.objects.get(user_id=user_data.id)
    profilepic = ProfileImg.objects.get(user_id=user_data.id)
    obj = JobRequirments.objects.get(id=job)
    print(obj.id)
    dump =  FresherQualification.objects.filter(jobrequirments__id=obj.id)
    # import pdb;pdb.set_trace()
    if data in dump:
         messages.info(request,'your already applied for the role of')
    else:
         obj.fresherqualification.add(data)
         messages.info(request,'your successfully applied for the role of .')
    # import pdb;pdb.set_trace()
    return render(request,'userpage.html',{
        'user_data':user_data,
        'student_jobs':student_jobs,
        'user_personal_data':user_personal_data,
        'profilepic':profilepic,
        'obj':obj,
        'user_qualification':user_qualification,
        
    })
    
def Applied_Candidates(request,idd ,uidd):
    # import pdb;pdb.set_trace()
    user_data = User.objects.get(id = uidd)
    candidates=FresherQualification.objects.filter(jobrequirments__id=idd)
    temp =[]
    for p in candidates:
        print(p.id)
        dump = User.objects.get(fresherqualification__id=p.id)
        print(dump)
        temp.append(dump)
    print(temp)
    # messages.info(request,{'candidates':candidates})
    # return render(request,'companypage.html',{'candidates':candidates})
    return render(request,'candidates_list.html',{'candidates':candidates,'temp':temp,'user_data':user_data})
def candidate(request,idd,uidd):
    Suser_data = User.objects.get(id=idd)
    user_data = User.objects.get(id = uidd)
    summary = profilesummary.objects.get(user__id=Suser_data.id)
    user_img = ProfileImg.objects.get(user__id=Suser_data.id)
    course_data = FresherQualification.objects.get(user__id=Suser_data.id)
    extra_data = FresherData.objects.get(user__id=Suser_data.id)
    dump = 50
    forms = NotificationModel()
    return render(request,'candidate.html',{
    'user_data':user_data,
    'summary':summary,
    'Suser_data':Suser_data,
    'user_img':user_img,
    'course_data':course_data,
    'extra_data':extra_data,
    'dump':dump,
    'forms':forms,
    
    })
def candidate_search(request):
    username=request.POST.get('email')
    temp = User.objects.filter(username__icontains=username)
    return render(request,'candidates_list.html',{'temp':temp})

def studentlist(request):
    students_list = User.objects.filter(is_staff = False)
    summary = profilesummary.objects.all()
    # students_pic = ProfileImg.objects.all()
    # import pdb;pdb.set_trace()
    return render(request,'studentslist.html',{'students_list':students_list,'summary':summary})
    
def Resume_Edite(request):
    import pdb;pdb.set_trace()
    if request.method == "GET":
        qualification_id = request.POST.get('qualification_id')
        obj = FresherQualification.objects.get(id = qualification_id )
        forms = FresherQualificationModel(request.POST,request.FILES,instance=obj)
        if forms.is_valid():
            forms.save()
        import pdb;pdb.set_trace()
        pass
def User_intenction(request,dummy='dummy'):
    import pdb; pdb.set_trace()
    if request.method == "POST":
        notification = request.POST.get('notification')
        condition = request.POST.get('condition')
        name = request.POST.get('Name')
        subject = request.POST.get('Subject')
        message = request.POST.get('Message')
        user_id = request.POST.get('user_idd')
        sender_user_id = request.POST.get('user_id')
        user_data = User.objects.get(id = user_id)
        Sender_user_data = User.objects.get(id = sender_user_id)
        img = ProfileImg.objects.get(user_id = Sender_user_data.id)
        # import pdb;pdb.set_trace()
        if user_data.is_staff == True:
            obj = Notifications()
            obj.Name = name
            obj.Subject = subject
            obj.Message = message
            obj.Status ="Unread"
            obj.user = Sender_user_data
            obj.sender = user_data.id 
            obj.Profile = img.Profile
            obj.save()
            variable1= Notifications.objects.get(id = notification)
            return HttpResponseRedirect(reverse('jobkarleapp:Single_notification', args=[ variable1.id, user_data.id]))
        else:
            obj = Notifications()
            obj.Name = name
            obj.Subject = subject
            obj.Message = message
            obj.Status ="Unread"
            obj.user = user_data
            obj.sender = Sender_user_data.id
            obj.Profile = img.Profile
            obj.save()
            return HttpResponseRedirect(reverse('jobkarleapp:intenction', args=[user_data.id , Sender_user_data.id]))
    
def intenction(request,sUser_id ,User_id):
    # import pdb;pdb.set_trace()
    Suser_data = User.objects.get(id = sUser_id)
    user_data = User.objects.get(id = User_id)
    user_img = ProfileImg.objects.get(user__id=Suser_data.id)
    course_data = FresherQualification.objects.get(user__id=Suser_data.id)
    extra_data = FresherData.objects.get(user__id=Suser_data.id)
    dump = Notifications.objects.all()
    forms = NotificationModel()
    return render(request,'candidate.html',{'Suser_data':Suser_data,
    'user_data':user_data,
    'user_img':user_img,
    'course_data':course_data,
    'extra_data':extra_data,
    'dump':dump,
    'forms':forms,})
def notification_read(request,uidd):
    #import pdb;pdb.set_trace()
    variable2 = User.objects.get(id = uidd)
    # import pdb;pdb.set_trace()
    notifications=Notifications.objects.filter(user_id = variable2.id)
    notification_count=Notifications.objects.filter(Status = 'Unread',user_id = variable2.id).count()
    notification_unread=Notifications.objects.filter(user_id = variable2.id,Status = 'Unread')
    notification_read=Notifications.objects.filter(Status = 'Read')
    forms = NotificationModel()
    # import pdb;pdb.set_trace() 
    return render(request,'notification_view.html',{
    'variable2':variable2,
    'forms':forms,
    'notifications':notifications,
    'notification_count':notification_count,
    'notification_unread':notification_unread,
    'notification_read':notification_read,
    })
def Total_notifications(request,uidd):
    variable2 = User.objects.get(id = uidd)
    notifications=Notifications.objects.filter(user_id = variable2.id)
    notification_count=Notifications.objects.filter(Status = 'Unread',user_id = variable2.id).count()
    notification_unread=Notifications.objects.filter(user_id = variable2.id,Status = 'Unread')
    notification_read=Notifications.objects.filter(Status = 'Read')
    return render(request,'notification_view.html',{
    'variable2':variable2,
    'notifications':notifications,
    'notification_count':notification_count,
    'notification_unread':notification_unread,
    'notification_read':notification_read,})

def Total_sent_notifications(request,sidd,dummy='sent_notification'):
    variable2 = User.objects.get(id = sidd)
    notifications=Notifications.objects.filter(sender = variable2.id)
    return render(request,'notification_view.html',{
    'variable2':variable2,
    'notifications':notifications,
    'dummysent':dummy})
def Single_notification(request,idd,uidd,dummy='dummy'):
     #import pdb;pdb.set_trace()
    variable1= Notifications.objects.get(id = idd)
    variable1.Status = 'Read'
    variable1.save()
    variable2 = User.objects.get(id = uidd)
    company_user = User.objects.get(id = variable1.sender)
    Img = ProfileImg.objects.get(user_id = company_user.id)
    # import pdb;pdb.set_trace()
    notifications=Notifications.objects.filter(user_id = variable2.id)
    notification_count=Notifications.objects.filter(Status = 'Unread',user_id = variable2.id).count()
    notification_unread=Notifications.objects.filter(user_id = variable2.id,Status = 'Unread')
    notification_read=Notifications.objects.filter(Status = 'Read')
    forms = NotificationModel()
    # import pdb;pdb.set_trace() 
    return render(request,'notification_view.html',{'obj':variable1,
    'variable2':variable2,
    'forms':forms,
    'company_user':company_user,
    'Img':Img,
    'notifications':notifications,
    'notification_count':notification_count,
    'notification_unread':notification_unread,
    'notification_read':notification_read,
    'dummy':dummy,
    })
def Return_home(request,uidd):
    user_data = User.objects.get(id = uidd)
    return HttpResponseRedirect(reverse('jobkarleapp:ProfileData', args={user_data.id}))
 
# def DownloadCv_View(request,Cvpath):
#     #course_data = FresherQualification.objects.get(id = CvID)
#     #cvpath = course_data.Resume.url
#     ext = os.path.basename(Cvpath).split('.')[-1].lower()
#     # cannot be used to download py, db and sqlite3 files.
#     if ext not in ['py', 'db',  'sqlite3']:
#         response = FileResponse(open(Cvpath, 'rb'))
#         response['content_type'] = "application/octet-stream"
#         response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(Cvpath)
#         return response
#     else:
#         raise Http404
    # file_path = os.path.join(settings.MEDIA_ROOT,cvpath)
    # pdb.set_trace()
    # file_path += '/'
    # if os.path.exists(file_path):
    #     with open(file_path, 'rb') as fh:
    #         response = HttpResponse(fh.read(), content_type="application/studentresumes")
    #         response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
    #         return response
    # raise Http404