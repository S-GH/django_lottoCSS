from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Question
# Create your views here.
def index(request):
    # 등록 날짜 기준 sort
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # py > html로 정보를 보낼때 쓰는것은 context라고 부른다.
    context = {'latest_question_list':latest_question_list}
    return render(request,'polls/index.html',context)

def detail(request, question_id):
    # q = Question.objects.get(pk=question_id)
    q = get_object_or_404(Question,pk=question_id)
    return render(request, 'polls/detail.html', {'question':q})

def result(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request, 'polls/result.html', {'question':question})

def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        # choice_select는 detail.html의 radio버튼의 이름
        print(request.POST)
        selected_choice = question.choice_set.get(pk=request.POST['choice_select'])
    except:
        context = {'question':question,'error_message':"you didn't select a choice"}
        return render(request,'polls/detail.html',context)
    else:
        selected_choice.votes += 1
        selected_choice.save() # DB 저장
        return redirect('polls:result',question_id=question.id)
