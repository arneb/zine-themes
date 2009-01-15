# -*- coding: utf-8 -*-
"""
    kubrick_theme
    ~~~~~~~~~~~~~
    
    A port of the famous Kubrick theme for the Zine blogging engine.
    Some of the code in this file is taken from the bundled vessel theme.
    
    :copyright: (c) Arne Brodowski, Michael Heilemann 
    :license: GPL.
"""
from os.path import join, dirname
from zine.api import url_for, _
from zine.views.admin import render_admin_response
from zine.utils.admin import flash
from zine.utils import forms
from widgets import ListPages, MetaInfo


TEMPLATE_FILES = join(dirname(__file__), 'templates')
SHARED_FILES = join(dirname(__file__), 'shared')


blue_variation = u'kubrick_theme::blue.css'
variations = {
    blue_variation:             _('Blue'),
}

class ConfigurationForm(forms.Form):
    """Very simple form for the variation selection."""
    variation = forms.ChoiceField(_('Variation'))

    def __init__(self, initial=None):
        forms.Form.__init__(self, initial)
        choices = sorted(variations.items(), key=lambda x: x[1].lower())
        self.fields['variation'].choices = choices

def configure(request):
    """This callback is called from the admin panel if the theme configuration
    page is opened.  Because only the active theme can be configured it's
    perfectly okay to ship the template for the configuration page as part of
    the theme template folder.  No need to register a separate template folder
    just for the admin panel template.
    """
    cfg = request.app.cfg
    form = ConfigurationForm(initial=dict(
        variation=cfg['kubrick_theme/variation']
    ))

    if request.method == 'POST':
        if 'cancel' in request.form:
            return form.redirect('admin/theme')
        elif form.validate(request.form):
            flash(_('Variation changed successfully.'), 'configure')
            cfg.change_single('kubrick_theme/variation', form['variation'])
            return form.redirect('admin/theme')

    return render_admin_response('admin/configure_kubrick_theme.html',
                                 'options.theme', form=form.as_widget())


def add_variation(spec, title):
    """Registers a new variation."""
    variations[spec] = title
    
    
def setup(app, plugin):
    app.add_theme('kubrick', TEMPLATE_FILES, plugin.metadata, configuration_page=configure)
    app.add_shared_exports('kubrick_theme', SHARED_FILES)
    app.add_config_var('kubrick_theme/variation', forms.TextField(default=blue_variation))
    app.add_widget(ListPages)
    app.add_widget(MetaInfo)
    
