# other imports
import blog.views

urlpatterns = [
    # other patterns
    path("", blog.views.index)
    path("post/<slug>/", blog.views.post_detail, name="blog-post-detail")
]