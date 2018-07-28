from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
import datetime
from .models import Project
# Create your tests here.
def create_project(project_name,days):
    time=timezone.now()+datetime.timedelta(days=days)
    return Project.objects.create(project_name=project_name,creation_date=time)

class ProjectIndexViewTests(TestCase):
    def test_no_project(self):
        response=self.client.get(reverse('reqs:index'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"No projects available")
        self.assertQuerysetEqual(response.context['project_list'],[])

    def test_past_project(self):
        create_project(project_name="TestProject",days=-30)
        response=self.client.get(reverse('reqs:index'))
        self.assertQuerysetEqual(response.context['project_list'],['<Project: TestProject>'])
    
    def test_future_project(self):
        create_project(project_name="TestProject",days=30)
        response=self.client.get(reverse('reqs:index'))
        self.assertContains(response,"No projects available")
        self.assertQuerysetEqual(response.context['project_list'],[])
