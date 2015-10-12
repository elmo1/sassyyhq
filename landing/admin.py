from django.contrib import admin

from landing.models import Signup

class StoryAdmin(admin.ModelAdmin):
	list_display = ('email', 'created_at',)




admin.site.register(Signup, StoryAdmin)