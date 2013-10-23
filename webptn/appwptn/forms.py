from django import forms
from models import Person,Faculty,Article_category,Student,Article,Staff,Seminar_registration_form,Desk,Cpu_screen,Working_placement,Internship_course, Internship_application_form, Managerial_staff, Discussion_topic,Discussion,Discussion_attachment_file,Article_attachment_file, Topic_category, Local_topic, Local_topic_attachment_file, Document_category, Scientific_documentation, Author, Auhavelocal, Auhavescientdoc
class PersonForm(forms.ModelForm):	
	class Meta:
		model = Person
class FacultyForm(forms.ModelForm):
	class Meta:
		model = Faculty
class Article_categoryForm(forms.ModelForm):
	class Meta:
		model = Article_category
class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
class StaffForm(forms.ModelForm):
	class Meta:
		model = Staff
class Seminar_registration_formForm(forms.ModelForm):
	class Meta:
		model = Seminar_registration_form
class DeskForm(forms.ModelForm):
	class Meta:
		model = Desk
class Cpu_screenForm(forms.ModelForm):
	class Meta:
		model = Cpu_screen
class Working_placementForm(forms.ModelForm):
	class Meta:
		model = Working_placement
class Internship_courseForm(forms.ModelForm):
	class Meta:
		model = Internship_course
class Internship_application_formForm(forms.ModelForm):
	class Meta:
		model = Internship_application_form
class Managerial_staffForm(forms.ModelForm):
	class Meta:
		model = Managerial_staff
class Discussion_topicForm(forms.ModelForm):
	class Meta:
		model = Discussion_topic
class DiscussionForm(forms.ModelForm):
	class Meta:
		model = Discussion
class Discussion_attachment_fileForm(forms.ModelForm):
	class Meta:
		model = Discussion_attachment_file
class Article_attachment_fileForm(forms.ModelForm):
	class Meta:
		model = Article_attachment_file
class Topic_categoryForm(forms.ModelForm):
	class Meta:
		model = Topic_category
class Local_topicForm(forms.ModelForm):
	class Meta:
		model = Local_topic
class Local_topic_attachment_fileForm(forms.ModelForm):
	class Meta:
		model = Local_topic_attachment_file
class Document_categoryForm(forms.ModelForm):
	class Meta:
		model = Document_category
class Scientific_documentationForm(forms.ModelForm):
	class Meta:
		model = Scientific_documentation
class AuthorForm(forms.ModelForm):
	class Meta:
		model = Author
class AuhavelocalForm(forms.ModelForm):
	class Meta:
		model = Auhavelocal
class AuhavescientdocForm(forms.ModelForm):
	class Meta:
		model = Auhavescientdoc
class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100)
	message = forms.CharField()
	sender = forms.EmailField()
	cc_myself = forms.BooleanField(required=False)
