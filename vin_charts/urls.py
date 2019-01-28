from django.urls import path

from vin_charts import views

urlpatterns = [
    path("model-years/", views.ModelYearList.as_view(), name="model_year_list"),
]
