from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post, AboutUs
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ContactForm

# Create your views here.
# static demo data
# posts = [
#     {
#         "id": 1,
#         "title": "post 1",
#         "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla consectetur tortor vel magna tincidunt tempus. Maecenas eget maximus eros. Vivamus id nisl lacus. Donec et risus turpis. In nec efficitur purus, ac faucibus nulla. Aenean nec malesuada velit. Quisque ac mauris ac turpis semper interdum. ",
#     },
#     {
#         "id": 2,
#         "title": "post 2",
#         "content": "Sed et lorem et lacus consequat suscipit. Vestibulum dapibus sapien et eros aliquam, a dictum leo vehicula. Aliquam consequat turpis vitae lectus tristique, quis efficitur orci fermentum. Phasellus a ligula pulvinar, blandit eros at, euismod nisl. Nam pharetra urna id purus volutpat, a feugiat magna convallis. ",
#     },
#     {
#         "id": 3,
#         "title": "post 3",
#         "content": "Donec quis nisi vitae metus sodales fermentum ac eu eros. Nulla facilisi. Fusce bibendum nisl et varius vehicula. Duis volutpat convallis justo nec pharetra. Cras convallis dolor vitae hendrerit mollis. Curabitur ultrices odio vitae sapien fringilla rhoncus. Ut feugiat condimentum ligula, vel faucibus neque sollicitudin sed.",
#     },
#     {
#         "id": 4,
#         "title": "post 4",
#         "content": "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nam eget mauris hendrerit, lobortis urna id, sollicitudin est.",
#     },
# ]


def index(request):
    blog_title = "Latest Posts"
    all_posts = Post.objects.all()
    # paginate
    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request, "index.html", {"blog_title": blog_title, "page_obj": page_obj}
    )


def detail(request, slug):
    # getting static data
    # post = next((item for item in posts if item["id"] == int(post_id)), None)
    try:
        # getting data from model by post is
        post = Post.objects.get(slug=slug)
        related_posts = Post.objects.filter(category=post.category).exclude(pk=post.id)

    except Post.DoesNotExist:
        raise Http404("Post Does not exist!")
    # logger=logging.getLogger('testing')
    # logger.debug(f'post var is {post}')
    return render(
        request, "detail.html", {"post": post, "related_posts": related_posts}
    )


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST,request.FILES)
        # name = request.POST.get("name")
        # email = request.POST.get("email")
        # message = request.POST.get("message")
        logger = logging.getLogger("testing")
        if form.is_valid():
            form.save()
            # logger.debug(f"post data is {name} {email} {message}")
            # data save in db
            success_message = "Your Email has been sent!"
            return render(
                request,
                "contact.html",
                {"form": form, "success_message": success_message},
            )
        else:
            logger.debug(f"form validation failed")
        return render(
            request,
            "contact.html",
            # {"form": form, "name": name, "email": email, "message": message},
        )
    return render(request, "contact.html")


def about(request):
    about_contetn = AboutUs.objects.first().content
    return render(request, "about.html", {"about_contetn": about_contetn})


# def old_url_redirect(request):
#     return redirect(reverse("blog:new_page_url"))


# def new_url_view(request):
#     return HttpResponse("<h2>New URL</h2")
