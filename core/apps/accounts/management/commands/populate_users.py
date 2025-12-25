from django.core.management.base import BaseCommand
from apps.accounts.models import User
from faker import Faker
import random

faker = Faker()

class Command(BaseCommand):
    help = 'Populate the database with users'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=10,
            help='Number of users to create'
        )

    def handle(self, *args, **options):
        count = options['count']
        users = []

        for _ in range(count):
            email = faker.unique.email()
            role = random.choice(['ADMIN', 'MANAGER', 'USER'])
            user = User(
                email=email,
                role=role
            )
            user.set_password('password123')  # Set a default password
            users.append(user)

        User.objects.bulk_create(users)
        self.stdout.write(self.style.SUCCESS(f'Successfully created {count} users'))