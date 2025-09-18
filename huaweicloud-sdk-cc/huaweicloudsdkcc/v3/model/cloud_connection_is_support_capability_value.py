# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloudConnectionIsSupportCapabilityValue:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_support': 'bool'
    }

    attribute_map = {
        'is_support': 'is_support'
    }

    def __init__(self, is_support=None):
        r"""CloudConnectionIsSupportCapabilityValue

        The model defined in huaweicloud sdk

        :param is_support: 是否支持云连接能力。
        :type is_support: bool
        """
        
        

        self._is_support = None
        self.discriminator = None

        self.is_support = is_support

    @property
    def is_support(self):
        r"""Gets the is_support of this CloudConnectionIsSupportCapabilityValue.

        是否支持云连接能力。

        :return: The is_support of this CloudConnectionIsSupportCapabilityValue.
        :rtype: bool
        """
        return self._is_support

    @is_support.setter
    def is_support(self, is_support):
        r"""Sets the is_support of this CloudConnectionIsSupportCapabilityValue.

        是否支持云连接能力。

        :param is_support: The is_support of this CloudConnectionIsSupportCapabilityValue.
        :type is_support: bool
        """
        self._is_support = is_support

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
        if not isinstance(other, CloudConnectionIsSupportCapabilityValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
