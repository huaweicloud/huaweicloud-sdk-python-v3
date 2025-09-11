# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstancesStatisticsResponseBodyInstancesStatistics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'count': 'int'
    }

    attribute_map = {
        'status': 'status',
        'count': 'count'
    }

    def __init__(self, status=None, count=None):
        r"""InstancesStatisticsResponseBodyInstancesStatistics

        The model defined in huaweicloud sdk

        :param status: **参数解释**: 实例状态。 **取值范围**: - normal：实例状态正常。 - abnormal：实例状态异常。 - creating：实例创建中。 - createfail：实例创建失败。 - shutdown：实例已关机。 - deleted：实例已删除。
        :type status: str
        :param count: **参数解释**: 实例数量。 **取值范围**: 不涉及。
        :type count: int
        """
        
        

        self._status = None
        self._count = None
        self.discriminator = None

        self.status = status
        self.count = count

    @property
    def status(self):
        r"""Gets the status of this InstancesStatisticsResponseBodyInstancesStatistics.

        **参数解释**: 实例状态。 **取值范围**: - normal：实例状态正常。 - abnormal：实例状态异常。 - creating：实例创建中。 - createfail：实例创建失败。 - shutdown：实例已关机。 - deleted：实例已删除。

        :return: The status of this InstancesStatisticsResponseBodyInstancesStatistics.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this InstancesStatisticsResponseBodyInstancesStatistics.

        **参数解释**: 实例状态。 **取值范围**: - normal：实例状态正常。 - abnormal：实例状态异常。 - creating：实例创建中。 - createfail：实例创建失败。 - shutdown：实例已关机。 - deleted：实例已删除。

        :param status: The status of this InstancesStatisticsResponseBodyInstancesStatistics.
        :type status: str
        """
        self._status = status

    @property
    def count(self):
        r"""Gets the count of this InstancesStatisticsResponseBodyInstancesStatistics.

        **参数解释**: 实例数量。 **取值范围**: 不涉及。

        :return: The count of this InstancesStatisticsResponseBodyInstancesStatistics.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this InstancesStatisticsResponseBodyInstancesStatistics.

        **参数解释**: 实例数量。 **取值范围**: 不涉及。

        :param count: The count of this InstancesStatisticsResponseBodyInstancesStatistics.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, InstancesStatisticsResponseBodyInstancesStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
