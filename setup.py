"""Setup for excluded html XBlock."""

import os

from setuptools import setup


def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='excluded-html-xblock',
    version='0.1',
    description='HTML XBlock will help creating and using a secure, easy-to-use excluded HTML blocks',
    license='AGPL v3',
    packages=[
        'excluded_html_xblock',
    ],
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': [
            'excluded_html = excluded_html_xblock:ExcludedHtmlBlock',
        ]
    },
    package_data=package_data("excluded_html_xblock", ["static", "public"]),
)
