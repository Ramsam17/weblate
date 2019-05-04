# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-21 12:27
from __future__ import unicode_literals

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

import weblate.lang.models
import weblate.screenshots.fields
import weblate.trans.fields
import weblate.trans.mixins
import weblate.trans.validators
import weblate.utils.fields
import weblate.utils.render
from weblate.formats.models import FILE_FORMATS
from weblate.vcs.models import VCS_REGISTRY


class Migration(migrations.Migration):

    replaces = [('trans', '0001_initial'), ('trans', '0002_auto_20141021_1347'), ('trans', '0003_auto_20141021_1348'), ('trans', '0004_auto_20141021_1550'), ('trans', '0005_auto_20141021_1550'), ('trans', '0006_auto_20141021_1609'), ('trans', '0007_auto_20141022_1159'), ('trans', '0008_auto_20141104_1200'), ('trans', '0009_auto_20141110_1501'), ('trans', '0010_source_check_flags'), ('trans', '0011_auto_20141114_1008'), ('trans', '0012_translation_have_comment'), ('trans', '0013_auto_20141124_1036'), ('trans', '0014_auto_20141202_1101'), ('trans', '0015_auto_20141203_1345'), ('trans', '0016_auto_20141208_1029'), ('trans', '0017_auto_20150108_1424'), ('trans', '0018_auto_20150213_1447'), ('trans', '0019_auto_20150220_1354'), ('trans', '0020_auto_20150220_1356'), ('trans', '0021_auto_20150306_1605'), ('trans', '0022_auto_20150309_0932'), ('trans', '0023_project_owner'), ('trans', '0024_subproject_edit_template'), ('trans', '0025_subproject_post_update_script'), ('trans', '0026_auto_20150401_1029'), ('trans', '0027_auto_20150401_1030'), ('trans', '0028_auto_20150402_1430'), ('trans', '0029_auto_20150415_1318'), ('trans', '0030_change_subproject'), ('trans', '0031_auto_20150415_1339'), ('trans', '0032_subproject_agreement'), ('trans', '0033_auto_20150618_1138'), ('trans', '0034_auto_20150618_1140'), ('trans', '0035_auto_20150630_1208'), ('trans', '0036_auto_20150709_1005'), ('trans', '0037_auto_20150810_1348'), ('trans', '0038_auto_20150810_1354'), ('trans', '0039_remove_project_owner'), ('trans', '0040_auto_20150818_1643'), ('trans', '0041_auto_20150819_1457'), ('trans', '0042_auto_20150910_0854'), ('trans', '0043_auto_20150910_0909'), ('trans', '0044_auto_20150916_0952'), ('trans', '0045_auto_20150916_1007'), ('trans', '0046_auto_20151111_1456'), ('trans', '0047_project_source_language'), ('trans', '0048_auto_20151120_1306'), ('trans', '0049_auto_20151222_0949'), ('trans', '0050_auto_20151222_1006'), ('trans', '0051_auto_20151222_1059'), ('trans', '0052_install_group_acl'), ('trans', '0053_auto_20160202_1145'), ('trans', '0054_auto_20160202_1219'), ('trans', '0055_auto_20160202_1221'), ('trans', '0056_auto_20160202_1224'), ('trans', '0057_indexupdate_language_code'), ('trans', '0058_componentlist'), ('trans', '0059_auto_20160303_0934'), ('trans', '0060_auto_20160310_0950'), ('trans', '0061_auto_20160404_1841'), ('trans', '0062_auto_20160419_1429'), ('trans', '0063_whiteboardmessage_category'), ('trans', '0064_auto_20160428_1813'), ('trans', '0065_auto_20160722_0923'), ('trans', '0066_auto_20160816_1031'), ('trans', '0067_auto_20161024_0922'), ('trans', '0068_auto_20161025_1632'), ('trans', '0069_source_screenshot'), ('trans', '0070_auto_20161103_1412'), ('trans', '0071_auto_20170124_1345'), ('trans', '0072_auto_20170209_1234'), ('trans', '0073_auto_20170209_1359'), ('trans', '0074_auto_20170209_1412'), ('trans', '0075_auto_20170215_1750'), ('trans', '0076_auto_20170317_1239'), ('trans', '0077_auto_20170317_1514'), ('trans', '0078_auto_20170322_1112'), ('trans', '0079_autocomponentlist'), ('trans', '0080_auto_20170323_0838'), ('trans', '0081_auto_20170323_0953'), ('trans', '0082_change_old'), ('trans', '0083_auto_20170404_1633'), ('trans', '0084_auto_20170406_0858'), ('trans', '0085_auto_20170406_0904'), ('trans', '0086_remove_project_owners'), ('trans', '0087_suggestion_timestamp'), ('trans', '0088_auto_20170511_1545'), ('trans', '0089_auto_20170713_0946'), ('trans', '0090_auto_20170718_0857'), ('trans', '0091_auto_20170719_1612'), ('trans', '0092_auto_20170719_1616'), ('trans', '0093_remove_project_push_on_commit'), ('trans', '0094_unit_pending'), ('trans', '0095_auto_20170816_0853'), ('trans', '0096_auto_20170925_0941'), ('trans', '0097_project_access_control'), ('trans', '0098_migrate_acl'), ('trans', '0099_remove_project_enable_acl'), ('trans', '0100_auto_20170926_1404'), ('trans', '0101_auto_20171013_0948'), ('trans', '0102_auto_20171013_1319'), ('trans', '0103_auto_20171120_1131'), ('trans', '0104_unit_approved'), ('trans', '0105_auto_20171121_1134'), ('trans', '0106_unit_state'), ('trans', '0107_migrate_state'), ('trans', '0108_auto_20171121_1608'), ('trans', '0109_auto_20171121_1921'), ('trans', '0110_auto_20171122_1659'), ('trans', '0111_count_approved'), ('trans', '0112_auto_20171129_2009'), ('trans', '0113_auto_20171205_1424'), ('trans', '0114_remove_translation_enabled'), ('trans', '0115_auto_20171213_0958'), ('trans', '0116_project_enable_review'), ('trans', '0117_auto_20180104_1331'), ('trans', '0118_delete_advertisement'), ('trans', '0119_auto_20180124_1145'), ('trans', '0120_auto_20180129_1253'), ('trans', '0121_update_plurals'), ('trans', '0122_auto_20180129_1507'), ('trans', '0123_auto_20180215_1147'), ('trans', '0124_auto_20180215_1158'), ('trans', '0125_auto_20180309_1505'), ('trans', '0126_whiteboardmessage_message_html'), ('trans', '0127_auto_20180320_1547'), ('trans', '0128_componentlist_show_dashboard'), ('trans', '0129_auto_20180416_1541'), ('trans', '0130_auto_20180416_1503'), ('trans', '0131_auto_20180416_1610'), ('trans', '0132_auto_20180517_1413'), ('trans', '0133_auto_20180517_1425'), ('trans', '0134_auto_20180517_1624'), ('trans', '0135_auto_20180518_1149'), ('trans', '0136_auto_20180521_1048'), ('trans', '0137_commit_formatting'), ('trans', '0138_auto_20180521_1116'), ('trans', '0139_source_context'), ('trans', '0140_change_project'), ('trans', '0141_component_linked_component'), ('trans', '0142_linked_component_data'), ('trans', '0143_auto_20180609_1655')]

    initial = True

    dependencies = [
        ('lang', '0007_migrate_plurals'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Change',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('action', models.IntegerField(choices=[(0, 'Resource update'), (1, 'Translation completed'), (2, 'Translation changed'), (5, 'New translation'), (3, 'Comment added'), (4, 'Suggestion added'), (6, 'Automatic translation'), (7, 'Suggestion accepted'), (8, 'Translation reverted'), (9, 'Translation uploaded'), (10, 'Glossary added'), (11, 'Glossary updated'), (12, 'Glossary uploaded'), (13, 'New source string'), (14, 'Component locked'), (15, 'Component unlocked'), (16, 'Detected duplicate string'), (17, 'Committed changes'), (18, 'Pushed changes'), (19, 'Reset repository'), (20, 'Merged repository'), (21, 'Rebased repository'), (22, 'Failed merge on repository'), (23, 'Failed rebase on repository'), (28, 'Failed push on repository'), (24, 'Parse error'), (25, 'Removed translation'), (26, 'Suggestion removed'), (27, 'Search and replace'), (29, 'Suggestion removed during cleanup'), (30, 'Source string changed'), (31, 'New string added'), (32, 'Mass state change'), (33, 'Changed visibility'), (34, 'Added user'), (35, 'Removed user')], default=2)),
                ('target', models.TextField(blank=True, default='')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lang.Language')),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(db_index=True, max_length=190)),
                ('target', models.CharField(max_length=190)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lang.Language')),
            ],
            options={
                'ordering': ['source'],
            },
        ),
        migrations.CreateModel(
            name='IndexUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.BooleanField(default=True)),
                ('to_delete', models.BooleanField(default=False)),
                ('unitid', models.IntegerField(unique=True)),
                ('language_code', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Display name', max_length=60, unique=True, verbose_name='Project name')),
                ('slug', models.SlugField(help_text='Name used in URLs and filenames.', max_length=60, unique=True, verbose_name='URL slug')),
                ('web', models.URLField(help_text='Main website of translated project.', verbose_name='Project website')),
                ('mail', models.EmailField(blank=True, help_text='Mailing list for translators.', max_length=254, verbose_name='Mailing list')),
                ('instructions', models.URLField(blank=True, help_text='URL with instructions for translators.', verbose_name='Translation instructions')),
                ('set_translation_team', models.BooleanField(default=True, help_text='Lets Weblate update the \"Translation-Team\" file header of your project.', verbose_name='Set "Translation-Team" header')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
            bases=(models.Model, weblate.trans.mixins.URLMixin, weblate.trans.mixins.PathMixin),
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('priority', models.IntegerField(choices=[(60, 'Very high'), (80, 'High'), (100, 'Medium'), (120, 'Low'), (140, 'Very low')], default=100)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Display name', max_length=100, verbose_name='Component name')),
                ('slug', models.SlugField(help_text='Name used in URLs and filenames.', max_length=100, verbose_name='URL slug')),
                ('repo', models.CharField(help_text='URL of a repository, use weblate://project/component to share it with other component.', max_length=200, verbose_name='Source code repository')),
                ('push', models.CharField(blank=True, help_text='URL of a push repository, pushing is turned off if empty.', max_length=200, verbose_name='Repository push URL')),
                ('repoweb', models.URLField(blank=True, help_text='Link to repository browser, use %(branch)s for branch, %(file)s and %(line)s as filename and line placeholders.', validators=[weblate.utils.render.validate_repoweb], verbose_name='Repository browser')),
                ('git_export', models.CharField(blank=True, help_text='URL of repository where users can fetch changes from Weblate', max_length=200, verbose_name='Exported repository URL')),
                ('report_source_bugs', models.EmailField(blank=True, help_text='Email address for reports on errors in source strings. Leave empty for no emails.', max_length=254, verbose_name='Source string bug reporting address')),
                ('branch', models.CharField(blank=True, default='', help_text='Repository branch to translate', max_length=50, verbose_name='Repository branch')),
                ('filemask', models.CharField(help_text='Path of files to translate relative to repository root, use * instead of language code, for example: po/*.po or locale/*/LC_MESSAGES/django.po.', max_length=200, validators=[weblate.trans.validators.validate_filemask], verbose_name='Filemask')),
                ('template', models.CharField(blank=True, help_text='Filename of translation base file, containing all strings and their source; it is recommended for monolingual translation formats.', max_length=200, verbose_name='Monolingual base language file')),
                ('new_base', models.CharField(blank=True, help_text='Filename of file used for creating new translations. For gettext choose .pot file.', max_length=200, verbose_name='Base file for new translations')),
                ('file_format', models.CharField(choices=FILE_FORMATS.get_choices(), default='po', help_text='Automatic detection might fail for some formats and is slightly slower.', max_length=50, verbose_name='File format')),
                ('locked', models.BooleanField(default=False, help_text='Locked component will not get any translation updates.', verbose_name='Locked')),
                ('allow_translation_propagation', models.BooleanField(db_index=True, default=settings.DEFAULT_TRANSLATION_PROPAGATION, help_text='Whether translation updates in other components will cause automatic translation in this one', verbose_name='Allow translation propagation')),
                ('save_history', models.BooleanField(default=True, help_text='Whether Weblate should keep track of old translations.', verbose_name='Save translation history')),
                ('enable_suggestions', models.BooleanField(default=True, help_text='Whether to allow translation suggestions at all.', verbose_name='Turn on suggestions')),
                ('suggestion_voting', models.BooleanField(default=False, help_text='Whether users can vote for suggestions.', verbose_name='Suggestion voting')),
                ('suggestion_autoaccept', models.PositiveSmallIntegerField(default=0, help_text='Automatically accept suggestions with this number of votes, use 0 to disable.', validators=[weblate.trans.validators.validate_autoaccept], verbose_name='Autoaccept suggestions')),
                ('check_flags', models.TextField(blank=True, default='', help_text='Additional comma-separated flags to influence quality checks, check documentation for possible values.', validators=[weblate.trans.validators.validate_check_flags], verbose_name='Translation flags')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trans.Project', verbose_name='Project')),
            ],
            options={
                'ordering': ['priority', 'project__name', 'name'],
                'verbose_name': 'Component',
                'verbose_name_plural': 'Components',
            },
            bases=(models.Model, weblate.trans.mixins.URLMixin, weblate.trans.mixins.PathMixin),
        ),
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.TextField()),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lang.Language')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trans.Project')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('revision', models.CharField(blank=True, default='', max_length=100)),
                ('filename', models.CharField(max_length=200)),
                ('language_code', models.CharField(blank=True, default='', max_length=20)),
                ('commit_message', models.TextField(blank=True, default='')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lang.Language')),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trans.Component')),
            ],
            options={
                'ordering': ['language__name'],
            },
            bases=(models.Model, weblate.trans.mixins.URLMixin),
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.TextField(blank=True, default='')),
                ('context', models.TextField(blank=True, default='')),
                ('comment', models.TextField(blank=True, default='')),
                ('flags', models.TextField(blank=True, default='')),
                ('source', models.TextField()),
                ('previous_source', models.TextField(blank=True, default='')),
                ('target', models.TextField(blank=True, default='')),
                ('position', models.IntegerField()),
                ('has_suggestion', models.BooleanField(db_index=True, default=False)),
                ('has_comment', models.BooleanField(db_index=True, default=False)),
                ('has_failing_check', models.BooleanField(db_index=True, default=False)),
                ('num_words', models.IntegerField(default=0)),
                ('priority', models.IntegerField(default=100)),
                ('translation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trans.Translation')),
                ('content_hash', models.BigIntegerField(db_index=True)),
                ('id_hash', models.BigIntegerField()),
                ('pending', models.BooleanField(default=False)),
                ('state', models.IntegerField(choices=[(0, 'Empty'), (10, 'Needs editing'), (20, 'Translated'), (30, 'Approved')], db_index=True, default=0)),
            ],
            options={
                'ordering': ['priority', 'position'],
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positive', models.BooleanField(default=True)),
                ('suggestion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trans.Suggestion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WhiteboardMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='Message')),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lang.Language', verbose_name='Language')),
            ],
            options={
                'verbose_name': 'Whiteboard message',
                'verbose_name_plural': 'Whiteboard messages',
            },
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set([('suggestion', 'user')]),
        ),
        migrations.AddField(
            model_name='suggestion',
            name='votes',
            field=models.ManyToManyField(related_name='user_votes', through='trans.Vote', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='component',
            unique_together=set([('project', 'name'), ('project', 'slug')]),
        ),
        migrations.AddField(
            model_name='source',
            name='component',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trans.Component'),
        ),
        migrations.AddField(
            model_name='source',
            name='check_flags',
            field=models.TextField(blank=True, default='', validators=[weblate.trans.validators.validate_check_flags]),
        ),
        migrations.AddField(
            model_name='dictionary',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trans.Project'),
        ),
        migrations.AddField(
            model_name='comment',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trans.Project'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='change',
            name='dictionary',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trans.Dictionary'),
        ),
        migrations.AddField(
            model_name='change',
            name='translation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trans.Translation'),
        ),
        migrations.AddField(
            model_name='change',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trans.Unit'),
        ),
        migrations.AddField(
            model_name='change',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='enable_hooks',
            field=models.BooleanField(default=True, help_text='Whether to allow updating this repository by remote hooks.', verbose_name='Enable hooks'),
        ),
        migrations.AddField(
            model_name='component',
            name='commit_message',
            field=models.TextField(default=settings.DEFAULT_COMMIT_MESSAGE, help_text='You can use template language for various info, please consult the documentation for more details.', validators=[weblate.utils.render.validate_render_commit], verbose_name='Commit message when translating'),
        ),
        migrations.AddField(
            model_name='component',
            name='committer_email',
            field=models.EmailField(default=settings.DEFAULT_COMMITER_EMAIL, max_length=254, verbose_name='Committer email'),
        ),
        migrations.AddField(
            model_name='component',
            name='committer_name',
            field=models.CharField(default=settings.DEFAULT_COMMITER_NAME, max_length=200, verbose_name='Committer name'),
        ),
        migrations.AddField(
            model_name='component',
            name='license',
            field=models.CharField(blank=True, default='', help_text='Optional short summary of license used for translations.', max_length=150, verbose_name='Translation license'),
        ),
        migrations.AddField(
            model_name='component',
            name='license_url',
            field=models.URLField(blank=True, default='', help_text='Optional URL with license details.', verbose_name='License URL'),
        ),
        migrations.AddField(
            model_name='component',
            name='merge_style',
            field=models.CharField(choices=[('merge', 'Merge'), ('rebase', 'Rebase')], default=settings.DEFAULT_MERGE_STYLE, help_text='Define whether Weblate should merge the upstream repository or rebase changes onto it.', max_length=10, verbose_name='Merge style'),
        ),
        migrations.AddField(
            model_name='component',
            name='new_lang',
            field=models.CharField(choices=[('contact', 'Use contact form'), ('url', 'Point to translation instructions URL'), ('add', 'Automatically add language file'), ('none', 'No language additions')], default='add', help_text='How to handle requests for creating new translations.', max_length=10, verbose_name='New translation'),
        ),
        migrations.AddField(
            model_name='component',
            name='vcs',
            field=models.CharField(choices=VCS_REGISTRY.get_choices(), default=settings.DEFAULT_VCS, help_text='Version control system to use to access your repository containing translations. You can also choose additional integration with third party providers to submit merge requests.', max_length=20, verbose_name='Version control system'),
        ),
        migrations.AddField(
            model_name='component',
            name='edit_template',
            field=models.BooleanField(default=True, help_text='Whether users will be able to edit the base file for monolingual translations.', verbose_name='Edit base file'),
        ),
        migrations.AddField(
            model_name='change',
            name='component',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trans.Component'),
        ),
        migrations.AddField(
            model_name='component',
            name='agreement',
            field=models.TextField(blank=True, default='', help_text='User agreement which needs to be approved before a user can translate this component.', verbose_name='Contributor agreement'),
        ),
        migrations.AddField(
            model_name='component',
            name='language_regex',
            field=weblate.trans.fields.RegexField(default='^[^.]+$', help_text='Regular expression used to filter translation when scanning for filemask.', max_length=200, verbose_name='Language filter'),
        ),
        migrations.AddField(
            model_name='project',
            name='source_language',
            field=models.ForeignKey(default=weblate.lang.models.get_english_lang, help_text='Language used for source strings in all components', on_delete=django.db.models.deletion.CASCADE, to='lang.Language', verbose_name='Source language'),
        ),
        migrations.AddField(
            model_name='whiteboardmessage',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trans.Project', verbose_name='Project'),
        ),
        migrations.AddField(
            model_name='whiteboardmessage',
            name='component',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trans.Component', verbose_name='Component'),
        ),
        migrations.CreateModel(
            name='ComponentList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Display name', max_length=100, unique=True, verbose_name='Component list name')),
                ('slug', models.SlugField(help_text='Name used in URLs and filenames.', max_length=100, unique=True, verbose_name='URL slug')),
                ('components', models.ManyToManyField(to='trans.Component', blank=True)),
            ],
            options={
                'verbose_name': 'Component list',
                'verbose_name_plural': 'Component lists',
                'ordering': ['name'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='unit',
            unique_together=set([('translation', 'id_hash')]),
        ),
        migrations.AddField(
            model_name='whiteboardmessage',
            name='category',
            field=models.CharField(choices=[('info', 'Info (light blue)'), ('warning', 'Warning (yellow)'), ('danger', 'Danger (red)'), ('success', 'Success (green)'), ('primary', 'Primary (dark blue)')], default='info', help_text='Category defines color used for the message.', max_length=25, verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='component',
            name='add_message',
            field=models.TextField(default=settings.DEFAULT_ADD_MESSAGE, help_text='You can use template language for various info, please consult the documentation for more details.', validators=[weblate.utils.render.validate_render_commit], verbose_name='Commit message when adding translation'),
        ),
        migrations.AddField(
            model_name='component',
            name='delete_message',
            field=models.TextField(default=settings.DEFAULT_DELETE_MESSAGE, help_text='You can use template language for various info, please consult the documentation for more details.', validators=[weblate.utils.render.validate_render_commit], verbose_name='Commit message when removing translation'),
        ),
        migrations.AddField(
            model_name='component',
            name='priority',
            field=models.IntegerField(choices=[(60, 'Very high'), (80, 'High'), (100, 'Medium'), (120, 'Low'), (140, 'Very low')], default=100, help_text='Components with higher priority are offered first to translators.', verbose_name='Priority'),
        ),
        migrations.AddField(
            model_name='comment',
            name='content_hash',
            field=models.BigIntegerField(),
        ),
        migrations.AddField(
            model_name='suggestion',
            name='content_hash',
            field=models.BigIntegerField(),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='source',
            name='id_hash',
            field=models.BigIntegerField(),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='AutoComponentList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_match', weblate.trans.fields.RegexField(default='^$', help_text='Regular expression which is used to match project slug.', max_length=200, verbose_name='Project regular expression')),
                ('component_match', weblate.trans.fields.RegexField(default='^$', help_text='Regular expression which is used to match component slug.', max_length=200, verbose_name='Component regular expression')),
                ('componentlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trans.ComponentList', verbose_name='Component list to assign')),
            ],
            options={
                'verbose_name': 'Automatic component list assignment',
                'verbose_name_plural': 'Automatic component list assignments',
            },
        ),
        migrations.AddField(
            model_name='change',
            name='old',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='suggestion',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='component',
            name='commit_pending_age',
            field=models.IntegerField(default=settings.COMMIT_PENDING_HOURS, help_text='Time in hours after which any pending changes will be committed to the VCS.', verbose_name='Age of changes to commit'),
        ),
        migrations.AddField(
            model_name='component',
            name='push_on_commit',
            field=models.BooleanField(default=settings.DEFAULT_PUSH_ON_COMMIT, help_text='Whether the repository should be pushed upstream on every commit.', verbose_name='Push on commit'),
        ),
        migrations.AddField(
            model_name='project',
            name='access_control',
            field=models.IntegerField(choices=[(0, 'Public'), (1, 'Protected'), (100, 'Private'), (200, 'Custom')], default=settings.DEFAULT_ACCESS_CONTROL, help_text='How to restrict access to this project is detailed in the documentation.', verbose_name='Access control'),
        ),
        migrations.AddField(
            model_name='project',
            name='enable_review',
            field=models.BooleanField(default=False, help_text='Requires dedicated reviewers to approve translations.', verbose_name='Enable reviews'),
        ),
        migrations.AddField(
            model_name='translation',
            name='plural',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lang.Plural'),
        ),
        migrations.AlterIndexTogether(
            name='unit',
            index_together=set([('priority', 'position'), ('translation', 'pending')]),
        ),
        migrations.AlterIndexTogether(
            name='comment',
            index_together=set([('project', 'language', 'content_hash')]),
        ),
        migrations.AlterIndexTogether(
            name='suggestion',
            index_together=set([('project', 'language', 'content_hash')]),
        ),
        migrations.AddField(
            model_name='whiteboardmessage',
            name='message_html',
            field=models.BooleanField(default=False, blank=True, help_text='When turned off, URLs will be converted to links and any markup will be escaped.', verbose_name='Render as HTML'),
        ),
        migrations.AddField(
            model_name='componentlist',
            name='show_dashboard',
            field=models.BooleanField(db_index=True, default=True, help_text='When enabled this component list will be shown as a tab on the dashboard', verbose_name='Show on dashboard'),
        ),
        migrations.AlterUniqueTogether(
            name='source',
            unique_together=set([('id_hash', 'component')]),
        ),
        migrations.AlterUniqueTogether(
            name='translation',
            unique_together=set([('component', 'language')]),
        ),
        migrations.AddField(
            model_name='change',
            name='details',
            field=weblate.utils.fields.JSONField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='change',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trans.Project'),
        ),
        migrations.CreateModel(
            name='ContributorAgreement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trans.Component')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user__username'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='contributoragreement',
            unique_together=set([('user', 'component')]),
        ),
        migrations.AddField(
            model_name='source',
            name='context',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='component',
            name='linked_component',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='trans.Component', verbose_name='Project'),
        ),
    ]
