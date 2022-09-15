from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.start, name='start'),
    path('login', views.login, name='login'),
    path('third_page', views.third_page, name='third_page'),
    path('QP_first', views.QP_first, name='QP_first'),
    path('QP_Generate', views.QP_Generate, name='QP_Generate'),
    path('QP_Submit', views.QP_Submit, name='QP_Submit'),
    path('peer', views.peer, name='peer'),
    path('project', views.project, name='project'),
    path('notify', views.notify, name='notify'),
    path('languagepro', views.languagepro, name='languagepro'),
    path('pbl', views.pbl, name='pbl'),
]
