from django.shortcuts import render, render_to_response
from django.views.generic import View, TemplateView, ListView, DetailView
from django.http import HttpResponse
from django.db.models import Prefetch

from app.models import CV
from app.models import Project
from app.models import Skill
from app.models import SkillGroup

# Create your views here.
# Ref: https://stackoverflow.com/questions/22312873/django-views-py-version-of-sql-join-with-multi-table-query
def index(request):
    project_list = Project.objects.order_by('date_start').reverse().filter(person__id=1)
    skillgroup_list = SkillGroup.objects.filter(skill__person_id=1)
    
    d = {'project_list': project_list,'skillgroup_list': skillgroup_list}
    
    return render_to_response('index.html', context=d)

def cbv(request):
    return render(request, 'cbv.html')

class SkillListView(ListView):
    model = Skill
    template_name = 'skill_list.html'

class CBView(View):
    def get(self, request): 
        return HttpResponse('CBVs are cool')

class IndexView(TemplateView):
    template_name="index.html"
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context, then populate the context object with data
        context = super().get_context_data(**kwargs)
        context['project_list'] = Project.objects.order_by('date_start').reverse().filter(person_id=1).filter(cv__id=1)
        #context['skillgroup_list'] = SkillGroup.objects.filter(skill__person_id=1)

        #The Prefetch object is needed here in order to filter the child rows (the prefetch_related() method does not support this)
        context['skillgroup_list'] = SkillGroup.objects.prefetch_related(Prefetch('skill_set',
            queryset=Skill.objects.filter(person_id=1).filter(cv__id=1)))
        
        return context
    
    
class IndexViewExample(TemplateView):
    template_name='cbv.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme']='basic injection'
        return context

    
class SkillGroupListView(ListView):
    model = SkillGroup
    template_name='skillgroup_list.html'
    #The ListView that this view is extend will return a dictionary with the name <model>_list in lowercase, 
    #In this case "skillgroup_list"
    #The name of this dict can be changed by adding the following line to the class:
    #context_object_name='skillgroups'
    
class SkillGroupDetailView(DetailView):
    model = SkillGroup
    template_name='skillgroup_detail.html'
   
        