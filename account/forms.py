from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .models import User

class UserCreationForm(forms.ModelForm):
    #유저 생성 폼
    password1 = forms.CharField(label='비밀번호', widget=forms.PasswordInput) # 비밀번호 입력시 *로 표현하게 함
    password2 = forms.CharField(label='비밀번호 확인', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('user_id','user_name', 'department','email')

    def clean_password2(self):
        #일치확인
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("비밀번호가 일치하지 않습니다.")
        return password2
    
    def save(self, commit=True):
        #저장
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    #유저정보변경
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = (
            'user_id','user_name', 'department','email', 'is_admin', 'is_active'
        )
    
    def clean_password(self):
        return self.initial["password"]

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = (
        'user_id','user_name', 'department','email', 'is_admin', 'is_active'
    )
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('user_id', 'password')}),
        ('Personal info', {'fields': (
            'user_name', 'department', 'email',
        )}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields' : ('user_id','user_name', 'department', 'email', 'password1','password2',),
        }),
    )

    search_fields = ('user_id', 'department', 'user_name',)
    ordering = ('department', 'user_name',)
    filter_horizontal = ()