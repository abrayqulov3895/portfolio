
from django.shortcuts import render,HttpResponse
from account.forms import ContactForm
from django.http import HttpResponseRedirect,JsonResponse

from django.core.mail import send_mail,get_connection
from account.models import Brend,  Fair_price, IconInformation, Information, Language, Love_to, SpecialistInformation, Thoughts, Work
# from hackershack_website import settings
# Create your views here.

def home(request):
    informations = Information.objects.all()[:1]
    iconinformations = IconInformation.objects.all()[:5]
    specialistinformations = SpecialistInformation.objects.all()[:3]

    works = Work.objects.all()[:6]
    thoughts = Thoughts.objects.all()
    fairprices = Fair_price.objects.all()[:3]
    hobbes = Love_to.objects.all()[:3]
    langueages = Language.objects.all()[:5]
    brends = Brend.objects.all()[:4]
    context = {
        "informations":informations,
        'iconinformations':iconinformations,
        'specialistinformations':specialistinformations,
        'works':works,
        'thoughts':thoughts,
        'fairprices':fairprices,
        'hobbes':hobbes,
        'languages':langueages,
        'brends':brends
    }
    return render(request,'account/index.html',context)

def resume(request):
    informations = Information.objects.all()[:1]
    iconinformations = IconInformation.objects.all()[:5]
    specialistinformations = SpecialistInformation.objects.all()[:3]
    context = {
        "informations":informations,
        'iconinformations':iconinformations,
        'specialistinformations':specialistinformations
    }
    return render(request,'account/resume.html',context)

def portfolio(request):
    informations = Information.objects.all()[:1]
    iconinformations = IconInformation.objects.all()[:5]
    specialistinformations = SpecialistInformation.objects.all()[:3]
    context = {
        "informations":informations,
        'iconinformations':iconinformations,
        'specialistinformations':specialistinformations
    }
    return render(request,'account/portfolio.html',context)

def blog(request):
    informations = Information.objects.all()[:1]
    iconinformations = IconInformation.objects.all()[:5]
    specialistinformations = SpecialistInformation.objects.all()[:3]
    context = {
        "informations":informations,
        'iconinformations':iconinformations,
        'specialistinformations':specialistinformations
    }
    return render(request,'account/blog.html',context)

def contact(request):
    informations = Information.objects.all()[:1]
    iconinformations = IconInformation.objects.all()[:5]
    specialistinformations = SpecialistInformation.objects.all()[:3]

    # submitted = False
    # # print(request.POST)
    # if request.method == "POST":
    #     form = ContactForm(request.POST)
    #     print(form)

    #     if form.is_valid():
    #         cd = form.cleaned_data
    #         # assert False
            
    #         return HttpResponseRedirect('/contact?submitted = True')

    # else:
    #     form = ContactForm()
    #     if "submitted" in request.GET:
    #         submitted = True       
    if request.method =="GET":
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        if is_ajax:
            form = ContactForm(request.GET)
            if form.is_valid():
                form.save()
                message = 'Your message is save to data base!'
                
                return JsonResponse({'result':True, 'message':message})
            message = 'we must enter all dates'
           
            return JsonResponse({'result':False, 'message':message})
        
        
    context = {
        "informations":informations,
        'iconinformations':iconinformations,
        'specialistinformations':specialistinformations,
        
        
    }
    return render(request,'account/contact.html',context)
