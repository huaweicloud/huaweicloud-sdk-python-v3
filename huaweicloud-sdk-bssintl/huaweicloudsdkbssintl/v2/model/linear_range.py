# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LinearRange:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'min': 'int',
        'max': 'int',
        'step': 'int'
    }

    attribute_map = {
        'min': 'min',
        'max': 'max',
        'step': 'step'
    }

    def __init__(self, min=None, max=None, step=None):
        r"""LinearRange

        The model defined in huaweicloud sdk

        :param min: 线性属性的最小值
        :type min: int
        :param max: 线性属性的最大值
        :type max: int
        :param step: 线性属性的步长
        :type step: int
        """
        
        

        self._min = None
        self._max = None
        self._step = None
        self.discriminator = None

        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        if step is not None:
            self.step = step

    @property
    def min(self):
        r"""Gets the min of this LinearRange.

        线性属性的最小值

        :return: The min of this LinearRange.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        r"""Sets the min of this LinearRange.

        线性属性的最小值

        :param min: The min of this LinearRange.
        :type min: int
        """
        self._min = min

    @property
    def max(self):
        r"""Gets the max of this LinearRange.

        线性属性的最大值

        :return: The max of this LinearRange.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        r"""Sets the max of this LinearRange.

        线性属性的最大值

        :param max: The max of this LinearRange.
        :type max: int
        """
        self._max = max

    @property
    def step(self):
        r"""Gets the step of this LinearRange.

        线性属性的步长

        :return: The step of this LinearRange.
        :rtype: int
        """
        return self._step

    @step.setter
    def step(self, step):
        r"""Sets the step of this LinearRange.

        线性属性的步长

        :param step: The step of this LinearRange.
        :type step: int
        """
        self._step = step

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LinearRange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
