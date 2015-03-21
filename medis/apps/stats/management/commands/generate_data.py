from datetime import date

from django.core.management import BaseCommand
from faker import Factory
from mixer.backend.django import Mixer

from medis.apps.stats.models import Doctor, Ticket


class Command(BaseCommand):
    help = 'Create initial test data'

    def _create_doctors(self, mixer):
        mixer.cycle(10).blend(
            Doctor,
            speciality=mixer.SELECT,
            name=mixer.FAKE
        )

    def _create_tickets(self, mixer):
        fake = Factory.create()
        for i in xrange(60):
            mixer.blend(
                Ticket,
                doctor=mixer.SELECT,
                patient=mixer.FAKE,
                datetime=fake.date_time_between(
                    start_date=date(2014, 01, 01),
                    end_date=date(2014, 12, 31)
                )
            )

    def handle(self, *args, **options):
        mixer = Mixer(locale='ru')
        self._create_doctors(mixer)
        self._create_tickets(mixer)
