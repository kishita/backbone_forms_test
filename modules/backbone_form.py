# -*- coding: utf-8 -*-
from gluon import *

# For referencing static and views from other application
import os
#APP = os.path.basename(os.path.dirname(os.path.dirname(__file__)))

def add_lib():
    _urls = [URL('static', 'plugin_managed_form/test/lib/qnit.css'),
             URL('static', 'plugin_managed_form/test/lib/jquery-ui/flick/jquery-ui-1.8.14.custom.css'),
             URL('static', 'plugin_managed_form/distribution/backbone-forms.css'),
             URL('static', 'plugin_managed_form/test/lib/jquery-1.7.2.min.js'),
             URL('static', 'plugin_managed_form/test/lib/jquery-ui/jquery-ui-1.8.14.custom.min.js'),
             URL('static', 'plugin_managed_form/test/lib/qunit.js'),
             URL('static', 'plugin_managed_form/test/lib/underscore-1.3.3.min.js'),
             URL('static', 'plugin_managed_form/test/lib/backbone-0.9.2.min.js'),
             URL('static', 'plugin_managed_form/test/lib/backbone-deep-model.js'),
             URL('static', 'plugin_managed_form/test/lib/handlebars-1.0.0.beta.6.js'),
             URL('static', 'plugin_managed_form/distribution/backbone-forms.min.js'),
             URL('static', 'plugin_managed_form/distribution/editors/jquery-ui.min.js')]
            # URL('static', 'plugin_managed_form/test/_setup.js'),
            # URL('static', 'plugin_managed_form/test/helpers.js'),
    		# URL('static', 'plugin_managed_form/test/form.js'),
            # URL('static', 'plugin_managed_form/test/field.js'),
            # URL('static', 'plugin_managed_form/test/editors.js'),
            # URL('static', 'plugin_managed_form/test/validators.js'),
            # URL('static', 'plugin_managed_form/test/jquery-ui-editors.js')]

    for _url in _urls:
        if _url not in current.response.files:
            current.response.files.append(_url)