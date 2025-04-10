# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTenantVpcIgwRequestBodyVpcIgw:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpc_id': 'str',
        'network_id': 'str',
        'add_route': 'bool',
        'enable_ipv6': 'bool',
        'name': 'str'
    }

    attribute_map = {
        'vpc_id': 'vpc_id',
        'network_id': 'network_id',
        'add_route': 'add_route',
        'enable_ipv6': 'enable_ipv6',
        'name': 'name'
    }

    def __init__(self, vpc_id=None, network_id=None, add_route=None, enable_ipv6=None, name=None):
        r"""CreateTenantVpcIgwRequestBodyVpcIgw

        The model defined in huaweicloud sdk

        :param vpc_id: vpcid
        :type vpc_id: str
        :param network_id: 创建VPC IGW的network id
        :type network_id: str
        :param add_route: 是否添加默认路由
        :type add_route: bool
        :param enable_ipv6: 是否使能ipv6
        :type enable_ipv6: bool
        :param name: 虚拟IGW的名称
        :type name: str
        """
        
        

        self._vpc_id = None
        self._network_id = None
        self._add_route = None
        self._enable_ipv6 = None
        self._name = None
        self.discriminator = None

        self.vpc_id = vpc_id
        if network_id is not None:
            self.network_id = network_id
        if add_route is not None:
            self.add_route = add_route
        if enable_ipv6 is not None:
            self.enable_ipv6 = enable_ipv6
        if name is not None:
            self.name = name

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CreateTenantVpcIgwRequestBodyVpcIgw.

        vpcid

        :return: The vpc_id of this CreateTenantVpcIgwRequestBodyVpcIgw.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CreateTenantVpcIgwRequestBodyVpcIgw.

        vpcid

        :param vpc_id: The vpc_id of this CreateTenantVpcIgwRequestBodyVpcIgw.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def network_id(self):
        r"""Gets the network_id of this CreateTenantVpcIgwRequestBodyVpcIgw.

        创建VPC IGW的network id

        :return: The network_id of this CreateTenantVpcIgwRequestBodyVpcIgw.
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        r"""Sets the network_id of this CreateTenantVpcIgwRequestBodyVpcIgw.

        创建VPC IGW的network id

        :param network_id: The network_id of this CreateTenantVpcIgwRequestBodyVpcIgw.
        :type network_id: str
        """
        self._network_id = network_id

    @property
    def add_route(self):
        r"""Gets the add_route of this CreateTenantVpcIgwRequestBodyVpcIgw.

        是否添加默认路由

        :return: The add_route of this CreateTenantVpcIgwRequestBodyVpcIgw.
        :rtype: bool
        """
        return self._add_route

    @add_route.setter
    def add_route(self, add_route):
        r"""Sets the add_route of this CreateTenantVpcIgwRequestBodyVpcIgw.

        是否添加默认路由

        :param add_route: The add_route of this CreateTenantVpcIgwRequestBodyVpcIgw.
        :type add_route: bool
        """
        self._add_route = add_route

    @property
    def enable_ipv6(self):
        r"""Gets the enable_ipv6 of this CreateTenantVpcIgwRequestBodyVpcIgw.

        是否使能ipv6

        :return: The enable_ipv6 of this CreateTenantVpcIgwRequestBodyVpcIgw.
        :rtype: bool
        """
        return self._enable_ipv6

    @enable_ipv6.setter
    def enable_ipv6(self, enable_ipv6):
        r"""Sets the enable_ipv6 of this CreateTenantVpcIgwRequestBodyVpcIgw.

        是否使能ipv6

        :param enable_ipv6: The enable_ipv6 of this CreateTenantVpcIgwRequestBodyVpcIgw.
        :type enable_ipv6: bool
        """
        self._enable_ipv6 = enable_ipv6

    @property
    def name(self):
        r"""Gets the name of this CreateTenantVpcIgwRequestBodyVpcIgw.

        虚拟IGW的名称

        :return: The name of this CreateTenantVpcIgwRequestBodyVpcIgw.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateTenantVpcIgwRequestBodyVpcIgw.

        虚拟IGW的名称

        :param name: The name of this CreateTenantVpcIgwRequestBodyVpcIgw.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, CreateTenantVpcIgwRequestBodyVpcIgw):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
