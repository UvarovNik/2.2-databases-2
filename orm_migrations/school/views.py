from django.views.generic import ListView

from .models import Student


class StudentsListView(ListView):
    model = Student
    queryset = Student.objects.all().order_by('group').prefetch_related('teachers')
    template_name = 'school/students_list.html'


students_list = StudentsListView.as_view()
