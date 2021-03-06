from django.shortcuts import render, redirect

LANGS = (
    'Python',
    'JavaScript',
    'C#',
    'Java',
    'C',
    'HTML',
    'CSS'
)
LOCATIONS = (
    'San Jose',
    'Seattle',
    'Chicago',
    'New York',
    'Austin',
    'Online'
)

# Create your views here.

def index(request):
    context = {
        'locations': LOCATIONS,
        'languages': LANGS
    }
    return render(request, 'index.html', context)

def survey(request):
    if request.method == 'GET':
        return redirect('/')
    request.session['result'] = {
        'name': request.POST['name'],
        'location': request.POST['location'],
        'language': request.POST['language'],
        'comment': request.POST['comment']
    }
    return redirect('/result')

def result(request):
    context = {
        'result': request.session['result']
    }
    return render(request, 'result.html', context)
