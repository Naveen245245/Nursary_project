from django.urls import path
from n_app import views


urlpatterns = [
    path("", views.home),

    path("nursaries", views.nursaryList, name="nursary-list"),
    path("createNursary", views.createNursary, name="create-nursary"),
    path("viewNursary/<int:pk>/", views.viewNursary, name="view-nursary"),
    # path("confirmDelNursary", views.confirmDelNursary, name="confirm-del-nursary"),
    path("updateNursary/<int:pk>/", views.updateNursary, name="update-nursary"),
    path("delNursary/<int:pk>/", views.delNursary, name="delete-nursary"),

    path("viewNursary/<int:pk>/createOrder/",views.createOrder, name="create-order"),
    
    path("updateOrder/<int:pk>/", views.updateOrder, name="update-order"),
    path("delOrder/<int:pk>", views.delOrder, name="delete-order"),

    path('viewbed/<int:pk>/',views.bedView,name="view-bed"),
]


