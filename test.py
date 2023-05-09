class NewsUpdateView(UpdateView):
    model = News
    fields = ('title', 'body', 'image', 'category', 'status',)
    template_name = 'crud/news_edit.html'

urlpatterns = [
    path("news/<slug:news>",  news_list, name="all_news_list"),
]

def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {
        "news":news
    }

    return render(request, "news/news_detail.html", context)



from django.urls import reverse

class News(models.Model):
    ...
    def get_absolute_url(self):
        return reverse("news_detail_page", args=[self.slug])

# from .models import News

# def latest_news(request):
#     latest_news = News.published.all().order_by("-publish_time")[:10]
#     context = {
#         "latest_news": latest_news
#     }

#     return context


# class HomePageView(ListView):
#     model = News
#     template_name = 'news/home.html'
#     context_object_name = 'news'

#     def get_context_data(self, ** kwargs):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = Category.objects.all()
#         context['news_list'] = News.published.all().order_by('-publish_time')[:15]
#         return context
    

# class SubscriptionForm(forms.Form):
#     subject = forms.CharField(max_length=100)
#     message = forms.CharField(max_length=150)
#     email = forms.EmailField()

# def homePageView(request):
#     news = News.published.all()
#     categories = Category.objects.all()
#     context = {
#         "news": news,   
#         "categories": categories
#     }

#     return render(request, 'news/index.html', context)



# class PublishedManager(model.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(status=News.Status.Published)
    

# class News(model.Model):


#     objects = models.Manager() # Bu default manager hisoblandi. 
#     published = PublishedManager()

# # urlpatterns = [
# #     path("blog/",  BLogListVIew.as_view(), name="blog_detail"),
# # ]

# # from django.views.generic import ListView, DetailView

# # class BLogDetailVIew(DetailView):
# #     model = Blog
# #     template_name = "blog_detail.html"

#     # Klaslar contextdagi nomni avtomatik objects_list qilib oladi.


# News.published.all()
# # from django.shortcuts import get_object_or_404


# # def blogdetailview(request, id):
# #     # try:
# #     #     blog = Blog.objects.get(id=id)
# #     #     context = {
# #     #         "blog":blog
# #     #     }
# #     # except Blog.DoesNotExist:
# #     #     raise Http404("No blog found")
# #     # Yuqoridagi hammasini o'rniga
# #     blog = get_object_or_404(Blog, id=id)
# #     context = {
# #             "blog":blog
# #         }
    
# #     return render(request, "blog_detail.html", context=context) 

# # news1=News(title="news-title1", slug="news1-title", body="news1-body", category=category1)
# # news1.save()
# # News.objects.all()
# # news2=News.objects.create(title="news-title3", slug="news-title3", body="news-body3", category=category1)
# # news2.save()
# # News.objects.create(title="news-title4", slug="news-title4", body="news-body4", category=category1)
# # news2.title = "bu 2-yangilik sarlahvasi"
# # news2.save()
# # News.objects.all()
# # all_news = News.objects.all()
# # News.objects.filter(publish_time__year=2022)
# # News.objects.filter(title='bu 2-yangilik sarlahvasi')
# # News.objects.exclude(title="bu 2-yangilik sarlahvasi")
# # News.objects.all().order_by('title')
# # news = News.objects.get(id=3)
# # news.delete()
# # News.objects.all()      