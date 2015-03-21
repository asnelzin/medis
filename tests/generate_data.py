from mixer.backend.django import Mixer
from faker import Factory
from datetime import date

from medis.apps.stats.models import Doctor, Ticket


def create_doctors(mixer):
    mixer.cycle(10).blend(Doctor,
                          speciality=mixer.SELECT,
                          name=mixer.FAKE)


def create_tickets(mixer):
    fake = Factory.create()
    mixer.cycle(60).blend(Ticket,
                          doctor=mixer.SELECT,
                          patient=mixer.FAKE,
                          datetime=fake.date_time_between(start_date=date(2014, 01, 01), end_date=date(2014, 12, 31)))


def main():
    mixer = Mixer(locale='ru')
    create_doctors(mixer)
    create_tickets(mixer)


if __name__ == "__main__":
    main()