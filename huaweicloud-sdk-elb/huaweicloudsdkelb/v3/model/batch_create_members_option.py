# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateMembersOption:

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
        'address': 'str',
        'protocol_port': 'int',
        'subnet_cidr_id': 'str',
        'weight': 'int'
    }

    attribute_map = {
        'name': 'name',
        'address': 'address',
        'protocol_port': 'protocol_port',
        'subnet_cidr_id': 'subnet_cidr_id',
        'weight': 'weight'
    }

    def __init__(self, name=None, address=None, protocol_port=None, subnet_cidr_id=None, weight=None):
        """BatchCreateMembersOption

        The model defined in huaweicloud sdk

        :param name: 后端服务器名称。
        :type name: str
        :param address: 后端云服务器的对应的IP地址，这个IP必须在subnet_cidr_id字段的子网网段中。例如：192.168.3.11。  subnet_cidr_id为空代表添加跨VPC后端，此时address必须为ipv4地址。
        :type address: str
        :param protocol_port: 后端服务器端口号。
        :type protocol_port: int
        :param subnet_cidr_id: 后端云服务器所在的子网ID。该子网和后端云服务器关联的负载均衡器的子网必须在同一VPC下。  当所在LB未开启跨VPC后端，该参数必填。  当所在LB开启跨VPC后端，该参数非必填，表示添加跨VPC后端，此时address必须为ipv4地址， pool的协议必须为TCP/HTTP/HTTPS，pool所属的LB的跨VPC后端转发能力必须打开。
        :type subnet_cidr_id: str
        :param weight: 后端云服务器的权重，请求将根据pool配置的负载均衡算法和后端云服务器的权重进行负载分发。 权重值越大，分发的请求越多。权重为0的后端不再接受新的请求。  取值：0-100，默认1。  使用说明：若所在pool的lb_algorithm取值为SOURCE_IP，该字段无效。
        :type weight: int
        """
        
        

        self._name = None
        self._address = None
        self._protocol_port = None
        self._subnet_cidr_id = None
        self._weight = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.address = address
        self.protocol_port = protocol_port
        if subnet_cidr_id is not None:
            self.subnet_cidr_id = subnet_cidr_id
        if weight is not None:
            self.weight = weight

    @property
    def name(self):
        """Gets the name of this BatchCreateMembersOption.

        后端服务器名称。

        :return: The name of this BatchCreateMembersOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BatchCreateMembersOption.

        后端服务器名称。

        :param name: The name of this BatchCreateMembersOption.
        :type name: str
        """
        self._name = name

    @property
    def address(self):
        """Gets the address of this BatchCreateMembersOption.

        后端云服务器的对应的IP地址，这个IP必须在subnet_cidr_id字段的子网网段中。例如：192.168.3.11。  subnet_cidr_id为空代表添加跨VPC后端，此时address必须为ipv4地址。

        :return: The address of this BatchCreateMembersOption.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this BatchCreateMembersOption.

        后端云服务器的对应的IP地址，这个IP必须在subnet_cidr_id字段的子网网段中。例如：192.168.3.11。  subnet_cidr_id为空代表添加跨VPC后端，此时address必须为ipv4地址。

        :param address: The address of this BatchCreateMembersOption.
        :type address: str
        """
        self._address = address

    @property
    def protocol_port(self):
        """Gets the protocol_port of this BatchCreateMembersOption.

        后端服务器端口号。

        :return: The protocol_port of this BatchCreateMembersOption.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        """Sets the protocol_port of this BatchCreateMembersOption.

        后端服务器端口号。

        :param protocol_port: The protocol_port of this BatchCreateMembersOption.
        :type protocol_port: int
        """
        self._protocol_port = protocol_port

    @property
    def subnet_cidr_id(self):
        """Gets the subnet_cidr_id of this BatchCreateMembersOption.

        后端云服务器所在的子网ID。该子网和后端云服务器关联的负载均衡器的子网必须在同一VPC下。  当所在LB未开启跨VPC后端，该参数必填。  当所在LB开启跨VPC后端，该参数非必填，表示添加跨VPC后端，此时address必须为ipv4地址， pool的协议必须为TCP/HTTP/HTTPS，pool所属的LB的跨VPC后端转发能力必须打开。

        :return: The subnet_cidr_id of this BatchCreateMembersOption.
        :rtype: str
        """
        return self._subnet_cidr_id

    @subnet_cidr_id.setter
    def subnet_cidr_id(self, subnet_cidr_id):
        """Sets the subnet_cidr_id of this BatchCreateMembersOption.

        后端云服务器所在的子网ID。该子网和后端云服务器关联的负载均衡器的子网必须在同一VPC下。  当所在LB未开启跨VPC后端，该参数必填。  当所在LB开启跨VPC后端，该参数非必填，表示添加跨VPC后端，此时address必须为ipv4地址， pool的协议必须为TCP/HTTP/HTTPS，pool所属的LB的跨VPC后端转发能力必须打开。

        :param subnet_cidr_id: The subnet_cidr_id of this BatchCreateMembersOption.
        :type subnet_cidr_id: str
        """
        self._subnet_cidr_id = subnet_cidr_id

    @property
    def weight(self):
        """Gets the weight of this BatchCreateMembersOption.

        后端云服务器的权重，请求将根据pool配置的负载均衡算法和后端云服务器的权重进行负载分发。 权重值越大，分发的请求越多。权重为0的后端不再接受新的请求。  取值：0-100，默认1。  使用说明：若所在pool的lb_algorithm取值为SOURCE_IP，该字段无效。

        :return: The weight of this BatchCreateMembersOption.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this BatchCreateMembersOption.

        后端云服务器的权重，请求将根据pool配置的负载均衡算法和后端云服务器的权重进行负载分发。 权重值越大，分发的请求越多。权重为0的后端不再接受新的请求。  取值：0-100，默认1。  使用说明：若所在pool的lb_algorithm取值为SOURCE_IP，该字段无效。

        :param weight: The weight of this BatchCreateMembersOption.
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
        if not isinstance(other, BatchCreateMembersOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
