# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StatisticSeverityV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'critical': 'int',
        'major': 'int',
        'minor': 'int',
        'suggestion': 'int'
    }

    attribute_map = {
        'critical': 'critical',
        'major': 'major',
        'minor': 'minor',
        'suggestion': 'suggestion'
    }

    def __init__(self, critical=None, major=None, minor=None, suggestion=None):
        """StatisticSeverityV2

        The model defined in huaweicloud sdk

        :param critical: 致命问题数
        :type critical: int
        :param major: 严重问题数
        :type major: int
        :param minor: 一般问题数
        :type minor: int
        :param suggestion: 提示问题数
        :type suggestion: int
        """
        
        

        self._critical = None
        self._major = None
        self._minor = None
        self._suggestion = None
        self.discriminator = None

        if critical is not None:
            self.critical = critical
        if major is not None:
            self.major = major
        if minor is not None:
            self.minor = minor
        if suggestion is not None:
            self.suggestion = suggestion

    @property
    def critical(self):
        """Gets the critical of this StatisticSeverityV2.

        致命问题数

        :return: The critical of this StatisticSeverityV2.
        :rtype: int
        """
        return self._critical

    @critical.setter
    def critical(self, critical):
        """Sets the critical of this StatisticSeverityV2.

        致命问题数

        :param critical: The critical of this StatisticSeverityV2.
        :type critical: int
        """
        self._critical = critical

    @property
    def major(self):
        """Gets the major of this StatisticSeverityV2.

        严重问题数

        :return: The major of this StatisticSeverityV2.
        :rtype: int
        """
        return self._major

    @major.setter
    def major(self, major):
        """Sets the major of this StatisticSeverityV2.

        严重问题数

        :param major: The major of this StatisticSeverityV2.
        :type major: int
        """
        self._major = major

    @property
    def minor(self):
        """Gets the minor of this StatisticSeverityV2.

        一般问题数

        :return: The minor of this StatisticSeverityV2.
        :rtype: int
        """
        return self._minor

    @minor.setter
    def minor(self, minor):
        """Sets the minor of this StatisticSeverityV2.

        一般问题数

        :param minor: The minor of this StatisticSeverityV2.
        :type minor: int
        """
        self._minor = minor

    @property
    def suggestion(self):
        """Gets the suggestion of this StatisticSeverityV2.

        提示问题数

        :return: The suggestion of this StatisticSeverityV2.
        :rtype: int
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this StatisticSeverityV2.

        提示问题数

        :param suggestion: The suggestion of this StatisticSeverityV2.
        :type suggestion: int
        """
        self._suggestion = suggestion

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
        if not isinstance(other, StatisticSeverityV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
