# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class LoadQuickReplyShortcuts(BaseObject):
    """
    Loads quick reply shortcuts created by the current user. The loaded topics will be sent through updateQuickReplyShortcuts
    """

    ID: typing.Literal["loadQuickReplyShortcuts"] = Field(
        "loadQuickReplyShortcuts", validation_alias="@type", alias="@type"
    )