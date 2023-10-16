from django import forms
import re #Module này được sử dụng để làm việc với biểu thức chính quy, là một công cụ mạnh mẽ để xử lý và tìm kiếm các chuỗi dựa trên mẫu chuỗi.
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Tài Khoản', max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput())

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError('Mật khẩu không hợp lệ')
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Tên tài khoản có kí tự đặc biệt')
        try:
            #username ở trên nếu bằng username trong database
            User.objects.get(username  =   username)  #nếu mà xảy ra lỗi (nghĩa là user không trùng)  
                            #username(db)  username(self.clean...)
        except ObjectDoesNotExist:
            return username     #thì sẽ trả về username
        raise forms.ValidationError('Tài khoản đã tồn tại')
    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password1'])
