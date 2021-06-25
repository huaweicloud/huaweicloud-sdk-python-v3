# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class UpdateLogContents3Response(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'context': 'str'
    }

    attribute_map = {
        'context': 'context'
    }

    def __init__(self, context=None):
        """UpdateLogContents3Response - a model defined in huaweicloud sdk"""
        
        super(UpdateLogContents3Response, self).__init__()

        self._context = None
        self.discriminator = None

        if context is not None:
            self.context = context

    @property
    def context(self):
        """Gets the context of this UpdateLogContents3Response.

        查询结构化日志结果信息。此处仅为示例，具体参数名称取决于查询的字段。

        :return: The context of this UpdateLogContents3Response.
        :rtype: str
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this UpdateLogContents3Response.

        查询结构化日志结果信息。此处仅为示例，具体参数名称取决于查询的字段。

        :param context: The context of this UpdateLogContents3Response.
        :type: str
        """
        self._context = context

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
        if not isinstance(other, UpdateLogContents3Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other