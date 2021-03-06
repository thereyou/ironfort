# Generated by Django 2.0.5 on 2018-06-01 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fort', '0003_auto_20180601_0938'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='remoteuser',
            options={'verbose_name': '远程主机账户', 'verbose_name_plural': '远程主机账户'},
        ),
        migrations.AlterField(
            model_name='group',
            name='remote_user_bind_host',
            field=models.ManyToManyField(blank=True, to='fort.RemoteUserBindHost', verbose_name='组内关联的远程账户'),
        ),
        migrations.AlterField(
            model_name='remoteuser',
            name='remote_user_name',
            field=models.CharField(max_length=128, verbose_name='远程账户'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='remote_user_bind_hosts',
            field=models.ManyToManyField(blank=True, to='fort.RemoteUserBindHost', verbose_name='堡垒机用户关联的远程账户'),
        ),
    ]
