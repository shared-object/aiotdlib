# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetVideoChatRtmpUrl(BaseObject):
    """
    Returns RTMP URL for streaming to the chat; requires owner privileges

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["getVideoChatRtmpUrl"] = Field("getVideoChatRtmpUrl", validation_alias="@type", alias="@type")
    chat_id: Int53
