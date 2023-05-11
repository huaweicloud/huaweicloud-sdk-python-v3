# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OfflineCacheConfigsDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publish_order': 'str',
        'period': 'int',
        'capacity': 'int'
    }

    attribute_map = {
        'publish_order': 'publish_order',
        'period': 'period',
        'capacity': 'capacity'
    }

    def __init__(self, publish_order=None, period=None, capacity=None):
        """OfflineCacheConfigsDTO

        The model defined in huaweicloud sdk

        :param publish_order: 数据上报优先级，可选项：realtime_first实时数据优先 sequential按时序上报，默认realtime_first
        :type publish_order: str
        :param period: 节点离线缓存数据的储存天数，默认7，取值范围-1~14，-1表示存储天数没有限制
        :type period: int
        :param capacity: 节点离线缓存容量，单位MB，默认2048，取值范围500-8192
        :type capacity: int
        """
        
        

        self._publish_order = None
        self._period = None
        self._capacity = None
        self.discriminator = None

        if publish_order is not None:
            self.publish_order = publish_order
        if period is not None:
            self.period = period
        if capacity is not None:
            self.capacity = capacity

    @property
    def publish_order(self):
        """Gets the publish_order of this OfflineCacheConfigsDTO.

        数据上报优先级，可选项：realtime_first实时数据优先 sequential按时序上报，默认realtime_first

        :return: The publish_order of this OfflineCacheConfigsDTO.
        :rtype: str
        """
        return self._publish_order

    @publish_order.setter
    def publish_order(self, publish_order):
        """Sets the publish_order of this OfflineCacheConfigsDTO.

        数据上报优先级，可选项：realtime_first实时数据优先 sequential按时序上报，默认realtime_first

        :param publish_order: The publish_order of this OfflineCacheConfigsDTO.
        :type publish_order: str
        """
        self._publish_order = publish_order

    @property
    def period(self):
        """Gets the period of this OfflineCacheConfigsDTO.

        节点离线缓存数据的储存天数，默认7，取值范围-1~14，-1表示存储天数没有限制

        :return: The period of this OfflineCacheConfigsDTO.
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this OfflineCacheConfigsDTO.

        节点离线缓存数据的储存天数，默认7，取值范围-1~14，-1表示存储天数没有限制

        :param period: The period of this OfflineCacheConfigsDTO.
        :type period: int
        """
        self._period = period

    @property
    def capacity(self):
        """Gets the capacity of this OfflineCacheConfigsDTO.

        节点离线缓存容量，单位MB，默认2048，取值范围500-8192

        :return: The capacity of this OfflineCacheConfigsDTO.
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this OfflineCacheConfigsDTO.

        节点离线缓存容量，单位MB，默认2048，取值范围500-8192

        :param capacity: The capacity of this OfflineCacheConfigsDTO.
        :type capacity: int
        """
        self._capacity = capacity

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
        if not isinstance(other, OfflineCacheConfigsDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
