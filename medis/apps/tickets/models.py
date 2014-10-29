# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from django.db import models


class Speciality(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование специальности')

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'
        ordering = ['-pk']

    def __unicode__(self):
        return self.name


admin.site.register(Speciality)


class Doctor(models.Model):
    name = models.CharField(max_length=255, verbose_name='ФИО врача')
    specialty = models.ForeignKey(Speciality)

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'
        ordering = ['name', '-pk']

    def __unicode__(self):
        return self.name

admin.site.register(Doctor)


class Patient(models.Model):
    name = models.CharField(max_length=255, verbose_name='ФИО пациента')

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'
        ordering = ['name', '-pk']

    def __unicode__(self):
        return self.name

admin.site.register(Patient)


class TicketManager(models.Manager):
    def count_by_speciality(self, month, year):
        answer = {}
        for specialty in Speciality.objects.all():
            tickets = Ticket.objects.filter(doctor__in=specialty.doctor_set.all(), datetime__month=month,
                                                      datetime__year=year)
            patients = tickets.exclude(patient__isnull=True)
            answer[specialty.name] = {
                'tickets': tickets.count(),
                'patients': patients.count()
            }
        return answer

    def count_by_doctor(self, specialty, month, year):
        answer = {}
        for doctor in Doctor.objects.filter(specialty=specialty):
            tickets = Ticket.objects.filter(doctor=doctor, datetime__month=month, datetime__year=year)
            patients = tickets.exclude(patient__isnull=True)
            answer[doctor.name] = {
                'tickets': tickets.count(),
                'patients': patients.count()
            }
        return answer


class Ticket(models.Model):
    doctor = models.ForeignKey(Doctor)
    datetime = models.DateTimeField()
    patient = models.ForeignKey(Patient, null=True, blank=True)

    class Meta:
        verbose_name = 'Талон'
        verbose_name_plural = 'Талоны'
        ordering = ['-pk']

    def __unicode__(self):
        return '%s - %s' % (unicode(self.patient), unicode(self.doctor))

    objects = TicketManager()


admin.site.register(Ticket)