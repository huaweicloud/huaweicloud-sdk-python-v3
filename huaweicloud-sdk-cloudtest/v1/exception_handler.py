# -*- coding: utf-8 -*-

import json

from huaweicloudsdkcore.exceptions import exceptions

def handle_exception(response_body):
    return exceptions.SdkError()