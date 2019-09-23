from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.template import loader

from .models import Choice, Question, Suggestion
from .forms import suggestionFormForm


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):

        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Nah Fam.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def suggestionList(request):
    latest_suggestion_list = Suggestion.objects.order_by('-sub_date')[:5]
    template = loader.get_template('polls/SuggestionList.html')
    context = {
        'latest_suggestion_list': latest_suggestion_list,
    }
    return HttpResponse(template.render(context, request))
def suggestionDetail(request, pk):
    suggestion = get_object_or_404(Suggestion, pk=pk)
    return render(request, 'polls/suggestionDetail.html', {'suggestion': suggestion})
 #   try:
  #      selected_choice = suggestion.choice_set.get(pk=request.POST['Suggestion'])
   # except (KeyError, Suggestion.DoesNotExist):
def suggestionForm(request):

    if request.method == "POST":
        form = suggestionFormForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.sug_name = form.cleaned_data['sug_name']
            post.body_text = form.cleaned_data['body_text']

            post.sub_date = timezone.now()
            post.save()
            return HttpResponseRedirect(reverse('polls:suggestion'))
    else:
        form = suggestionFormForm()
        return render(request, 'suggestionForm.html', {'form': form})
