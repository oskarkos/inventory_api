from django.core.management.base import BaseCommand
from faker import Faker


class Command(BaseCommand):
    help = "Command Information"

    def handle(self, *args, **kwargs):
        
        fake = Faker("nl_NL")

        print(fake.name())