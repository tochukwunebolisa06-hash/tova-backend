from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChurchPartner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('subtitle', models.CharField(blank=True, default='', help_text='Optional second line under the name, e.g. the city.', max_length=120)),
                ('location', models.CharField(blank=True, default='', max_length=150)),
                ('logo_url', models.URLField(blank=True, default='', help_text="Link to the church's logo image (PNG/SVG). Leave blank for a placeholder.", max_length=500)),
                ('quote', models.TextField(max_length=700)),
                ('author', models.CharField(help_text='Who the quote is from, e.g. the church name.', max_length=150)),
                ('role', models.CharField(blank=True, default='', help_text='e.g. Lead Pastor & Church Leadership Team', max_length=150)),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=5)),
                ('order', models.PositiveIntegerField(default=0, help_text='Lower numbers show first in the carousel.')),
                ('is_published', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Church partner',
                'verbose_name_plural': 'Church partners',
                'ordering': ['order', 'created_at'],
            },
        ),
        migrations.CreateModel(
            name='PartnershipInquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('church_name', models.CharField(max_length=150)),
                ('contact_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, default='', max_length=30)),
                ('message', models.TextField(blank=True, default='', max_length=1000)),
                ('is_contacted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Partnership inquiry',
                'verbose_name_plural': 'Partnership inquiries',
                'ordering': ['-created_at'],
            },
        ),
    ]