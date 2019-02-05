from django.urls import path

from vin_charts import views

urlpatterns = [
    path("model-years/", views.ModelYearList.as_view(), name="model_year_list"),
    path("chassis/<slug:slug>,<int:pk>/", views.ChassisDetail.as_view(), name="chassis_detail"),
    path("engines/<slug:slug>,<int:pk>/", views.EngineDetail.as_view(), name="engine_detail"),
    path("vehicles/<slug:slug>,<int:pk>/", views.VehicleDetail.as_view(), name="vehicle_detail"),
    path("transmissions/<slug:slug>,<int:pk>/", views.TransmissionDetail.as_view(), name="transmission_detail"),
    path("vehicles/<int:model_year>/", views.VehicleList.as_view(), name="vehicle_list"),
]
