
project = "Camera Projection Painter"
author = "Vlad Erium (ssh4), Ivan Perevala (ivpe)"
version = "3.6.0"
copyright = "2023 BlenderHQ"

extensions = [
    "sphinx.ext.coverage",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
    "sphinx_rtd_theme",
]

source_suffix = '.rst'
master_doc = 'index'

language = "en"
locale_dirs = ['locale/']
gettext_compact = True
gettext_location = False

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_templates_path = ["_templates"]
html_theme_options = {
    "display_version": True,
    "style_external_links": True,
}
