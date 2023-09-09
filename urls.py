from django.urls import path


from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("form/", views.home_view, name="form"),
    # path("<int:pk>/delete/", views.deleteView, name="delete"),

    path('<int:pk>/delete/', views.delete_items, name="delete_items"),
    path('update/<int:pk>', views.update_items, name='update_items'),
  
    
   
]