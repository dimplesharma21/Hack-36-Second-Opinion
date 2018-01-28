from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import*
#reg details
def regdetailsadd(request):
    return render(request, 'regdetails/change.html')

def regdetailscreate(request):
    member1 = regdetails(Full_Name=request.POST['Full_Name'],User_Name=request.POST['User_Name'],Password=request.POST['Password'],CPassword=request.POST['CPassword'], Gender=request.POST['Gender'], Mobile_Number=request.POST['Mobile_Number'], Day=request.POST['Day'], Month=request.POST['Month'], Year=request.POST['Year'], Address=request.POST['Address'], Pin_code=request.POST['Pin_code'], Country=request.POST['Country'], E_mail=request.POST['E_mail'], prev_cons=request.POST['prev_cons'], Appointment_type=request.POST['Appointment_type'])
    member1.save()
    return redirect('/regdetails')

def regdetailsedit(request, id):
    members1 = regdetails.objects.get(id=id)
    context = {'members1': members1}
    return render(request, 'regdetails/change.html', context)

def regdetailsupdate(request, id):
    member1 = regdetails.objects.get(id=id)
    member1.Full_Name = request.POST['Full_Name']
    member1.User_Name = request.POST['User_Name']
    member1.Password = request.POST['Password']
    member1.CPassword = request.POST['CPassword']
    member1.Gender = request.POST['Gender']
    member1.Mobile_Number = request.POST['Mobile_Number']
    member1.Day = request.POST['Day']
    member1.Month = request.POST['Month']
    member1.Year = request.POST['Year']
    member1.Address = request.POST['Address']
    member1.Pin_code = request.POST['Pin_code']
    member1.Country = request.POST['Country']
    member1.E_mail = request.POST['E_mail']
    member1.prev_cons = request.POST['prev_cons']
    member1.Appointment_type = request.POST['Appointment_type']  
    member1.save()
    return redirect('/regdetails')

def regdetailsdelete(request, id):
    member1 = regdetails.objects.get(id=id)
    member1.delete()
    return redirect('/regdetails')

#cardio
def cardiosee(request):
    return render(request, 'cardio/cardiology.html') 

def cardioadd(request):
    return render(request, 'cardio/change.html')

def cardiocreate(request):
    member2 = cardio(ECG_report=request.POST['ECG_report'],Echocardiography_report=request.POST['Echocardiography_report'],Echocardiography_images=request.POST['Echocardiography_images'],Cardiac_biomarkers=request.POST['Cardiac_biomarkers'], Coronary_angiography=request.POST['Coronary_angiography'], otherreport=request.POST['otherreport'], category=request.POST['category'], textarea=request.POST['textarea'], )
    member2.save()
    return redirect('/cardio')

def cardioedit(request, id):
    members2 = cardio.objects.get(id=id)
    context = {'members2': members2}
    return render(request, 'cardio/change.html', context)

def cardioupdate(request, id):
    member2 = cardio.objects.get(id=id)
    member2.ECG_report = request.POST['ECG_report']
    member2.Echocardiography_report = request.POST['Echocardiography_report']
    member2.Echocardiography_images = request.POST['Echocardiography_images']
    member2.Cardiac_biomarkers = request.POST['Cardiac_biomarkers']
    member2.Coronary_angiography = request.POST['Coronary_angiography']
    member2.otherreport = request.POST['otherreport']
    member2.category = request.POST['category']
    member2.textarea = request.POST['textarea']
    member2.save()
    return redirect('/cardio')

def cardiodelete(request, id):
    member2 = cardio.objects.get(id=id)
    member2.delete()
    return redirect('/cardio')

#neurology
def neurologyformsee(request):
    return render(request, 'neurologyform/neurology.html') 
def neurologyformadd(request):
    return render(request, 'neurologyform/change.html')

def neurologyformcreate(request):
    member10 = neurologyform(mri=request.POST['mri'],bloodtest=request.POST['bloodtest'],ncv=request.POST['ncv'],textarea=request.POST['textarea'])
    member10.save()
    return redirect('/neurologyform')

def neurologyformedit(request, id):
    members10 = neurologyform.objects.get(id=id)
    context = {'members10': members10}
    return render(request, 'neurologyform/change.html', context)

def neurologyformupdate(request, id):
    member10 = neurologyform.objects.get(id=id)
    member10.mri = request.POST['mri']
    member10.bloodtest = request.POST['bloodtest']
    member10.ncv = request.POST['ncv']
    member10.textarea = request.POST['textarea']
    member10.save()
    return redirect('/neurologyform')

def neurologyformdelete(request, id):
    member10 = neurologyform.objects.get(id=id)
    member10.delete()
    return redirect('/neurologyform')   

#nephrology

def nephrologysee(request):
    return render(request, 'nephrology/nephrology.html') 
def nephrologyadd(request):
    return render(request, 'nephrology/change.html')

def nephrologycreate(request):
    member9 = nephrology(usg=request.POST['usg'],ctscan=request.POST['ctscan'],other=request.POST['other'],textarea=request.POST['textarea'])
    member9.save()
    return redirect('/nephrology')

def nephrologyedit(request, id):
    members9 = nephrology.objects.get(id=id)
    context = {'members9': members9}
    return render(request, 'nephrology/change.html', context)

def nephrologyupdate(request, id):
    member9 = nephrology.objects.get(id=id)
    member9.usg = request.POST['usg']
    member9.ctscan = request.POST['ctscan']
    member9.other = request.POST['other']
    member9.textarea = request.POST['textarea']
    member9.save()
    return redirect('/nephrology')

def nephrologydelete(request, id):
    member9 = nephrology.objects.get(id=id)
    member9.delete()
    return redirect('/nephrology')



