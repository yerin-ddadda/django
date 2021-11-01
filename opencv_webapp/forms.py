from django import forms
from .models import ImageUploadModel

class SimpleUploadForm(forms.Form):
    title = forms.CharField(max_length=50)
    image = forms.ImageField()
    # file = forms.FileField()
    # 빈양식되고, html에서 보여주면 html에서 인풋태그 두개 만들어줌


    #class Meta:~~ 이렇게 모델 forms.ModelForm 이거를 폼으로 바꿈

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUploadModel # 실제 테이블
        fields = ('description', 'document', )
