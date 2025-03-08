from django import forms
from .models import PrintOrder, UploadedDocument
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedDocument
        fields = ['file']

class PrintOrderForm(forms.ModelForm):
    class Meta:
        model = PrintOrder
        fields = ['amount', 'page_size', 'paper_type', 'print_color', 'print_sides', 'binding', 'copies', 'transaction_id', 'unique_url', 'total_pages']


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']


# class DocumentForm(forms.ModelForm):
#     class Meta:
#         model = Document
#         fields = ['file', 'num_copies', 'color_type', 'double_sided']  # ❌ REMOVE 'paper_size'
