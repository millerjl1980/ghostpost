# Generated by Django 3.0.6 on 2020-05-14 21:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boast', models.BooleanField(default=True, help_text='If it is not a boast, it will be listed as a roast!', verbose_name='boast?')),
                ('content', models.CharField(max_length=280)),
                ('up_vote', models.IntegerField()),
                ('down_vote', models.IntegerField()),
                ('sub_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
