# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StatusMetric:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enabled': 'int',
        'disabled': 'int',
        'error': 'int',
        'is_percentage': 'bool'
    }

    attribute_map = {
        'enabled': 'enabled',
        'disabled': 'disabled',
        'error': 'error',
        'is_percentage': 'is_percentage'
    }

    def __init__(self, enabled=None, disabled=None, error=None, is_percentage=None):
        r"""StatusMetric

        The model defined in huaweicloud sdk

        :param enabled: 已开启的数量
        :type enabled: int
        :param disabled: 未开启的数量
        :type disabled: int
        :param error: 错误的数量
        :type error: int
        :param is_percentage: 是否百分比
        :type is_percentage: bool
        """
        
        

        self._enabled = None
        self._disabled = None
        self._error = None
        self._is_percentage = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if disabled is not None:
            self.disabled = disabled
        if error is not None:
            self.error = error
        if is_percentage is not None:
            self.is_percentage = is_percentage

    @property
    def enabled(self):
        r"""Gets the enabled of this StatusMetric.

        已开启的数量

        :return: The enabled of this StatusMetric.
        :rtype: int
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this StatusMetric.

        已开启的数量

        :param enabled: The enabled of this StatusMetric.
        :type enabled: int
        """
        self._enabled = enabled

    @property
    def disabled(self):
        r"""Gets the disabled of this StatusMetric.

        未开启的数量

        :return: The disabled of this StatusMetric.
        :rtype: int
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        r"""Sets the disabled of this StatusMetric.

        未开启的数量

        :param disabled: The disabled of this StatusMetric.
        :type disabled: int
        """
        self._disabled = disabled

    @property
    def error(self):
        r"""Gets the error of this StatusMetric.

        错误的数量

        :return: The error of this StatusMetric.
        :rtype: int
        """
        return self._error

    @error.setter
    def error(self, error):
        r"""Sets the error of this StatusMetric.

        错误的数量

        :param error: The error of this StatusMetric.
        :type error: int
        """
        self._error = error

    @property
    def is_percentage(self):
        r"""Gets the is_percentage of this StatusMetric.

        是否百分比

        :return: The is_percentage of this StatusMetric.
        :rtype: bool
        """
        return self._is_percentage

    @is_percentage.setter
    def is_percentage(self, is_percentage):
        r"""Sets the is_percentage of this StatusMetric.

        是否百分比

        :param is_percentage: The is_percentage of this StatusMetric.
        :type is_percentage: bool
        """
        self._is_percentage = is_percentage

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
        if not isinstance(other, StatusMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
