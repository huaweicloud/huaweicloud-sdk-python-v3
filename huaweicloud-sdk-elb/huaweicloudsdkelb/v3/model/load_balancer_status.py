# coding: utf-8

import pprint
import re

import six





class LoadBalancerStatus:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'provisioning_status': 'str',
        'listeners': 'list[LoadBalancerStatusListener]',
        'pools': 'list[LoadBalancerStatusPool]',
        'id': 'str',
        'operating_status': 'str'
    }

    attribute_map = {
        'name': 'name',
        'provisioning_status': 'provisioning_status',
        'listeners': 'listeners',
        'pools': 'pools',
        'id': 'id',
        'operating_status': 'operating_status'
    }

    def __init__(self, name=None, provisioning_status=None, listeners=None, pools=None, id=None, operating_status=None):
        """LoadBalancerStatus - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._provisioning_status = None
        self._listeners = None
        self._pools = None
        self._id = None
        self._operating_status = None
        self.discriminator = None

        self.name = name
        self.provisioning_status = provisioning_status
        self.listeners = listeners
        self.pools = pools
        self.id = id
        self.operating_status = operating_status

    @property
    def name(self):
        """Gets the name of this LoadBalancerStatus.

        负载均衡器名称。

        :return: The name of this LoadBalancerStatus.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LoadBalancerStatus.

        负载均衡器名称。

        :param name: The name of this LoadBalancerStatus.
        :type: str
        """
        self._name = name

    @property
    def provisioning_status(self):
        """Gets the provisioning_status of this LoadBalancerStatus.

        负载均衡器的配置状态。 可以为：ACTIVE、PENDING_CREATE 或者ERROR。说明：该字段为预留字段，暂未启用，默认为ACTIVE。

        :return: The provisioning_status of this LoadBalancerStatus.
        :rtype: str
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        """Sets the provisioning_status of this LoadBalancerStatus.

        负载均衡器的配置状态。 可以为：ACTIVE、PENDING_CREATE 或者ERROR。说明：该字段为预留字段，暂未启用，默认为ACTIVE。

        :param provisioning_status: The provisioning_status of this LoadBalancerStatus.
        :type: str
        """
        self._provisioning_status = provisioning_status

    @property
    def listeners(self):
        """Gets the listeners of this LoadBalancerStatus.

        负载均衡器关联的监听器列表。

        :return: The listeners of this LoadBalancerStatus.
        :rtype: list[LoadBalancerStatusListener]
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        """Sets the listeners of this LoadBalancerStatus.

        负载均衡器关联的监听器列表。

        :param listeners: The listeners of this LoadBalancerStatus.
        :type: list[LoadBalancerStatusListener]
        """
        self._listeners = listeners

    @property
    def pools(self):
        """Gets the pools of this LoadBalancerStatus.

        负载均衡器关联的后端云服务器组列表。

        :return: The pools of this LoadBalancerStatus.
        :rtype: list[LoadBalancerStatusPool]
        """
        return self._pools

    @pools.setter
    def pools(self, pools):
        """Sets the pools of this LoadBalancerStatus.

        负载均衡器关联的后端云服务器组列表。

        :param pools: The pools of this LoadBalancerStatus.
        :type: list[LoadBalancerStatusPool]
        """
        self._pools = pools

    @property
    def id(self):
        """Gets the id of this LoadBalancerStatus.

        负载均衡器ID

        :return: The id of this LoadBalancerStatus.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LoadBalancerStatus.

        负载均衡器ID

        :param id: The id of this LoadBalancerStatus.
        :type: str
        """
        self._id = id

    @property
    def operating_status(self):
        """Gets the operating_status of this LoadBalancerStatus.

        负载均衡器的操作状态。 可以为：ONLINE、OFFLINE、DEGRADED、DISABLED或NO_MONITOR。说明：该字段为预留字段，暂未启用，默认为ONLINE。

        :return: The operating_status of this LoadBalancerStatus.
        :rtype: str
        """
        return self._operating_status

    @operating_status.setter
    def operating_status(self, operating_status):
        """Sets the operating_status of this LoadBalancerStatus.

        负载均衡器的操作状态。 可以为：ONLINE、OFFLINE、DEGRADED、DISABLED或NO_MONITOR。说明：该字段为预留字段，暂未启用，默认为ONLINE。

        :param operating_status: The operating_status of this LoadBalancerStatus.
        :type: str
        """
        self._operating_status = operating_status

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LoadBalancerStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
