from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.login,name="login"),
    path('registration_data',views.registrationdata,name='registrationdata'),
    path('registration_create',views.registrationcreate,name='registration_create'),
    path('Workers_data',views.Workers_data,name='workers_data'),
    path('user_interface',views.user_interface,name='user_interface'),
    path('user_home',views.user_home,name='user_home'),
    path('wr_prf_usr',views.wr_prf_usr,name='wr_prf_usr'),
    path('usr_ctct_wrkr',views.usr_ctct_wrkr,name='usr_ctct_wrkr'),
    path('admin_interface',views.admin_interface,name='admin_interface'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('wrkr_prof',views.wrkr_prof,name='wrkr_prof'),
    path('user_edit_prof',views.user_edit_prof,name='user_edit_prof'),
    path('wrkr_interface',views.wrkr_interface,name='wrkr_interface'),
    path('wrkr_home',views.wrkr_home,name='wrkr_home'),
    path('admin_worker_view',views.admin_worker_view,name='admin_worker_view'),
    path('admin_worker_prof',views.admin_worker_prof,name='admin_worker_prof'),
    path('admin_user_view',views.admin_user_view,name='admin_user_view'),
    path('admin_change_pass',views.admin_change_pass,name='admin_change_pass'),
    path('wrkr_chngeid',views.wrkr_chngeid,name='wrkr_chngeid'),
    path('user_about',views.user_about,name='user_about'),
    path('user_contact',views.user_contact,name='user_contact'),
    path('logout',views.logout_view, name='logout'),
    
]
