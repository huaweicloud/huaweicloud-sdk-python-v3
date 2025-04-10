# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SeveritySummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'critical_count': 'int',
        'high_count': 'int',
        'informational_count': 'int',
        'low_count': 'int',
        'medium_count': 'int',
        'unspecified_count': 'int'
    }

    attribute_map = {
        'critical_count': 'critical_count',
        'high_count': 'high_count',
        'informational_count': 'informational_count',
        'low_count': 'low_count',
        'medium_count': 'medium_count',
        'unspecified_count': 'unspecified_count'
    }

    def __init__(self, critical_count=None, high_count=None, informational_count=None, low_count=None, medium_count=None, unspecified_count=None):
        r"""SeveritySummary

        The model defined in huaweicloud sdk

        :param critical_count: 重大合规性报告数量
        :type critical_count: int
        :param high_count: 高合规性报告数量
        :type high_count: int
        :param informational_count: 信息性合规性报告数量
        :type informational_count: int
        :param low_count: 低合规性报告数量
        :type low_count: int
        :param medium_count: 中级合规性报告数量
        :type medium_count: int
        :param unspecified_count: 未指定合规性报告数量
        :type unspecified_count: int
        """
        
        

        self._critical_count = None
        self._high_count = None
        self._informational_count = None
        self._low_count = None
        self._medium_count = None
        self._unspecified_count = None
        self.discriminator = None

        if critical_count is not None:
            self.critical_count = critical_count
        if high_count is not None:
            self.high_count = high_count
        if informational_count is not None:
            self.informational_count = informational_count
        if low_count is not None:
            self.low_count = low_count
        if medium_count is not None:
            self.medium_count = medium_count
        if unspecified_count is not None:
            self.unspecified_count = unspecified_count

    @property
    def critical_count(self):
        r"""Gets the critical_count of this SeveritySummary.

        重大合规性报告数量

        :return: The critical_count of this SeveritySummary.
        :rtype: int
        """
        return self._critical_count

    @critical_count.setter
    def critical_count(self, critical_count):
        r"""Sets the critical_count of this SeveritySummary.

        重大合规性报告数量

        :param critical_count: The critical_count of this SeveritySummary.
        :type critical_count: int
        """
        self._critical_count = critical_count

    @property
    def high_count(self):
        r"""Gets the high_count of this SeveritySummary.

        高合规性报告数量

        :return: The high_count of this SeveritySummary.
        :rtype: int
        """
        return self._high_count

    @high_count.setter
    def high_count(self, high_count):
        r"""Sets the high_count of this SeveritySummary.

        高合规性报告数量

        :param high_count: The high_count of this SeveritySummary.
        :type high_count: int
        """
        self._high_count = high_count

    @property
    def informational_count(self):
        r"""Gets the informational_count of this SeveritySummary.

        信息性合规性报告数量

        :return: The informational_count of this SeveritySummary.
        :rtype: int
        """
        return self._informational_count

    @informational_count.setter
    def informational_count(self, informational_count):
        r"""Sets the informational_count of this SeveritySummary.

        信息性合规性报告数量

        :param informational_count: The informational_count of this SeveritySummary.
        :type informational_count: int
        """
        self._informational_count = informational_count

    @property
    def low_count(self):
        r"""Gets the low_count of this SeveritySummary.

        低合规性报告数量

        :return: The low_count of this SeveritySummary.
        :rtype: int
        """
        return self._low_count

    @low_count.setter
    def low_count(self, low_count):
        r"""Sets the low_count of this SeveritySummary.

        低合规性报告数量

        :param low_count: The low_count of this SeveritySummary.
        :type low_count: int
        """
        self._low_count = low_count

    @property
    def medium_count(self):
        r"""Gets the medium_count of this SeveritySummary.

        中级合规性报告数量

        :return: The medium_count of this SeveritySummary.
        :rtype: int
        """
        return self._medium_count

    @medium_count.setter
    def medium_count(self, medium_count):
        r"""Sets the medium_count of this SeveritySummary.

        中级合规性报告数量

        :param medium_count: The medium_count of this SeveritySummary.
        :type medium_count: int
        """
        self._medium_count = medium_count

    @property
    def unspecified_count(self):
        r"""Gets the unspecified_count of this SeveritySummary.

        未指定合规性报告数量

        :return: The unspecified_count of this SeveritySummary.
        :rtype: int
        """
        return self._unspecified_count

    @unspecified_count.setter
    def unspecified_count(self, unspecified_count):
        r"""Sets the unspecified_count of this SeveritySummary.

        未指定合规性报告数量

        :param unspecified_count: The unspecified_count of this SeveritySummary.
        :type unspecified_count: int
        """
        self._unspecified_count = unspecified_count

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
        if not isinstance(other, SeveritySummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
