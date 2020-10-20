# coding: utf-8

import pprint
import re

import six





class LoadBalancerStatusListener:


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
        'pools': 'list[LoadBalancerStatusPool]',
        'l7policies': 'list[LoadBalancerStatusPolicy]',
        'id': 'str',
        'operating_status': 'str'
    }

    attribute_map = {
        'name': 'name',
        'provisioning_status': 'provisioning_status',
        'pools': 'pools',
        'l7policies': 'l7policies',
        'id': 'id',
        'operating_status': 'operating_status'
    }

    def __init__(self, name=None, provisioning_status='ACTIVE', pools=None, l7policies=None, id=None, operating_status=None):
        """LoadBalancerStatusListener - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._provisioning_status = None
        self._pools = None
        self._l7policies = None
        self._id = None
        self._operating_status = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if provisioning_status is not None:
            self.provisioning_status = provisioning_status
        if pools is not None:
            self.pools = pools
        if l7policies is not None:
            self.l7policies = l7policies
        if id is not None:
            self.id = id
        if operating_status is not None:
            self.operating_status = operating_status

    @property
    def name(self):
        """Gets the name of this LoadBalancerStatusListener.

        负载均衡器下监听器的名称。

        :return: The name of this LoadBalancerStatusListener.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LoadBalancerStatusListener.

        负载均衡器下监听器的名称。

        :param name: The name of this LoadBalancerStatusListener.
        :type: str
        """
        self._name = name

    @property
    def provisioning_status(self):
        """Gets the provisioning_status of this LoadBalancerStatusListener.

        provisioning状态。 可以为ACTIVE、PENDING_CREATE 或者ERROR。

        :return: The provisioning_status of this LoadBalancerStatusListener.
        :rtype: str
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        """Sets the provisioning_status of this LoadBalancerStatusListener.

        provisioning状态。 可以为ACTIVE、PENDING_CREATE 或者ERROR。

        :param provisioning_status: The provisioning_status of this LoadBalancerStatusListener.
        :type: str
        """
        self._provisioning_status = provisioning_status

    @property
    def pools(self):
        """Gets the pools of this LoadBalancerStatusListener.

        挂载在监听器下的后端主机组。

        :return: The pools of this LoadBalancerStatusListener.
        :rtype: list[LoadBalancerStatusPool]
        """
        return self._pools

    @pools.setter
    def pools(self, pools):
        """Sets the pools of this LoadBalancerStatusListener.

        挂载在监听器下的后端主机组。

        :param pools: The pools of this LoadBalancerStatusListener.
        :type: list[LoadBalancerStatusPool]
        """
        self._pools = pools

    @property
    def l7policies(self):
        """Gets the l7policies of this LoadBalancerStatusListener.

        7层转发策略

        :return: The l7policies of this LoadBalancerStatusListener.
        :rtype: list[LoadBalancerStatusPolicy]
        """
        return self._l7policies

    @l7policies.setter
    def l7policies(self, l7policies):
        """Sets the l7policies of this LoadBalancerStatusListener.

        7层转发策略

        :param l7policies: The l7policies of this LoadBalancerStatusListener.
        :type: list[LoadBalancerStatusPolicy]
        """
        self._l7policies = l7policies

    @property
    def id(self):
        """Gets the id of this LoadBalancerStatusListener.

        监听器ID。

        :return: The id of this LoadBalancerStatusListener.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LoadBalancerStatusListener.

        监听器ID。

        :param id: The id of this LoadBalancerStatusListener.
        :type: str
        """
        self._id = id

    @property
    def operating_status(self):
        """Gets the operating_status of this LoadBalancerStatusListener.

        操作状态。 可以为：ONLINE、OFFLINE、DEGRADED、DISABLED或NO_MONITOR。说明：该字段为预留字段，暂未启用，默认为ONLINE。

        :return: The operating_status of this LoadBalancerStatusListener.
        :rtype: str
        """
        return self._operating_status

    @operating_status.setter
    def operating_status(self, operating_status):
        """Sets the operating_status of this LoadBalancerStatusListener.

        操作状态。 可以为：ONLINE、OFFLINE、DEGRADED、DISABLED或NO_MONITOR。说明：该字段为预留字段，暂未启用，默认为ONLINE。

        :param operating_status: The operating_status of this LoadBalancerStatusListener.
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
        if not isinstance(other, LoadBalancerStatusListener):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
