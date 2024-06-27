from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('api/questions/', views.QuestionList.as_view(), name='question-list'),
    path('api/questions/<int:pk>/', views.QuestionDetail.as_view(), name='question-detail'),
    path('api/choices/', views.ChoiceList.as_view(), name='choice-list'),
    path('api/choices/<int:pk>/', views.ChoiceDetail.as_view(), name='choice-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

