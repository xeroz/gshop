from django.views.generic import TemplateView
from django.shortcuts import redirect, HttpResponseRedirect, render
from .forms import Registrationform


class ProfileTemplateView(TemplateView):
    template_name = 'shop/users/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileTemplateView, self).get_context_data(**kwargs)
        return context


def create(request):
    if request.method == 'POST':
        form = Registrationform(request.POST)
        print (form, 'uuuuuuuuuuu')
        if form.is_valid():
            print('ddddddddddd')
            form.save()
            return redirect('/login')
        else:
            print('eeeeeeeeeeeeee')
            data = {'form': form}
            return render(request, 'shop/users/profile.html', data)
