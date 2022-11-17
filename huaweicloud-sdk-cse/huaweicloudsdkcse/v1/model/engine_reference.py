# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EngineReference:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpc': 'str',
        'az_list': 'list[str]',
        'network_id': 'str',
        'subnet_cidr': 'str',
        'subnet_cidr_v6': 'str',
        'subnet_gateway': 'str',
        'public_ip_id': 'str',
        'service_limit': 'int',
        'instance_limit': 'int',
        'inputs': 'dict(str, str)'
    }

    attribute_map = {
        'vpc': 'vpc',
        'az_list': 'az_list',
        'network_id': 'network_id',
        'subnet_cidr': 'subnet_cidr',
        'subnet_cidr_v6': 'subnet_cidr_v6',
        'subnet_gateway': 'subnet_gateway',
        'public_ip_id': 'public_ip_id',
        'service_limit': 'service_limit',
        'instance_limit': 'instance_limit',
        'inputs': 'inputs'
    }

    def __init__(self, vpc=None, az_list=None, network_id=None, subnet_cidr=None, subnet_cidr_v6=None, subnet_gateway=None, public_ip_id=None, service_limit=None, instance_limit=None, inputs=None):
        """EngineReference

        The model defined in huaweicloud sdk

        :param vpc: vpc名称
        :type vpc: str
        :param az_list: 微服务引擎专享版部署的可用区列表
        :type az_list: list[str]
        :param network_id: 微服务引擎专享版子网网络ID
        :type network_id: str
        :param subnet_cidr: 微服务引擎专享版ipv4子网划分
        :type subnet_cidr: str
        :param subnet_cidr_v6: 微服务引擎专享版ipv6子网划分
        :type subnet_cidr_v6: str
        :param subnet_gateway: 微服务引擎专享版子网网关
        :type subnet_gateway: str
        :param public_ip_id: 微服务引擎专享版公网地址ID
        :type public_ip_id: str
        :param service_limit: 微服务引擎专享版可支持的微服务总数
        :type service_limit: int
        :param instance_limit: 微服务引擎专享版可支持的实例总数
        :type instance_limit: int
        :param inputs: 微服务引擎专享版附加参数
        :type inputs: dict(str, str)
        """
        
        

        self._vpc = None
        self._az_list = None
        self._network_id = None
        self._subnet_cidr = None
        self._subnet_cidr_v6 = None
        self._subnet_gateway = None
        self._public_ip_id = None
        self._service_limit = None
        self._instance_limit = None
        self._inputs = None
        self.discriminator = None

        if vpc is not None:
            self.vpc = vpc
        if az_list is not None:
            self.az_list = az_list
        if network_id is not None:
            self.network_id = network_id
        if subnet_cidr is not None:
            self.subnet_cidr = subnet_cidr
        if subnet_cidr_v6 is not None:
            self.subnet_cidr_v6 = subnet_cidr_v6
        if subnet_gateway is not None:
            self.subnet_gateway = subnet_gateway
        if public_ip_id is not None:
            self.public_ip_id = public_ip_id
        if service_limit is not None:
            self.service_limit = service_limit
        if instance_limit is not None:
            self.instance_limit = instance_limit
        if inputs is not None:
            self.inputs = inputs

    @property
    def vpc(self):
        """Gets the vpc of this EngineReference.

        vpc名称

        :return: The vpc of this EngineReference.
        :rtype: str
        """
        return self._vpc

    @vpc.setter
    def vpc(self, vpc):
        """Sets the vpc of this EngineReference.

        vpc名称

        :param vpc: The vpc of this EngineReference.
        :type vpc: str
        """
        self._vpc = vpc

    @property
    def az_list(self):
        """Gets the az_list of this EngineReference.

        微服务引擎专享版部署的可用区列表

        :return: The az_list of this EngineReference.
        :rtype: list[str]
        """
        return self._az_list

    @az_list.setter
    def az_list(self, az_list):
        """Sets the az_list of this EngineReference.

        微服务引擎专享版部署的可用区列表

        :param az_list: The az_list of this EngineReference.
        :type az_list: list[str]
        """
        self._az_list = az_list

    @property
    def network_id(self):
        """Gets the network_id of this EngineReference.

        微服务引擎专享版子网网络ID

        :return: The network_id of this EngineReference.
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this EngineReference.

        微服务引擎专享版子网网络ID

        :param network_id: The network_id of this EngineReference.
        :type network_id: str
        """
        self._network_id = network_id

    @property
    def subnet_cidr(self):
        """Gets the subnet_cidr of this EngineReference.

        微服务引擎专享版ipv4子网划分

        :return: The subnet_cidr of this EngineReference.
        :rtype: str
        """
        return self._subnet_cidr

    @subnet_cidr.setter
    def subnet_cidr(self, subnet_cidr):
        """Sets the subnet_cidr of this EngineReference.

        微服务引擎专享版ipv4子网划分

        :param subnet_cidr: The subnet_cidr of this EngineReference.
        :type subnet_cidr: str
        """
        self._subnet_cidr = subnet_cidr

    @property
    def subnet_cidr_v6(self):
        """Gets the subnet_cidr_v6 of this EngineReference.

        微服务引擎专享版ipv6子网划分

        :return: The subnet_cidr_v6 of this EngineReference.
        :rtype: str
        """
        return self._subnet_cidr_v6

    @subnet_cidr_v6.setter
    def subnet_cidr_v6(self, subnet_cidr_v6):
        """Sets the subnet_cidr_v6 of this EngineReference.

        微服务引擎专享版ipv6子网划分

        :param subnet_cidr_v6: The subnet_cidr_v6 of this EngineReference.
        :type subnet_cidr_v6: str
        """
        self._subnet_cidr_v6 = subnet_cidr_v6

    @property
    def subnet_gateway(self):
        """Gets the subnet_gateway of this EngineReference.

        微服务引擎专享版子网网关

        :return: The subnet_gateway of this EngineReference.
        :rtype: str
        """
        return self._subnet_gateway

    @subnet_gateway.setter
    def subnet_gateway(self, subnet_gateway):
        """Sets the subnet_gateway of this EngineReference.

        微服务引擎专享版子网网关

        :param subnet_gateway: The subnet_gateway of this EngineReference.
        :type subnet_gateway: str
        """
        self._subnet_gateway = subnet_gateway

    @property
    def public_ip_id(self):
        """Gets the public_ip_id of this EngineReference.

        微服务引擎专享版公网地址ID

        :return: The public_ip_id of this EngineReference.
        :rtype: str
        """
        return self._public_ip_id

    @public_ip_id.setter
    def public_ip_id(self, public_ip_id):
        """Sets the public_ip_id of this EngineReference.

        微服务引擎专享版公网地址ID

        :param public_ip_id: The public_ip_id of this EngineReference.
        :type public_ip_id: str
        """
        self._public_ip_id = public_ip_id

    @property
    def service_limit(self):
        """Gets the service_limit of this EngineReference.

        微服务引擎专享版可支持的微服务总数

        :return: The service_limit of this EngineReference.
        :rtype: int
        """
        return self._service_limit

    @service_limit.setter
    def service_limit(self, service_limit):
        """Sets the service_limit of this EngineReference.

        微服务引擎专享版可支持的微服务总数

        :param service_limit: The service_limit of this EngineReference.
        :type service_limit: int
        """
        self._service_limit = service_limit

    @property
    def instance_limit(self):
        """Gets the instance_limit of this EngineReference.

        微服务引擎专享版可支持的实例总数

        :return: The instance_limit of this EngineReference.
        :rtype: int
        """
        return self._instance_limit

    @instance_limit.setter
    def instance_limit(self, instance_limit):
        """Sets the instance_limit of this EngineReference.

        微服务引擎专享版可支持的实例总数

        :param instance_limit: The instance_limit of this EngineReference.
        :type instance_limit: int
        """
        self._instance_limit = instance_limit

    @property
    def inputs(self):
        """Gets the inputs of this EngineReference.

        微服务引擎专享版附加参数

        :return: The inputs of this EngineReference.
        :rtype: dict(str, str)
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this EngineReference.

        微服务引擎专享版附加参数

        :param inputs: The inputs of this EngineReference.
        :type inputs: dict(str, str)
        """
        self._inputs = inputs

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
        if not isinstance(other, EngineReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
