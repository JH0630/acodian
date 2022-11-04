from django.views.generic import ListView
from company.models import Company


class ComlangLV(ListView):
    model = Company
    template_name = "company/com_lang.html"


class ComdutyLV(ListView):
    model = Company
    template_name = "company/com_duty.html"

