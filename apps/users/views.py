from django.views.generic import TemplateView


class LoginTemplateView(TemplateView):
    template_name = 'shop/users/login.html'

    def get_context_data(self, **kwargs):
        context = super(LoginTemplateView, self).get_context_data(**kwargs)
        return context
