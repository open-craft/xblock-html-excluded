"""This XBlock help creating a secure and easy-to-use HTML blocks in edx-platform."""
from __future__ import absolute_import

from xblock.completable import XBlockCompletionMode
from xblock.fields import (
    Scope,
    String,
)
from xblockutils.studio_editable import StudioEditableXBlockMixin
from xmodule.html_module import HtmlBlock

from .utils import _  # pylint: disable=protected-access


class ExcludedHtmlBlock(StudioEditableXBlockMixin, HtmlBlock):
    """
    This XBlock will disable completion and add provide an HTML WYSIWYG interface in Studio to be rendered in LMS.
    """

    display_name = String(
        display_name=_('Display Name'),
        help=_('The display name for this component.'),
        scope=Scope.settings,
        default=_('Exclusion')
    )
    editor = 'raw'
    has_custom_completion = True
    completion_mode = XBlockCompletionMode.EXCLUDED

    editable_fields = ('display_name', 'data')
    _class_tags = {}
