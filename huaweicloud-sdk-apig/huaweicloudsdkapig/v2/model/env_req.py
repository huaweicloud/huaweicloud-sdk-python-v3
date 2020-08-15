# coding: utf-8

import pprint
import re

import six





class EnvReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'remark': 'str'
    }

    attribute_map = {
        'name': 'name',
        'remark': 'remark'
    }

    def __init__(self, name=None, remark=None):
        """EnvReq - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._remark = None
        self.discriminator = None

        self.name = name
        if remark is not None:
            self.remark = remark

    @property
    def name(self):
        """Gets the name of this EnvReq.

        环境的名称，支持英文，数字，下划线，且只能以英文字母开头。

        :return: The name of this EnvReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EnvReq.

        环境的名称，支持英文，数字，下划线，且只能以英文字母开头。

        :param name: The name of this EnvReq.
        :type: str
        """
        self._name = name

    @property
    def remark(self):
        """Gets the remark of this EnvReq.

        描述信息 > 中文字符必须为UTF-8或者unicode编码。

        :return: The remark of this EnvReq.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this EnvReq.

        描述信息 > 中文字符必须为UTF-8或者unicode编码。

        :param remark: The remark of this EnvReq.
        :type: str
        """
        self._remark = remark

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
        if not isinstance(other, EnvReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
