import datetime
import ast
import os
import yaml

# Configuration for the Sphinx documentation builder.
# All configuration specific to your project should be done in this file.
#
# If you're new to Sphinx and don't want any advanced or custom features,
# just go through the items marked 'TODO'.
#
# A complete list of built-in Sphinx configuration values:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
#
# Our starter pack uses the custom Canonical Sphinx extension
# to keep all documentation based on it consistent and on brand:
# https://github.com/canonical/canonical-sphinx


#######################
# Project information #
#######################

# Project name
#
#
# DONE: Update with the official name of your project or product


project = "Ubuntu Boards"
author = "Canonical Ltd."
version = '0.1'

# Sidebar documentation title; best kept reasonably short
#
# DONE: To include a version number, add it here (hardcoded or automated).
#
# DONE: To disable the title, set to an empty string.

html_title = f'{project} documentation'


# Copyright string; shown at the bottom of the page
#
# Now, the starter pack uses CC-BY-SA as the license
# and the current year as the copyright year.
#
# DONE: If your docs need another license, specify it instead of 'CC-BY-SA'.
#
# DONE: If your documentation is a part of the code repository of your project,
#       it inherits the code license instead; specify it instead of 'CC-BY-SA'.
#
# NOTE: For static works, it is common to provide the first publication year.
#       Another option is to provide both the first year of publication
#       and the current year, especially for docs that frequently change,
#       e.g. 2022–2023 (note the en-dash).
#
#       A way to check a repo's creation date is to get a classic GitHub token
#       with 'repo' permissions; see https://github.com/settings/tokens
#       Next, use 'curl' and 'jq' to extract the date from the API's output:
#
#       curl -H 'Authorization: token <TOKEN>' \
#         -H 'Accept: application/vnd.github.v3.raw' \
#         https://api.github.com/repos/canonical/<REPO> | jq '.created_at'

copyright = f'{datetime.date.today():%Y} CC-BY-SA, {author}'


# Documentation website URL
#
# DONE: Update with the official URL of your docs or leave empty if unsure.
#
# NOTE: The Open Graph Protocol (OGP) enhances page display in a social graph
#       and is used by social media platforms; see https://ogp.me/

ogp_site_url = "https://canonical-ubuntu-boards.readthedocs-hosted.com/"


# Preview name of the documentation website
#
# DONE: To use a different name for the project in previews, update as needed.

ogp_site_name = project


# Preview image URL
#
# DONE: To customise the preview image, update as needed.

ogp_image = "https://assets.ubuntu.com/v1/253da317-image-document-ubuntudocs.svg"


# Product favicon; shown in bookmarks, browser tabs, etc.

# DONE: To customise the favicon, uncomment and update as needed.

# html_favicon = '.sphinx/_static/favicon.png'


# Dictionary of values to pass into the Sphinx context for all pages:
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_context

html_context = {
    # Product page URL; can be different from product docs URL
    #
    # DONE: Change to your product website URL,
    #       dropping the 'https://' prefix, e.g. 'ubuntu.com/lxd'.
    #
    # DONE: If there's no such website,
    #       remove the {{ product_page }} link from the page header template
    #       (usually .sphinx/_templates/header.html; also, see README.rst).
    "product_page": "ubuntu.com",
    # Product tag image; the orange part of your logo, shown in the page header
    #
    # DONE: To add a tag image, uncomment and update as needed.
    # 'product_tag': '_static/tag.png',
    # Your Discourse instance URL
    #
    # DONE: Change to your Discourse instance URL or leave empty.
    #
    # NOTE: If set, adding ':discourse: 123' to an .rst file
    #       will add a link to Discourse topic 123 at the bottom of the page.
    "discourse": "https://discourse.ubuntu.com/c/foundations/",
    # Your Mattermost channel URL
    #
    # DONE: Change to your Mattermost channel URL or leave empty.
    "mattermost": "",
    # Your Matrix channel URL
    #
    # DONE: Change to your Matrix channel URL or leave empty.
    "matrix": "",
    # Your documentation GitHub repository URL
    #
    # DONE: Change to your documentation GitHub repository URL or leave empty.
    #
    # NOTE: If set, links for viewing the documentation source files
    #       and creating GitHub issues are added at the bottom of each page.
    "github_url": "https://github.com/canonical/ubuntu-boards-documentation",
    # Docs branch in the repo; used in links for viewing the source files
    #
    # DONE: To customise the branch, uncomment and update as needed.
    'repo_default_branch': 'main',
    # Docs location in the repo; used in links for viewing the source files
    #


    # DONE: To customise the directory, uncomment and update as needed.
    "repo_folder": "/",
    # DONE: To enable or disable the Previous / Next buttons at the bottom of pages
    # Valid options: none, prev, next, both
    # "sequential_nav": "both",
    # DONE: To enable listing contributors on individual pages, set to True
    "display_contributors": False,

    # Required for feedback button    
    'github_issues': 'enabled',
}

