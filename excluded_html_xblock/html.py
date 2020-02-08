"""This XBlock help creating a secure and easy-to-use HTML blocks in edx-platform."""
from __future__ import absolute_import

import logging

from html_xblock import HTML5XBlock
from html_xblock.utils import _  # pylint: disable=protected-access
from xblock.completable import XBlockCompletionMode
from xblock.fields import Scope, String
from xblockutils.resources import ResourceLoader

log = logging.getLogger(__name__)  # pylint: disable=invalid-name
xblock_loader = ResourceLoader(__name__)  # pylint: disable=invalid-name


class ExcludedHTML5XBlock(HTML5XBlock):
    """
    This XBlock will disable completion and add provide and  an HTML WYSIWYG interface in Studio to be rendered in LMS.
    """

    display_name = String(
        display_name=_('Display Name'),
        help=_('The display name for this component.'),
        scope=Scope.settings,
        default=_('Exclusion')
    )
    has_custom_completion = True
    completion_mode = XBlockCompletionMode.EXCLUDED
