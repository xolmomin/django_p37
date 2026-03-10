from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path
from django.utils import timezone
from django.utils.timezone import now

from apps.models import Topic, News, Image


@admin.register(Topic)
class TopicModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'custom_name', 'count_chars', 'is_active')
    search_fields = ('name',)
    actions = ['activate_topics']

    @admin.display(description='boshqacha nom', ordering='name')
    def custom_name(self, obj: Topic):
        return obj.name

    @admin.display(description='Belgilar soni')
    def count_chars(self, obj: Topic):
        return len(obj.name)

    @admin.action(description='Aktivlashtirish')
    def activate_topics(self, request, queryset):
        queryset.update(is_active=True)


# @admin.register(Image)
# class ImageModelAdmin(admin.ModelAdmin):
#     pass

class ImageStackedInline(admin.StackedInline):
    model = Image
    min_num = 1
    extra = 2
    max_num = 3
    can_delete = False


@admin.register(News)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'custom_created_at', 'custom_topics', 'image_count')
    inlines = [ImageStackedInline]

    @admin.display(description='Sanasi')
    def custom_created_at(self, obj: News):
        local_time = timezone.localtime(obj.created_at)
        current_time = timezone.localtime(timezone.now())
        return f"{local_time.strftime('%H:%M:%S')} ({current_time.strftime('%H:%M:%S')})"

    @admin.display(description='Rasmlar soni')
    def image_count(self, obj: News):
        return obj.images.count()

    @admin.display(description='boshqacha nom')
    def custom_topics(self, obj: News):
        return ', '.join(obj.topics.values_list('name', flat=True))
        # text = ''
        # for topic in obj.topics.all():
        #     text += f"{topic.name},"
        # return text

# from apps.models import Category, Product
#
#
# @admin.register(Category)
# class CategoryModelAdmin(admin.ModelAdmin):
#     list_display = 'name', 'is_active'
#     change_list_template = "apps/category_changelist.html"
#
#     def get_urls(self):
#         urls = super().get_urls()
#         my_urls = [
#             path('immortal/', self.set_immortal),
#             path('mortal/', self.set_mortal),
#         ]
#         return my_urls + urls
#
#     def set_immortal(self, request):
#         self.model.objects.all().update(is_active=True)
#         self.message_user(request, "hammasi OK")
#         return HttpResponseRedirect("../")
#
#     def set_mortal(self, request):
#         self.model.objects.all().update(is_active=False)
#         self.message_user(request, "Hammasi atmen")
#         return HttpResponseRedirect("../")
#
#
# @admin.register(Product)
# class ProductModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'price']
