from django.db import models
from django.contrib.auth.models import User

# User table already exists created by django

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

# We define the above tuples to have choices.
# The first value will be stored in DB and the second value is the display name for users.


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    # related_name is used for a reverse relation, suppose user object is current_user we
    # can use current_user.blog_posts.all() to get all posts by a user
    updated_on = models.DateTimeField(auto_now=True)  # will store datetime.now() when .save() is called
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)  # will store datetime.now() when object is created
    status = models.IntegerField(choices=STATUS, default=0)  # choices always takes tuples

    class Meta:
        ordering = ['-created_on']
        # The posts will be sorted in descending based on creation time('-' sign indicates descending order)

    def __str__(self):
        return self.title

