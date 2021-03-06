# Generated by Django 3.1.6 on 2021-05-09 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0059_apply_collection_ordering'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(blank=True, help_text='enter your Facebook URL')),
                ('twitter', models.URLField(blank=True, help_text='enter your Twitter URL')),
                ('instagram', models.URLField(blank=True, help_text='enter your Instagram URL')),
                ('youtube', models.URLField(blank=True, help_text='enter your Youtube URL')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
