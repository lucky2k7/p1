from django.http import HttpResponse
from django.shortcuts import render

def aboutUs(request):
    return HttpResponse("welcome to about us page")

def contect(request):
    return HttpResponse("<h2>Email:- Lakhanrs210@gmail.com \n mob:- 8440823412</h2>")

# def course_details(request,courseid):
#     return HttpResponse(courseid)

# def course_details(request, coursename):
#     return HttpResponse(coursename)

def course_details(request, course_details):
    return HttpResponse(course_details)

def home_page(request):
    data = {
        "title":"Home",
        "bdata": "lakhan saini",
        "cdata":["lakhan","saini"],
        "ddata" : [
            {"name":"Lakhan","age":"25"},
            {"name":"Saini","age":"26"}
        ],
        'edata':[8440823412, 9680888975]
    }
    return render(request, "index.html", data)