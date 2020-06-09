from django import forms
from django.forms import ModelForm,Textarea
from .models import Fresher,FresherData,FresherQualification,Qualification_Course,JobRequirments,ProfileImg,Notifications
from django.contrib.auth.models import User

class FresherModel(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super(FresherModel,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
            self.fields[field].widget.attrs["placeholder"] = field
    class Meta:
        model = User
        fields = '__all__'
class FresherDataModel(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super(FresherDataModel,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
            self.fields[field].widget.attrs["placeholder"] = field
            if field == 'Nationality':
                self.fields[field].widget.attrs["id"] = "id_country"
    class Meta:
        model = FresherData
        exclude = '__all__'
class FresherQualificationModel(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super(FresherQualificationModel,self).__init__(*args,**kwargs)
        # self.fields['Course'].queryset = Qualification_Course.objects.none()
        # if 'country' in self.data:
        #      try:
        #          Highest_Qualification_id = int(self.data.get('country'))
        #          self.fields['Course'].queryset = Qualification_Course.objects.filter(country=Highest_Qualification_id).order_by('name')
        #      except (ValueError, TypeError):
        #          pass  # invalid input from the client; ignore and fallback to empty City queryset
        # elif self.instance.pk:
        #     self.fields['Course'].queryset = self.instance.Highest_Qualification.Course_set.order_by('name')
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = "form-control"
            self.fields[field].widget.attrs['placeholder'] = field
    class Meta:
        model = FresherQualification
        exclude = ['user','SubQualification']
class ProfileImgModel(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super(ProfileImgModel,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']="upload-input"
    class Meta:
        model = ProfileImg
        exclude = ['user']
class JobRequirmentsModel(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super(JobRequirmentsModel,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
            self.fields[field].widget.attrs["placeholder"] = field
            if field == 'Company_Description':
                self.fields[field].widget.attrs['class'] = "form-control z-depth-1"
                self.fields[field].widget.attrs["id"] = "exampleFormControlTextarea6"
            if field == 'Roles_and_Responsabulity':
                self.fields[field].widget.attrs['class'] = "form-control z-depth-1"
                self.fields[field].widget.attrs["id"] = "exampleFormControlTextarea6"
    class Meta:
        model = JobRequirments
        fields = '__all__'
        widgets = {
                'Company_Description': Textarea(attrs={'cols':80 ,'rows':5}),
                'Roles_and_Responsabulity': Textarea(attrs={'cols':80 ,'rows':5})}
class NotificationModel(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super(NotificationModel,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
            self.fields[field].widget.attrs["placeholder"] = field
    class Meta:
        model = Notifications
        exclude = ['Status','user']