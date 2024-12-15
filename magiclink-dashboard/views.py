from django.shortcuts import render
from django.http import JsonResponse
from .ragsearch import get_answer

def ragsearch_view(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        if question:
            answer = get_answer(question)
            return JsonResponse({'answer': answer})
    return render(request, 'ragsearch.html')
