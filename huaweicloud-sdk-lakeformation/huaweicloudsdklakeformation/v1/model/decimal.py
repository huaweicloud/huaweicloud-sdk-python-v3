# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Decimal:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scale': 'int',
        'unscaled': 'str'
    }

    attribute_map = {
        'scale': 'scale',
        'unscaled': 'unscaled'
    }

    def __init__(self, scale=None, unscaled=None):
        """Decimal

        The model defined in huaweicloud sdk

        :param scale: 整数部分
        :type scale: int
        :param unscaled: 小数部分
        :type unscaled: str
        """
        
        

        self._scale = None
        self._unscaled = None
        self.discriminator = None

        if scale is not None:
            self.scale = scale
        if unscaled is not None:
            self.unscaled = unscaled

    @property
    def scale(self):
        """Gets the scale of this Decimal.

        整数部分

        :return: The scale of this Decimal.
        :rtype: int
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        """Sets the scale of this Decimal.

        整数部分

        :param scale: The scale of this Decimal.
        :type scale: int
        """
        self._scale = scale

    @property
    def unscaled(self):
        """Gets the unscaled of this Decimal.

        小数部分

        :return: The unscaled of this Decimal.
        :rtype: str
        """
        return self._unscaled

    @unscaled.setter
    def unscaled(self, unscaled):
        """Sets the unscaled of this Decimal.

        小数部分

        :param unscaled: The unscaled of this Decimal.
        :type unscaled: str
        """
        self._unscaled = unscaled

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
        if not isinstance(other, Decimal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
