# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        """LoadBalancerStatusMember

        The model defined in huaweicloud sdk

        :param provisioning_status: 后端服务器配置状态。取值：ACTIVE表示使用中。
        :type provisioning_status: str
        :param address: 后端服务器的IP地址。
        :type address: str
        :param protocol_port: 后端服务器的端口号。取值范围[1, 65535]。
        :type protocol_port: int
        :param id: 后端服务器ID。
        :type id: str
        :param operating_status: 后端服务器的操作状态。  取值： - ONLINE：后端服务器正常运行。 - NO_MONITOR：后端服务器健康检查未开启。 - DISABLED：后端服务器不可用。所属负载均衡器或后端服务器组或该后端服务器的admin_state_up&#x3D;flase时， 会出现该状态。注意该状态仅在当前接口中返回。 - OFFLINE：关联ECS已下线。
        :type operating_status: str
        """
        
        

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

        后端服务器配置状态。取值：ACTIVE表示使用中。

        :return: The provisioning_status of this LoadBalancerStatusMember.
        :rtype: str
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        """Sets the provisioning_status of this LoadBalancerStatusMember.

        后端服务器配置状态。取值：ACTIVE表示使用中。

        :param provisioning_status: The provisioning_status of this LoadBalancerStatusMember.
        :type provisioning_status: str
        """
        self._provisioning_status = provisioning_status

    @property
    def address(self):
        """Gets the address of this LoadBalancerStatusMember.

        后端服务器的IP地址。

        :return: The address of this LoadBalancerStatusMember.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this LoadBalancerStatusMember.

        后端服务器的IP地址。

        :param address: The address of this LoadBalancerStatusMember.
        :type address: str
        """
        self._address = address

    @property
    def protocol_port(self):
        """Gets the protocol_port of this LoadBalancerStatusMember.

        后端服务器的端口号。取值范围[1, 65535]。

        :return: The protocol_port of this LoadBalancerStatusMember.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        """Sets the protocol_port of this LoadBalancerStatusMember.

        后端服务器的端口号。取值范围[1, 65535]。

        :param protocol_port: The protocol_port of this LoadBalancerStatusMember.
        :type protocol_port: int
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
        :type id: str
        """
        self._id = id

    @property
    def operating_status(self):
        """Gets the operating_status of this LoadBalancerStatusMember.

        后端服务器的操作状态。  取值： - ONLINE：后端服务器正常运行。 - NO_MONITOR：后端服务器健康检查未开启。 - DISABLED：后端服务器不可用。所属负载均衡器或后端服务器组或该后端服务器的admin_state_up=flase时， 会出现该状态。注意该状态仅在当前接口中返回。 - OFFLINE：关联ECS已下线。

        :return: The operating_status of this LoadBalancerStatusMember.
        :rtype: str
        """
        return self._operating_status

    @operating_status.setter
    def operating_status(self, operating_status):
        """Sets the operating_status of this LoadBalancerStatusMember.

        后端服务器的操作状态。  取值： - ONLINE：后端服务器正常运行。 - NO_MONITOR：后端服务器健康检查未开启。 - DISABLED：后端服务器不可用。所属负载均衡器或后端服务器组或该后端服务器的admin_state_up=flase时， 会出现该状态。注意该状态仅在当前接口中返回。 - OFFLINE：关联ECS已下线。

        :param operating_status: The operating_status of this LoadBalancerStatusMember.
        :type operating_status: str
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
        if not isinstance(other, LoadBalancerStatusMember):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
