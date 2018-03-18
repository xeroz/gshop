from django.views.generic import TemplateView


class ProfileTemplateView(TemplateView):
    template_name = 'shop/users/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileTemplateView, self).get_context_data(**kwargs)
        return context
