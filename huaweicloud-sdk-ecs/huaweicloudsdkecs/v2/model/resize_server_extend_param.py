# coding: utf-8

import pprint
import re

import six





class ResizeServerExtendParam:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'is_auto_pay': 'str'
    }

    attribute_map = {
        'is_auto_pay': 'isAutoPay'
    }

    def __init__(self, is_auto_pay=None):
        """ResizeServerExtendParam - a model defined in huaweicloud sdk"""
        
        

        self._is_auto_pay = None
        self.discriminator = None

        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay

    @property
    def is_auto_pay(self):
        """Gets the is_auto_pay of this ResizeServerExtendParam.

        下单订购后，是否自动从客户的账户中支付，而不需要客户手动去进行支付。  - “true”：是（自动支付） - “false”：否（需要客户手动支付）  > 说明： >  > 当弹性云服务器是按包年包月计费时生效，该值为空时默认为客户手动支付。

        :return: The is_auto_pay of this ResizeServerExtendParam.
        :rtype: str
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        """Sets the is_auto_pay of this ResizeServerExtendParam.

        下单订购后，是否自动从客户的账户中支付，而不需要客户手动去进行支付。  - “true”：是（自动支付） - “false”：否（需要客户手动支付）  > 说明： >  > 当弹性云服务器是按包年包月计费时生效，该值为空时默认为客户手动支付。

        :param is_auto_pay: The is_auto_pay of this ResizeServerExtendParam.
        :type: str
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
        if not isinstance(other, ResizeServerExtendParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
