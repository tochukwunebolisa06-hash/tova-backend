from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waitlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waitlistentry',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='waitlistentry',
            name='phone',
            field=models.CharField(
                blank=True,
                help_text='International format, e.g. +2348012345678.',
                max_length=20,
                null=True,
                unique=True,
            ),
        ),
        migrations.AddConstraint(
            model_name='waitlistentry',
            constraint=models.CheckConstraint(
                condition=models.Q(('email__isnull', False), ('phone__isnull', False), _connector='OR'),
                name='waitlist_email_or_phone_required',
            ),
        ),
    ]