from django.shortcuts import render
from django.contrib.auth.decorators import login_required

html_content = [ {'brand': 'Billing Admin'} ]

@login_required
def index(request):
    context = { 
        'posts': html_content 
    }
    return render(request, 'frontend/index.html', context)