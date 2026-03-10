from django.db.models import CharField, Model, ForeignKey, CASCADE, ManyToManyField, ImageField
from django.db.models.fields import IntegerField, TextField, BooleanField, DateTimeField


class Topic(Model):
    name = CharField(verbose_name='Nomi', max_length=255)
    is_active = BooleanField(default=False)

    def __str__(self):
        return self.name


class News(Model):
    title = CharField(max_length=255)
    topics = ManyToManyField('apps.Topic', blank=True)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'
        unique_together = (
            ('title', 'topics'),
        )


class Image(Model):
    image = ImageField(upload_to='news/%Y/%m/d')
    news = ForeignKey('apps.News', CASCADE, related_name='images')
