from django.shortcuts import render

from .models import Category, Course, Tag


def course_list(request):
    # courses = Course.objects.all().order_by('-date')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    current_user = request.user
    
    if current_user.is_authenticated:
        enrolled_courses = current_user.courses_joined.all()
        courses = Course.objects.all().order_by('-date')
        for course in enrolled_courses:
            courses = courses.exclude(id=course.id)
    else:
        courses = Course.objects.all().order_by('-date')
        
    
    context = {
        'courses':courses,
        'categories':categories,
        'tags':tags,
    }
    
    return render(request,'courses.html', context)


def course_detail(request, category_slug, course_id):
    current_user = request.user
    course = Course.objects.get(category__slug=category_slug, id=course_id)
    courses = Course.objects.all().order_by('-date')
    
    if current_user.is_authenticated:
        enrolled_courses = current_user.courses_joined.all()
    else:
        enrolled_courses = courses
        
        
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    context={
        'course': course,
        'categories':categories,
        'tags':tags,
        'enrolled_courses':enrolled_courses,
    }
    return render(request,'course.html',context)


def category_list(request, category_slug):
    courses = Course.objects.all().filter(category__slug=category_slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    context={
        'courses': courses,
        'categories':categories,
        'tags':tags,
    }
    return render(request,'courses.html',context)


def tag_list(request, tag_slug):
    courses = Course.objects.all().filter(tags__slug=tag_slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    context={
        'courses': courses,
        'categories':categories,
        'tags':tags,
    }
    return render(request,'courses.html',context)


def search(request):
    courses = Course.objects.filter(name__contains=request.GET['search'])
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    context = {
        'courses':courses,
        'categories':categories,
        'tags':tags
    }    
    return render(request,'courses.html',context)


# def search(request):
#     courses = Course.objects.filter(description__contains=request.GET['search'])
#     categories = Category.objects.all()
#     tags = Tag.objects.all()
    
#     context = {
#         'courses':courses,
#         'categories':categories,
#         'tags':tags
#     }    
#     return render(request,'courses.html',context)