# coding: utf-8

import pprint
import re

import six





class UpdateSubReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'callbackurl': 'str'
    }

    attribute_map = {
        'callbackurl': 'callbackurl'
    }

    def __init__(self, callbackurl=None):
        """UpdateSubReq - a model defined in huaweicloud sdk"""
        
        

        self._callbackurl = None
        self.discriminator = None

        if callbackurl is not None:
            self.callbackurl = callbackurl

    @property
    def callbackurl(self):
        """Gets the callbackurl of this UpdateSubReq.

        订阅的回调地址，用于接收对应资源事件的通知消息，例如：https://10.10.10.10:443/callbackurltest。

        :return: The callbackurl of this UpdateSubReq.
        :rtype: str
        """
        return self._callbackurl

    @callbackurl.setter
    def callbackurl(self, callbackurl):
        """Sets the callbackurl of this UpdateSubReq.

        订阅的回调地址，用于接收对应资源事件的通知消息，例如：https://10.10.10.10:443/callbackurltest。

        :param callbackurl: The callbackurl of this UpdateSubReq.
        :type: str
        """
        self._callbackurl = callbackurl

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateSubReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
