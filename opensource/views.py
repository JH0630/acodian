
from django.views.generic import ListView
from opensource.models import Opensource


class OsLV(ListView):
    model = Opensource
    template_name = "opensource/os_trend.html"


class OslangLV(ListView):
    model = Opensource
    template_name = "opensource/os_lang.html"


class OsliceLV(ListView):
    model = Opensource
    template_name = "opensource/os_lice.html"
