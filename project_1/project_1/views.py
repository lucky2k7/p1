from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .form import UserForm
from .form import subjects
from city.models import City

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
    result = None
    city_data = City.objects.all()
    # if request.method=="GET":
    #     result = request.GET['result']
    # print(result)
    data = {
        "title":"Home",
        'city_data':city_data,
        # "bdata": "lakhan saini",
        # "cdata":["lakhan","saini"],
        # "ddata" : [
        #     {"name":"Lakhan","age":"25"},
        #     {"name":"Saini","age":"26"}
        # ],
        # 'edata':[8440823412, 9680888975],
        "content":"London, the capital of England and the United Kingdom, is a 21st-century city with history stretching back to Roman times. At its centre stand the imposing Houses of Parliament, the iconic ‘Big Ben’ clock tower and Westminster Abbey, siteof British monarch coronations. Across the Thames River, the London Eye observation wheel provides panoramic views of the South Bank cultural complex, and the entire city."
    }
    # if(result != None):
    #     data["result"]=result
    # print(data['result'])
    return render(request, "index.html", data)
def tokyo(request):
    city_data = City.objects.all()
    for city in city_data:
        if city.city_tital == "tokyo":
            data = {
                'title':city.city_tital,
                'content':city.city_description
            }
    # data = {
    #     "title" : "tokyo",
    #     "content":"Tokyo, Japan’s busy capital, mixes the ultramodern and the traditional, from neon-lit skyscrapers to historic temples. The opulent Meiji Shinto Shrine is known for its towering gate and surrounding woods. The Imperial Palace sits amid large public gardens. The city's many museums offer exhibits ranging from classical art (in the Tokyo National Museum) to a reconstructed kabuki theater (in the Edo-Tokyo Museum)."
    # }
    return render(request, "content.html", data)
def newyork(request):
    citydata = City.objects.all()
    print(citydata)
    for i in citydata:
        if i.city_tital == "New York":
            data = {
                'title':i.city_tital,
                'content':i.city_description,
            }
    # data = {
    #     "title" : "New York",
    #     "content":"New York City comprises 5 boroughs sitting where the Hudson River meets the Atlantic Ocean. At its core is Manhattan, a densely populated borough that’s among the world’s major commercial, financial and cultural centers. Its iconic sites include skyscrapers such as the Empire State Building and sprawling Central Park. Broadway theater is staged in neon-lit Times Square."
    # }
    return render(request, "newyork.html",data)

def user_input(request):
    data = {}
    try:
        if request.method=="GET":
        #     name = request.GET['name']
        #     email = request.GET['email']
            # name = request.GET.get('name')
            # email = request.GET
            print(request.GET)
            # print(name)
            pass    
        elif request.method=="POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            print(request.POST)
            url = "/?result={}".format("you-redirected-from-userinput-page")
            url = "/?result=you-redirected-from-userinput-page"
            if(name == "" or email == ""):
                return HttpResponseRedirect("/userinput")
            return HttpResponseRedirect(url)

        data = {
            "name":name,
            'email':email,
            "title" : "User Input Page",
        }

    except:
        pass
    
    if len(data)==0:
        return render(request,"userinput.html")
    else:
        return render(request,"userinput.html", data) 

def submitform(request):
    # return HttpResponse(request)
    # return render(request, "userinput.html")
    return HttpResponseRedirect("/")

def UserForms(request):
    fn = UserForm()
    data = {
        'form':fn,
    }
    return render(request, "UserForm.html", data)    

def marksheet(request):
    try:
        if request.method=="POST":
            if request.POST.get('subject1')=="":
                data = {
                    'error':True,
                    'subjects':subjects(),
                }
                return render(request,'marksheet.html',data)
            s1 = eval(request.POST.get('subject1'))
            s2 = eval(request.POST.get('subject2'))
            s3 = eval(request.POST.get('subject3'))
            s4 = eval(request.POST.get('subject4'))
            s5 = eval(request.POST.get('subject5'))
            s6 = eval(request.POST.get('subject6'))

            t = s1+s2+s3+s4+s5+s6
            p = t*100/600
            if p >=60:
                g = 'First Devision'
            elif p >=50:
                g = 'Second Devision'
            elif p >=33:
                g = 'Thired Devision'
            else:
                g = "Fail"
            data = {
                'total':t,
                'percent':p,
                'grade':g,
                'subjects':subjects(),
            }
            # print(data)
            return render(request, 'marksheet.html', data)
    except:
        pass
    data = {
        'subjects':subjects(),
    }
    print(data)
    return render(request, 'marksheet.html',data)

def display(request):
    citydata = City.objects.all().order_by('id')[0:2]
    data = {
        'citydata': citydata,
    }

    return render(request, "content.html", data)

def city_detail(request,id):
    single_city_data = City.objects.get(id=id)
    all_city_data = City.objects.all()
    data = {
        'single_city_data': single_city_data,
        'city_data': all_city_data,
    }
    return render(request, 'news_details.html',data)