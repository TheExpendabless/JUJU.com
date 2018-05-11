
from django import forms
from illustration.models import UserProfile,UserCollect

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)


class RegisterForm(forms.Form):
    username = forms.CharField(required=True,min_length=4)
    password = forms.CharField(required=True,min_length=6)
    repeat = forms.CharField(required=True,min_length=6)

# 用于个人中心修改个人信息
class UserInfoForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['username','email','mobile']

class UserCollectForm(forms.ModelForm):
    class Meta:
        model = UserCollect
        fields = ['user','community_id']

# 重置密码
class ResetPwdForm(forms.Form):
    oldpassword = forms.CharField(required=True)
    newpassword = forms.CharField(required=True, min_length=6)
    repeatpassword = forms.CharField(required=True, min_length=6)