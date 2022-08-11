import datetime

from django.shortcuts import render
from main.models import *
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.

def mainHandler(request):
    if not request.session.get('user_id', None):
        return redirect('/login')

    if request.POST:
        action = request.POST.get('action', '')
        student_id = int(request.POST.get('student_id', 0))
        status = int(request.POST.get('status', 0))
        if action == 'student_go':
            st = Student.objects.get(id=student_id)
            st.status = status
            st.save()

    current_user = User.objects.get(id=int(request.session.get('user_id', 0)))
    search_value = request.GET.get('search', None)
    dtn = datetime.datetime.now()


    if search_value:
        students = Student.objects.filter(Q(iin__contains=search_value) | Q(first_name__contains=search_value))
    else:
        students = Student.objects.all()
    student_ids = []
    sinflar_ids = []
    for st in students:
        student_ids.append(st.id)
        sinflar_ids.append(st.sinf.id)
    lessons = Lesson.objects.filter(sinf__id__in = sinflar_ids)
    lesson_ids = []
    for li in lessons:
        lesson_ids.append(li.id)
    lesson_times = LessonTime.objects.filter(Q(lesson_id__id__in = lesson_ids) & Q(start_time__lte = dtn) & Q(stop_time__gte = dtn) & Q(week_day = (dtn.weekday()+1)))


    return render(request, 'main.html', {
        'current_user': current_user,
        'students': students,
        'lessons': lessons,
        'lesson_times': lesson_times

                                          })
def vhodHandler(request):
    if request.POST:
        login = request.POST.get('login', '')
        password = request.POST.get('password', '')
        if login and password:
            user = authenticate(username=login, password=password)
            if user is not None:
                request.session['user_id'] = user.id
                print(user)
                return redirect('/main')
            else:
                return redirect('/login')

    return render(request, 'vhod.html', {
                                          })

def exitHandler(request):
    del request.session['user_id']

    return render(request, 'vhod.html', {
                                          })


def classHandler(request):
    if not request.session.get('user_id', None):
        return redirect('/login')
    page = 'class'
    current_user = User.objects.get(id=int(request.session.get('user_id', 0)))
    stages = []
    sinfs = Sinf.objects.all()
    for s in sinfs:
        if s.stage not in stages:
            stages.append(s.stage)
    stages.sort()
    print(stages)



    return render(request, 'class.html', {
        'sinfs': sinfs,
        'current_user': current_user,
        'stages': stages,
        'page': page
    })


def classItemHandler(request,sinf_id):
    if not request.session.get('user_id', None):
        return redirect('/login')
    page = 'class'
    current_user = User.objects.get(id=int(request.session.get('user_id', 0)))

    sinf = Sinf.objects.get(id=int(sinf_id))
    students =Student.objects.filter(sinf__id = int(sinf_id))
    weeks = Week.objects.all().order_by('id')
    lessons = Lesson.objects.filter(sinf__id = int(sinf_id))
    lesid = LessonTime.objects.filter(lesson_id__sinf__id = int(sinf_id))

    lesson_ids =[]
    for l in lessons:
        lesson_ids.append(l.id)

    new_lesson_times = {}
    new_lesson_times_items = []

    lesson_times = LessonTime.objects.filter(lesson_id__id__in = lesson_ids).order_by('start_time', 'stop_time')
    for lt in lesson_times:
        if f'{lt.start_time}-{lt.stop_time}' not in new_lesson_times:
            new_lesson_times[f'{lt.start_time}-{lt.stop_time}'] = []
            new_lesson_times_items.append(f'{lt.start_time}-{lt.stop_time}')
        new_lesson_times[f'{lt.start_time}-{lt.stop_time}'].append(lt)

    return render(request, 'classitem.html', {
        'sinf': sinf,
        'lesson_times': lesson_times,
        'weeks': weeks,
        'students': students,
        'lesid': lesid,
        'new_lesson_times_items': new_lesson_times_items,
        'new_lesson_times': new_lesson_times,
        'current_user': current_user,
        'page': page
    })

