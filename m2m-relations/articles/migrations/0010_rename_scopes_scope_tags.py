# Generated by Django 4.2.4 on 2023-08-26 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_rename_scopes_article_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scope',
            old_name='scopes',
            new_name='tags',
        ),
    ]