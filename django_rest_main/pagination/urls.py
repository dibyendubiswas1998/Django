from django.urls import path
from .admin import *
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("blogs/", BlogsViewSets.as_view(), name="blog"),
    path("comments/", CommentsViewSets.as_view(), name="comments"),
    
    # PK based Operation:
    path("blogs/<int:pk>/", BlogDetail.as_view(), name="blog1"),
    path("comments/<int:pk>/", CommentDetail.as_view(), name="comments2"),
    
    
    # employee:
    path("employees/", EmployeeDetails.as_view(), name="employees"),
]
