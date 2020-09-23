from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Type the help text here'

    def handle(self, *args, **options):
        # Add yout logic here
        # This is the task that will be run
        print("using print()")
        self.stdout.write('custom command is running ....')