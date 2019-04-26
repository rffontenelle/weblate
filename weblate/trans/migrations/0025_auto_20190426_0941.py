# Generated by Django 2.2 on 2019-04-26 09:41

from django.db import migrations, models
import weblate.utils.render


def migrate_repoweb(apps, schema_editor):
    Component = apps.get_model('trans', 'Component')
    for component in Component.objects.exclude(repoweb=''):
        component.repoweb = weblate.utils.render.migrate_repoweb(
            component.repoweb
        )
        component.save()


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0024_resolve_auto_format'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='repoweb',
            field=models.URLField(blank=True, help_text='Link to repository browser, use {{branch}} for branch, {{filename}} and {{line}} as filename and line placeholders.', validators=[weblate.utils.render.validate_repoweb], verbose_name='Repository browser'),
        ),
        migrations.RunPython(migrate_repoweb, migrations.RunPython.noop),
    ]
