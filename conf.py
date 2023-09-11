
project = "Camera Projection Painter"
author = "Vlad Kuzmin (ssh4), Ivan Perevala (ivpe)"
version = "3.6.0"

extensions = [
    "sphinx.ext.coverage",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
]

source_suffix = '.rst'
master_doc = 'index'

language = "uk"  # Українською.

# sphinx-intl
locale_dirs = ['locale/']   # path is example but recommended.
gettext_compact = False     # optional.

# sphinx.ext.intersphinx
intersphinx_disabled_reftypes = ["*"]

# html
html_theme = "sphinx_rtd_theme"
html_logo = "bhq_logo_color_v0.svg"
html_static_path = ["_static"]
html_templates_path = ["_templates"]
html_theme_options = {
    "display_version": True,
    "style_external_links": True,
}

