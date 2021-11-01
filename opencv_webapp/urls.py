from django.urls import path
from . import views
from django.conf import settings
#메인 settingf 끌고온거
from django.conf.urls.static import static

app_name = 'opencv_webapp'

urlpatterns = [
    path('',views.first_view, name='first_view'), #127.0.0.1:8000/~~~
    path('simple_upload/', views.simple_upload, name='simple_upload'), #127.0.0.1:8000/simple_upload/
    # 모델 안써서 심플이라고 했음
    path('detect_face/', views.detect_face, name='detect_face'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 미디어 폴더의 경로,
# 그 폴더 경로
# 유저한테 바로바로 갈수있게 열어놓는 경
