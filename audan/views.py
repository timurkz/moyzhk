from django.shortcuts import render
from .models import City, Building, Post
from django.http import JsonResponse
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
    
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

cities = City.objects.all()

# Create your views here.
def index(request):
    return render(request, "audan/index.html", {
        "cities": City.objects.all(),
        "buildings": Building.objects.all()
    })
    

class PostListView(ListView):
    model = Post
    template_name = 'audan/building.html'
    context_object_name = 'posts'
    ordering = ['-date_created']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['zhk','title','body','price','phone_number','image']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['zhk','title','body','price','phone_number','image']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def post(request):
    post = request.GET.get()

def search_building(request):
    building = request.GET.get('zhk')
    payload = []

    if building:
        list_buildings = Building.objects.filter(name__icontains=building)

        for building in list_buildings:
            payload.append(building.name)
    
    return JsonResponse({'status':200, 'data' : payload})

def building(request):
    building = request.GET.get('zhk')
    if building:
        building_id = Building.objects.filter(name__iexact=building).first()
        if building_id:
            return render(request, "audan/building.html", {
                "posts": building_id.posts.all(),
                "building": building_id
            })

        else:
            return HttpResponse("<legend>Мы к Вам скоро придем :)</legend>")
