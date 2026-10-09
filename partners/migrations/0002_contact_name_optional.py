from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partnershipinquiry',
            name='contact_name',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
    ]