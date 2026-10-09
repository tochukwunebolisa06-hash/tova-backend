from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0003_testimonial_category_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='is_approved',
            field=models.BooleanField(
                default=True,
                help_text='Untick to hide a testimonial from the public site.',
            ),
        ),
    ]