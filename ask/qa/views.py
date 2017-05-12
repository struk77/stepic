from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.http import HttpResponse
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO)

logger = logging.getLogger(__name__)

def test(request, *args, **kwargs):
    return HttpResponse('OK')
    
@require_GET
def question_details(request, question_id):
    question = get_object_or_404(Question, question_id=question_id)
    return render(request, 'question/question_details.html', {
        'question':     question,
        })
