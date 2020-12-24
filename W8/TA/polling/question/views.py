from django.shortcuts import render
from .models import Question, Answer, Choice
from django.views.generic import ListView, DetailView, View, CreateView
from .forms import AnswerForm
from django.shortcuts import redirect
from django.contrib import messages
from .forms import QuestionForm, ChoiceForm


# Create your views here.


class Home(ListView):
    template_name = 'home.html'
    context_object_name = 'questions'
    queryset = Question.objects.all().order_by('date')[:5]


class QuestionList(ListView):
    template_name = 'question_list.html'
    context_object_name = 'questions'
    model = Question


class QuestionDetail(DetailView):
    template_name = 'question_detail.html'
    context_object_name = 'question'
    model = Question


class QuestionResult(DetailView):
    template_name = 'question-result.html'
    context_object_name = 'question'
    model = Question


class VoteQuestion(View):

    def get(self, request, pk, *args, **kwargs):
        template_name = 'question-vote.html'
        context = {'form': AnswerForm, 'question': Question.objects.get(id=pk)}
        return render(request, template_name, context)

    def post(self, request, pk, *args, **kwargs):
        if self.request.user.is_authenticated:
            post_data_dict = request.POST
            user = self.request.user
            choice_number = post_data_dict['answer_number']
            question = Question.objects.get(id=pk)
            print('question: ', question)
            choice = Choice.objects.get(question=question, choice_number=choice_number)
            print('choice: ', choice)
            answers = Answer.objects.filter(profile=user, question=question)
            print('answer: ', answers)
            if not answers:
                print('before create')
                answer = Answer.objects.create(profile=user, question=question, choice=choice)
                print(answer)
                print('after create')
            else:
                messages.error(request, 'you are voted', fail_silently=True)
                print('ssssss')
                return redirect('question-result', pk=pk)
            return redirect('question-result', pk=pk)
        else:
            return redirect('login')


class AddQuestion(View):

    def get(self, request, *args, **kwargs):
        qform = QuestionForm()
        template_name = 'add_question.html'
        context = {'qform': qform}
        return render(request, template_name, context)

    def post(self, request, *args, **kwargs):
        if request.user.is_superuser:
            qform = QuestionForm(self.request.POST)
            if qform.is_valid():
                qform.save()
                return redirect('choice-add')

        else:
            redirect('home')


class AddChoice(View):

    def get(self, request, *args, **kwargs):
        cform = ChoiceForm()
        template_name = 'add_choice.html'
        context = {'cform': cform}
        return render(request, template_name, context)

    def post(self, request, *args, **kwargs):
        if request.user.is_superuser:
            cform = ChoiceForm(request.POST)
            if cform.is_valid():
                cform.save()
                return redirect('choice-add')
        else:
            redirect('home')