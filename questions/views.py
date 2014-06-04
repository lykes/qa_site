from django.core.urlresolvers import reverse
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from .models import Answer
from .models import Question


class AnswerListView(ListView):
    model = Answer


class QuestionCreateView(CreateView):
    model = Question

    def get_success_url(self):
        return reverse('questions:detail', kwargs={'pk': self.object.pk})


class QuestionDetailView(DetailView):
    model = Question

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        context['answers'] = Answer.objects.filter(question=self.object)
        return context


class QuestionListView(ListView):
    model = Question


class QuestionUpdateView(UpdateView):
    model = Question

    def get_success_url(self):
        return reverse('questions:detail', kwargs={'pk': self.object.pk})
