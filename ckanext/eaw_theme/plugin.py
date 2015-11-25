import ckan.plugins as plugins
import ckan.plugins.toolkit as tk


class Eaw_ThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    # IConfigurer

    def update_config(self, config_):
        tk.add_template_directory(config_, 'templates')
        tk.add_public_directory(config_, 'public')
        tk.add_resource('fanstatic/vendor/bootstrap-switch', 'bootstrap-switch')
        tk.add_resource('fanstatic', 'eaw_theme')

