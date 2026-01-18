"""
URL configuration for medink project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from med.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index, name='index'),  # Default route
    # path('login/', login, name='login'),
    path('index/', index, name='index'),
    path('logout/',logout_view, name='logout'),
    path('profile/', profile, name='profile'),
    path('signup/', signup, name='signup'),
    path('popupform/', popupform, name='popupform'),
    path('report/<int:id>/', report, name='report'),
    path('user_detail/<int:id>/', user_detail, name='user_detail'),
    path('imagingA/', imagingA, name='imagingA'),
    path('RADS/', RADS, name='RADS'),
    path('signup_view/', signup_view, name='signup'),
    path('', login_view, name='login'),
    path('invoice/', invoice, name='invoice'),
    path('payment/', payment, name='payment'),
    path('api/patient/<int:id>/download/<str:format>/', download_report, name='download_report'),
    path('api/patient/add/',add_patient, name='add_patient'),
    path('api/patient/<int:id>/update/',update_report, name='update_report'),
    path('api/patient/<int:id>/', get_patient, name='get_patient'),
    path('api/patient/<int:id>/update/', update_report, name='update_report'),
    path('api/patient/<int:patient_id>/reports/', get_reports, name='get_reports'),
    path('api/patient/<int:patient_id>/reports/create/', create_report, name='create_report'),
    path('api/report/<int:report_id>/', get_report, name='get_report'),
    path('api/report/<int:report_id>/update/', update_report, name='update_report'),
    path('api/report/<int:report_id>/delete/', delete_report, name='delete_report'),
    path('assign_patient/<int:patient_id>/', assign_patient, name='assign_patient'),
    path("super-admin/", super_admin, name="super_admin"),
    path("user/toggle/<int:id>/", toggle_user_status, name="toggle_user_status"),
    path("user/role/<int:id>/<str:role>/", change_user_role, name="change_user_role"),
    path('assign_patient_superadmin/', assign_patient_superadmin, name='assign_patient_superadmin'),
    path('patients/',patients, name='patients'),
    path('add-user/', add_user, name='add_user'),
    # path('admin-details/<int:admin_id>/', admin_details, name='admin_details'),
    # path("admin_details/", admin_details, name="admin_details"),
    path('user-list/', user_list, name='user_list'),
    path('user-details/<int:user_id>/', user_details_api, name='user_details_api'),
    path('update-user/<int:user_id>/', update_user, name='update_user'),
    path('delete-user/<int:user_id>/', delete_user, name='delete_user'),
    path('create-user-page/',create_user_page, name='create_user_page'),
    path('api/admin-details/<int:admin_id>/', admin_details_api, name='admin_details_api'),
    path('admin-details/<int:admin_id>/', admin_details_page, name='admin_details_page'),
    path("api/delete-multiple/", delete_multiple, name="delete_multiple"),
    path("api/patient/<int:id>/edit/", edit_patient),
    path('impersonate/<int:user_id>/', impersonate_with_password, name='impersonate'),
    path("api/patient/<int:pk>/save-cropped-image/", save_cropped_image),
    path("api/patient/<int:pk>/save-images/", save_images),
    path('api/admin/hospitals/',admin_hospitals_api, name='admin_hospitals_api'),
    path('api/profile/', get_profile, name='get_profile'),
    path('api/profile/update/', update_profile, name='update_profile'),
    path('api/admin/create-user/', create_user, name='create_user'),

]
    
    # API endpoints
#     path('api/patient/add/', add_patient, name='add_patient'),
#     path('api/patient/<int:id>/', get_patient, name='get_patient'),
#     path('api/patient/<int:id>/update/', update_report, name='update_report'),
#     path('api/patient/<int:id>/delete/', delete_patient, name='delete_patient'),
# ]


