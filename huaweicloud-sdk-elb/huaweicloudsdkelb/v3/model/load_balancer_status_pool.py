# coding: utf-8

import pprint
import re

import six





class LoadBalancerStatusPool:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'provisioning_status': 'str',
        'name': 'str',
        'healthmonitor': 'LoadBalancerStatusHealthMonitor',
        'members': 'list[LoadBalancerStatusMember]',
        'id': 'str',
        'operating_status': 'str'
    }

    attribute_map = {
        'provisioning_status': 'provisioning_status',
        'name': 'name',
        'healthmonitor': 'healthmonitor',
        'members': 'members',
        'id': 'id',
        'operating_status': 'operating_status'
    }

    def __init__(self, provisioning_status=None, name=None, healthmonitor=None, members=None, id=None, operating_status=None):
        """LoadBalancerStatusPool - a model defined in huaweicloud sdk"""
        
        

        self._provisioning_status = None
        self._name = None
        self._healthmonitor = None
        self._members = None
        self._id = None
        self._operating_status = None
        self.discriminator = None

        if provisioning_status is not None:
            self.provisioning_status = provisioning_status
        if name is not None:
            self.name = name
        if healthmonitor is not None:
            self.healthmonitor = healthmonitor
        if members is not None:
            self.members = members
        if id is not None:
            self.id = id
        if operating_status is not None:
            self.operating_status = operating_status

    @property
    def provisioning_status(self):
        """Gets the provisioning_status of this LoadBalancerStatusPool.

        provisioning的状态。 可以为：ACTIVE、PENDING_CREATE 或者ERROR。说明：该字段为预留字段，暂未启用，默认为ACTIVE。

        :return: The provisioning_status of this LoadBalancerStatusPool.
        :rtype: str
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        """Sets the provisioning_status of this LoadBalancerStatusPool.

        provisioning的状态。 可以为：ACTIVE、PENDING_CREATE 或者ERROR。说明：该字段为预留字段，暂未启用，默认为ACTIVE。

        :param provisioning_status: The provisioning_status of this LoadBalancerStatusPool.
        :type: str
        """
        self._provisioning_status = provisioning_status

    @property
    def name(self):
        """Gets the name of this LoadBalancerStatusPool.

        后端服务器组名。

        :return: The name of this LoadBalancerStatusPool.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LoadBalancerStatusPool.

        后端服务器组名。

        :param name: The name of this LoadBalancerStatusPool.
        :type: str
        """
        self._name = name

    @property
    def healthmonitor(self):
        """Gets the healthmonitor of this LoadBalancerStatusPool.


        :return: The healthmonitor of this LoadBalancerStatusPool.
        :rtype: LoadBalancerStatusHealthMonitor
        """
        return self._healthmonitor

    @healthmonitor.setter
    def healthmonitor(self, healthmonitor):
        """Sets the healthmonitor of this LoadBalancerStatusPool.


        :param healthmonitor: The healthmonitor of this LoadBalancerStatusPool.
        :type: LoadBalancerStatusHealthMonitor
        """
        self._healthmonitor = healthmonitor

    @property
    def members(self):
        """Gets the members of this LoadBalancerStatusPool.

        后端服务器。

        :return: The members of this LoadBalancerStatusPool.
        :rtype: list[LoadBalancerStatusMember]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this LoadBalancerStatusPool.

        后端服务器。

        :param members: The members of this LoadBalancerStatusPool.
        :type: list[LoadBalancerStatusMember]
        """
        self._members = members

    @property
    def id(self):
        """Gets the id of this LoadBalancerStatusPool.

        后端服务器组ID。

        :return: The id of this LoadBalancerStatusPool.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LoadBalancerStatusPool.

        后端服务器组ID。

        :param id: The id of this LoadBalancerStatusPool.
        :type: str
        """
        self._id = id

    @property
    def operating_status(self):
        """Gets the operating_status of this LoadBalancerStatusPool.

        操作状态。 可以为：ONLINE、OFFLINE、DEGRADED、DISABLED或NO_MONITOR。说明：该字段为预留字段，暂未启用，默认为ONLINE。

        :return: The operating_status of this LoadBalancerStatusPool.
        :rtype: str
        """
        return self._operating_status

    @operating_status.setter
    def operating_status(self, operating_status):
        """Sets the operating_status of this LoadBalancerStatusPool.

        操作状态。 可以为：ONLINE、OFFLINE、DEGRADED、DISABLED或NO_MONITOR。说明：该字段为预留字段，暂未启用，默认为ONLINE。

        :param operating_status: The operating_status of this LoadBalancerStatusPool.
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
        if not isinstance(other, LoadBalancerStatusPool):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