# TODO: To enable the edit button on pages, uncomment and change the link to a
# public repository on GitHub or Launchpad. Any of the following link domains
# are accepted:
# - https://github.com/example-org/example"
# - https://launchpad.net/example
# - https://git.launchpad.net/example
#
html_theme_options = {
'source_edit_link': 'https://github.com/canonical/ubuntu-boards-documentation',
}

# Project slug; see https://meta.discourse.org/t/what-is-category-slug/87897
#
# DONE: If your documentation is hosted on https://docs.ubuntu.com/,
#       uncomment and update as needed.

# slug = ''


# Template and asset locations

html_static_path = []
templates_path = []


#############
# Redirects #
#############

# To set up redirects: https://documatt.gitlab.io/sphinx-reredirects/usage.html
# For example: 'explanation/old-name.html': '../how-to/prettify.html',

# To set up redirects in the Read the Docs project dashboard:
# https://docs.readthedocs.io/en/stable/guides/redirects.html

# NOTE: If undefined, set to None, or empty,
#       the sphinx_reredirects extension will be disabled.

redirects = {}


###########################
# Link checker exceptions #
###########################

# A regex list of URLs that are ignored by 'make linkcheck'
#
# DONE: Remove or adjust the ACME entry after you update the contributing guide

linkcheck_ignore = [
    "http://127.0.0.1:8000",
    "https://github.com/canonical/ACME/*",
    "https://www.gnu.org/software/grub/"
    ]


# A regex list of URLs where anchors are ignored by 'make linkcheck'

linkcheck_anchors_ignore_for_url = []

# give linkcheck multiple tries on failure
# linkcheck_timeout = 30
linkcheck_retries = 3

########################
# Configuration extras #
########################

# Custom MyST syntax extensions; see
# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html
#
# NOTE: By default, the following MyST extensions are enabled:
#       substitution, deflist, linkify

# myst_enable_extensions = set()


# Custom Sphinx extensions; see
# https://www.sphinx-doc.org/en/master/usage/extensions/index.html

# NOTE: The canonical_sphinx extension is required for the starter pack.
#       It automatically enables the following extensions:
#       - custom-rst-roles
#       - myst_parser
#       - notfound.extension
#       - related-links
#       - sphinx_copybutton
#       - sphinx_design
#       - sphinx_reredirects
#       - sphinx_tabs.tabs
#       - sphinxcontrib.jquery
#       - sphinxext.opengraph
#       - terminal-output
#       - youtube-links

extensions = [
    "canonical_sphinx",
    "sphinxcontrib.cairosvgconverter",
    "sphinx_last_updated_by_git",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "canonical.ubuntu-images",
]

# Excludes files or directories from processing

exclude_patterns = [
    "readme.rst",
    "doc-cheat-sheet*",
]

# Adds custom CSS files, located under 'html_static_path'

# html_css_files = []


# Adds custom JavaScript files, located under 'html_static_path'

# html_js_files = []


# Specifies a reST snippet to be appended to each .rst file

rst_epilog = """
.. include:: /reuse/links.txt
"""

# Feedback button at the top; enabled by default
#
# DONE: To disable the button, uncomment this.

# disable_feedback_button = True


# Your manpage URL
#
# DONE: To enable manpage links, uncomment and update as needed.
#
# NOTE: If set, adding ':manpage:' to an .rst file
#       adds a link to the corresponding man section at the bottom of the page.

# manpages_url = f'https://manpages.ubuntu.com/manpages/{codename}/en/' + \
#     f'man{section}/{page}.{section}.html'
# If you are using the :manpage: role, set this variable to the URL for the version
# that you want to link to:
manpages_url = (
    'https://manpages.ubuntu.com/manpages/noble/en/'
    'man{section}/{page}.{section}.html')



# Specifies a reST snippet to be prepended to each .rst file
# This defines a :center: role that centers table cell content.
# This defines a :h2: role that styles content for use with PDF generation.

rst_prolog = """
.. role:: center
   :class: align-center
.. role:: h2
    :class: hclass2
.. role:: woke-ignore
    :class: woke-ignore
.. role:: vale-ignore
    :class: vale-ignore
"""

# Workaround for https://github.com/canonical/canonical-sphinx/issues/34

if "discourse_prefix" not in html_context and "discourse" in html_context:
    html_context["discourse_prefix"] = html_context["discourse"] + "/t/"

# Set up some simple aliases for bugs and packages
extlinks = {
    'lp-bug': ('https://bugs.launchpad.net/bugs/%s', 'LP: #%s'),
    'lp-pkg': ('https://launchpad.net/ubuntu/+source/%s', '%s'),
}

# Ensure PDF output is useful when printed
latex_show_pagerefs = True
latex_show_urls = 'footnote'

intersphinx_mapping = {
    'subiquity': ('https://canonical-subiquity.readthedocs-hosted.com/en/latest', None),
    'cloudinit': ('https://cloudinit.readthedocs.io/en/latest/', None),
}
