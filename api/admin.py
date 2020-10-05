from cms.extensions import PageExtensionAdmin
from django.contrib import admin

from .models import PageDetailExtension, Post, Donation, Volunteer, Testimonial, Video, AllowedDomain, \
    BeautifulGoogleSearch, BeautifulGoogleResult
from tracker.models import Story, Task, Developer, SpentTime

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