def studentHandler(request):
    if not request.session.get('user_id', None):
        return redirect('/login')
    page = 'student'
    stage = int(request.GET.get('stage',0))
    symbol = request.GET.get('symbol','')
    status = int(request.GET.get('status',-1))
    diagnoz = int(request.GET.get('diagnoz',0))

    current_user = User.objects.get(id=int(request.session.get('user_id', 0)))
    students = Student.objects.all()
    if diagnoz:
        students = Student.objects.filter(Q(diagnoz__id=diagnoz))
        if stage:
            students = Student.objects.filter(Q(sinf__stage=stage) & Q(diagnoz__id=diagnoz))
            if symbol:
                students = Student.objects.filter(Q(diagnoz__id=diagnoz) & Q(sinf__stage=stage) & Q(sinf__symbol=symbol))
                if status > -1:
                    students = Student.objects.filter(Q(diagnoz__id=diagnoz) & Q(sinf__stage=stage) & Q(sinf__symbol=symbol) & Q(status=status))
            else:
                if status > -1:
                    students = Student.objects.filter(Q(sinf__stage=stage) & Q(status=status))
    else:
        if status > -1:
            students = Student.objects.filter(Q(status=status))
        if stage > 0:
            students = Student.objects.filter(Q(sinf__stage=stage))
        if diagnoz > 0:
            students = Student.objects.filter(Q(diagnoz__id=diagnoz))



    sinfs = Sinf.objects.all()
    diagnozs = Diagnoz.objects.all()
    all_sinf = Sinf.objects.all()
    a = range(1,10)
    new_symbols = []
    for asi in all_sinf:
        if asi.symbol not in new_symbols:
            new_symbols.append(asi.symbol)


    return render(request, 'student.html', {
        'students': students,
        'a':a,
        'new_symbols':new_symbols,
        'current_user': current_user,
        'all_sinf':all_sinf,
        'stage': stage,
        'symbol': symbol,
        'status': status,
        'page': page,
        'diagnoz': diagnoz,
        'diagnozs': diagnozs

    })


def studentItemHandler(request,student_id):
    if not request.session.get('user_id', None):
        return redirect('/login')
    current_user = User.objects.get(id=int(request.session.get('user_id', 0)))
    page = 'student'

    parents = Student_parent.objects.all()
    student = Student.objects.get(id=int(student_id))
    return render(request, 'studentitem.html', {
        'student': student,
        'current_user': current_user,
        'page': page,
        'parents': parents
    })

def prepodHandler(request):
    if not request.session.get('user_id', None):
        return redirect('/login')
    page = 'prepod'
    doljn = int(request.GET.get('doljn', '0'))
    current_user = User.objects.get(id=int(request.session.get('user_id', 0)))

    prepod = InfoTeacher.objects.all()
    if doljn:
        prepod = InfoTeacher.objects.filter(Q(doljnost__id=doljn))
    dolj = Doljnost.objects.all()

    return render(request, 'prepod.html', {
        'prepod': prepod,
        'dolj':dolj,
        'doljn':doljn,
        'current_user': current_user,
        'page': page
    })


def prepodItemHandler(request, prepod_id):
    if not request.session.get('user_id', None):
        return redirect('/login')
    page = 'prepod'
    current_user = User.objects.get(id=int(request.session.get('user_id', 0)))

    prepod = InfoTeacher.objects.get(id=int(prepod_id))

    return render(request, 'prepoditem.html', {
        'prepod': prepod,
        'current_user': current_user,
        'page': page
    })

def lessonHandler(request,):
    if not request.session.get('user_id', None):
        return redirect('/login')
    page = 'lesson'
    current_user = User.objects.get(id=int(request.session.get('user_id', 0)))
    sinflar = Sinf.objects.all().order_by('stage', 'symbol')
    sinflar_obj = []

    for ss in sinflar:
        sinf_id = ss.id
        sinf = Sinf.objects.get(id=int(sinf_id))
        weeks = Week.objects.all().order_by('id')
        lessons = Lesson.objects.filter(sinf__id=int(sinf_id))


        lesson_ids = []
        for l in lessons:
            lesson_ids.append(l.id)

        new_lesson_times = {}
        new_lesson_times_items = []

        lesson_times = LessonTime.objects.filter(lesson_id__id__in=lesson_ids).order_by('start_time', 'stop_time')
        for lt in lesson_times:
            if f'{lt.start_time}-{lt.stop_time}' not in new_lesson_times:
                new_lesson_times[f'{lt.start_time}-{lt.stop_time}'] = []
                new_lesson_times_items.append(f'{lt.start_time}-{lt.stop_time}')
            new_lesson_times[f'{lt.start_time}-{lt.stop_time}'].append(lt)

        sinf_obj = {
            'sinf': sinf,
            'new_lesson_times': new_lesson_times,
            'new_lesson_times_items': new_lesson_times_items

        }
        sinflar_obj.append(sinf_obj)




    return render(request, 'lesson.html', {
        'sinflar_obj':sinflar_obj,
        'weeks': weeks,
        'current_user': current_user,
        'page': page
        })

