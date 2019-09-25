from django.urls import path

from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.LandingView, name='landing'),
    path('login/', views.LoginView, name='login'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('suggestion/list/', views.suggestionList, name='suggestion'),
    # path('suggestion/<int:pk>/', views.suggestionDetail, name='suggestionDetail'),
    # path('suggestion/', views.suggestionForm, name='suggestionForm')
]
