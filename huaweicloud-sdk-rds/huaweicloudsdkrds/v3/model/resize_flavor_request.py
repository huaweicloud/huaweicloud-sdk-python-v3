# coding: utf-8

import pprint
import re

import six





class ResizeFlavorRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'spec_code': 'str',
        'is_auto_pay': 'bool'
    }

    attribute_map = {
        'spec_code': 'spec_code',
        'is_auto_pay': 'is_auto_pay'
    }

    def __init__(self, spec_code=None, is_auto_pay=None):
        """ResizeFlavorRequest - a model defined in huaweicloud sdk"""
        
        

        self._spec_code = None
        self._is_auto_pay = None
        self.discriminator = None

        self.spec_code = spec_code
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay

    @property
    def spec_code(self):
        """Gets the spec_code of this ResizeFlavorRequest.

        资源规格编码。

        :return: The spec_code of this ResizeFlavorRequest.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this ResizeFlavorRequest.

        资源规格编码。

        :param spec_code: The spec_code of this ResizeFlavorRequest.
        :type: str
        """
        self._spec_code = spec_code

    @property
    def is_auto_pay(self):
        """Gets the is_auto_pay of this ResizeFlavorRequest.

        变更包周期实例的规格时可指定，表示是否自动从客户的账户中支付。

        :return: The is_auto_pay of this ResizeFlavorRequest.
        :rtype: bool
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        """Sets the is_auto_pay of this ResizeFlavorRequest.

        变更包周期实例的规格时可指定，表示是否自动从客户的账户中支付。

        :param is_auto_pay: The is_auto_pay of this ResizeFlavorRequest.
        :type: bool
        """
        self._is_auto_pay = is_auto_pay

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
        if not isinstance(other, ResizeFlavorRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
