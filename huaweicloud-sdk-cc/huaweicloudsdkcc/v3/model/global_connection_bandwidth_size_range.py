# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GlobalConnectionBandwidthSizeRange:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'charge_mode': 'str',
        'min': 'int',
        'max': 'int'
    }

    attribute_map = {
        'charge_mode': 'charge_mode',
        'min': 'min',
        'max': 'max'
    }

    def __init__(self, charge_mode=None, min=None, max=None):
        """GlobalConnectionBandwidthSizeRange

        The model defined in huaweicloud sdk

        :param charge_mode: 描述计费类型，描述可选计费类型。 取值范围：     bwd: 按带宽计费     95: 按传统型95计费
        :type charge_mode: str
        :param min: 全域互联带宽最小值，单位Mbit/s。
        :type min: int
        :param max: 全域互联带宽最大值，单位Mbit/s。
        :type max: int
        """
        
        

        self._charge_mode = None
        self._min = None
        self._max = None
        self.discriminator = None

        if charge_mode is not None:
            self.charge_mode = charge_mode
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max

    @property
    def charge_mode(self):
        """Gets the charge_mode of this GlobalConnectionBandwidthSizeRange.

        描述计费类型，描述可选计费类型。 取值范围：     bwd: 按带宽计费     95: 按传统型95计费

        :return: The charge_mode of this GlobalConnectionBandwidthSizeRange.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this GlobalConnectionBandwidthSizeRange.

        描述计费类型，描述可选计费类型。 取值范围：     bwd: 按带宽计费     95: 按传统型95计费

        :param charge_mode: The charge_mode of this GlobalConnectionBandwidthSizeRange.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def min(self):
        """Gets the min of this GlobalConnectionBandwidthSizeRange.

        全域互联带宽最小值，单位Mbit/s。

        :return: The min of this GlobalConnectionBandwidthSizeRange.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this GlobalConnectionBandwidthSizeRange.

        全域互联带宽最小值，单位Mbit/s。

        :param min: The min of this GlobalConnectionBandwidthSizeRange.
        :type min: int
        """
        self._min = min

    @property
    def max(self):
        """Gets the max of this GlobalConnectionBandwidthSizeRange.

        全域互联带宽最大值，单位Mbit/s。

        :return: The max of this GlobalConnectionBandwidthSizeRange.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this GlobalConnectionBandwidthSizeRange.

        全域互联带宽最大值，单位Mbit/s。

        :param max: The max of this GlobalConnectionBandwidthSizeRange.
        :type max: int
        """
        self._max = max

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
        if not isinstance(other, GlobalConnectionBandwidthSizeRange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
