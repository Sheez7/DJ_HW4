# Generated by Django 4.2.4 on 2023-08-26 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_rename_tags_scope_scopes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='scopes',
            new_name='tags',
        ),
    ]
