from django.core.management.base import BaseCommand
from apps.accounts.models import User
import random
from faker import Faker

faker = Faker()

class Command(BaseCommand):
    help = 'Update existing users with new random data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=10,
            help='Number of users to update'
        )

    def handle(self, *args, **options):
        count = options['count']
        users = User.objects.all()

        if not users.exists():
            self.stdout.write(self.style.ERROR('No users found to update.'))
            return
        users_to_update = random.sample(list(users), min(count, users.count()))
        for user in users_to_update:
            user.first_name = faker.first_name()
            user.last_name = faker.last_name()
            user.email = faker.unique.email()
            user.role = random.choice(['ADMIN', 'MANAGER', 'USER'])
            user.set_password('newpassword123')  # Update to a new default password
            user.save()       

        self.stdout.write(self.style.SUCCESS(f'Successfully updated {len(users_to_update)} users')) 