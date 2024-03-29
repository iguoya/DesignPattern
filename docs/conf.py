# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------

project = '设计模式C++版'
copyright = '2022, tiger'
author = 'tiger'

# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # 'recommonmark',
    # 'sphinx_markdown_tables',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.graphviz',
    'sphinxcontrib.mermaid',
    'sphinxcontrib.plantuml',
    'sphinxcontrib.needs',
    'myst_parser',
    'sphinx_gallery.gen_gallery',
    'sphinx.ext.intersphinx',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# source_parsers = {
#     '.md': 'recommonmark.parser.CommonMarkParser',
# }

source_suffix = ['.rst']

# on_rtd = os.environ.get('READTHEDOCS') == 'True'
# if on_rtd:
#     plantuml = 'java -Djava.awt.headless=true -jar ./utils/plantuml.jar'
# else:
#     plantuml = 'java -jar %s' % os.path.join(os.path.dirname(__file__), "utils", "plantuml.jar")

# plantuml_output_format = 'png'


sphinx_gallery_conf = {
    # path to your example scripts
    'examples_dirs': ['sample-gallery-1', 'sample-gallery-2'],
    # path to where to save gallery generated output
    'gallery_dirs': ['auto_gallery-1', 'auto_gallery-2'],
    # specify that examples should be ordered according to filename
    # 'within_subsection_order': FileNameSortKey,
    # directory where function granular galleries are stored
    'backreferences_dir': 'gen_modules/backreferences',
    # Modules for which function level galleries are created.  In
    # this case sphinx_gallery and numpy in a tuple of strings.
    # 'doc_module': ('SampleModule'),
}
