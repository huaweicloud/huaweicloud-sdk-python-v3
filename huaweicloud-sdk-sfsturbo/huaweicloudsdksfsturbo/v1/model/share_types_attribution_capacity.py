# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShareTypesAttributionCapacity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max': 'int',
        'min': 'int',
        'step': 'float'
    }

    attribute_map = {
        'max': 'max',
        'min': 'min',
        'step': 'step'
    }

    def __init__(self, max=None, min=None, step=None):
        r"""ShareTypesAttributionCapacity

        The model defined in huaweicloud sdk

        :param max: 最大容量
        :type max: int
        :param min: 最小容量
        :type min: int
        :param step: 容量梯度
        :type step: float
        """
        
        

        self._max = None
        self._min = None
        self._step = None
        self.discriminator = None

        if max is not None:
            self.max = max
        if min is not None:
            self.min = min
        if step is not None:
            self.step = step

    @property
    def max(self):
        r"""Gets the max of this ShareTypesAttributionCapacity.

        最大容量

        :return: The max of this ShareTypesAttributionCapacity.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        r"""Sets the max of this ShareTypesAttributionCapacity.

        最大容量

        :param max: The max of this ShareTypesAttributionCapacity.
        :type max: int
        """
        self._max = max

    @property
    def min(self):
        r"""Gets the min of this ShareTypesAttributionCapacity.

        最小容量

        :return: The min of this ShareTypesAttributionCapacity.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        r"""Sets the min of this ShareTypesAttributionCapacity.

        最小容量

        :param min: The min of this ShareTypesAttributionCapacity.
        :type min: int
        """
        self._min = min

    @property
    def step(self):
        r"""Gets the step of this ShareTypesAttributionCapacity.

        容量梯度

        :return: The step of this ShareTypesAttributionCapacity.
        :rtype: float
        """
        return self._step

    @step.setter
    def step(self, step):
        r"""Sets the step of this ShareTypesAttributionCapacity.

        容量梯度

        :param step: The step of this ShareTypesAttributionCapacity.
        :type step: float
        """
        self._step = step

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
        if not isinstance(other, ShareTypesAttributionCapacity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
