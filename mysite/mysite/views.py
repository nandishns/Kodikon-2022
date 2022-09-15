# Created by @me
from django.http import HttpResponse
from django.shortcuts import render
from .tr_mod import translate

# def index(request):
#
#     return render(request, 'index.html', params)

# def about(request):
#     return HttpResponse("This is about page <a href='/'>Home</a>")

# def about(request):
#     sites = ['''<h1>For Entertainment </h1><a href = "https://www.youtube.com" >youtube video</a>''',
#              '''<h1>For Interaction </h1><a href = "https://www.facebook.com" >Facebook</a>''',
#              '''<h1>For Insight   </h1><a href = "https://www.ted.com/talks" >Ted Talk</a>''',
#              '''<h1>For Internship   </h1><a href="https://internshala.com" >Intenship</a>''',
#              ]
#     return HttpResponse((sites))

def start(request):
    return render(request,"start.html")
def login(request):
    return render(request,"login_page.html")
def third_page(request):
    print(request.GET.get('slide'))
    return render(request,"third_page.html")

def QP_first(request):
    return render(request, 'domain.html')

dom = 0
lang = 'en'

def QP_Generate(request):
    global dom
    global lang
    lang = request.GET.get('language', 'en')
    dom = int(request.GET.get('domain', 1))
    if dom == 1:
        f = open("qp2.txt", "r")
    elif dom == 2:
        f = open("qp1.txt", "r")
    params = {'question1': f.readline(), 'q1a': f.readline(), 'q1b': f.readline(), 'q1c': f.readline(), 'q1d': f.readline(),
              'question2': f.readline(), 'q2a': f.readline(), 'q2b': f.readline(), 'q2c': f.readline(), 'q2d': f.readline(),
              'question3': f.readline(), 'q3a': f.readline(), 'q3b': f.readline(), 'q3c': f.readline(), 'q3d': f.readline(),
              'question4': f.readline(), 'q4a': f.readline(), 'q4b': f.readline(), 'q4c': f.readline(), 'q4d': f.readline(),
              'question5': f.readline(), 'q5a': f.readline(), 'q5b': f.readline(), 'q5c': f.readline(), 'q5d': f.readline()
              }
    f.close()
    if lang != 'en':
        for i in params:
            params[i] = translate(params[i], lang)
    return render(request, 'self_assessment.html', params)

def QP_Submit(request):
    q1, q2, q3, q4, q5 = request.GET.get('q1', 'off'), request.GET.get('q2', 'off'), request.GET.get('q3', 'off'), request.GET.get('q4', 'off'), request.GET.get('q5', 'off')
    if dom == 1:
        f = open("qp2_ans.txt", "r")
        f2 = open("qp2.txt", "r")
    elif dom == 2:
        f = open("qp1_ans.txt", "r")
        f2 = open("qp1.txt", "r")
    ans = f.readlines()
    ans = [i.strip() for i in ans]
    params = {'question1': f2.readline(), 'q1a': f2.readline(), 'q1b': f2.readline(), 'q1c': f2.readline(),
              'q1d': f2.readline(),
                'question2': f2.readline(), 'q2a': f2.readline(), 'q2b': f2.readline(), 'q2c': f2.readline(),
                'q2d': f2.readline(),
                'question3': f2.readline(), 'q3a': f2.readline(), 'q3b': f2.readline(), 'q3c': f2.readline(),
                'q3d': f2.readline(),
                'question4': f2.readline(), 'q4a': f2.readline(), 'q4b': f2.readline(), 'q4c': f2.readline(),
                'q4d': f2.readline(),
                'question5': f2.readline(), 'q5a': f2.readline(), 'q5b': f2.readline(), 'q5c': f2.readline(),
                'q5d': f2.readline()
              }
    f.close()
    f2.close()
    if lang != 'en':
        for i in params:
            params[i] = translate(params[i], lang)
    score = 0
    if q1 == ans[0]:
        q1 = chr(96+int(q1))
        score += 1
        params[f'q1{q1}'] = params[f'q1{q1}'] + '✅'
    else:
        q1 = chr(96 + int(q1))
        answ = chr(96 + int(ans[0]))
        params[f'q1{q1}'] = params[f'q1{q1}'] + "❌"
        params[f'q1{answ}'] = params[f'q1{answ}'] + "✅"
    if q2 == ans[1]:
        q2 = chr(96+int(q2))
        score += 1
        params[f'q2{q2}'] = params[f'q2{q2}'] + "✅"
    else:
        q2 = chr(96 + int(q2))
        answ = chr(96 + int(ans[1]))
        params[f'q2{q2}'] = params[f'q2{q2}'] + "❌"
        params[f'q2{answ}'] = params[f'q2{answ}'] + "✅"
    if q3 == ans[2]:
        q3 = chr(96+int(q3))
        score += 1
        params[f'q3{q3}'] = params[f'q3{q3}'] + "✅"
    else:
        q3 = chr(96 + int(q3))
        answ = chr(96 + int(ans[2]))
        params[f'q3{q3}'] = params[f'q3{q3}'] + "❌"
        params[f'q3{answ}'] = params[f'q3{answ}'] + "✅"
    if q4 == ans[3]:
        q4 = chr(96+int(q4))
        score += 1
        params[f'q4{q4}'] = params[f'q4{q4}'] + "✅"
    else:
        q4 = chr(96 + int(q4))
        answ = chr(96 + int(ans[3]))
        params[f'q4{q4}'] = params[f'q4{q4}'] + "❌"
        params[f'q4{answ}'] = params[f'q4{answ}'] + "✅"
    if q5 == ans[4]:
        q5 = chr(96+int(q5))
        score += 1
        params[f'q5{q5}'] = params[f'q5{q5}'] + "✅"
    else:
        q5 = chr(96 + int(q5))
        answ = chr(96 + int(ans[4]))
        params[f'q5{q5}'] = params[f'q5{q5}'] + "❌"
        params[f'q5{answ}'] = params[f'q5{answ}'] + "✅"
    params['message'] = f'Your score is {score}/5'
    # return HttpResponse(request, '<a href=".">Home</a>', params)
    return render(request, 'self_assessment.html', params)

def peer(request):
    return render(request,'peer.html')

def project(request):
    return render(request,'project.html')

def notify(request):
    return render(request, 'notify.html')

def languagepro(request):
    return render(request, 'languagepro.html')

def pbl(request):
    return render(request, 'pbl.html')
