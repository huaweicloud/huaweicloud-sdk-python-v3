# coding: utf-8

import pprint
import re

import six





class PreheatingTaskBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'urls': 'list[str]'
    }

    attribute_map = {
        'urls': 'urls'
    }

    def __init__(self, urls=None):
        """PreheatingTaskBody - a model defined in huaweicloud sdk"""
        
        

        self._urls = None
        self.discriminator = None

        self.urls = urls

    @property
    def urls(self):
        """Gets the urls of this PreheatingTaskBody.

        输入示例：abc.com/image/1.png，多个URL之间需要用逗号分隔，目前不支持对目录的预热，单个url的长度限制为10240字符,单次最多输入1000个url。

        :return: The urls of this PreheatingTaskBody.
        :rtype: list[str]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        """Sets the urls of this PreheatingTaskBody.

        输入示例：abc.com/image/1.png，多个URL之间需要用逗号分隔，目前不支持对目录的预热，单个url的长度限制为10240字符,单次最多输入1000个url。

        :param urls: The urls of this PreheatingTaskBody.
        :type: list[str]
        """
        self._urls = urls

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
        if not isinstance(other, PreheatingTaskBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
