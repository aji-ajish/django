from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging

# Create your views here.

posts = [
    {
        "id": 1,
        "title": "post 1",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla consectetur tortor vel magna tincidunt tempus. Maecenas eget maximus eros. Vivamus id nisl lacus. Donec et risus turpis. In nec efficitur purus, ac faucibus nulla. Aenean nec malesuada velit. Quisque ac mauris ac turpis semper interdum. ",
    },
    {
        "id": 2,
        "title": "post 2",
        "content": "Sed et lorem et lacus consequat suscipit. Vestibulum dapibus sapien et eros aliquam, a dictum leo vehicula. Aliquam consequat turpis vitae lectus tristique, quis efficitur orci fermentum. Phasellus a ligula pulvinar, blandit eros at, euismod nisl. Nam pharetra urna id purus volutpat, a feugiat magna convallis. ",
    },
    {
        "id": 3,
        "title": "post 3",
        "content": "Donec quis nisi vitae metus sodales fermentum ac eu eros. Nulla facilisi. Fusce bibendum nisl et varius vehicula. Duis volutpat convallis justo nec pharetra. Cras convallis dolor vitae hendrerit mollis. Curabitur ultrices odio vitae sapien fringilla rhoncus. Ut feugiat condimentum ligula, vel faucibus neque sollicitudin sed.",
    },
    {
        "id": 4,
        "title": "post 4",
        "content": "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nam eget mauris hendrerit, lobortis urna id, sollicitudin est.",
    },
]


def index(request):
    blog_title = "Latest Posts"
    return render(request, "index.html", {"blog_title": blog_title, "posts": posts})


def detail(request, post_id):
    post=next((item for item in posts if item["id"] == int(post_id)), None)
    # logger=logging.getLogger('testing')
    # logger.debug(f'post var is {post}')
    return render(request, "detail.html", {"post": post})


def old_url_redirect(request):
    return redirect(reverse("blog:new_page_url"))


def new_url_view(request):
    return HttpResponse("<h2>New URL</h2")
