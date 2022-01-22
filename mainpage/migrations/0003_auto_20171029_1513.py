
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_auto_20171029_0603'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.AddField(
            model_name='project',
            name='img_name',
            field=models.CharField(default='calculator', max_length=100),
            preserve_default=False,
        ),
    ]
