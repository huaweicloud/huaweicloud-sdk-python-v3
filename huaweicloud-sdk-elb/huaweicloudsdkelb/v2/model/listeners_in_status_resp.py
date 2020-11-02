# coding: utf-8

import pprint
import re

import six





class ListenersInStatusResp:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'pools': 'list[PoolsInStatusResp]',
        'l7policies': 'list[L7policiesInStatusResp]',
        'operating_status': 'str',
        'provisioning_status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'pools': 'pools',
        'l7policies': 'l7policies',
        'operating_status': 'operating_status',
        'provisioning_status': 'provisioning_status'
    }

    def __init__(self, id=None, name=None, pools=None, l7policies=None, operating_status=None, provisioning_status=None):
        """ListenersInStatusResp - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._name = None
        self._pools = None
        self._l7policies = None
        self._operating_status = None
        self._provisioning_status = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.pools = pools
        self.l7policies = l7policies
        self.operating_status = operating_status
        self.provisioning_status = provisioning_status

    @property
    def id(self):
        """Gets the id of this ListenersInStatusResp.

        监听器ID

        :return: The id of this ListenersInStatusResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListenersInStatusResp.

        监听器ID

        :param id: The id of this ListenersInStatusResp.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListenersInStatusResp.

        监听器名称

        :return: The name of this ListenersInStatusResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListenersInStatusResp.

        监听器名称

        :param name: The name of this ListenersInStatusResp.
        :type: str
        """
        self._name = name

    @property
    def pools(self):
        """Gets the pools of this ListenersInStatusResp.

        监听器关联的后端云服务器组列表

        :return: The pools of this ListenersInStatusResp.
        :rtype: list[PoolsInStatusResp]
        """
        return self._pools

    @pools.setter
    def pools(self, pools):
        """Sets the pools of this ListenersInStatusResp.

        监听器关联的后端云服务器组列表

        :param pools: The pools of this ListenersInStatusResp.
        :type: list[PoolsInStatusResp]
        """
        self._pools = pools

    @property
    def l7policies(self):
        """Gets the l7policies of this ListenersInStatusResp.

        监听器关联的转发策略列表

        :return: The l7policies of this ListenersInStatusResp.
        :rtype: list[L7policiesInStatusResp]
        """
        return self._l7policies

    @l7policies.setter
    def l7policies(self, l7policies):
        """Sets the l7policies of this ListenersInStatusResp.

        监听器关联的转发策略列表

        :param l7policies: The l7policies of this ListenersInStatusResp.
        :type: list[L7policiesInStatusResp]
        """
        self._l7policies = l7policies

    @property
    def operating_status(self):
        """Gets the operating_status of this ListenersInStatusResp.

        监听器的操作状态；该字段为预留字段，暂未启用。默认为ONLINE。

        :return: The operating_status of this ListenersInStatusResp.
        :rtype: str
        """
        return self._operating_status

    @operating_status.setter
    def operating_status(self, operating_status):
        """Sets the operating_status of this ListenersInStatusResp.

        监听器的操作状态；该字段为预留字段，暂未启用。默认为ONLINE。

        :param operating_status: The operating_status of this ListenersInStatusResp.
        :type: str
        """
        self._operating_status = operating_status

    @property
    def provisioning_status(self):
        """Gets the provisioning_status of this ListenersInStatusResp.

        监听器的配置状态；该字段为预留字段，暂未启用。默认为ACTIVE。

        :return: The provisioning_status of this ListenersInStatusResp.
        :rtype: str
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        """Sets the provisioning_status of this ListenersInStatusResp.

        监听器的配置状态；该字段为预留字段，暂未启用。默认为ACTIVE。

        :param provisioning_status: The provisioning_status of this ListenersInStatusResp.
        :type: str
        """
        self._provisioning_status = provisioning_status

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
        if not isinstance(other, ListenersInStatusResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
