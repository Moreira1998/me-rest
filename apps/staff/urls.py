from django.urls import path, include
from apps.staff.viewsets import StaffViewSet, RoleViewSet

from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from apps.staff.views import StaffList, StaffNew


from apps.staff.views import UserList, UserCreate, UserUpdate, UserDelete
# -------------------------------------------------------->
# Routers ApI
routers = DefaultRouter()
routers.register(r'', StaffViewSet)
routers.register(r'role', RoleViewSet)

app_name = 'staff'

urlpatterns = [

    # -------------------------------------------------------->
    # Path Routers API
    path('api/', include(routers.urls)),

    # -------------------------------------------------------->
    # Path Token

    path('login/', obtain_jwt_token),

    # -------------------------------------------------------->
    # Path Staff

    path('', StaffList.as_view(), name='staff_list'),
    path('new', StaffNew.as_view(), name='staff_new'),

    # -------------------------------------------------------->
    # Path User

    path('user', UserList.as_view(), name='user_list'),
    path('New', UserCreate.as_view(), name='user_new'),
    path('Edit/<int:pk>', UserUpdate.as_view(), name='user_update'),
    path('delete/<int:pk>', UserDelete.as_view(), name='user_delete'),

]
