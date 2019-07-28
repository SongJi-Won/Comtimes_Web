from django.db import models

# Create your models here.

# class User(models.Model):
#     user_number = models.IntegerField(primary_key=True)
#     user_id = models.CharField(max_length=20)
#     password = models.CharField(max_length=20)
#     name = models.CharField(max_length=10)
#     email = models.CharField(max_length=20)
#     is_reporter = models.BooleanField(default= False)
#
#     def __str__(self):
#         return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    # author = models.ForeignKey('User', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]


def article_img_path(instance, filename):
    extension = filename.split('.')[-1]
    # return 'article/{}/{}.{}'.format(instance.post.id, instance.id, extension)
    return 'article_image/%s/%s/%s' % (instance.post.id, instance.id, extension)

class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_images')
    image = models.ImageField(upload_to=article_img_path)
    explanation = models.CharField(max_length=100)

    def __str__(self):
        return self.explanation


