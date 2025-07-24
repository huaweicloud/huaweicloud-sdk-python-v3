# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShareTypesAttributionBandwidth:

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
        'step': 'int',
        'density': 'float',
        'base': 'int'
    }

    attribute_map = {
        'max': 'max',
        'min': 'min',
        'step': 'step',
        'density': 'density',
        'base': 'base'
    }

    def __init__(self, max=None, min=None, step=None, density=None, base=None):
        r"""ShareTypesAttributionBandwidth

        The model defined in huaweicloud sdk

        :param max: 最大带宽
        :type max: int
        :param min: 最小带宽
        :type min: int
        :param step: 带宽梯度
        :type step: int
        :param density: 带宽密度
        :type density: float
        :param base: 基础带宽
        :type base: int
        """
        
        

        self._max = None
        self._min = None
        self._step = None
        self._density = None
        self._base = None
        self.discriminator = None

        if max is not None:
            self.max = max
        if min is not None:
            self.min = min
        if step is not None:
            self.step = step
        if density is not None:
            self.density = density
        if base is not None:
            self.base = base

    @property
    def max(self):
        r"""Gets the max of this ShareTypesAttributionBandwidth.

        最大带宽

        :return: The max of this ShareTypesAttributionBandwidth.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        r"""Sets the max of this ShareTypesAttributionBandwidth.

        最大带宽

        :param max: The max of this ShareTypesAttributionBandwidth.
        :type max: int
        """
        self._max = max

    @property
    def min(self):
        r"""Gets the min of this ShareTypesAttributionBandwidth.

        最小带宽

        :return: The min of this ShareTypesAttributionBandwidth.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        r"""Sets the min of this ShareTypesAttributionBandwidth.

        最小带宽

        :param min: The min of this ShareTypesAttributionBandwidth.
        :type min: int
        """
        self._min = min

    @property
    def step(self):
        r"""Gets the step of this ShareTypesAttributionBandwidth.

        带宽梯度

        :return: The step of this ShareTypesAttributionBandwidth.
        :rtype: int
        """
        return self._step

    @step.setter
    def step(self, step):
        r"""Sets the step of this ShareTypesAttributionBandwidth.

        带宽梯度

        :param step: The step of this ShareTypesAttributionBandwidth.
        :type step: int
        """
        self._step = step

    @property
    def density(self):
        r"""Gets the density of this ShareTypesAttributionBandwidth.

        带宽密度

        :return: The density of this ShareTypesAttributionBandwidth.
        :rtype: float
        """
        return self._density

    @density.setter
    def density(self, density):
        r"""Sets the density of this ShareTypesAttributionBandwidth.

        带宽密度

        :param density: The density of this ShareTypesAttributionBandwidth.
        :type density: float
        """
        self._density = density

    @property
    def base(self):
        r"""Gets the base of this ShareTypesAttributionBandwidth.

        基础带宽

        :return: The base of this ShareTypesAttributionBandwidth.
        :rtype: int
        """
        return self._base

    @base.setter
    def base(self, base):
        r"""Sets the base of this ShareTypesAttributionBandwidth.

        基础带宽

        :param base: The base of this ShareTypesAttributionBandwidth.
        :type base: int
        """
        self._base = base

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
        if not isinstance(other, ShareTypesAttributionBandwidth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
