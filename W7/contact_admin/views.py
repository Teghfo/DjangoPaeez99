from django.shortcuts import render
from django.views.generic.edit import FormView, UpdateView, DeleteView, CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy

from .forms import ContactForm
from .models import Comment


class CommentListView(ListView):
    pass


class ContactEmailForm(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = 'contact/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)


class CommentCreate(CreateView):
    model = Comment
    fields = ['comment']
    template_name_suffix = '_create_form'


class CommentUpdate(UpdateView):
    model = Comment
    fields = ['comment']
    template_name_suffix = '_update_form'


class CommentDelete(DeleteView):
    model = Comment
    success_url = reverse_lazy('comments-list')
