from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO)

logger = logging.getLogger(__name__)

def test(request, *args, **kwargs):
    logger.INFO("huyase")
    return HttpResponse('OK')