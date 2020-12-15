# coding: utf-8

import pprint
import re

import six





class LoadBalancerStatusMember:


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
        'address': 'str',
        'protocol_port': 'int',
        'id': 'str',
        'operating_status': 'str'
    }

    attribute_map = {
        'provisioning_status': 'provisioning_status',
        'address': 'address',
        'protocol_port': 'protocol_port',
        'id': 'id',
        'operating_status': 'operating_status'
    }

    def __init__(self, provisioning_status=None, address=None, protocol_port=None, id=None, operating_status=None):
        """LoadBalancerStatusMember - a model defined in huaweicloud sdk"""
        
        

        self._provisioning_status = None
        self._address = None
        self._protocol_port = None
        self._id = None
        self._operating_status = None
        self.discriminator = None

        if provisioning_status is not None:
            self.provisioning_status = provisioning_status
        if address is not None:
            self.address = address
        if protocol_port is not None:
            self.protocol_port = protocol_port
        if id is not None:
            self.id = id
        if operating_status is not None:
            self.operating_status = operating_status

    @property
    def provisioning_status(self):
        """Gets the provisioning_status of this LoadBalancerStatusMember.

        provisioning的状态。 可以为：ACTIVE、PENDING_CREATE 或者ERROR。 说明：该字段为预留字段，暂未启用，默认为ACTIVE。

        :return: The provisioning_status of this LoadBalancerStatusMember.
        :rtype: str
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        """Sets the provisioning_status of this LoadBalancerStatusMember.

        provisioning的状态。 可以为：ACTIVE、PENDING_CREATE 或者ERROR。 说明：该字段为预留字段，暂未启用，默认为ACTIVE。

        :param provisioning_status: The provisioning_status of this LoadBalancerStatusMember.
        :type: str
        """
        self._provisioning_status = provisioning_status

    @property
    def address(self):
        """Gets the address of this LoadBalancerStatusMember.

        后端服务器ip。

        :return: The address of this LoadBalancerStatusMember.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this LoadBalancerStatusMember.

        后端服务器ip。

        :param address: The address of this LoadBalancerStatusMember.
        :type: str
        """
        self._address = address

    @property
    def protocol_port(self):
        """Gets the protocol_port of this LoadBalancerStatusMember.

        后端协议号。 取值范围[1, 65535]。

        :return: The protocol_port of this LoadBalancerStatusMember.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        """Sets the protocol_port of this LoadBalancerStatusMember.

        后端协议号。 取值范围[1, 65535]。

        :param protocol_port: The protocol_port of this LoadBalancerStatusMember.
        :type: int
        """
        self._protocol_port = protocol_port

    @property
    def id(self):
        """Gets the id of this LoadBalancerStatusMember.

        后端服务器ID。

        :return: The id of this LoadBalancerStatusMember.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LoadBalancerStatusMember.

        后端服务器ID。

        :param id: The id of this LoadBalancerStatusMember.
        :type: str
        """
        self._id = id

    @property
    def operating_status(self):
        """Gets the operating_status of this LoadBalancerStatusMember.

        操作状态。 可以为：ONLINE、OFFLINE、DEGRADED、DISABLED或NO_MONITOR。默认为ONLINE。

        :return: The operating_status of this LoadBalancerStatusMember.
        :rtype: str
        """
        return self._operating_status

    @operating_status.setter
    def operating_status(self, operating_status):
        """Sets the operating_status of this LoadBalancerStatusMember.

        操作状态。 可以为：ONLINE、OFFLINE、DEGRADED、DISABLED或NO_MONITOR。默认为ONLINE。

        :param operating_status: The operating_status of this LoadBalancerStatusMember.
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
        if not isinstance(other, LoadBalancerStatusMember):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
