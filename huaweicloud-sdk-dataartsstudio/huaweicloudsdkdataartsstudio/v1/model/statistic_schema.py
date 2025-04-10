# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StatisticSchema:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'increase': 'int',
        'total': 'int',
        'standard_coverage': 'float'
    }

    attribute_map = {
        'increase': 'increase',
        'total': 'total',
        'standard_coverage': 'standard_coverage'
    }

    def __init__(self, increase=None, total=None, standard_coverage=None):
        r"""StatisticSchema

        The model defined in huaweicloud sdk

        :param increase: 本月新增。
        :type increase: int
        :param total: 总量。
        :type total: int
        :param standard_coverage: 标准覆盖率。
        :type standard_coverage: float
        """
        
        

        self._increase = None
        self._total = None
        self._standard_coverage = None
        self.discriminator = None

        if increase is not None:
            self.increase = increase
        if total is not None:
            self.total = total
        if standard_coverage is not None:
            self.standard_coverage = standard_coverage

    @property
    def increase(self):
        r"""Gets the increase of this StatisticSchema.

        本月新增。

        :return: The increase of this StatisticSchema.
        :rtype: int
        """
        return self._increase

    @increase.setter
    def increase(self, increase):
        r"""Sets the increase of this StatisticSchema.

        本月新增。

        :param increase: The increase of this StatisticSchema.
        :type increase: int
        """
        self._increase = increase

    @property
    def total(self):
        r"""Gets the total of this StatisticSchema.

        总量。

        :return: The total of this StatisticSchema.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this StatisticSchema.

        总量。

        :param total: The total of this StatisticSchema.
        :type total: int
        """
        self._total = total

    @property
    def standard_coverage(self):
        r"""Gets the standard_coverage of this StatisticSchema.

        标准覆盖率。

        :return: The standard_coverage of this StatisticSchema.
        :rtype: float
        """
        return self._standard_coverage

    @standard_coverage.setter
    def standard_coverage(self, standard_coverage):
        r"""Sets the standard_coverage of this StatisticSchema.

        标准覆盖率。

        :param standard_coverage: The standard_coverage of this StatisticSchema.
        :type standard_coverage: float
        """
        self._standard_coverage = standard_coverage

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
        if not isinstance(other, StatisticSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
