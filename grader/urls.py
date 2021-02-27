from django.urls import path,include
from  . import views
from django.conf import settings

urlpatterns = [
    path('', views.index, name="home"),
    path('graph/', views.graph, name="graph"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('sample/', views.sample_forms, name='sample'),
    path('student/', views.student_forms, name='student'),
    path('check/', views.check, name='check'),
    path('about/', views.about, name='aboutUs'),
    path('resultg/', views.results_graph, name='resultg'),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)