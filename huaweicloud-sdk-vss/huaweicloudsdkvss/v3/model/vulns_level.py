# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulnsLevel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'high': 'int',
        'middle': 'int',
        'low': 'int',
        'hint': 'int'
    }

    attribute_map = {
        'high': 'high',
        'middle': 'middle',
        'low': 'low',
        'hint': 'hint'
    }

    def __init__(self, high=None, middle=None, low=None, hint=None):
        """VulnsLevel

        The model defined in huaweicloud sdk

        :param high: 高危漏洞数
        :type high: int
        :param middle: 中危漏洞数
        :type middle: int
        :param low: 低危漏洞数
        :type low: int
        :param hint: 提示危漏洞数
        :type hint: int
        """
        
        

        self._high = None
        self._middle = None
        self._low = None
        self._hint = None
        self.discriminator = None

        if high is not None:
            self.high = high
        if middle is not None:
            self.middle = middle
        if low is not None:
            self.low = low
        if hint is not None:
            self.hint = hint

    @property
    def high(self):
        """Gets the high of this VulnsLevel.

        高危漏洞数

        :return: The high of this VulnsLevel.
        :rtype: int
        """
        return self._high

    @high.setter
    def high(self, high):
        """Sets the high of this VulnsLevel.

        高危漏洞数

        :param high: The high of this VulnsLevel.
        :type high: int
        """
        self._high = high

    @property
    def middle(self):
        """Gets the middle of this VulnsLevel.

        中危漏洞数

        :return: The middle of this VulnsLevel.
        :rtype: int
        """
        return self._middle

    @middle.setter
    def middle(self, middle):
        """Sets the middle of this VulnsLevel.

        中危漏洞数

        :param middle: The middle of this VulnsLevel.
        :type middle: int
        """
        self._middle = middle

    @property
    def low(self):
        """Gets the low of this VulnsLevel.

        低危漏洞数

        :return: The low of this VulnsLevel.
        :rtype: int
        """
        return self._low

    @low.setter
    def low(self, low):
        """Sets the low of this VulnsLevel.

        低危漏洞数

        :param low: The low of this VulnsLevel.
        :type low: int
        """
        self._low = low

    @property
    def hint(self):
        """Gets the hint of this VulnsLevel.

        提示危漏洞数

        :return: The hint of this VulnsLevel.
        :rtype: int
        """
        return self._hint

    @hint.setter
    def hint(self, hint):
        """Sets the hint of this VulnsLevel.

        提示危漏洞数

        :param hint: The hint of this VulnsLevel.
        :type hint: int
        """
        self._hint = hint

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VulnsLevel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
