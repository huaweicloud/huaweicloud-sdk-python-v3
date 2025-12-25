# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UsageMetric:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'used': 'str',
        'un_used': 'str',
        'is_percentage': 'bool'
    }

    attribute_map = {
        'used': 'used',
        'un_used': 'un_used',
        'is_percentage': 'is_percentage'
    }

    def __init__(self, used=None, un_used=None, is_percentage=None):
        r"""UsageMetric

        The model defined in huaweicloud sdk

        :param used: 已使用
        :type used: str
        :param un_used: 未使用
        :type un_used: str
        :param is_percentage: 是否百分比
        :type is_percentage: bool
        """
        
        

        self._used = None
        self._un_used = None
        self._is_percentage = None
        self.discriminator = None

        if used is not None:
            self.used = used
        if un_used is not None:
            self.un_used = un_used
        if is_percentage is not None:
            self.is_percentage = is_percentage

    @property
    def used(self):
        r"""Gets the used of this UsageMetric.

        已使用

        :return: The used of this UsageMetric.
        :rtype: str
        """
        return self._used

    @used.setter
    def used(self, used):
        r"""Sets the used of this UsageMetric.

        已使用

        :param used: The used of this UsageMetric.
        :type used: str
        """
        self._used = used

    @property
    def un_used(self):
        r"""Gets the un_used of this UsageMetric.

        未使用

        :return: The un_used of this UsageMetric.
        :rtype: str
        """
        return self._un_used

    @un_used.setter
    def un_used(self, un_used):
        r"""Sets the un_used of this UsageMetric.

        未使用

        :param un_used: The un_used of this UsageMetric.
        :type un_used: str
        """
        self._un_used = un_used

    @property
    def is_percentage(self):
        r"""Gets the is_percentage of this UsageMetric.

        是否百分比

        :return: The is_percentage of this UsageMetric.
        :rtype: bool
        """
        return self._is_percentage

    @is_percentage.setter
    def is_percentage(self, is_percentage):
        r"""Sets the is_percentage of this UsageMetric.

        是否百分比

        :param is_percentage: The is_percentage of this UsageMetric.
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
        if not isinstance(other, UsageMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
