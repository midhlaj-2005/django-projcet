from django.urls import path
from.import views 

urlpatterns = [
    path("",views.home ,name="home"),
#     path("str/",views.home1,name="abc"),
#     path("now/",views.home2,name="now")
    path("app1/",views.view_book,name="app") ,
    path('book/',views.add_book,name='add_book')
]