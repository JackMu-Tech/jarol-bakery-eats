from django.contrib import admin
from .models import TeamMember, CompanyInfo, Testimonial

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'image_tag', 'created_at')
    search_fields = ('name', 'position')
    list_filter = ('created_at',)
    readonly_fields = ('created_at', 'updated_at', 'image_tag')
    list_per_page = 20
    date_hierarchy = 'created_at'

    def image_tag(self, obj):
        return '<img src="{}" style="max-width:100px; max-height:100px;" />'.format(obj.image.url)
    image_tag.short_description = 'Image Preview'
    image_tag.allow_tags = True

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'email', 'created_at')
    search_fields = ('name', 'address', 'phone', 'email')
    list_filter = ('created_at',)
    readonly_fields = ('created_at', 'updated_at')
    list_per_page = 20
    date_hierarchy = 'created_at'

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'created_at')
    search_fields = ('author_name',)
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)
    list_per_page = 20
    date_hierarchy = 'created_at'
