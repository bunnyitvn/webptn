from django.db import models
from datetime import datetime
# Create your models here.
class Faculty(models.Model):
	IDfaculty = models.AutoField(primary_key = True)
	name = models.CharField(max_length=300)
 	def __unicode__(self):
        	return self.name
class Person(models.Model):
	IDperson  = models.AutoField(primary_key = True)
	IDfaculty  = models.ForeignKey(Faculty)
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	name = models.CharField(max_length=300)
	status = models.TextField(max_length=300)
	def __unicode__(self):
        	return self.name
class Student(models.Model):
	IDstudent = models.AutoField(primary_key = True)
	IDperson = models.ForeignKey(Person)
	def __unicode__(self):
        	return self.IDstudent
class Staff(models.Model):
	IDperson = models.ForeignKey(Person)
	IDstaff = models.AutoField(primary_key = True)
	def __unicode__(self):
        	return self.IDstaff
class Seminar_registration_form(models.Model):
	IDseminar = models.AutoField(primary_key = True)
	IDperson = models.ForeignKey(Person)
	datetime = models.DateTimeField('Date register',default=datetime.now(),blank=True)
	def __unicode__(self):
		return self.IDseminar
class Desk(models.Model):
	IDdesk = models.AutoField(primary_key = True)
	name = models.CharField(max_length=300)
	status = models.TextField(max_length=300)
	def __unicode__(self):
        	return self.name
class Cpu_screen(models.Model):
	IDcpu = models.AutoField(primary_key = True)
	IDdesk = models.ForeignKey(Desk)
	name = models.CharField(max_length=300)
	status = models.TextField(max_length=300)
	description = models.TextField()
	def __unicode__(self):
        	return self.name
class Working_placement(models.Model):
	IDperson = models.ForeignKey(Person)
	IDdesk = models.ForeignKey(Desk)
	IDworking  = models.AutoField(primary_key = True)
	datetime = models.DateTimeField('Ngay dang ki',default=datetime.now(),blank=True)
	def __unicode__(self):
		return self.IDworking
class Internship_course(models.Model):
	IDinternship = models.AutoField(primary_key = True)
	timestart = models.DateTimeField('Ngay bat dau',default=datetime.now(),blank=True)
	timeend = models.DateTimeField('Ngay ket thuc',default=datetime.now(),blank=True)
	def __unicode__(self):
		return self.IDinternship
class Internship_application_form(models.Model):
	IDinternappform = models.AutoField(primary_key = True)
	IDstudent= models.IntegerField(default=0)
	IDinternship = models.ForeignKey(Internship_course)
	def __unicode_(self):
		return self.IDinternappform
class Managerial_staff(models.Model):
	IDinternship = models.ForeignKey(Internship_course)
	IDstaff = models.ForeignKey(Staff)
	def __unicode__(self):
		return self.IDinternship
class Discussion_topic(models.Model):
	IDdistopic = models.AutoField(primary_key = True)
	IDperson = models.ForeignKey(Person)
	name = models.CharField(max_length=300)
	poststatus = models.TextField(max_length=300)
	def __unicode__(self):
		return self.IDdistopic
class Discussion(models.Model):
	IDdiscussion = models.AutoField(primary_key = True)
	IDperson = models.ForeignKey(Person)
	IDdistopic = models.ForeignKey(Discussion_topic)
	content = models.TextField()
	timestamp = models.DateTimeField('Ngay dang',default=datetime.now(),blank=True)
	def __unicode__(self):
		return self.IDdiscussion
class Discussion_attachment_file(models.Model):
	IDdisattfile = models.AutoField(primary_key = True)
	IDdiscussion = models.ForeignKey(Discussion)
	name = models.CharField(max_length=300)
	link = models.CharField(max_length=300)
	def __unicode__(self):
		return self.IDdisattfile
class Article_category(models.Model):
	IDarticate = models.AutoField(primary_key = True)
	name = models.CharField(max_length=300)
	def __unicode__(self):
        	return self.name
class Article(models.Model):
	IDarticle = models.AutoField(primary_key = True)
	IDarticate = models.ForeignKey(Article_category)
	title = models.CharField(max_length=300)
	image = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/no-img.jpg')
	shortdescription = models.TextField(max_length=300)
	content = models.TextField()
	hightlightstatus= models.IntegerField(default=0)
	poststatus= models.IntegerField(default=0)
	timestamp  = models.DateTimeField('Ngay dang',default=datetime.now(),blank=True)
	def __unicode__(self):
        	return self.title
class Article_attachment_file(models.Model):
	IDartattfile = models.AutoField(primary_key = True)
	IDarticle = models.ForeignKey(Article)
	name = models.CharField(max_length=300)
	link = models.CharField(max_length=300)
	def __unicode__(self):
		return self.name
class Topic_category(models.Model):
	IDtocate = models.AutoField(primary_key = True)
	name = models.CharField(max_length=300)	
	def __unicode__(self):
		return self.name
class Local_topic(models.Model):
	IDlocaltopic = models.AutoField(primary_key = True)
	IDlocalcate = models.ForeignKey(Topic_category)
	title = models.CharField(max_length=300)
	numberofpages= models.IntegerField(default=0)
	publishingtime  = models.DateTimeField('Ngay dang',default=datetime.now(),blank=True)
	publicstatus= models.IntegerField(default=0)
	def __unicode__(self):
		return self.title
class Local_topic_attachment_file(models.Model):
	IDlocaltoattfile = models.AutoField(primary_key = True)
	IDlocaltopic = models.ForeignKey(Local_topic)
	name = models.CharField(max_length=300)
	link = models.CharField(max_length=300)
	def __unicode__(self):
		return self.name
class Document_category(models.Model):
	IDdoccate = models.AutoField(primary_key = True)
	name = models.CharField(max_length=300)
	def __unicode__(self):
		return self.name
class Scientific_documentation(models.Model):
	IDscientdoc = models.AutoField(primary_key = True)
	IDdoccate = models.ForeignKey(Document_category)
	title = models.CharField(max_length=300)
	numberofpages= models.IntegerField(default=0)
	publishingtime  = models.DateTimeField('Ngay dang',default=datetime.now(),blank=True)
	publicstatus= models.IntegerField(default=0)
	def __unicode__(self):
		return self.title
class Author(models.Model):
	IDauthor = models.AutoField(primary_key = True)
	name = models.CharField(max_length=300)
	email = models.CharField(max_length=300)
	def __unicode__(self):
		return self.name
class Auhavelocal(models.Model):
	IDauthor = models.ForeignKey(Author)
	IDlocaltopic = models.ForeignKey(Local_topic)
	def __unicode__(self):
		return self.IDauthor
class Auhavescientdoc(models.Model):
	IDauthor = models.ForeignKey(Author)
	IDscientdoc = models.ForeignKey(Scientific_documentation)
	def __unicode__(self):
		return self.IDauthor

