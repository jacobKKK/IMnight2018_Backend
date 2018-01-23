from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


import datetime
import random
import logging
testlog = logging.getLogger('testdevelop')


class HoldingVocherManager(models.Manager):
    def use_vocher(self, user, vocher):
        try:
            vochers = HoldingVocher.objects.filter(
                user=user).filter(vocher=vocher).all()
        except Exception as error:
            testlog.error(error)
        else:
            if (len(vochers) > 1):
                testlog.error("A user can't hold more than one vocher.")
            for vocher in vochers:
                vocher.used = True

    def get_vochers(self, user):
        vochers = HoldingVocher.objects.filter(user=user).values('vocher')
        return pvochers

    def get_daily(self, user):
        try:
            daily_vocher = HoldingVocher.objects.filter(
                user=user).filter(created__date=datetime.date.today())
        except Exception as error:
            testlog.error(error)
            return HoldingVocher.objects.none()

        if daily_vocher:
            return daily_vocher
        else:
            own_HoldingVocher = HoldingVocher.objects.filter(user=user).all()
            own_vocher_pk = []
            for holdingVocher in own_HoldingVocher:
                own_vocher_pk.append(holdingVocher.vocher.pk)

            try:
                all_vochers = Vocher.objects.filter.exclude(
                    pk__in=own_vocher_pk).all()
            except Exception as error:
                testlog.error(error)
                all_vochers = []

            """random choice a performer and return"""
            num = len(all_vochers)
            # check if already draw all performers
            if num <= 0:
                # all performer are draw
                return HoldingVocher.objects.none()

            else:
                index = random.randint(0, num - 1)
                vocher = all_vochers[index]

                try:
                    daily_vocher = self.create(
                        vocher=vocher, user=user)
                    daily_vocher.save()
                except ValidationError as error:
                    testlog.error(error)
                    return HoldingVocher.objects.none()
                except Exception as error:
                    testlog.warning(error)
                    return HoldingVocher.objects.none()
                else:
                    # return objects must be iterable
                    daily_vocher = [daily_vocher]
                    return daily_vocher


class HoldingVocher(models.Model):
    vocher = models.ForeignKey(
        Vocher, on_delete=models.CASCADE, related_name='vocher')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    used = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)

    objects = HoldingVocherManager()


class Store(models.Model):
    storename = models.TextField(blank=False, default="Store")
    img = models.URLField(
        blank=False, default="https://i.imgur.com/67A5cyq.jpg")
    title = models.TextField(null=True, blank=True)
    sub_title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class Vocher(models.Model):
    title = models.TextField(blank=False, default="Vocher")
    sub_title = models.TextField()
    img = models.URLField(
        blank=False, default="https://i.imgur.com/67A5cyq.jpg")
    description = models.TextField(null=True, blank=True)

    store = models.ForeignKey(
        Store, on_delete=models.CASCADE, related_name='store')
