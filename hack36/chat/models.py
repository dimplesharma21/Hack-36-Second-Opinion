from django.db import models
from .validate import Numerics
from .validate import alphaSpaces
from .validate import no
from .validate import decimals
from .validate import alphanumeric
# Create your models here.
SELECT_CHOICES=(('Male','Male'),('Female','Female'),('Transgender','Transgender'))
APPT_CHOICES=(('Heart Checkup','Heart Checkup'),('Eye Checkup','Eye Checkup'),('Hearing Test','Hearing Test'),('Blood Test','Blood Test'),('Normal Consulting','Normal Consulting'),('Skin Care','Skin Care'))
DATE_CHOICES=(('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12'),('13','13'),('14','14'),('15','15'),('16','16'),('17','17'),('18','18'),('19','19'),('20','20'),('21','21'),('22','22'),('23','23'),('24','24'),('25','25'),('26','26'),('27','27'),('28','28'),('29','29'),('30','30'),('31','31'))
MONTH_CHOICES=(('January','January'),('February','February'),('March','March'),('April','April'),('May','May'),('June','June'),('July','July'),('August','August'),('September','September'),('October','October'),('November','November'),('December','December'))
CATEGORY1_CHOICES=(('Coronary Angiography','Coronary Angiography'),('Angiography','Angiography'),('Bypass Surgery','Bypass Surgery'))

CATEGORY10_CHOICES=(('Urgent','Urgent'),('Routine/Non-urgent','Routine/Non-urgent'))
CATEGORY9_CHOICES=(('Urgent','Urgent'),('Routine','Routine'))
CATEGORY8_CHOICES=(('dialysis','dialysis'),('renal','renal'),('socatother','socatother'))
class regdetails(models.Model):
	Full_Name=models.CharField(max_length=20)
	User_Name=models.CharField(max_length=20)
	Password=models.CharField(max_length=20)
	CPassword=models.CharField(max_length=20)
	Gender=models.CharField(max_length=20, choices=SELECT_CHOICES)
	Mobile_Number=models.CharField(max_length=10,validators=[Numerics])
	Day=models.CharField(max_length=2, choices=DATE_CHOICES)
	Month=models.CharField(max_length=10, choices=MONTH_CHOICES)
	Year=models.CharField(max_length=4)
	Address=models.TextField()
	Pin_code=models.CharField(max_length=6, validators=[no])
	Country=models.CharField(max_length=20)
	E_mail=models.CharField(max_length=40)
	prev_cons=models.TextField(verbose_name=("Previous Consulting Details"))
	Appointment_type=models.CharField(max_length=20, choices=APPT_CHOICES)


class cardio(models.Model):
	ECG_report=models.CharField(max_length=100)
	Echocardiography_report=models.CharField(max_length=100)
	Echocardiography_images=models.CharField(max_length=100)
	Cardiac_biomarkers=models.CharField(max_length=100)
	Coronary_angiography=models.CharField(max_length=100)
	otherreport=models.CharField(max_length=100)
	category=models.CharField(max_length=100, choices=CATEGORY1_CHOICES)
	textarea=models.TextField()


class neurologyform(models.Model):
      mri=models.CharField(max_length=100)
      ctscan=models.CharField(max_length=100)
      ncv=models.CharField(max_length=100)
      category=models.CharField(max_length=100,choices=CATEGORY10_CHOICES)
      others=models.CharField(max_length=100)
      textarea=models.TextField()



class nephrology(models.Model):
    usg=models.CharField(max_length=100)
    bloodtest=models.CharField(max_length=100)
    other=models.CharField(max_length=100)
    textarea=models.TextField()
    category=models.CharField(max_length=100,choices=CATEGORY9_CHOICES)
    category1=models.CharField(max_length=100,choices=CATEGORY8_CHOICES)