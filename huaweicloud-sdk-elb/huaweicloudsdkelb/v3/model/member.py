# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Member:


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
        'project_id': 'str',
        'pool_id': 'str',
        'admin_state_up': 'bool',
        'subnet_cidr_id': 'str',
        'protocol_port': 'int',
        'weight': 'int',
        'address': 'str',
        'ip_version': 'str',
        'device_owner': 'str',
        'device_id': 'str',
        'operating_status': 'str',
        'loadbalancer_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'project_id': 'project_id',
        'pool_id': 'pool_id',
        'admin_state_up': 'admin_state_up',
        'subnet_cidr_id': 'subnet_cidr_id',
        'protocol_port': 'protocol_port',
        'weight': 'weight',
        'address': 'address',
        'ip_version': 'ip_version',
        'device_owner': 'device_owner',
        'device_id': 'device_id',
        'operating_status': 'operating_status',
        'loadbalancer_id': 'loadbalancer_id'
    }

    def __init__(self, id=None, name=None, project_id=None, pool_id=None, admin_state_up=None, subnet_cidr_id=None, protocol_port=None, weight=None, address=None, ip_version=None, device_owner=None, device_id=None, operating_status=None, loadbalancer_id=None):
        """Member - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._name = None
        self._project_id = None
        self._pool_id = None
        self._admin_state_up = None
        self._subnet_cidr_id = None
        self._protocol_port = None
        self._weight = None
        self._address = None
        self._ip_version = None
        self._device_owner = None
        self._device_id = None
        self._operating_status = None
        self._loadbalancer_id = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.project_id = project_id
        if pool_id is not None:
            self.pool_id = pool_id
        self.admin_state_up = admin_state_up
        if subnet_cidr_id is not None:
            self.subnet_cidr_id = subnet_cidr_id
        self.protocol_port = protocol_port
        self.weight = weight
        self.address = address
        self.ip_version = ip_version
        if device_owner is not None:
            self.device_owner = device_owner
        if device_id is not None:
            self.device_id = device_id
        self.operating_status = operating_status
        if loadbalancer_id is not None:
            self.loadbalancer_id = loadbalancer_id

    @property
    def id(self):
        """Gets the id of this Member.

        后端云服务器ID。

        :return: The id of this Member.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Member.

        后端云服务器ID。

        :param id: The id of this Member.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Member.

        后端云服务器名称。

        :return: The name of this Member.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Member.

        后端云服务器名称。

        :param name: The name of this Member.
        :type: str
        """
        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this Member.

        后端云服务器所在的项目ID。

        :return: The project_id of this Member.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Member.

        后端云服务器所在的项目ID。

        :param project_id: The project_id of this Member.
        :type: str
        """
        self._project_id = project_id

    @property
    def pool_id(self):
        """Gets the pool_id of this Member.

        所属服务器组ID。  注意：该字段当前仅GET /v3/{project_id}/elb/members 接口可见。

        :return: The pool_id of this Member.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """Sets the pool_id of this Member.

        所属服务器组ID。  注意：该字段当前仅GET /v3/{project_id}/elb/members 接口可见。

        :param pool_id: The pool_id of this Member.
        :type: str
        """
        self._pool_id = pool_id

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this Member.

        后端云服务器的管理状态；该字段虽然支持创建、更新，但实际取值决定于后端云服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。

        :return: The admin_state_up of this Member.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this Member.

        后端云服务器的管理状态；该字段虽然支持创建、更新，但实际取值决定于后端云服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。

        :param admin_state_up: The admin_state_up of this Member.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def subnet_cidr_id(self):
        """Gets the subnet_cidr_id of this Member.

        后端云服务器所在的子网ID。该子网和后端云服务器关联的负载均衡器的子网必须在同一VPC下。只支持指定IPv4的子网ID。暂不支持IPv6。 为空代表当前member为跨VPC后端

        :return: The subnet_cidr_id of this Member.
        :rtype: str
        """
        return self._subnet_cidr_id

    @subnet_cidr_id.setter
    def subnet_cidr_id(self, subnet_cidr_id):
        """Sets the subnet_cidr_id of this Member.

        后端云服务器所在的子网ID。该子网和后端云服务器关联的负载均衡器的子网必须在同一VPC下。只支持指定IPv4的子网ID。暂不支持IPv6。 为空代表当前member为跨VPC后端

        :param subnet_cidr_id: The subnet_cidr_id of this Member.
        :type: str
        """
        self._subnet_cidr_id = subnet_cidr_id

    @property
    def protocol_port(self):
        """Gets the protocol_port of this Member.

        后端服务器端口号

        :return: The protocol_port of this Member.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        """Sets the protocol_port of this Member.

        后端服务器端口号

        :param protocol_port: The protocol_port of this Member.
        :type: int
        """
        self._protocol_port = protocol_port

    @property
    def weight(self):
        """Gets the weight of this Member.

        后端云服务器的权重，请求按权重在同一后端云服务器组下的后端云服务器间分发。权重为0的后端不再接受新的请求。当后端云服务器所在的后端云服务器组的lb_algorithm的取值为SOURCE_IP时，该字段无效。

        :return: The weight of this Member.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this Member.

        后端云服务器的权重，请求按权重在同一后端云服务器组下的后端云服务器间分发。权重为0的后端不再接受新的请求。当后端云服务器所在的后端云服务器组的lb_algorithm的取值为SOURCE_IP时，该字段无效。

        :param weight: The weight of this Member.
        :type: int
        """
        self._weight = weight

    @property
    def address(self):
        """Gets the address of this Member.

        后端云服务器的对应的IP地址，这个IP必须在subnet_cidr_id字段的子网网段中。例如：192.168.3.11。只能指定为主网卡的IP。

        :return: The address of this Member.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Member.

        后端云服务器的对应的IP地址，这个IP必须在subnet_cidr_id字段的子网网段中。例如：192.168.3.11。只能指定为主网卡的IP。

        :param address: The address of this Member.
        :type: str
        """
        self._address = address

    @property
    def ip_version(self):
        """Gets the ip_version of this Member.

        只读属性，根据传入的address字段自动判断之后生成，取值范围(v4、v6)

        :return: The ip_version of this Member.
        :rtype: str
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this Member.

        只读属性，根据传入的address字段自动判断之后生成，取值范围(v4、v6)

        :param ip_version: The ip_version of this Member.
        :type: str
        """
        self._ip_version = ip_version

    @property
    def device_owner(self):
        """Gets the device_owner of this Member.

        设备使用者，为空表示后端服务器未关联到ECS。  注意：该字段当前仅GET /v3/{project_id}/elb/members 接口可见。

        :return: The device_owner of this Member.
        :rtype: str
        """
        return self._device_owner

    @device_owner.setter
    def device_owner(self, device_owner):
        """Sets the device_owner of this Member.

        设备使用者，为空表示后端服务器未关联到ECS。  注意：该字段当前仅GET /v3/{project_id}/elb/members 接口可见。

        :param device_owner: The device_owner of this Member.
        :type: str
        """
        self._device_owner = device_owner

    @property
    def device_id(self):
        """Gets the device_id of this Member.

        关联的ECS ID，为空表示后端服务器未关联到ECS。  注意：该字段当前仅GET /v3/{project_id}/elb/members 接口可见。

        :return: The device_id of this Member.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this Member.

        关联的ECS ID，为空表示后端服务器未关联到ECS。  注意：该字段当前仅GET /v3/{project_id}/elb/members 接口可见。

        :param device_id: The device_id of this Member.
        :type: str
        """
        self._device_id = device_id

    @property
    def operating_status(self):
        """Gets the operating_status of this Member.

        后端云服务器的健康状态，可以为ONLINE，NO_MONITOR，OFFLINE。

        :return: The operating_status of this Member.
        :rtype: str
        """
        return self._operating_status

    @operating_status.setter
    def operating_status(self, operating_status):
        """Sets the operating_status of this Member.

        后端云服务器的健康状态，可以为ONLINE，NO_MONITOR，OFFLINE。

        :param operating_status: The operating_status of this Member.
        :type: str
        """
        self._operating_status = operating_status

    @property
    def loadbalancer_id(self):
        """Gets the loadbalancer_id of this Member.

        所属负载均衡器ID。  注意：该字段当前仅GET /v3/{project_id}/elb/members 接口可见。

        :return: The loadbalancer_id of this Member.
        :rtype: str
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        """Sets the loadbalancer_id of this Member.

        所属负载均衡器ID。  注意：该字段当前仅GET /v3/{project_id}/elb/members 接口可见。

        :param loadbalancer_id: The loadbalancer_id of this Member.
        :type: str
        """
        self._loadbalancer_id = loadbalancer_id

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
        if not isinstance(other, Member):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
