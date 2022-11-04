from django.views.generic import ListView
from company.models import Company


class AllLV(ListView):
    model = Company
    template_name = "all/all.html"
