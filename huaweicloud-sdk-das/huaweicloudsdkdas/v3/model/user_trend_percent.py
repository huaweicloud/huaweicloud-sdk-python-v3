# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserTrendPercent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'percent_le10_count': 'int',
        'percent10_to50_count': 'int',
        'percent50_to80_count': 'int',
        'percent_gl80_count': 'int'
    }

    attribute_map = {
        'percent_le10_count': 'percent_le10_count',
        'percent10_to50_count': 'percent10_to50_count',
        'percent50_to80_count': 'percent50_to80_count',
        'percent_gl80_count': 'percent_gl80_count'
    }

    def __init__(self, percent_le10_count=None, percent10_to50_count=None, percent50_to80_count=None, percent_gl80_count=None):
        r"""UserTrendPercent

        The model defined in huaweicloud sdk

        :param percent_le10_count: 百分比小于等于10%的数量
        :type percent_le10_count: int
        :param percent10_to50_count: 百分比大于10%小于等于50%的数量
        :type percent10_to50_count: int
        :param percent50_to80_count: 百分比大于50%小于等于80%的数量
        :type percent50_to80_count: int
        :param percent_gl80_count: 百分比大于80%的数量
        :type percent_gl80_count: int
        """
        
        

        self._percent_le10_count = None
        self._percent10_to50_count = None
        self._percent50_to80_count = None
        self._percent_gl80_count = None
        self.discriminator = None

        if percent_le10_count is not None:
            self.percent_le10_count = percent_le10_count
        if percent10_to50_count is not None:
            self.percent10_to50_count = percent10_to50_count
        if percent50_to80_count is not None:
            self.percent50_to80_count = percent50_to80_count
        if percent_gl80_count is not None:
            self.percent_gl80_count = percent_gl80_count

    @property
    def percent_le10_count(self):
        r"""Gets the percent_le10_count of this UserTrendPercent.

        百分比小于等于10%的数量

        :return: The percent_le10_count of this UserTrendPercent.
        :rtype: int
        """
        return self._percent_le10_count

    @percent_le10_count.setter
    def percent_le10_count(self, percent_le10_count):
        r"""Sets the percent_le10_count of this UserTrendPercent.

        百分比小于等于10%的数量

        :param percent_le10_count: The percent_le10_count of this UserTrendPercent.
        :type percent_le10_count: int
        """
        self._percent_le10_count = percent_le10_count

    @property
    def percent10_to50_count(self):
        r"""Gets the percent10_to50_count of this UserTrendPercent.

        百分比大于10%小于等于50%的数量

        :return: The percent10_to50_count of this UserTrendPercent.
        :rtype: int
        """
        return self._percent10_to50_count

    @percent10_to50_count.setter
    def percent10_to50_count(self, percent10_to50_count):
        r"""Sets the percent10_to50_count of this UserTrendPercent.

        百分比大于10%小于等于50%的数量

        :param percent10_to50_count: The percent10_to50_count of this UserTrendPercent.
        :type percent10_to50_count: int
        """
        self._percent10_to50_count = percent10_to50_count

    @property
    def percent50_to80_count(self):
        r"""Gets the percent50_to80_count of this UserTrendPercent.

        百分比大于50%小于等于80%的数量

        :return: The percent50_to80_count of this UserTrendPercent.
        :rtype: int
        """
        return self._percent50_to80_count

    @percent50_to80_count.setter
    def percent50_to80_count(self, percent50_to80_count):
        r"""Sets the percent50_to80_count of this UserTrendPercent.

        百分比大于50%小于等于80%的数量

        :param percent50_to80_count: The percent50_to80_count of this UserTrendPercent.
        :type percent50_to80_count: int
        """
        self._percent50_to80_count = percent50_to80_count

    @property
    def percent_gl80_count(self):
        r"""Gets the percent_gl80_count of this UserTrendPercent.

        百分比大于80%的数量

        :return: The percent_gl80_count of this UserTrendPercent.
        :rtype: int
        """
        return self._percent_gl80_count

    @percent_gl80_count.setter
    def percent_gl80_count(self, percent_gl80_count):
        r"""Sets the percent_gl80_count of this UserTrendPercent.

        百分比大于80%的数量

        :param percent_gl80_count: The percent_gl80_count of this UserTrendPercent.
        :type percent_gl80_count: int
        """
        self._percent_gl80_count = percent_gl80_count

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
        if not isinstance(other, UserTrendPercent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
