#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Bot client dedicated to Google services.

"""
from ...apis import GoogleServiceAPI


__all__ = ["GoogleSearchBot"]


class GoogleSearchBot(Template):
    """
    GoogleSearchBot class for performing text searches.
    
    Example:
    
        >>> from pybots import GoogleSearchBot
        >>> with GoogleSearchBot("...api-key...") as bot:
                bot.search("test", count=10)
    """
    def __init__(self, *args, **kwargs):
        pass
        #TODO

