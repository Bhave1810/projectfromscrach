from django.contrib import admin
from .models import PropertyCategory, Property, PropertyImage, PropertyVideo, Favorite


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1


class PropertyVideoInline(admin.TabularInline):
    model = PropertyVideo
    extra = 1


@admin.register(PropertyCategory)
class PropertyCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'city', 'price', 'status', 'is_featured')
    list_filter = ('status', 'is_featured', 'city', 'category')
    search_fields = ('title', 'city', 'location')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PropertyImageInline, PropertyVideoInline]


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'supabase_user_id', 'property', 'created_at')
