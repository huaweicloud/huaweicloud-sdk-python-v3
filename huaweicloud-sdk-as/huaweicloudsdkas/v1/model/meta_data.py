# coding: utf-8

import pprint
import re

import six





class MetaData:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'customize_key': 'str'
    }

    attribute_map = {
        'customize_key': 'customize_key'
    }

    def __init__(self, customize_key=None):
        """MetaData - a model defined in huaweicloud sdk"""
        
        

        self._customize_key = None
        self.discriminator = None

        if customize_key is not None:
            self.customize_key = customize_key

    @property
    def customize_key(self):
        """Gets the customize_key of this MetaData.

        用户自定义数据总长度不大于512字节。用户自定义键不能是空串，不能包含符号.，以及不能以符号$开头。说明：Windows弹性云服务器Administrator用户的密码。示例：键（固定）：admin_pass值：cloud.1234创建密码方式鉴权的Windows弹性云服务器时为必选字段。

        :return: The customize_key of this MetaData.
        :rtype: str
        """
        return self._customize_key

    @customize_key.setter
    def customize_key(self, customize_key):
        """Sets the customize_key of this MetaData.

        用户自定义数据总长度不大于512字节。用户自定义键不能是空串，不能包含符号.，以及不能以符号$开头。说明：Windows弹性云服务器Administrator用户的密码。示例：键（固定）：admin_pass值：cloud.1234创建密码方式鉴权的Windows弹性云服务器时为必选字段。

        :param customize_key: The customize_key of this MetaData.
        :type: str
        """
        self._customize_key = customize_key

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
        if not isinstance(other, MetaData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
