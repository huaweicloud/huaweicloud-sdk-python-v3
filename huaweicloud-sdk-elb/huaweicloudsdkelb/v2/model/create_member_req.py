# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMemberReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tenant_id': 'str',
        'name': 'str',
        'admin_state_up': 'bool',
        'protocol_port': 'int',
        'subnet_id': 'str',
        'address': 'str',
        'weight': 'int'
    }

    attribute_map = {
        'tenant_id': 'tenant_id',
        'name': 'name',
        'admin_state_up': 'admin_state_up',
        'protocol_port': 'protocol_port',
        'subnet_id': 'subnet_id',
        'address': 'address',
        'weight': 'weight'
    }

    def __init__(self, tenant_id=None, name=None, admin_state_up=None, protocol_port=None, subnet_id=None, address=None, weight=None):
        """CreateMemberReq

        The model defined in huaweicloud sdk

        :param tenant_id: 后端云服务器所在的项目ID。
        :type tenant_id: str
        :param name: 后端云服务器名称。
        :type name: str
        :param admin_state_up: 后端云服务器的管理状态；该字段虽然支持创建、更新，但实际取值决定于后端云服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。
        :type admin_state_up: bool
        :param protocol_port: 后端端口和协议号
        :type protocol_port: int
        :param subnet_id: 后端云服务器所在的子网ID。该子网和后端云服务器关联的负载均衡器的子网必须在同一VPC下。只支持指定IPv4的子网ID。暂不支持IPv6。
        :type subnet_id: str
        :param address: 后端云服务器的对应的IP地址，这个IP必须在subnet_id字段的子网网段中。例如：192.168.3.11。只能指定为主网卡的IP。
        :type address: str
        :param weight: 后端云服务器的权重，请求按权重在同一后端云服务器组下的后端云服务器间分发。权重为0的后端不再接受新的请求。当后端云服务器所在的后端云服务器组的lb_algorithm的取值为SOURCE_IP时，该字段无效。
        :type weight: int
        """
        
        

        self._tenant_id = None
        self._name = None
        self._admin_state_up = None
        self._protocol_port = None
        self._subnet_id = None
        self._address = None
        self._weight = None
        self.discriminator = None

        if tenant_id is not None:
            self.tenant_id = tenant_id
        if name is not None:
            self.name = name
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        self.protocol_port = protocol_port
        self.subnet_id = subnet_id
        self.address = address
        if weight is not None:
            self.weight = weight

    @property
    def tenant_id(self):
        """Gets the tenant_id of this CreateMemberReq.

        后端云服务器所在的项目ID。

        :return: The tenant_id of this CreateMemberReq.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this CreateMemberReq.

        后端云服务器所在的项目ID。

        :param tenant_id: The tenant_id of this CreateMemberReq.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def name(self):
        """Gets the name of this CreateMemberReq.

        后端云服务器名称。

        :return: The name of this CreateMemberReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateMemberReq.

        后端云服务器名称。

        :param name: The name of this CreateMemberReq.
        :type name: str
        """
        self._name = name

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this CreateMemberReq.

        后端云服务器的管理状态；该字段虽然支持创建、更新，但实际取值决定于后端云服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。

        :return: The admin_state_up of this CreateMemberReq.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this CreateMemberReq.

        后端云服务器的管理状态；该字段虽然支持创建、更新，但实际取值决定于后端云服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。

        :param admin_state_up: The admin_state_up of this CreateMemberReq.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def protocol_port(self):
        """Gets the protocol_port of this CreateMemberReq.

        后端端口和协议号

        :return: The protocol_port of this CreateMemberReq.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        """Sets the protocol_port of this CreateMemberReq.

        后端端口和协议号

        :param protocol_port: The protocol_port of this CreateMemberReq.
        :type protocol_port: int
        """
        self._protocol_port = protocol_port

    @property
    def subnet_id(self):
        """Gets the subnet_id of this CreateMemberReq.

        后端云服务器所在的子网ID。该子网和后端云服务器关联的负载均衡器的子网必须在同一VPC下。只支持指定IPv4的子网ID。暂不支持IPv6。

        :return: The subnet_id of this CreateMemberReq.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this CreateMemberReq.

        后端云服务器所在的子网ID。该子网和后端云服务器关联的负载均衡器的子网必须在同一VPC下。只支持指定IPv4的子网ID。暂不支持IPv6。

        :param subnet_id: The subnet_id of this CreateMemberReq.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def address(self):
        """Gets the address of this CreateMemberReq.

        后端云服务器的对应的IP地址，这个IP必须在subnet_id字段的子网网段中。例如：192.168.3.11。只能指定为主网卡的IP。

        :return: The address of this CreateMemberReq.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this CreateMemberReq.

        后端云服务器的对应的IP地址，这个IP必须在subnet_id字段的子网网段中。例如：192.168.3.11。只能指定为主网卡的IP。

        :param address: The address of this CreateMemberReq.
        :type address: str
        """
        self._address = address

    @property
    def weight(self):
        """Gets the weight of this CreateMemberReq.

        后端云服务器的权重，请求按权重在同一后端云服务器组下的后端云服务器间分发。权重为0的后端不再接受新的请求。当后端云服务器所在的后端云服务器组的lb_algorithm的取值为SOURCE_IP时，该字段无效。

        :return: The weight of this CreateMemberReq.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this CreateMemberReq.

        后端云服务器的权重，请求按权重在同一后端云服务器组下的后端云服务器间分发。权重为0的后端不再接受新的请求。当后端云服务器所在的后端云服务器组的lb_algorithm的取值为SOURCE_IP时，该字段无效。

        :param weight: The weight of this CreateMemberReq.
        :type weight: int
        """
        self._weight = weight

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
        if not isinstance(other, CreateMemberReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
