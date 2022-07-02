from django.shortcuts import render
from .models import Student, Article

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_articles = Article.objects.all().count()
    
   
    # The 'all()' is implied by default.
    num_students = Student.objects.count()

    context = {
        'num_articles': num_articles,
        
        'num_students': num_students,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic
class ArticleListView(generic.ListView):
    model = Article
    context_object_name = 'article_list'   # your own name for the list as a template variable
    queryset = Article.objects.all()
#queryset = Article.objects.filter(headline__icontains='learning')[:5] # Get 5 books containing the title war
    template_name = 'students/article_list.html'  # Specify your own template name/location
 
    
from django.shortcuts import Http404 
class ArticleDetailView(generic.DetailView):
    model = Article
    
    def article_detail_view(request, primary_key):
        try:
            article = Article.objects.get(pk=primary_key)
        except Article.DoesNotExist:
            raise Http404('Book does not exist')

        return render(request, 'home/article_detail.html', context={'article': article})
    



        
        