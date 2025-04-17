# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HierarchicalValue:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'critical': 'float',
        'major': 'float',
        'minor': 'float',
        'info': 'float'
    }

    attribute_map = {
        'critical': 'critical',
        'major': 'major',
        'minor': 'minor',
        'info': 'info'
    }

    def __init__(self, critical=None, major=None, minor=None, info=None):
        r"""HierarchicalValue

        The model defined in huaweicloud sdk

        :param critical: 紧急级别的阈值
        :type critical: float
        :param major: 重要级别的阈值
        :type major: float
        :param minor: 次要级别的阈值
        :type minor: float
        :param info: 提示级别的阈值
        :type info: float
        """
        
        

        self._critical = None
        self._major = None
        self._minor = None
        self._info = None
        self.discriminator = None

        if critical is not None:
            self.critical = critical
        if major is not None:
            self.major = major
        if minor is not None:
            self.minor = minor
        if info is not None:
            self.info = info

    @property
    def critical(self):
        r"""Gets the critical of this HierarchicalValue.

        紧急级别的阈值

        :return: The critical of this HierarchicalValue.
        :rtype: float
        """
        return self._critical

    @critical.setter
    def critical(self, critical):
        r"""Sets the critical of this HierarchicalValue.

        紧急级别的阈值

        :param critical: The critical of this HierarchicalValue.
        :type critical: float
        """
        self._critical = critical

    @property
    def major(self):
        r"""Gets the major of this HierarchicalValue.

        重要级别的阈值

        :return: The major of this HierarchicalValue.
        :rtype: float
        """
        return self._major

    @major.setter
    def major(self, major):
        r"""Sets the major of this HierarchicalValue.

        重要级别的阈值

        :param major: The major of this HierarchicalValue.
        :type major: float
        """
        self._major = major

    @property
    def minor(self):
        r"""Gets the minor of this HierarchicalValue.

        次要级别的阈值

        :return: The minor of this HierarchicalValue.
        :rtype: float
        """
        return self._minor

    @minor.setter
    def minor(self, minor):
        r"""Sets the minor of this HierarchicalValue.

        次要级别的阈值

        :param minor: The minor of this HierarchicalValue.
        :type minor: float
        """
        self._minor = minor

    @property
    def info(self):
        r"""Gets the info of this HierarchicalValue.

        提示级别的阈值

        :return: The info of this HierarchicalValue.
        :rtype: float
        """
        return self._info

    @info.setter
    def info(self, info):
        r"""Sets the info of this HierarchicalValue.

        提示级别的阈值

        :param info: The info of this HierarchicalValue.
        :type info: float
        """
        self._info = info

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
        if not isinstance(other, HierarchicalValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
