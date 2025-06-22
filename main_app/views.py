from django.shortcuts import render, redirect
from .forms import SignForm, ReviewForm


def index(request):
    success = False  # Это флаг для отображения успешного сообщения
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем форму в базе данных
            success = True  # Устанавливаем флаг, чтобы отобразить сообщение об успехе
            form = SignForm()  # Очищаем форму после успешной отправки
    else:
        form = SignForm()  # Создаём форму с дефолтными значениями

    return render(request, 'main/index.html', {'form': form, 'success': success})


def about(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()  # или любая ваша логика
            return render(request, 'main/about.html', {
                'form': SignForm(),  # очистка формы
                'success': True  # флаг успешной отправки
            })
    else:
        form = SignForm()

    return render(request, 'main/about.html', {
        'form': form,
        'success': False
    })

def courses_online(request):
    if request.method == 'GET':
        return render(request,'main/courses_online.html')


def courses_2_4(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()  # или любая ваша логика
            return render(request, 'main/courses_2_4.html', {
                'form': SignForm(),  # очистка формы
                'success': True  # флаг успешной отправки
            })
    else:
        form = SignForm()

    return render(request, 'main/courses_2_4.html', {
        'form': form,
        'success': False
    })

def courses_4_6(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()  # или любая ваша логика
            return render(request, 'main/courses_4_6.html', {
                'form': SignForm(),  # очистка формы
                'success': True  # флаг успешной отправки
            })
    else:
        form = SignForm()

    return render(request, 'main/courses_4_6.html', {
        'form': form,
        'success': False
    })

def courses_6_7(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()  # или любая ваша логика
            return render(request, 'main/courses_6_7.html', {
                'form': SignForm(),  # очистка формы
                'success': True  # флаг успешной отправки
            })
    else:
        form = SignForm()

    return render(request, 'main/courses_6_7.html', {
        'form': form,
        'success': False
    })


def courses_7_9(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()  # или любая ваша логика
            return render(request, 'main/courses_7_9.html', {
                'form': SignForm(),  # очистка формы
                'success': True  # флаг успешной отправки
            })
    else:
        form = SignForm()

    return render(request, 'main/courses_7_9.html', {
        'form': form,
        'success': False
    })


def courses_9_11(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()  # или любая ваша логика
            return render(request, 'main/courses_9_11.html', {
                'form': SignForm(),  # очистка формы
                'success': True  # флаг успешной отправки
            })
    else:
        form = SignForm()

    return render(request, 'main/courses_9_11.html', {
        'form': form,
        'success': False
    })


def courses_11_13(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()  # или любая ваша логика
            return render(request, 'main/courses_11_13.html', {
                'form': SignForm(),  # очистка формы
                'success': True  # флаг успешной отправки
            })
    else:
        form = SignForm()

    return render(request, 'main/courses_11_13.html', {
        'form': form,
        'success': False
    })