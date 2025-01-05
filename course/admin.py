from django.contrib import admin
from unfold.admin import ModelAdmin

from course.models import Course

# Register your models here.
# Course setup for the super user admin interface


class CourseModelAdmin(ModelAdmin):
    # Display fields in changeform in compressed mode
    compressed_fields = True  # Default: False

    # Warn before leaving unsaved changes in changeform
    warn_unsaved_form = True  # Default: False

    # Display submit button in filters
    list_filter_submit = False

    # Display changelist in fullwidth
    list_fullwidth = False

    # Set to False, to enable filter as "sidebar"
    list_filter_sheet = True

    # Position horizontal scrollbar in changelist at the top
    list_horizontal_scrollbar_top = False

    # Dsable select all action in changelist
    list_disable_select_all = False

    list_display = [
        "unit",
        "name",
        "created_at",
        "modified_at",
    ]


admin.site.register(Course, CourseModelAdmin)
