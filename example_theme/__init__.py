from os.path import join, dirname
from zine.api import _
from zine.plugins import kubrick_theme


SHARED_FILES = join(dirname(__file__), 'shared')


def setup(app, plugin):
    app.add_shared_exports('example_theme', SHARED_FILES)
    kubrick_theme.add_variation(u'example_theme::example.css', _('Example'))