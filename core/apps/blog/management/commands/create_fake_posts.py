from django.core.management.base import BaseCommand
from apps.accounts.models import User
from apps.blog.models import Post
from faker import Faker
import random
from django.utils import timezone

fake = Faker()

class Command(BaseCommand):
    help = 'Create fake blog posts for testing purposes'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count', 
            type=int, 
            default=10,
            help='Number of fake posts to create')
        parser.add_argument(
            "--published",
            action="store_true",
            help="Create only published posts",
        )

    def handle(self, *args, **options):
        count = options['count']
        published_only = options['published']

        users = User.objects.all()
        if not users.exists():
            self.stdout.write(self.style.ERROR('No users found. Please create users before adding posts.'))
            return
        
        posts = []
        for _ in range(count):
            posts.append(Post(
                added_by=random.choice(users),
                title=fake.sentence(nb_words=6),
                content=fake.paragraph(nb_sentences=10),
            ))

        Post.objects.bulk_create(posts)
        self.stdout.write(self.style.SUCCESS(f'Successfully created {count} fake posts.'))

