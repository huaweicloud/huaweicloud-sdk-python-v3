# coding: utf-8

import pprint
import re

import six





class ParamsReqBean:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'target_value': 'str'
    }

    attribute_map = {
        'key': 'key',
        'target_value': 'target_value'
    }

    def __init__(self, key=None, target_value=None):
        """ParamsReqBean - a model defined in huaweicloud sdk"""
        
        

        self._key = None
        self._target_value = None
        self.discriminator = None

        self.key = key
        self.target_value = target_value

    @property
    def key(self):
        """Gets the key of this ParamsReqBean.

        数据库参数名

        :return: The key of this ParamsReqBean.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ParamsReqBean.

        数据库参数名

        :param key: The key of this ParamsReqBean.
        :type: str
        """
        self._key = key

    @property
    def target_value(self):
        """Gets the target_value of this ParamsReqBean.

        目标数据库参数值

        :return: The target_value of this ParamsReqBean.
        :rtype: str
        """
        return self._target_value

    @target_value.setter
    def target_value(self, target_value):
        """Sets the target_value of this ParamsReqBean.

        目标数据库参数值

        :param target_value: The target_value of this ParamsReqBean.
        :type: str
        """
        self._target_value = target_value

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
        if not isinstance(other, ParamsReqBean):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other