# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceLimitForUpgrade:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cpu_limit': 'str',
        'memory_limit': 'str'
    }

    attribute_map = {
        'cpu_limit': 'cpu_limit',
        'memory_limit': 'memory_limit'
    }

    def __init__(self, cpu_limit=None, memory_limit=None):
        r"""ResourceLimitForUpgrade

        The model defined in huaweicloud sdk

        :param cpu_limit: cpu限额。
        :type cpu_limit: str
        :param memory_limit: 内存限额。
        :type memory_limit: str
        """
        
        

        self._cpu_limit = None
        self._memory_limit = None
        self.discriminator = None

        if cpu_limit is not None:
            self.cpu_limit = cpu_limit
        if memory_limit is not None:
            self.memory_limit = memory_limit

    @property
    def cpu_limit(self):
        r"""Gets the cpu_limit of this ResourceLimitForUpgrade.

        cpu限额。

        :return: The cpu_limit of this ResourceLimitForUpgrade.
        :rtype: str
        """
        return self._cpu_limit

    @cpu_limit.setter
    def cpu_limit(self, cpu_limit):
        r"""Sets the cpu_limit of this ResourceLimitForUpgrade.

        cpu限额。

        :param cpu_limit: The cpu_limit of this ResourceLimitForUpgrade.
        :type cpu_limit: str
        """
        self._cpu_limit = cpu_limit

    @property
    def memory_limit(self):
        r"""Gets the memory_limit of this ResourceLimitForUpgrade.

        内存限额。

        :return: The memory_limit of this ResourceLimitForUpgrade.
        :rtype: str
        """
        return self._memory_limit

    @memory_limit.setter
    def memory_limit(self, memory_limit):
        r"""Sets the memory_limit of this ResourceLimitForUpgrade.

        内存限额。

        :param memory_limit: The memory_limit of this ResourceLimitForUpgrade.
        :type memory_limit: str
        """
        self._memory_limit = memory_limit

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
        if not isinstance(other, ResourceLimitForUpgrade):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
