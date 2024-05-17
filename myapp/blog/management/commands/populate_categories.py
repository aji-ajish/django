from typing import Any
from blog.models import Categories
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "This command insert categories data"

    def handle(self, *args: Any, **options: Any):
        # Delete existing data
        Categories.objects.all().delete()
        
        categories = ['Sports', 'Technology', 'Science', 'Art', 'Food']
        for category_name in categories:
            Categories.objects.create(name=category_name)

        self.stdout.write(self.style.SUCCESS("Completed inserting successfully"))
