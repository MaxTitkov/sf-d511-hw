# Generated by Django 2.2.6 on 2019-11-12 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0007_auto_20191112_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(through='p_library.Inspiration', to='p_library.Author'),
        ),
    ]
