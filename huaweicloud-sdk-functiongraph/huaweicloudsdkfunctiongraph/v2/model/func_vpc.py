# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FuncVpc:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'namespace': 'str',
        'vpc_name': 'str',
        'vpc_id': 'str',
        'subnet_name': 'str',
        'subnet_id': 'str',
        'cidr': 'str',
        'gateway': 'str',
        'security_groups': 'list[str]',
        'is_safety': 'bool'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'namespace': 'namespace',
        'vpc_name': 'vpc_name',
        'vpc_id': 'vpc_id',
        'subnet_name': 'subnet_name',
        'subnet_id': 'subnet_id',
        'cidr': 'cidr',
        'gateway': 'gateway',
        'security_groups': 'security_groups',
        'is_safety': 'is_safety'
    }

    def __init__(self, domain_id=None, namespace=None, vpc_name=None, vpc_id=None, subnet_name=None, subnet_id=None, cidr=None, gateway=None, security_groups=None, is_safety=None):
        r"""FuncVpc

        The model defined in huaweicloud sdk

        :param domain_id: 域名id。
        :type domain_id: str
        :param namespace: 租户的project id。
        :type namespace: str
        :param vpc_name: 虚拟私有云名称。
        :type vpc_name: str
        :param vpc_id: 虚拟私有云唯一标识。
        :type vpc_id: str
        :param subnet_name: 子网名称。
        :type subnet_name: str
        :param subnet_id: 子网编号。
        :type subnet_id: str
        :param cidr: 子网掩码。
        :type cidr: str
        :param gateway: 网关。
        :type gateway: str
        :param security_groups: 安全组
        :type security_groups: list[str]
        :param is_safety: 是否开启安全访问。开启时，需要您自行配置VPCEP网络但可以提供更安全的VPC连接访问并打通内网域名。注意：开启后无法关闭。
        :type is_safety: bool
        """
        
        

        self._domain_id = None
        self._namespace = None
        self._vpc_name = None
        self._vpc_id = None
        self._subnet_name = None
        self._subnet_id = None
        self._cidr = None
        self._gateway = None
        self._security_groups = None
        self._is_safety = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if namespace is not None:
            self.namespace = namespace
        if vpc_name is not None:
            self.vpc_name = vpc_name
        self.vpc_id = vpc_id
        if subnet_name is not None:
            self.subnet_name = subnet_name
        self.subnet_id = subnet_id
        if cidr is not None:
            self.cidr = cidr
        if gateway is not None:
            self.gateway = gateway
        if security_groups is not None:
            self.security_groups = security_groups
        if is_safety is not None:
            self.is_safety = is_safety

    @property
    def domain_id(self):
        r"""Gets the domain_id of this FuncVpc.

        域名id。

        :return: The domain_id of this FuncVpc.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this FuncVpc.

        域名id。

        :param domain_id: The domain_id of this FuncVpc.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def namespace(self):
        r"""Gets the namespace of this FuncVpc.

        租户的project id。

        :return: The namespace of this FuncVpc.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this FuncVpc.

        租户的project id。

        :param namespace: The namespace of this FuncVpc.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def vpc_name(self):
        r"""Gets the vpc_name of this FuncVpc.

        虚拟私有云名称。

        :return: The vpc_name of this FuncVpc.
        :rtype: str
        """
        return self._vpc_name

    @vpc_name.setter
    def vpc_name(self, vpc_name):
        r"""Sets the vpc_name of this FuncVpc.

        虚拟私有云名称。

        :param vpc_name: The vpc_name of this FuncVpc.
        :type vpc_name: str
        """
        self._vpc_name = vpc_name

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this FuncVpc.

        虚拟私有云唯一标识。

        :return: The vpc_id of this FuncVpc.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this FuncVpc.

        虚拟私有云唯一标识。

        :param vpc_id: The vpc_id of this FuncVpc.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_name(self):
        r"""Gets the subnet_name of this FuncVpc.

        子网名称。

        :return: The subnet_name of this FuncVpc.
        :rtype: str
        """
        return self._subnet_name

    @subnet_name.setter
    def subnet_name(self, subnet_name):
        r"""Sets the subnet_name of this FuncVpc.

        子网名称。

        :param subnet_name: The subnet_name of this FuncVpc.
        :type subnet_name: str
        """
        self._subnet_name = subnet_name

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this FuncVpc.

        子网编号。

        :return: The subnet_id of this FuncVpc.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this FuncVpc.

        子网编号。

        :param subnet_id: The subnet_id of this FuncVpc.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def cidr(self):
        r"""Gets the cidr of this FuncVpc.

        子网掩码。

        :return: The cidr of this FuncVpc.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        r"""Sets the cidr of this FuncVpc.

        子网掩码。

        :param cidr: The cidr of this FuncVpc.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def gateway(self):
        r"""Gets the gateway of this FuncVpc.

        网关。

        :return: The gateway of this FuncVpc.
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        r"""Sets the gateway of this FuncVpc.

        网关。

        :param gateway: The gateway of this FuncVpc.
        :type gateway: str
        """
        self._gateway = gateway

    @property
    def security_groups(self):
        r"""Gets the security_groups of this FuncVpc.

        安全组

        :return: The security_groups of this FuncVpc.
        :rtype: list[str]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        r"""Sets the security_groups of this FuncVpc.

        安全组

        :param security_groups: The security_groups of this FuncVpc.
        :type security_groups: list[str]
        """
        self._security_groups = security_groups

    @property
    def is_safety(self):
        r"""Gets the is_safety of this FuncVpc.

        是否开启安全访问。开启时，需要您自行配置VPCEP网络但可以提供更安全的VPC连接访问并打通内网域名。注意：开启后无法关闭。

        :return: The is_safety of this FuncVpc.
        :rtype: bool
        """
        return self._is_safety

    @is_safety.setter
    def is_safety(self, is_safety):
        r"""Sets the is_safety of this FuncVpc.

        是否开启安全访问。开启时，需要您自行配置VPCEP网络但可以提供更安全的VPC连接访问并打通内网域名。注意：开启后无法关闭。

        :param is_safety: The is_safety of this FuncVpc.
        :type is_safety: bool
        """
        self._is_safety = is_safety

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
        if not isinstance(other, FuncVpc):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
