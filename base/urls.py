from django.urls import path
from .views import *

urlpatterns = [
    path('', CandidateDirectoryListView.as_view(), name='candidate_list'),
    path('candidate/<int:pk>/', CandidateDirectoryDetailView.as_view(), name='candidate_detail'),
    path('add_candidate/', CandidateDirectoryCreateView.as_view(), name='add_candidate'),
    path('candidates/<int:pk>/edit/', CandidateEditView.as_view(), name='candidate_edit'),
    path('delete_candidate/<int:pk>/', CandidateDeleteView.as_view(), name='delete_candidate'),
    path('signup/', SignUpView.as_view(), name = "signup"),
    path('login/', LoginView.as_view(), name = "login"),
    path('logout/', LogoutView.as_view(), name = "logout"),
]