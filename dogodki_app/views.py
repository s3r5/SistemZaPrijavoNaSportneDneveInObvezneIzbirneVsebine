from django.views.generic.base import TemplateView

# Create your views here.

class DashboardView(TemplateView):
	template_name = "dogodki/dashboard.html"