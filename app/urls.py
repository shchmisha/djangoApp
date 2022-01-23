from django.urls import path, include
# from .views import ArticleList

from rest_framework.routers import DefaultRouter
from app.views import ExerciseViewSet, WorkoutViewSet, UserViewSet

router = DefaultRouter()
router.register("exercise", ExerciseViewSet)
router.register("users", UserViewSet)
router.register("workouts", WorkoutViewSet)

urlpatterns = [
    # path('articles/', article_list),
    # path('articles/<slug:slug>/', article_details),
    # path('articles/', ArticleList.as_view())
    path('', include(router.urls))
]
