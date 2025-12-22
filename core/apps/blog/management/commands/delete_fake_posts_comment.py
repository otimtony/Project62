from django.core.management.base import BaseCommand
from apps.blog.models import Comment

class Command(BaseCommand):
    help = 'Delete all fake posts and comments from the database'

    def handle(self, *args, **options):
        deleted_comments, _ = Comment.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'Successfully deleted {deleted_comments} comments.'))