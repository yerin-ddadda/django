from django.shortcuts import render
from .forms import SimpleUploadForm, ImageUploadForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .cv_functions import cv_detect_face


# Create your views here.
def first_view(request):
    return render(request, 'opencv_webapp/first_view.html', {}) # 컨텍스트 안가져감


def simple_upload(request):
    # 유저로부터 받아들이는 html 폼태그에서 action안쓰고 post요청 하나로 해보는거 함
    if request.method == 'POST':
        print(request.POST) # 파일들만 여기로 묶여서 안넘어감
        print(request.FILES)
        # request.FILE['image'] # 이걸로 유저가 업로드한 파일 가져오는거임.

        form = SimpleUploadForm(request.POST, request.FILES) # 포스트 요청이니까 채워진 양식임
        # 파일을 끼기 시작하니까 request.FILE 적어줌
        if form.is_valid(): # 이미지 파일이 밎다면
            # 파일을 잠시 변수에 저장하자
            myfile = request.FILES['image'] # 유저가 업로드한 파일을 변수명에 저장
            # 저장할때 filesystem사용
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            # 파일, 경로를 저장해서 save함수 실행되면서 저장 마쳐지며 리턴해서 받아내고,
            # 유저한테 보여주거나, 이미지 태그에 이미지 띄워주거나 html에 보내주거나
            # 이제 바깥으로 내보내기
            context = {'form':form, 'uploaded_file_url':uploaded_file_url} # 똑같은 키값, 밸류 적기
            return render(request, 'opencv_webapp/simple_upload.html', context)

            #
            # fs.save(myfile.name, myfile) # 저장하고싶은 파일 경로를 포함한 이름?, 파일 객체(파일 자체 )순서대로
            #
            # # 저장이 된거 돌려보내고 싶으면
            # filename = fs.save(myfile.name, myfile) # 경로명 같은거 꺼내줌
            # uploaded_file_url = fs.url(filename)

    else: # get요청
        form = SimpleUploadForm() # 빈양식되고
        return render(request, 'opencv_webapp/simple_upload.html', {'form':form})


def detect_face(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():

            post = form.save(commit=False)
            post.save()

            imageURL = settings.MEDIA_URL + form.instance.document.name
            cv_detect_face(settings.MEDIA_ROOT_URL + imageURL)

            context = {'form':form, 'post':post}
            return render(request, "opencv_webapp/detect_face.html", context)
    else:
        form = ImageUploadForm()

        context = {'form':form}
        return render(request, "opencv_webapp/detect_face.html", context)
