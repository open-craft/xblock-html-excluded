"""
HTML XBlock tests
"""
from __future__ import print_function

import unittest

from xblock.completable import XBlockCompletionMode
from xblock.field_data import DictFieldData
from xblock.test.tools import TestRuntime

import excluded_html_xblock


class TestExcludedHTMLXBlock(unittest.TestCase):
    """
    Unit tests for `excluded_html_xblock`
    """

    def setUp(self):
        self.runtime = TestRuntime()

    def test_render(self):
        """
        Test a basic rendering.
        """
        field_data = DictFieldData({
            'data': 'Safe <b>html</b><script>alert(\'javascript\');</script>'
        })
        block = excluded_html_xblock.ExcludedHTML5XBlock(self.runtime, field_data, None)
        self.assertEqual(block.has_custom_completion, True)
        self.assertEqual(XBlockCompletionMode.get_mode(block), XBlockCompletionMode.EXCLUDED)

        fragment = block.student_view()
        self.assertIn(
            '<div>Safe <b>html</b>&lt;script&gt;alert(\'javascript\');&lt;/script&gt;</div>',
            fragment.content
        )
