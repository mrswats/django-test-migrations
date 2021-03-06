# -*- coding: utf-8 -*-
# Generated by Django 2.2.7 on 2019-11-19 21:25

from django.db import migrations

from main_app.logic.pure.migrations import is_clean_item


def _set_clean_flag(apps, schema_editor):
    """
    Performs the data migration.

    We can't import the ``SomeItem`` model directly as it may be a newer
    version than this migration expects. We use the historical version.

    We are using ``.all()`` because
    we don't have a lot of ``SomeItem`` instances.
    In real-life you should not do that.
    """
    SomeItem = apps.get_model('main_app', 'SomeItem')
    for instance in SomeItem.objects.all():
        instance.is_clean = is_clean_item(instance)
        instance.save(update_fields=['is_clean'])


def _remove_clean_flags(apps, schema_editor):
    """
    This is just a noop example of a rollback function.

    It is not used in our simple case,
    but it should be implemented for more complex scenarios.
    """


class Migration(migrations.Migration):
    """Performs the logical data migration for ``SomeItem``."""

    dependencies = [
        ('main_app', '0002_someitem_is_clean'),
    ]

    operations = [
        migrations.RunPython(_set_clean_flag, _remove_clean_flags),
    ]
