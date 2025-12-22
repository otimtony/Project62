from django.core.management.base import BaseCommand
from apps.products.models import Category
import random
from faker import Faker

faker = Faker()

class Command(BaseCommand):
    help = 'Populate the database with product categories'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count', 
            type=int, 
            default=10,
            help='Number of product categories to create')
        
    def handle(self, *args, **options):
        count = options['count']
        categories = []

        for _ in range(count):
            categories.append(Category(
                name=faker.unique.word().title(),
                description=faker.sentence(nb_words=10)
            ))

        Category.objects.bulk_create(categories)
        self.stdout.write(self.style.SUCCESS(f'Successfully created {count} product categories.'))