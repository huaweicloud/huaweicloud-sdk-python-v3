# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterGroupSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_namespaces': 'list[str]',
        'federation_id': 'str',
        'description': 'str',
        'dns_suffix': 'list[str]',
        'federation_expiration_timestamp': 'str',
        'policy_id': 'str',
        'federation_version': 'str',
        'connect_gateway_endpoints': 'list[ConnectEndpoint]'
    }

    attribute_map = {
        'rule_namespaces': 'ruleNamespaces',
        'federation_id': 'federationId',
        'description': 'description',
        'dns_suffix': 'dnsSuffix',
        'federation_expiration_timestamp': 'federationExpirationTimestamp',
        'policy_id': 'policyId',
        'federation_version': 'federationVersion',
        'connect_gateway_endpoints': 'connectGatewayEndpoints'
    }

    def __init__(self, rule_namespaces=None, federation_id=None, description=None, dns_suffix=None, federation_expiration_timestamp=None, policy_id=None, federation_version=None, connect_gateway_endpoints=None):
        r"""ClusterGroupSpec

        The model defined in huaweicloud sdk

        :param rule_namespaces: 权限策略关联的命名空间列表
        :type rule_namespaces: list[str]
        :param federation_id: 舰队启用联邦ID
        :type federation_id: str
        :param description: 描述信息
        :type description: str
        :param dns_suffix: 舰队对应联邦的DNS后缀，开启联邦后可见
        :type dns_suffix: list[str]
        :param federation_expiration_timestamp: 联邦到期时间戳
        :type federation_expiration_timestamp: str
        :param policy_id: 策略管理id
        :type policy_id: str
        :param federation_version: 舰队启用联邦的版本
        :type federation_version: str
        :param connect_gateway_endpoints: 集群联邦连接网关节点列表，仅当舰队开启集群联邦时有值
        :type connect_gateway_endpoints: list[:class:`huaweicloudsdkucs.v1.ConnectEndpoint`]
        """
        
        

        self._rule_namespaces = None
        self._federation_id = None
        self._description = None
        self._dns_suffix = None
        self._federation_expiration_timestamp = None
        self._policy_id = None
        self._federation_version = None
        self._connect_gateway_endpoints = None
        self.discriminator = None

        if rule_namespaces is not None:
            self.rule_namespaces = rule_namespaces
        if federation_id is not None:
            self.federation_id = federation_id
        if description is not None:
            self.description = description
        if dns_suffix is not None:
            self.dns_suffix = dns_suffix
        if federation_expiration_timestamp is not None:
            self.federation_expiration_timestamp = federation_expiration_timestamp
        if policy_id is not None:
            self.policy_id = policy_id
        if federation_version is not None:
            self.federation_version = federation_version
        if connect_gateway_endpoints is not None:
            self.connect_gateway_endpoints = connect_gateway_endpoints

    @property
    def rule_namespaces(self):
        r"""Gets the rule_namespaces of this ClusterGroupSpec.

        权限策略关联的命名空间列表

        :return: The rule_namespaces of this ClusterGroupSpec.
        :rtype: list[str]
        """
        return self._rule_namespaces

    @rule_namespaces.setter
    def rule_namespaces(self, rule_namespaces):
        r"""Sets the rule_namespaces of this ClusterGroupSpec.

        权限策略关联的命名空间列表

        :param rule_namespaces: The rule_namespaces of this ClusterGroupSpec.
        :type rule_namespaces: list[str]
        """
        self._rule_namespaces = rule_namespaces

    @property
    def federation_id(self):
        r"""Gets the federation_id of this ClusterGroupSpec.

        舰队启用联邦ID

        :return: The federation_id of this ClusterGroupSpec.
        :rtype: str
        """
        return self._federation_id

    @federation_id.setter
    def federation_id(self, federation_id):
        r"""Sets the federation_id of this ClusterGroupSpec.

        舰队启用联邦ID

        :param federation_id: The federation_id of this ClusterGroupSpec.
        :type federation_id: str
        """
        self._federation_id = federation_id

    @property
    def description(self):
        r"""Gets the description of this ClusterGroupSpec.

        描述信息

        :return: The description of this ClusterGroupSpec.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ClusterGroupSpec.

        描述信息

        :param description: The description of this ClusterGroupSpec.
        :type description: str
        """
        self._description = description

    @property
    def dns_suffix(self):
        r"""Gets the dns_suffix of this ClusterGroupSpec.

        舰队对应联邦的DNS后缀，开启联邦后可见

        :return: The dns_suffix of this ClusterGroupSpec.
        :rtype: list[str]
        """
        return self._dns_suffix

    @dns_suffix.setter
    def dns_suffix(self, dns_suffix):
        r"""Sets the dns_suffix of this ClusterGroupSpec.

        舰队对应联邦的DNS后缀，开启联邦后可见

        :param dns_suffix: The dns_suffix of this ClusterGroupSpec.
        :type dns_suffix: list[str]
        """
        self._dns_suffix = dns_suffix

    @property
    def federation_expiration_timestamp(self):
        r"""Gets the federation_expiration_timestamp of this ClusterGroupSpec.

        联邦到期时间戳

        :return: The federation_expiration_timestamp of this ClusterGroupSpec.
        :rtype: str
        """
        return self._federation_expiration_timestamp

    @federation_expiration_timestamp.setter
    def federation_expiration_timestamp(self, federation_expiration_timestamp):
        r"""Sets the federation_expiration_timestamp of this ClusterGroupSpec.

        联邦到期时间戳

        :param federation_expiration_timestamp: The federation_expiration_timestamp of this ClusterGroupSpec.
        :type federation_expiration_timestamp: str
        """
        self._federation_expiration_timestamp = federation_expiration_timestamp

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ClusterGroupSpec.

        策略管理id

        :return: The policy_id of this ClusterGroupSpec.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ClusterGroupSpec.

        策略管理id

        :param policy_id: The policy_id of this ClusterGroupSpec.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def federation_version(self):
        r"""Gets the federation_version of this ClusterGroupSpec.

        舰队启用联邦的版本

        :return: The federation_version of this ClusterGroupSpec.
        :rtype: str
        """
        return self._federation_version

    @federation_version.setter
    def federation_version(self, federation_version):
        r"""Sets the federation_version of this ClusterGroupSpec.

        舰队启用联邦的版本

        :param federation_version: The federation_version of this ClusterGroupSpec.
        :type federation_version: str
        """
        self._federation_version = federation_version

    @property
    def connect_gateway_endpoints(self):
        r"""Gets the connect_gateway_endpoints of this ClusterGroupSpec.

        集群联邦连接网关节点列表，仅当舰队开启集群联邦时有值

        :return: The connect_gateway_endpoints of this ClusterGroupSpec.
        :rtype: list[:class:`huaweicloudsdkucs.v1.ConnectEndpoint`]
        """
        return self._connect_gateway_endpoints

    @connect_gateway_endpoints.setter
    def connect_gateway_endpoints(self, connect_gateway_endpoints):
        r"""Sets the connect_gateway_endpoints of this ClusterGroupSpec.

        集群联邦连接网关节点列表，仅当舰队开启集群联邦时有值

        :param connect_gateway_endpoints: The connect_gateway_endpoints of this ClusterGroupSpec.
        :type connect_gateway_endpoints: list[:class:`huaweicloudsdkucs.v1.ConnectEndpoint`]
        """
        self._connect_gateway_endpoints = connect_gateway_endpoints

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ClusterGroupSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
