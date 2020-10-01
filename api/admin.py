from cms.extensions import PageExtensionAdmin
from django.contrib import admin

from .models import PageDetailExtension, Post, Donation, Volunteer, Testimonial, Video


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


admin.site.register(PageDetailExtension, PageDetailExtensionAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Donation, DonationAdmin)
admin.site.register(Post, PostAdmin)
