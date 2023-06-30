# -*- coding: utf-8 -*-

import re

class AddressUtil:
    def __init__(self):
        pass

    def isFile(self, content):
        return content.startswith("file://")

    def getFileName(self, content):
        if self.isFile(content):
            filename = re.sub("^file://(.*)$", "\g<1>", content)
            return filename

    def getAddressList(self, content):
        return content.split("\n")





