from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.views.generic import TemplateView

from blogzine.blog_post.models import  CreatePost


class HomeView(TemplateView):
    template_name = 'common/index.html'


class AboutView(TemplateView):
    template_name = 'common/about-us.html'


class DashboardView(LoginRequiredMixin , TemplateView):
    template_name = 'common/dashboard.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Filter posts by the currently logged-in user
        user_posts = CreatePost.objects.filter(author=self.request.user)

        paginator = Paginator(user_posts, 10)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['page_obj'] = page_obj

        return context