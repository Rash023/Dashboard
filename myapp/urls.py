from django.urls import path
from . import views

urlpatterns = [
   path('Home',views.HomePage,name="Home"),  #Route for home page
   path('Post',views.Schedule_Post,name="Post"),  #Route to Shcedule New Post
   path('Analytics',views.Analytics,name="Analytics"), #Route to view Analytics
   path('login/',views.login_user,name="login"),     #Route to login
   path('',views.register_user,name="register"),   #Route to Register user
   path('Comments',views.Comments,name="Comments"), #Route to View Comments on Particular Posts
   path('Reach',views.Reach,name="Reach")   #Route to View Aggregated Reach

]


