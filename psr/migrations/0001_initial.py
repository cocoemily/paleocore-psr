# Generated by Django 2.2.13 on 2021-02-05 15:17

import ckeditor.fields
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExcavationUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=6)),
                ('extent', django.contrib.gis.db.models.fields.MultiPointField(blank=True, null=True, srid=4326)),
            ],
            options={
                'verbose_name': 'PSR Excavation Unit',
                'verbose_name_plural': 'PSR Excavation Units',
            },
        ),
        migrations.CreateModel(
            name='GeologicalContext',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, help_text='The date and time this resource was first created.', verbose_name='Created')),
                ('problem', models.BooleanField(default=False, help_text='Is there a problem with this record that needs attention?')),
                ('problem_comment', models.TextField(blank=True, help_text='Description of the problem.', max_length=255, null=True)),
                ('remarks', ckeditor.fields.RichTextField(blank=True, help_text='General remarks about this database record.', null=True, verbose_name='Record Remarks')),
                ('last_import', models.BooleanField(default=False)),
                ('georeference_remarks', models.TextField(blank=True, max_length=500, null=True)),
                ('formation', models.CharField(blank=True, max_length=50, null=True)),
                ('member', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.TextField(blank=True, max_length=255, null=True)),
                ('context_type', models.CharField(blank=True, max_length=255, null=True)),
                ('context_number', models.IntegerField(blank=True, null=True)),
                ('basis_of_record', models.CharField(blank=True, help_text='e.g. Observed item or Collected item', max_length=50, verbose_name='Basis of Record')),
                ('collecting_method', models.CharField(blank=True, max_length=50, null=True, verbose_name='Collecting Method')),
                ('collection_code', models.CharField(blank=True, max_length=10, null=True)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('stratigraphic_section', models.CharField(blank=True, max_length=50, null=True)),
                ('stratigraphic_formation', models.CharField(blank=True, max_length=255, null=True, verbose_name='Formation')),
                ('stratigraphic_member', models.CharField(blank=True, max_length=255, null=True, verbose_name='Member')),
                ('upper_limit_in_section', models.DecimalField(blank=True, decimal_places=8, default=None, max_digits=38, null=True)),
                ('lower_limit_in_section', models.DecimalField(blank=True, decimal_places=8, default=None, max_digits=38, null=True)),
                ('analytical_unit_1', models.CharField(blank=True, max_length=255, null=True)),
                ('analytical_unit_2', models.CharField(blank=True, max_length=255, null=True)),
                ('analytical_unit_3', models.CharField(blank=True, max_length=255, null=True)),
                ('analytical_unit_found', models.CharField(blank=True, max_length=255, null=True)),
                ('analytical_unit_likely', models.CharField(blank=True, max_length=255, null=True)),
                ('analytical_unit_simplified', models.CharField(blank=True, max_length=255, null=True)),
                ('in_situ', models.BooleanField(blank=True, default=None, null=True)),
                ('ranked', models.BooleanField(blank=True, default=False, null=True)),
                ('weathering', models.SmallIntegerField(blank=True, null=True)),
                ('surface_modification', models.CharField(blank=True, max_length=255, null=True, verbose_name='Surface Mod')),
                ('geology_type', models.TextField(blank=True, max_length=255, null=True)),
                ('dip', models.CharField(blank=True, max_length=255, null=True)),
                ('strike', models.CharField(blank=True, max_length=255, null=True)),
                ('color', models.CharField(blank=True, max_length=255, null=True)),
                ('texture', models.CharField(blank=True, max_length=255, null=True)),
                ('height', models.DecimalField(blank=True, decimal_places=8, max_digits=38, null=True)),
                ('width', models.DecimalField(blank=True, decimal_places=8, max_digits=38, null=True)),
                ('depth', models.DecimalField(blank=True, decimal_places=8, max_digits=38, null=True)),
                ('slope_character', models.TextField(blank=True, max_length=64000, null=True)),
                ('sediment_presence', models.BooleanField(blank=True, default=None, null=True)),
                ('sediment_character', models.TextField(blank=True, max_length=64000, null=True)),
                ('cave_mouth_character', models.TextField(blank=True, max_length=64000, null=True)),
                ('rockfall_character', models.TextField(blank=True, max_length=64000, null=True)),
                ('speleothem_character', models.TextField(blank=True, max_length=64000, null=True)),
                ('size_of_loess', models.CharField(blank=True, max_length=255, null=True)),
                ('mean_thickness', models.DecimalField(blank=True, decimal_places=8, default=None, max_digits=38, null=True)),
                ('max_thickness', models.DecimalField(blank=True, decimal_places=8, default=None, max_digits=38, null=True)),
                ('landscape_position', models.CharField(blank=True, max_length=255, null=True)),
                ('surface_inclination', models.CharField(blank=True, max_length=255, null=True)),
                ('presence_coarse_components', models.BooleanField(blank=True, default=None, null=True)),
                ('amount_coarse_components', models.DecimalField(blank=True, decimal_places=8, default=None, max_digits=38, null=True)),
                ('number_sediment_layers', models.SmallIntegerField(blank=True, null=True)),
                ('number_soil_horizons', models.SmallIntegerField(blank=True, null=True)),
                ('number_cultural_horizons', models.SmallIntegerField(blank=True, null=True)),
                ('number_coarse_layers', models.SmallIntegerField(blank=True, null=True)),
                ('presence_vertical_profile', models.BooleanField(default=False)),
                ('context_remarks', models.TextField(blank=True, max_length=500, null=True, verbose_name='Context Remarks')),
                ('error_notes', models.CharField(blank=True, max_length=255, null=True)),
                ('notes', models.CharField(blank=True, max_length=254, null=True)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(srid=4326)),
                ('point', django.contrib.gis.db.models.fields.GeometryField(srid=4326)),
                ('date_collected', models.DateTimeField(blank=True, null=True, verbose_name='Date Collected')),
                ('date_last_modified', models.DateTimeField(auto_now=True, verbose_name='Date Last Modified')),
                ('image', models.FileField(blank=True, max_length=255, null=True, upload_to='uploads/images/psr')),
            ],
            options={
                'verbose_name': 'PSR Geological Context',
                'verbose_name_plural': 'PSR Geological Contexts',
                'ordering': ['context_number'],
            },
        ),
        migrations.CreateModel(
            name='IdentificationQualifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, help_text='The date and time this resource was first created.', verbose_name='Created')),
                ('date_last_modified', models.DateTimeField(default=django.utils.timezone.now, help_text='The date and time this resource was last altered.', verbose_name='Modified')),
                ('problem', models.BooleanField(default=False, help_text='Is there a problem with this record that needs attention?')),
                ('problem_comment', models.TextField(blank=True, help_text='Description of the problem.', max_length=255, null=True)),
                ('remarks', ckeditor.fields.RichTextField(blank=True, help_text='General remarks about this database record.', null=True, verbose_name='Record Remarks')),
                ('last_import', models.BooleanField(default=False)),
                ('name', models.CharField(blank=True, max_length=15, unique=True)),
                ('qualified', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'PSR ID Qualifier',
                'verbose_name_plural': 'PSR ID Qualifiers',
            },
        ),
        migrations.CreateModel(
            name='Occurrence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, help_text='The date and time this resource was first created.', verbose_name='Created')),
                ('date_last_modified', models.DateTimeField(default=django.utils.timezone.now, help_text='The date and time this resource was last altered.', verbose_name='Modified')),
                ('problem_comment', models.TextField(blank=True, help_text='Description of the problem.', max_length=255, null=True)),
                ('remarks', ckeditor.fields.RichTextField(blank=True, help_text='General remarks about this database record.', null=True, verbose_name='Record Remarks')),
                ('last_import', models.BooleanField(default=False)),
                ('georeference_remarks', models.TextField(blank=True, max_length=500, null=True)),
                ('date_recorded', models.DateTimeField(blank=True, help_text='Date and time the item was observed or collected.', null=True, verbose_name='Date Rec')),
                ('year_collected', models.IntegerField(blank=True, help_text='The year, event or field campaign during which the item was found.', null=True, verbose_name='Year')),
                ('barcode', models.IntegerField(blank=True, help_text='For collected items only.', null=True, verbose_name='Barcode')),
                ('field_number', models.CharField(blank=True, max_length=50, null=True)),
                ('basis_of_record', models.CharField(blank=True, help_text='e.g. Observed item or Collected item', max_length=50, verbose_name='Basis of Record')),
                ('find_type', models.CharField(blank=True, max_length=255, verbose_name='Find Type')),
                ('item_number', models.IntegerField(blank=True, null=True, verbose_name='Item #')),
                ('item_type', models.CharField(blank=True, max_length=255, verbose_name='Item Type')),
                ('item_description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Description')),
                ('item_count', models.IntegerField(blank=True, default=1, null=True, verbose_name='Item Count')),
                ('collector', models.CharField(blank=True, max_length=50, null=True, verbose_name='Collector')),
                ('finder', models.CharField(blank=True, max_length=50, null=True, verbose_name='Finder')),
                ('collecting_method', models.CharField(blank=True, max_length=50, null=True, verbose_name='Collecting Method')),
                ('field_id', models.CharField(blank=True, max_length=50, null=True, verbose_name='Field ID')),
                ('suffix', models.IntegerField(blank=True, null=True, verbose_name='Suffix')),
                ('cat_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='Cat Number')),
                ('prism', models.DecimalField(blank=True, decimal_places=8, max_digits=38, null=True)),
                ('point', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('item_part', models.CharField(blank=True, max_length=10, null=True, verbose_name='Item Part')),
                ('disposition', models.CharField(blank=True, max_length=255, null=True, verbose_name='Disposition')),
                ('preparation_status', models.CharField(blank=True, max_length=50, null=True, verbose_name='Prep Status')),
                ('collection_remarks', models.TextField(blank=True, max_length=255, null=True, verbose_name='Collection Remarks')),
                ('date_collected', models.DateTimeField(blank=True, null=True, verbose_name='Date Collected')),
                ('problem', models.BooleanField(blank=True, default=False, null=True)),
                ('problem_remarks', models.TextField(blank=True, max_length=64000, null=True)),
                ('collection_code', models.CharField(blank=True, max_length=20, null=True, verbose_name='Collection Code')),
                ('drainage_region', models.CharField(blank=True, max_length=255, null=True, verbose_name='Drainage Region')),
                ('image', models.FileField(blank=True, max_length=255, null=True, upload_to='uploads/images/psr')),
            ],
            options={
                'verbose_name': 'PSR Survey Occurrence',
                'verbose_name_plural': 'PSR Survey Occurrences',
                'ordering': ['collection_code', 'geological_context', 'item_number', 'item_part'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, help_text='The date and time this resource was first created.', verbose_name='Created')),
                ('date_last_modified', models.DateTimeField(default=django.utils.timezone.now, help_text='The date and time this resource was last altered.', verbose_name='Modified')),
                ('problem', models.BooleanField(default=False, help_text='Is there a problem with this record that needs attention?')),
                ('problem_comment', models.TextField(blank=True, help_text='Description of the problem.', max_length=255, null=True)),
                ('remarks', ckeditor.fields.RichTextField(blank=True, help_text='General remarks about this database record.', null=True, verbose_name='Record Remarks')),
                ('last_import', models.BooleanField(default=False)),
                ('last_name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Last Name')),
                ('first_name', models.CharField(blank=True, max_length=256, null=True, verbose_name='First Name')),
            ],
            options={
                'verbose_name': 'PSR Person',
                'verbose_name_plural': 'PSR People',
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='TaxonRank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, help_text='The date and time this resource was first created.', verbose_name='Created')),
                ('date_last_modified', models.DateTimeField(default=django.utils.timezone.now, help_text='The date and time this resource was last altered.', verbose_name='Modified')),
                ('problem', models.BooleanField(default=False, help_text='Is there a problem with this record that needs attention?')),
                ('problem_comment', models.TextField(blank=True, help_text='Description of the problem.', max_length=255, null=True)),
                ('remarks', ckeditor.fields.RichTextField(blank=True, help_text='General remarks about this database record.', null=True, verbose_name='Record Remarks')),
                ('last_import', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('plural', models.CharField(max_length=50, unique=True)),
                ('ordinal', models.IntegerField(unique=True)),
            ],
            options={
                'verbose_name': 'PSR Taxon Rank',
                'verbose_name_plural': 'PSR Taxon Ranks',
            },
        ),
        migrations.CreateModel(
            name='Aggregate',
            fields=[
                ('occurrence_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='psr.Occurrence')),
                ('screen_size', models.CharField(blank=True, max_length=255, null=True)),
                ('burning', models.BooleanField(default=False)),
                ('bone', models.BooleanField(default=False)),
                ('microfauna', models.BooleanField(default=False)),
                ('pebbles', models.BooleanField(default=False)),
                ('smallplatforms', models.DecimalField(blank=True, decimal_places=8, max_digits=38, null=True)),
                ('smalldebris', models.DecimalField(blank=True, decimal_places=8, max_digits=38, null=True)),
                ('tinyplatforms', models.DecimalField(blank=True, decimal_places=8, max_digits=38, null=True)),
                ('tinydebris', models.DecimalField(blank=True, decimal_places=8, max_digits=38, null=True)),
                ('counts', models.IntegerField(blank=True, null=True)),
                ('weights', models.IntegerField(blank=True, null=True)),
                ('bull_find_remarks', models.TextField(blank=True, max_length=64000, null=True)),
            ],
            options={
                'verbose_name': 'PSR Bulk Find',
                'verbose_name_plural': 'PSR Bulk Finds',
            },
            bases=('psr.occurrence',),
        ),
        migrations.CreateModel(
            name='Archaeology',
            fields=[
                ('occurrence_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='psr.Occurrence')),
                ('archaeology_type', models.CharField(blank=True, max_length=255, null=True)),
                ('period', models.CharField(blank=True, max_length=255, null=True)),
                ('archaeology_preparation', models.CharField(blank=True, max_length=255, null=True)),
                ('archaeology_remarks', models.TextField(blank=True, max_length=64000, null=True)),
                ('length_mm', models.DecimalField(blank=True, decimal_places=8, max_digits=38, null=True)),
                ('width_mm', models.DecimalField(blank=True, decimal_places=8, max_digits=38, null=True)),
                ('thick_mm', models.DecimalField(blank=True, decimal_places=8, max_digits=38, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=8, max_digits=38, null=True)),
                ('archaeology_notes', models.TextField(blank=True, max_length=64000, null=True)),
            ],
            options={
                'verbose_name': 'PSR Survey Archaeology',
                'verbose_name_plural': 'PSR Survey Archaeology',
            },
            bases=('psr.occurrence',),
        ),
        migrations.CreateModel(
            name='Geology',
            fields=[
                ('occurrence_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='psr.Occurrence')),
                ('geology_type', models.CharField(blank=True, max_length=255, null=True)),
                ('dip', models.DecimalField(blank=True, decimal_places=8, max_digits=38, null=True)),
                ('strike', models.DecimalField(blank=True, decimal_places=8, max_digits=38, null=True)),
                ('color', models.CharField(blank=True, max_length=255, null=True)),
                ('texture', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'PSR Survey Geology',
                'verbose_name_plural': 'PSR Survey Geology',
            },
            bases=('psr.occurrence',),
        ),
        migrations.CreateModel(
            name='Taxon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, help_text='The date and time this resource was first created.', verbose_name='Created')),
                ('date_last_modified', models.DateTimeField(default=django.utils.timezone.now, help_text='The date and time this resource was last altered.', verbose_name='Modified')),
                ('problem', models.BooleanField(default=False, help_text='Is there a problem with this record that needs attention?')),
                ('problem_comment', models.TextField(blank=True, help_text='Description of the problem.', max_length=255, null=True)),
                ('remarks', ckeditor.fields.RichTextField(blank=True, help_text='General remarks about this database record.', null=True, verbose_name='Record Remarks')),
                ('last_import', models.BooleanField(default=False)),
                ('label', models.CharField(blank=True, help_text='For a species, the name field contains the specific epithet and the label contains the full\n    scientific name, e.g. Homo sapiens, name = sapiens, label = Homo sapiens', max_length=244, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='psr.Taxon')),
                ('rank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='psr.TaxonRank')),
            ],
            options={
                'verbose_name': 'PSR Taxon',
                'verbose_name_plural': 'PSR Taxa',
            },
        ),
        migrations.AddField(
            model_name='occurrence',
            name='found_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='occurrence_found_by', to='psr.Person'),
        ),
        migrations.AddField(
            model_name='occurrence',
            name='geological_context',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='psr.GeologicalContext'),
        ),
        migrations.AddField(
            model_name='occurrence',
            name='recorded_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='occurrence_recorded_by', to='psr.Person'),
        ),
        migrations.AddField(
            model_name='occurrence',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='psr.ExcavationUnit'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/images')),
                ('description', models.TextField(blank=True, null=True)),
                ('locality', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='psr_contexts_image', to='psr.GeologicalContext')),
                ('occurrence', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='psr_occurrences_image', to='psr.Occurrence')),
            ],
        ),
        migrations.AddField(
            model_name='geologicalcontext',
            name='recorded_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='geo_context_recorded_by', to='psr.Person'),
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='uploads/files')),
                ('description', models.TextField(blank=True, null=True)),
                ('locality', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='psr_contexts_file', to='psr.GeologicalContext')),
                ('occurrence', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='psr_occurrences_file', to='psr.Occurrence')),
            ],
        ),
        migrations.AddField(
            model_name='excavationunit',
            name='geological_context',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='psr.GeologicalContext'),
        ),
        migrations.CreateModel(
            name='ExcavationOccurrence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, help_text='The date and time this resource was first created.', verbose_name='Created')),
                ('date_last_modified', models.DateTimeField(default=django.utils.timezone.now, help_text='The date and time this resource was last altered.', verbose_name='Modified')),
                ('problem', models.BooleanField(default=False, help_text='Is there a problem with this record that needs attention?')),
                ('problem_comment', models.TextField(blank=True, help_text='Description of the problem.', max_length=255, null=True)),
                ('remarks', ckeditor.fields.RichTextField(blank=True, help_text='General remarks about this database record.', null=True, verbose_name='Record Remarks')),
                ('last_import', models.BooleanField(default=False)),
                ('georeference_remarks', models.TextField(blank=True, max_length=500, null=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('date_recorded', models.DateTimeField(blank=True, help_text='Date and time the item was observed or collected.', null=True, verbose_name='Date Rec')),
                ('year_collected', models.IntegerField(blank=True, help_text='The year, event or field campaign during which the item was found.', null=True, verbose_name='Year')),
                ('barcode', models.IntegerField(blank=True, help_text='For collected items only.', null=True, verbose_name='Barcode')),
                ('field_number', models.CharField(blank=True, max_length=50, null=True)),
                ('field_id', models.CharField(blank=True, max_length=50, null=True, verbose_name='Field ID')),
                ('cat_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='Cat Number')),
                ('prism', models.CharField(blank=True, max_length=50, null=True)),
                ('level', models.CharField(blank=True, max_length=100, null=True)),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
                ('excavator', models.CharField(blank=True, max_length=100, null=True)),
                ('point', django.contrib.gis.db.models.fields.MultiPointField(blank=True, dim=3, null=True, srid=-1)),
                ('date_collected', models.DateTimeField(blank=True, null=True, verbose_name='Date Collected')),
                ('found_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='excav_occurrence_found_by', to='psr.Person')),
                ('geological_context', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='psr.GeologicalContext')),
                ('unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='psr.ExcavationUnit')),
            ],
            options={
                'verbose_name': 'PSR Excavated Occurrence',
                'verbose_name_plural': 'PSR Excavated Occurrences',
            },
        ),
        migrations.CreateModel(
            name='Bone',
            fields=[
                ('archaeology_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='psr.Archaeology')),
                ('cutmarks', models.BooleanField(default=False)),
                ('burning', models.BooleanField(default=False)),
                ('part', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'PSR Archaeological Fauna',
                'verbose_name_plural': 'PSR Archaeological Fauna',
            },
            bases=('psr.archaeology',),
        ),
        migrations.CreateModel(
            name='Ceramic',
            fields=[
                ('archaeology_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='psr.Archaeology')),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('decorated', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'PSR Ceramic',
                'verbose_name_plural': 'PSR Ceramic',
            },
            bases=('psr.archaeology',),
        ),
        migrations.CreateModel(
            name='Lithic',
            fields=[
                ('archaeology_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='psr.Archaeology')),
                ('dataclass', models.CharField(blank=True, max_length=255, null=True)),
                ('fbtype', models.SmallIntegerField(blank=True, null=True)),
                ('form', models.CharField(blank=True, max_length=255, null=True)),
                ('technique', models.CharField(blank=True, max_length=255, null=True)),
                ('cortex', models.DecimalField(blank=True, decimal_places=8, max_digits=38, null=True)),
                ('coretype', models.CharField(blank=True, max_length=255, null=True)),
                ('platsurf', models.CharField(blank=True, max_length=255, null=True)),
                ('scarmorph', models.CharField(blank=True, max_length=255, null=True)),
                ('edgedamage', models.CharField(blank=True, max_length=255, null=True)),
                ('platwidth', models.DecimalField(blank=True, decimal_places=8, max_digits=38, null=True)),
                ('platthick', models.DecimalField(blank=True, decimal_places=8, max_digits=38, null=True)),
                ('epa', models.DecimalField(blank=True, decimal_places=8, max_digits=38, null=True)),
                ('scarlength', models.DecimalField(blank=True, decimal_places=8, max_digits=38, null=True)),
            ],
            options={
                'verbose_name': 'PSR Lithic',
                'verbose_name_plural': 'PSR Lithics',
            },
            bases=('psr.archaeology',),
        ),
        migrations.CreateModel(
            name='Biology',
            fields=[
                ('occurrence_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='psr.Occurrence')),
                ('biology_type', models.CharField(blank=True, max_length=255, null=True)),
                ('sex', models.CharField(blank=True, max_length=50, null=True, verbose_name='Sex')),
                ('life_stage', models.CharField(blank=True, max_length=50, null=True, verbose_name='Life Stage')),
                ('size_class', models.CharField(blank=True, max_length=50, null=True, verbose_name='Size Class')),
                ('verbatim_taxon', models.CharField(blank=True, max_length=1024, null=True)),
                ('verbatim_identification_qualifier', models.CharField(blank=True, max_length=255, null=True)),
                ('taxonomy_remarks', models.TextField(blank=True, max_length=500, null=True)),
                ('type_status', models.CharField(blank=True, max_length=50, null=True)),
                ('fauna_notes', models.TextField(blank=True, max_length=64000, null=True)),
                ('identification_qualifier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bio_occurrences', to='psr.IdentificationQualifier')),
                ('taxon', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='bio_occurrences', to='psr.Taxon')),
            ],
            options={
                'verbose_name': 'PSR Survey Biology',
                'verbose_name_plural': 'PSR Survey Biology',
            },
            bases=('psr.occurrence',),
        ),
    ]