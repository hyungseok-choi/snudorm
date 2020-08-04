# Generated by Django 3.0.8 on 2020-08-05 01:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='이름')),
                ('nickname', models.CharField(max_length=15, verbose_name='닉네임')),
                ('building_category', models.CharField(choices=[('bachelor', '학부생활관'), ('family', '가족생활관'), ('master', '대학원생활관'), ('BK', 'BK생활관')], max_length=20, verbose_name='생활관')),
                ('building_dong', models.CharField(choices=[('903', '903동'), ('901', '901동'), ('902', '902동'), ('906', '906동'), ('900', '900동'), ('904', '904동'), ('905', '905동')], max_length=20, verbose_name='동')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
