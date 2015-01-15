# -*- coding: utf-8 -*-
from django import forms

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from django.core.exceptions import ObjectDoesNotExist

from contrib.captcha import CaptchaField
from pine.settings import MIN_PASSWORD_LEN, CHECK_STRENGTH

from captcha.fields import CaptchaField

_digit = set(map(chr, range(48, 58)))
_upper = set(map(chr, range(65, 91)))
_lower = set(map(chr, range(97,123)))

class RegistrationForm(forms.Form):
    """Form for creating new users. """

    username = forms.EmailField(
        required   = True,
        label      = "E-mail",
        help_text  = u"此项将是您的登录名.",
    )
    username_again = forms.EmailField(
        required   = True,
        label      = "E-mail (再次输入)",
        help_text  = u"请确保这是一个有效的邮件地址.",
    )

    password = forms.CharField(
        required   = True,
        label      = u"密码",
        widget     = forms.PasswordInput(),
        help_text  = u"请使用大写字母,小写字母与数字的组合.",
    )
    password_again = forms.CharField(
        required   = True,
        label      = u"再次输入密码",
        widget     = forms.PasswordInput(),
    )

    first_name = forms.CharField(
        required   = True,
        label      = u"名",
        help_text  = "请输入您的名字.",
    )

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        
        all_symbols = set(first_name)
        first_symbol = set(first_name[0])
        
        if ( first_symbol & _lower):
            raise forms.ValidationError('First letter must be Uppercase.')

        elif not ( all_symbols & _lower ):
            raise forms.ValidationError('Only CAPITALS are not allowed.')

        elif ( all_symbols & _digit ):
            raise forms.ValidationError('Digits are not allowed in first name.')

        return first_name

    last_name = forms.CharField(
        required   = True,
        label      = u"姓",
        help_text  = "请输入您的姓氏.",
    )

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        
        all_symbols = set(last_name)
        first_symbol = set(last_name[0])
        
        if ( first_symbol & _lower):
            raise forms.ValidationError('First letter must be Uppercase.')
                 
        elif not ( all_symbols & _lower ):
            raise forms.ValidationError('Only CAPITALS are not allowed.')

        elif ( all_symbols & _digit ):
            raise forms.ValidationError('Digits are not allowed in last name.')

        return last_name

#     captcha = CaptchaField(
#         required   = True,
#         label      = "安全码",
#     )
    
    captcha2 = CaptchaField(
        required = True,
        label = u"安区码",
    )

    def clean_username(self):
        """Make sure that `login` is unique in the system. """
        username = self.cleaned_data['username']

        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username

        raise forms.ValidationError('E-mail already in use.')

    def clean_username_again(self):
        """Make sure that user verified `login` that he entered. """
        if 'username' in self.cleaned_data:
            username       = self.cleaned_data['username']
            username_again = self.cleaned_data['username_again']

            if username == username_again:
                return username
        else:
            return None

        raise forms.ValidationError('E-mails do not match.')

    def clean_password(self):
        """Make sure `password` isn't too easy to break. """
        password = self.cleaned_data['password']

        if CHECK_STRENGTH:
            if len(password) < MIN_PASSWORD_LEN:
                raise forms.ValidationError('Password must have at least %i characters.' % MIN_PASSWORD_LEN)

            symbols = set(password)

            if not ((_digit & symbols and _upper & symbols) or \
                    (_digit & symbols and _lower & symbols) or \
                    (_lower & symbols and _upper & symbols)):
                raise forms.ValidationError('Password is too weak, please choose a better one.')

        return password

    def clean_password_again(self):
        """Make sure that the user verified the `password` he entered. """
        if 'password' in self.cleaned_data:
            password       = self.cleaned_data['password']
            password_again = self.cleaned_data['password_again']

            if password == password_again:
                return password
        else:
            return None

        raise forms.ValidationError('Passwords do not match.')

class RegisterForm(forms.Form):
    
    error_css_class = 'error'
    required_css_class = 'required'
    
    Course_A = 'C1'
    Course_B = 'C2'
    Course_C = 'C3'
    KID_COURSE_CHOICES = (
        ( u'编程', (
                        (Course_A, u'Karel机器人'),
                        (Course_C, u'Python编程入门'),
                    )
         ),
        ( u'3D作图',(
                        (Course_B, u'Plasm 3D作图'),
                    )
        ),
    )
    student_name = forms.CharField(label=u'学生姓名',max_length=100)
    age = forms.IntegerField(label=u'年龄',initial='10')
    parent_name = forms.CharField(label=u'家长姓名')
    phone = forms.CharField(label=u'联系电话')
    courses = forms.MultipleChoiceField(label=u'希望学习的课程',choices=KID_COURSE_CHOICES,initial=['C1','C2'])
    mugshot = forms.ImageField(label=u'头像')
    
