"""
Featured metadata plugin for Pelican
====================================

Looks for an asset filename listed as "Feature: image.png" in the article metadata.
Process the tag and URLify the asset so it can be embedded by templates.

Settings:
FEATURED_ASSETS_PATH = 'static/assets'

The path to where featured assets are stored, recommended that you use one of your STATIC_PATHS.
"""


from pelican import signals


def process_feature(article_generator, metadata):
    if 'feature' in metadata.keys() and \
            'FEATURED_ASSETS_PATH' in article_generator.settings.keys():
        url = article_generator.settings['FEATURED_ASSETS_PATH'] + '/' + metadata['feature']
        metadata['feature_url'] = url


def register():
    signals.article_generate_context.connect(process_feature)