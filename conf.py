
project = "Camera Projection Painter"
author = "Vlad Kuzmin (ssh4), Ivan Perevala (ivpe)"
version = "3.6.0"

extensions = [
    "sphinx.ext.coverage",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
    "sphinx_rtd_theme",
]

source_suffix = '.rst'
master_doc = 'index'

language = "uk"
locale_dirs = ['locale/']
gettext_compact = True

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_templates_path = ["_templates"]
html_theme_options = {
    "display_version": True,
    "style_external_links": True,
}
