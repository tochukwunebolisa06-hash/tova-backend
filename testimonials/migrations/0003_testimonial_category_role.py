from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0002_testimonial_university'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='category',
            field=models.CharField(
                choices=[('student', 'Student / Member'), ('leader', 'Pastor / Church leader')],
                default='student',
                help_text='Which column of the Home page this appears in.',
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='role',
            field=models.CharField(
                blank=True,
                default='',
                help_text="Shown under the name, e.g. 'Senior Pastor, Lagos'. Falls back to the university if blank.",
                max_length=150,
            ),
        ),
    ]