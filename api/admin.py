from django.utils.html import format_html

from cms.extensions import PageExtensionAdmin
from django.contrib import admin

from .models import PageDetailExtension, Post, Donation, Volunteer, Testimonial, Video, AllowedDomain, \
    BeautifulGoogleSearch, BeautifulGoogleResult, BeautifulGumtreeResult, BeautifulGumtreeSearch, GumtreeProvince, \
    GumtreeCategory, GumtreeCategoryLabel, BeautifulGumtreeQuery, GumtreeLocation
from tracker.models import Story, Task, Developer, SpentTime
from .models import Gallery as BlogGallery


class PageDetailExtensionAdmin(PageExtensionAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    pass


class DonationAdmin(admin.ModelAdmin):
    pass


class VolunteerAdmin(admin.ModelAdmin):
    pass


class TestimonialAdmin(admin.ModelAdmin):
    pass


class VideoAdmin(admin.ModelAdmin):
    pass


class StoryAdmin(admin.ModelAdmin):
    pass


class TaskAdmin(admin.ModelAdmin):
    pass


class DeveloperAdmin(admin.ModelAdmin):
    pass


class SpentTimeAdmin(admin.ModelAdmin):
    pass


class AllowedDomainAdmin(admin.ModelAdmin):
    pass


class BeautifulGoogleSearchAdmin(admin.ModelAdmin):
    pass


class BeautifulGoogleResultAdmin(admin.ModelAdmin):
    pass


class BeautifulGumtreeSearchAdmin(admin.ModelAdmin):

    list_display = ("term", "date_created")


class BeautifulGumtreeResultAdmin(admin.ModelAdmin):

    list_display = ("title", "query", "location", "admin_image", "price")


class BlogGalleryAdmin(admin.ModelAdmin):

    fields = ["blog_post", "image", "caption", "active"]
    list_display = ("blog_post", "image", "active")
    pass


class GumtreeProvinceAdmin(admin.ModelAdmin):

    pass


class GumtreeCategoryAdmin(admin.ModelAdmin):

    pass


class GumtreeCategoryLabelAdmin(admin.ModelAdmin):

    pass


class BeautifulGumtreeQueryAdmin(admin.ModelAdmin):
    list_display = ( "term", "running")
    pass

class GumtreeLocationAdmin(admin.ModelAdmin):

    pass

admin.site.register(PageDetailExtension, PageDetailExtensionAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Donation, DonationAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Story, StoryAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Developer, DeveloperAdmin)
admin.site.register(SpentTime, SpentTimeAdmin)
admin.site.register(AllowedDomain, AllowedDomainAdmin)
admin.site.register(BeautifulGoogleSearch, BeautifulGoogleSearchAdmin)
admin.site.register(BeautifulGoogleResult, BeautifulGoogleResultAdmin)
admin.site.register(BeautifulGumtreeSearch, BeautifulGumtreeSearchAdmin)
admin.site.register(BeautifulGumtreeResult, BeautifulGumtreeResultAdmin)
admin.site.register(BlogGallery, BlogGalleryAdmin)

admin.site.register(GumtreeProvince, GumtreeProvinceAdmin)
admin.site.register(GumtreeCategory, GumtreeCategoryAdmin)
admin.site.register(GumtreeCategoryLabel, GumtreeCategoryLabelAdmin)
admin.site.register(BeautifulGumtreeQuery, BeautifulGumtreeQueryAdmin)
admin.site.register(GumtreeLocation, GumtreeLocationAdmin)
