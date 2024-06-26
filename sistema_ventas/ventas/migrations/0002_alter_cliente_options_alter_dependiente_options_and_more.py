# Generated by Django 5.0.6 on 2024-06-04 02:52

from django.db import migrations, models
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

def create_groups_and_permissions(apps, schema_editor):
    Venta = apps.get_model('ventas', 'Venta')
    Cliente = apps.get_model('ventas', 'Cliente')
    Dependiente = apps.get_model('ventas', 'Dependiente')

    # Crear grupos
    view_all_sales_group, created = Group.objects.get_or_create(name='View All Sales')
    manage_users_group, created = Group.objects.get_or_create(name='Manage Users')

    # Obtener los ContentTypes
    venta_ct = ContentType.objects.get_for_model(Venta)
    cliente_ct = ContentType.objects.get_for_model(Cliente)
    dependiente_ct = ContentType.objects.get_for_model(Dependiente)

    # Crear permisos personalizados
    permissions = [
        ('can_view_all_sales', 'Can view all sales', venta_ct),
        ('can_view_all_clients', 'Can view all clients', cliente_ct),
        ('can_view_all_dependents', 'Can view all dependents', dependiente_ct),
    ]

    for codename, name, content_type in permissions:
        permission, created = Permission.objects.get_or_create(
            codename=codename,
            name=name,
            content_type=content_type,
        )
        view_all_sales_group.permissions.add(permission)

    # Añadir permisos para gestionar usuarios
    manage_users_group.permissions.add(
        Permission.objects.get(codename='add_user'),
        Permission.objects.get(codename='change_user'),
        Permission.objects.get(codename='delete_user'),
        Permission.objects.get(codename='view_user'),
    )

class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name': 'clientes', 'verbose_name_plural': 'clientes'},
        ),
        migrations.AlterModelOptions(
            name='dependiente',
            options={'verbose_name': 'depende', 'verbose_name_plural': 'dependes'},
        ),
        migrations.AlterModelOptions(
            name='venta',
            options={'verbose_name': 'nombre_plan'},
        ),
        migrations.RunPython(create_groups_and_permissions),
    ]
