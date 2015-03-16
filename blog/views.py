from django.shortcuts import render, render_to_response
from django.views import generic

from blog.models import Posts

class MainView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Posts.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    template_name = 'blog/detail.html'
    model = Posts
    context_object_name = 'post'

'''def detail(request, question_id):
    post = Posts.objects.get(pk=question_id)
    return render(request, 'blog/detail.html', {'post': post})'''

def contact(request):
    return render(request, 'blog/contact.html')

