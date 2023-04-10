# Generated by Django 4.2 on 2023-04-05 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orgroam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('file', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, null=True)),
                ('hash', models.TextField()),
                ('atime', models.TextField()),
                ('mtime', models.TextField()),
            ],
            options={
                'db_table': 'files',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos', models.TextField()),
                ('dest', models.TextField()),
                ('type', models.TextField()),
                ('properties', models.TextField()),
            ],
            options={
                'db_table': 'links',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ref',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.TextField()),
                ('type', models.TextField()),
            ],
            options={
                'db_table': 'refs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='orgroam.node')),
                ('tag', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'tags',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Files',
        ),
        migrations.DeleteModel(
            name='Links',
        ),
        migrations.DeleteModel(
            name='Refs',
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
    ]
