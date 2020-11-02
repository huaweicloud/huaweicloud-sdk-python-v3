# coding: utf-8

import pprint
import re

import six





class MembersInStatusResp:


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
        'address': 'str',
        'protocol_port': 'int',
        'operating_status': 'str',
        'provisioning_status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'address': 'address',
        'protocol_port': 'protocol_port',
        'operating_status': 'operating_status',
        'provisioning_status': 'provisioning_status'
    }

    def __init__(self, id=None, address=None, protocol_port=None, operating_status=None, provisioning_status=None):
        """MembersInStatusResp - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._address = None
        self._protocol_port = None
        self._operating_status = None
        self._provisioning_status = None
        self.discriminator = None

        self.id = id
        self.address = address
        self.protocol_port = protocol_port
        self.operating_status = operating_status
        self.provisioning_status = provisioning_status

    @property
    def id(self):
        """Gets the id of this MembersInStatusResp.

        后端云服务器ID

        :return: The id of this MembersInStatusResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MembersInStatusResp.

        后端云服务器ID

        :param id: The id of this MembersInStatusResp.
        :type: str
        """
        self._id = id

    @property
    def address(self):
        """Gets the address of this MembersInStatusResp.

        后端云服务器的IP地址

        :return: The address of this MembersInStatusResp.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this MembersInStatusResp.

        后端云服务器的IP地址

        :param address: The address of this MembersInStatusResp.
        :type: str
        """
        self._address = address

    @property
    def protocol_port(self):
        """Gets the protocol_port of this MembersInStatusResp.

        后端云服务器的端口号

        :return: The protocol_port of this MembersInStatusResp.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        """Sets the protocol_port of this MembersInStatusResp.

        后端云服务器的端口号

        :param protocol_port: The protocol_port of this MembersInStatusResp.
        :type: int
        """
        self._protocol_port = protocol_port

    @property
    def operating_status(self):
        """Gets the operating_status of this MembersInStatusResp.

        后端云服务器的健康检状态；可以为：ONLINE：健康检查在线；OFFLINE：健康检查离线；DISABLED：后端云服务器无对应的弹性云服务器；NO_MONITOR：健康检查未开启

        :return: The operating_status of this MembersInStatusResp.
        :rtype: str
        """
        return self._operating_status

    @operating_status.setter
    def operating_status(self, operating_status):
        """Sets the operating_status of this MembersInStatusResp.

        后端云服务器的健康检状态；可以为：ONLINE：健康检查在线；OFFLINE：健康检查离线；DISABLED：后端云服务器无对应的弹性云服务器；NO_MONITOR：健康检查未开启

        :param operating_status: The operating_status of this MembersInStatusResp.
        :type: str
        """
        self._operating_status = operating_status

    @property
    def provisioning_status(self):
        """Gets the provisioning_status of this MembersInStatusResp.

        监听器的配置状态；该字段为预留字段，暂未启用。默认为ACTIVE。

        :return: The provisioning_status of this MembersInStatusResp.
        :rtype: str
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        """Sets the provisioning_status of this MembersInStatusResp.

        监听器的配置状态；该字段为预留字段，暂未启用。默认为ACTIVE。

        :param provisioning_status: The provisioning_status of this MembersInStatusResp.
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
        if not isinstance(other, MembersInStatusResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
