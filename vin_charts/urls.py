from django.urls import path

from vin_charts import views

urlpatterns = [
    path("model-years/", views.ModelYearList.as_view(), name="model_year_list"),
    path("vehicles/<slug:slug>,<int:pk>/", views.VehicleDetail.as_view(), name="vehicle_detail"),
    path("vehicles/<int:model_year>/", views.VehicleList.as_view(), name="vehicle_list"),
]
