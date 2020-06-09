from django.contrib import admin
from django.urls import path,re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.FresherRigister,name="FresherRigister"),
    path('FresherRigister',views.FresherRigister,name="FresherRigister"),
    path('CompanyRegister',views.CompanyRegister,name="CompanyRegister"),
    path('Login',views.Login,name='Login'),
    path('<int:User_id>/fresherdata/',views.fresherdata,name='fresherdata'),
    path('FreshExtradata',views.FreshExtradata,name='FreshExtradata'),
    path('<int:User_id>/ProfileData/',views.ProfileData,name='ProfileData'),
    path('<int:User_id>/Companyprofile_data/',views.Companyprofile_data,name='Companyprofile_data'),
    path('<int:User_id>/Support_Course/',views.Support_Course,name='Support_Course'),
    path('load_Course',views.load_Course,name='load_Course'),
    path('<int:idd>/mulltisearch/',views.mulltisearch,name='mulltisearch'),
    path('country_list',views.country_list,name='country_list'),
    path('<int:User_id>/fresherqualification/',views.fresherqualification,name="fresherqualification"),
    path('fresherqualificationextra',views.fresherqualificationextra,name="fresherqualificationextra"),
    path('<int:User_id>/Profiledef/',views.Profiledef,name='Profiledef'),
    path('Profileextradef',views.Profileextradef,name='Profileextradef'),
    path('job_postview',views.job_postview,name='job_postview'),
    # path('job_applied',views.job_applied,name='job_applied'),
    path('Logout',views.Logout,name='Logout'),
    path('<int:idd>/Apply_Click/',views.Apply_Click,name='Apply_Click'),
    path('<int:idd>/<int:uidd>/Applied_Candidates/',views.Applied_Candidates,name='Applied_Candidates'),
    path('<int:idd>/<int:uidd>/candidate/',views.candidate,name='candidate'),
    path('candidate_search',views.candidate_search,name='candidate_search'),
    path('studentlist', views.studentlist,name='studentlist'),
    path('Resume_Edite', views.Resume_Edite,name='Resume_Edite'),
    path('<int:sUser_id><int:User_id>/intenction/', views.intenction,name='intenction'),
    path('User_intenction', views.User_intenction,name='User_intenction'),
    path('<int:idd>/<int:uidd>/notification_read/',views.notification_read,name='notification_read'),
    
]