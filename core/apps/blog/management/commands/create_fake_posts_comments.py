from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.blog.models import Post, Comment
from faker import Faker
import random
from django.utils import timezone

fake = Faker()

class Command(BaseCommand):
    help = 'Create fake blog posts and comments for testing purposes'

    def add_arguments(self, parser):
        parser.add_argument(
            '--comments_count', 
            type=int, 
            default=5,
            help='Number of fake comments per post to create')


    def handle(self, *args, **options):
        comments_count = options['comments_count']

        users = User.objects.all()
        posts = Post.objects.all()

        if not posts.exists():
            self.stdout.write(self.style.ERROR('No posts found. Please create posts before adding comments.'))
            return
        
        if not users.exists():
            self.stdout.write(self.style.ERROR('No users found. Please create users before adding posts and comments.'))
            return

        comments = []
        for post in posts:
            for _ in range(comments_count):
                comments.append(Comment(
                    post=post,
                    author=random.choice(users),
                    text=fake.paragraph(nb_sentences=3),
                ))

        Comment.objects.bulk_create(comments)
        self.stdout.write(self.style.SUCCESS(f'Successfully created {comments_count * posts.count()} fake comments.'))