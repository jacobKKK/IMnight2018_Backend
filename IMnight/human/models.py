from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.core.exceptions import ValidationError

import datetime
import random


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    # daily_performer = models.ForeignKey(
    #     DailyPerformer, on_delete=models.CASCADE, related_name='daily_performer')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


def is_client(user):
        # chelk if user is in Clients Group
    return user.groups.filter(name='Clients').exists()


def is_performer(user):
    # chelk if user is in Performers Group
    return user.groups.filter(name='Performers').exists()


class RelationshipManager(models.Manager):
    def get_performers(self, user):
        # if is_performer(user):
        #     return ValidationError("You can't get performers list from a performer")

        performers = Relationship.objects.filter(client=user).all()
        return performers

    def get_clients(self, user):
        # if is_client(user):
        #     return ValidationError("You can't get clients list from a client")

        clients = Relationship.objects.filter(performer=user).all()
        return clients

    def create_relationship(self, client, performer):
        relationship = self.create(client=client, performer=performer)
        return relationship

    def get_daily(self, user):
        daily_performer = Relationship.objects.filter(
            client=user).filter(created__date=datetime.date.today())

        if daily_performer:
            # already draw daily performer
            return daily_performer
        else:
            # not yet draw daily performer
            own_relationship = Relationship.objects.filter(client=user).all()
            own_performer_pk = []

            for relationship in own_relationship:
                own_performer_pk.append(relationship.performer.pk)

            all_performers = User.objects.filter(
                groups__name='Performers').exclude(pk__in=own_performer_pk).all()

            # random choice a performer and return
            # check if own all performers
            num = len(all_performers)
            if num <= 0:
                # all performer are draw
                return Relationship.objects.none()

            else:
                index = random.randint(0, num - 1)
                performer = all_performers[index]
                daily_performer = self.create_relationship(
                    client=user, performer=performer)
                daily_performer.save()

            # return QuerySet
            daily_performer = [daily_performer]
            return daily_performer


class Relationship(models.Model):
    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='client')
    performer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='performer')
    created = models.DateTimeField(default=timezone.now)

    # set the model manager to FriendshipManager()
    objects = RelationshipManager()

    class Meta:
        # verbose_name = 'Relationship'
        # verbose_name_plural = 'Relationship'
        unique_together = ('client', 'performer')

    def __unicode__(self):
        return "Client #%s has relationship with Performer #%s" % (self.client, self.performer)

    def save(self, *args, **kwargs):
        # Some identity check for the User
        if not is_client(self.client):
            raise ValidationError("self.client is not in Clients Group")
        if not is_performer(self.performer):
            raise ValidationError("self.performer is not in Performers Group")
        if self.client == self.performer:
            raise ValidationError(
                "self.client and slef.performer can't be same person")

        super(Relationship, self).save(*args, **kwargs)
