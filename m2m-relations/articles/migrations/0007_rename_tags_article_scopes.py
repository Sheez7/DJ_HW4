# Generated by Django 4.2.4 on 2023-08-26 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_rename_scopes_article_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='tags',
            new_name='scopes',
        ),
    ]