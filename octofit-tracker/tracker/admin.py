from django.contrib import admin
from .models import Activity


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
	list_display = ('user', 'activity_type', 'duration_minutes', 'distance_km', 'calories', 'timestamp')
	list_filter = ('activity_type', 'timestamp')
	search_fields = ('user__username', 'activity_type')
