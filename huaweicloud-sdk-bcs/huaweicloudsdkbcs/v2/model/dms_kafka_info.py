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
        'status': 'str',
        'status_detail': 'str',
        'order_fade_enabled': 'bool',
        'addr': 'list[str]',
        'order_fade_enable': 'bool',
        'order_fade_cache': 'int'
    }

    attribute_map = {
        'status': 'status',
        'status_detail': 'status_detail',
        'order_fade_enabled': 'order_fade_enabled',
        'addr': 'addr',
        'order_fade_enable': 'order_fade_enable',
        'order_fade_cache': 'order_fade_cache'
    }

    def __init__(self, status=None, status_detail=None, order_fade_enabled=None, addr=None, order_fade_enable=None, order_fade_cache=None):
        """DmsKafkaInfo

        The model defined in huaweicloud sdk

        :param status: 状态
        :type status: str
        :param status_detail: 状态详情
        :type status_detail: str
        :param order_fade_enabled: 是否允许order老化
        :type order_fade_enabled: bool
        :param addr: Kafka连接地址
        :type addr: list[str]
        :param order_fade_enable: Kafka模式下，是否开启共识节点老化
        :type order_fade_enable: bool
        :param order_fade_cache: Kafka模式下，开启共识节点后的老化阈值
        :type order_fade_cache: int
        """
        
        

        self._status = None
        self._status_detail = None
        self._order_fade_enabled = None
        self._addr = None
        self._order_fade_enable = None
        self._order_fade_cache = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if status_detail is not None:
            self.status_detail = status_detail
        if order_fade_enabled is not None:
            self.order_fade_enabled = order_fade_enabled
        if addr is not None:
            self.addr = addr
        if order_fade_enable is not None:
            self.order_fade_enable = order_fade_enable
        if order_fade_cache is not None:
            self.order_fade_cache = order_fade_cache

    @property
    def status(self):
        """Gets the status of this DmsKafkaInfo.

        状态

        :return: The status of this DmsKafkaInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DmsKafkaInfo.

        状态

        :param status: The status of this DmsKafkaInfo.
        :type status: str
        """
        self._status = status

    @property
    def status_detail(self):
        """Gets the status_detail of this DmsKafkaInfo.

        状态详情

        :return: The status_detail of this DmsKafkaInfo.
        :rtype: str
        """
        return self._status_detail

    @status_detail.setter
    def status_detail(self, status_detail):
        """Sets the status_detail of this DmsKafkaInfo.

        状态详情

        :param status_detail: The status_detail of this DmsKafkaInfo.
        :type status_detail: str
        """
        self._status_detail = status_detail

    @property
    def order_fade_enabled(self):
        """Gets the order_fade_enabled of this DmsKafkaInfo.

        是否允许order老化

        :return: The order_fade_enabled of this DmsKafkaInfo.
        :rtype: bool
        """
        return self._order_fade_enabled

    @order_fade_enabled.setter
    def order_fade_enabled(self, order_fade_enabled):
        """Sets the order_fade_enabled of this DmsKafkaInfo.

        是否允许order老化

        :param order_fade_enabled: The order_fade_enabled of this DmsKafkaInfo.
        :type order_fade_enabled: bool
        """
        self._order_fade_enabled = order_fade_enabled

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
