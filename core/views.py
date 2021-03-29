from django.views.generic import TemplateView
from .models import Servico, Funcionario, Recurso
import random


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        recursos = Recurso.objects.all()
        context['recursos_l'] = recursos[0:3]
        context['recursos_r'] = recursos[3:6]
        return context
