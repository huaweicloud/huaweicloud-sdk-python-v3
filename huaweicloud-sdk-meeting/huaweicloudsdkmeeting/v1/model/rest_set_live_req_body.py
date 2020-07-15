# coding: utf-8

import pprint
import re

import six





class RestSetLiveReqBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'is_live': 'int'
    }

    attribute_map = {
        'is_live': 'isLive'
    }

    def __init__(self, is_live=0):
        """RestSetLiveReqBody - a model defined in huaweicloud sdk"""
        
        

        self._is_live = None
        self.discriminator = None

        self.is_live = is_live

    @property
    def is_live(self):
        """Gets the is_live of this RestSetLiveReqBody.

        默认值为0。 - 0: 停止会议直播。 - 1: 启动会议直播。

        :return: The is_live of this RestSetLiveReqBody.
        :rtype: int
        """
        return self._is_live

    @is_live.setter
    def is_live(self, is_live):
        """Sets the is_live of this RestSetLiveReqBody.

        默认值为0。 - 0: 停止会议直播。 - 1: 启动会议直播。

        :param is_live: The is_live of this RestSetLiveReqBody.
        :type: int
        """
        self._is_live = is_live

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
        if not isinstance(other, RestSetLiveReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
