# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .sponsored_message import SponsoredMessage
from ..base_object import BaseObject


class SponsoredMessages(BaseObject):
    """
    Contains a list of sponsored messages
    
    Params:
        messages (:obj:`list[SponsoredMessage]`)
            List of sponsored messages
        
    """

    ID: str = Field("sponsoredMessages", alias="@type")
    messages: list[SponsoredMessage]

    @staticmethod
    def read(q: dict) -> SponsoredMessages:
        return SponsoredMessages.construct(**q)