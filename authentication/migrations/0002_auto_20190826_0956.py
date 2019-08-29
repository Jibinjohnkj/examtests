# Generated by Django 2.2.4 on 2019-08-26 09:56

from django.db import migrations
from django.contrib.auth.management import create_permissions

from authentication.models import User

def migrate_permissions(apps, schema_editor):
    for app_config in apps.get_app_configs():
        app_config.models_module = True
        create_permissions(app_config, apps=apps, verbosity=0)
        app_config.models_module = None

def create_default_teacher(apps, schema_editor):
    User.objects.create_user(username='ann',
                             email='ann@gmail.com',
                             is_staff=True,
                             password='ann@123',
                             type='Teacher')

def assign_teacher_permissions(apps, schema_editor):
    Permission = apps.get_model('auth', 'Permission')
    default_teacher = User.objects.get(email='ann@gmail.com')

    permission_list = [
        'add_exam',
        'change_exam',
        'delete_exam',
        'view_exam',
        'add_question',
        'change_question',
        'delete_question',
        'view_question',
        'add_option',
        'change_option',
        'delete_option',
        'view_option',
    ]

    permissions = Permission.objects.filter(codename__in=permission_list).values_list('id',flat=True)
    default_teacher.user_permissions.set(permissions)

class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('multiplechoice', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate_permissions),
        migrations.RunPython(create_default_teacher),
        migrations.RunPython(assign_teacher_permissions),
    ]
