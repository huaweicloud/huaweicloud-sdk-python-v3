# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DmsKafkaInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'addr': 'list[str]',
        'order_fade_enable': 'bool',
        'order_fade_cache': 'int'
    }

    attribute_map = {
        'addr': 'addr',
        'order_fade_enable': 'order_fade_enable',
        'order_fade_cache': 'order_fade_cache'
    }

    def __init__(self, addr=None, order_fade_enable=None, order_fade_cache=None):
        """DmsKafkaInfo

        The model defined in huaweicloud sdk

        :param addr: Kafka连接地址
        :type addr: list[str]
        :param order_fade_enable: Kafka模式下，是否开启共识节点老化
        :type order_fade_enable: bool
        :param order_fade_cache: Kafka模式下，开启共识节点后的老化阈值
        :type order_fade_cache: int
        """
        
        

        self._addr = None
        self._order_fade_enable = None
        self._order_fade_cache = None
        self.discriminator = None

        if addr is not None:
            self.addr = addr
        if order_fade_enable is not None:
            self.order_fade_enable = order_fade_enable
        if order_fade_cache is not None:
            self.order_fade_cache = order_fade_cache

    @property
    def addr(self):
        """Gets the addr of this DmsKafkaInfo.

        Kafka连接地址

        :return: The addr of this DmsKafkaInfo.
        :rtype: list[str]
        """
        return self._addr

    @addr.setter
    def addr(self, addr):
        """Sets the addr of this DmsKafkaInfo.

        Kafka连接地址

        :param addr: The addr of this DmsKafkaInfo.
        :type addr: list[str]
        """
        self._addr = addr

    @property
    def order_fade_enable(self):
        """Gets the order_fade_enable of this DmsKafkaInfo.

        Kafka模式下，是否开启共识节点老化

        :return: The order_fade_enable of this DmsKafkaInfo.
        :rtype: bool
        """
        return self._order_fade_enable

    @order_fade_enable.setter
    def order_fade_enable(self, order_fade_enable):
        """Sets the order_fade_enable of this DmsKafkaInfo.

        Kafka模式下，是否开启共识节点老化

        :param order_fade_enable: The order_fade_enable of this DmsKafkaInfo.
        :type order_fade_enable: bool
        """
        self._order_fade_enable = order_fade_enable

    @property
    def order_fade_cache(self):
        """Gets the order_fade_cache of this DmsKafkaInfo.

        Kafka模式下，开启共识节点后的老化阈值

        :return: The order_fade_cache of this DmsKafkaInfo.
        :rtype: int
        """
        return self._order_fade_cache

    @order_fade_cache.setter
    def order_fade_cache(self, order_fade_cache):
        """Sets the order_fade_cache of this DmsKafkaInfo.

        Kafka模式下，开启共识节点后的老化阈值

        :param order_fade_cache: The order_fade_cache of this DmsKafkaInfo.
        :type order_fade_cache: int
        """
        self._order_fade_cache = order_fade_cache

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
        if not isinstance(other, DmsKafkaInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
