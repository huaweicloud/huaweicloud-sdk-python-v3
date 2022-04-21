# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceStatistics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'unhealth': 'int',
        'total': 'int',
        'type_statistics': 'int'
    }

    attribute_map = {
        'unhealth': 'unhealth',
        'total': 'total',
        'type_statistics': 'type_statistics'
    }

    def __init__(self, unhealth=None, total=None, type_statistics=None):
        """InstanceStatistics

        The model defined in huaweicloud sdk

        :param unhealth: 该资源分组中当前处在告警状态的资源个数。
        :type unhealth: int
        :param total: 该资源分组中资源的总个数。
        :type total: int
        :param type_statistics: 该资源分组中选择的资源类型个数，如资源分组添加了弹性云服务、弹性公网IP和带宽则值为2。
        :type type_statistics: int
        """
        
        

        self._unhealth = None
        self._total = None
        self._type_statistics = None
        self.discriminator = None

        if unhealth is not None:
            self.unhealth = unhealth
        if total is not None:
            self.total = total
        if type_statistics is not None:
            self.type_statistics = type_statistics

    @property
    def unhealth(self):
        """Gets the unhealth of this InstanceStatistics.

        该资源分组中当前处在告警状态的资源个数。

        :return: The unhealth of this InstanceStatistics.
        :rtype: int
        """
        return self._unhealth

    @unhealth.setter
    def unhealth(self, unhealth):
        """Sets the unhealth of this InstanceStatistics.

        该资源分组中当前处在告警状态的资源个数。

        :param unhealth: The unhealth of this InstanceStatistics.
        :type unhealth: int
        """
        self._unhealth = unhealth

    @property
    def total(self):
        """Gets the total of this InstanceStatistics.

        该资源分组中资源的总个数。

        :return: The total of this InstanceStatistics.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this InstanceStatistics.

        该资源分组中资源的总个数。

        :param total: The total of this InstanceStatistics.
        :type total: int
        """
        self._total = total

    @property
    def type_statistics(self):
        """Gets the type_statistics of this InstanceStatistics.

        该资源分组中选择的资源类型个数，如资源分组添加了弹性云服务、弹性公网IP和带宽则值为2。

        :return: The type_statistics of this InstanceStatistics.
        :rtype: int
        """
        return self._type_statistics

    @type_statistics.setter
    def type_statistics(self, type_statistics):
        """Sets the type_statistics of this InstanceStatistics.

        该资源分组中选择的资源类型个数，如资源分组添加了弹性云服务、弹性公网IP和带宽则值为2。

        :param type_statistics: The type_statistics of this InstanceStatistics.
        :type type_statistics: int
        """
        self._type_statistics = type_statistics

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
        if not isinstance(other, InstanceStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
