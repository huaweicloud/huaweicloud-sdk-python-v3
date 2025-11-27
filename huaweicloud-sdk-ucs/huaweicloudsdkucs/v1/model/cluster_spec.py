# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sync_mode': 'str',
        'cluster_group_id': 'str',
        'manage_type': 'str',
        'rule_namespaces': 'list[RuleNamespace]',
        'api_endpoint': 'str',
        'secret_ref': 'LocalSecretReference',
        'insecure_skip_tls_verification': 'bool',
        'proxy_url': 'str',
        'provider': 'str',
        'type': 'str',
        'category': 'str',
        'enable_dist_mgt': 'bool',
        'region': 'str',
        'country': 'str',
        'city': 'str',
        'project_id': 'str',
        'project_name': 'str',
        'zone': 'str',
        'taints': 'list[Taint]',
        'is_downloaded_cert': 'bool',
        'policy_id': 'str',
        'operator_namespace': 'str',
        'connect_proxy_endpoints': 'list[ConnectEndpoint]'
    }

    attribute_map = {
        'sync_mode': 'syncMode',
        'cluster_group_id': 'clusterGroupID',
        'manage_type': 'manageType',
        'rule_namespaces': 'ruleNamespaces',
        'api_endpoint': 'apiEndpoint',
        'secret_ref': 'secretRef',
        'insecure_skip_tls_verification': 'insecureSkipTLSVerification',
        'proxy_url': 'proxyURL',
        'provider': 'provider',
        'type': 'type',
        'category': 'category',
        'enable_dist_mgt': 'enableDistMgt',
        'region': 'region',
        'country': 'country',
        'city': 'city',
        'project_id': 'projectID',
        'project_name': 'projectName',
        'zone': 'zone',
        'taints': 'taints',
        'is_downloaded_cert': 'IsDownloadedCert',
        'policy_id': 'policyId',
        'operator_namespace': 'operatorNamespace',
        'connect_proxy_endpoints': 'connectProxyEndpoints'
    }

    def __init__(self, sync_mode=None, cluster_group_id=None, manage_type=None, rule_namespaces=None, api_endpoint=None, secret_ref=None, insecure_skip_tls_verification=None, proxy_url=None, provider=None, type=None, category=None, enable_dist_mgt=None, region=None, country=None, city=None, project_id=None, project_name=None, zone=None, taints=None, is_downloaded_cert=None, policy_id=None, operator_namespace=None, connect_proxy_endpoints=None):
        r"""ClusterSpec

        The model defined in huaweicloud sdk

        :param sync_mode: 集群和karmada控制面之间的同步模式
        :type sync_mode: str
        :param cluster_group_id: 容器舰队id
        :type cluster_group_id: str
        :param manage_type: 集群类型，取值如下： - grouped：在舰队中纳管的集群 - discrete：未加入舰队的集群 
        :type manage_type: str
        :param rule_namespaces: 集群包含的RuleNamespace列表
        :type rule_namespaces: list[:class:`huaweicloudsdkucs.v1.RuleNamespace`]
        :param api_endpoint: apiserver地址
        :type api_endpoint: str
        :param secret_ref: 
        :type secret_ref: :class:`huaweicloudsdkucs.v1.LocalSecretReference`
        :param insecure_skip_tls_verification: 是否跳过https校验
        :type insecure_skip_tls_verification: bool
        :param proxy_url: 代理链接
        :type proxy_url: str
        :param provider: 提供商
        :type provider: str
        :param type: 类型
        :type type: str
        :param category: 类别
        :type category: str
        :param enable_dist_mgt: CCE Turbo集群是否支持管理边缘基础设施。
        :type enable_dist_mgt: bool
        :param region: 区域
        :type region: str
        :param country: 国家
        :type country: str
        :param city: 城市
        :type city: str
        :param project_id: 项目id
        :type project_id: str
        :param project_name: 项目名
        :type project_name: str
        :param zone: 地区
        :type zone: str
        :param taints: 污点
        :type taints: list[:class:`huaweicloudsdkucs.v1.Taint`]
        :param is_downloaded_cert: 是否已经下载过证书
        :type is_downloaded_cert: bool
        :param policy_id: 策略管理id
        :type policy_id: str
        :param operator_namespace: 集群所属domainID
        :type operator_namespace: str
        :param connect_proxy_endpoints: 连接代理服务器的终端节点服务ID列表，仅非华为云集群返回该字段
        :type connect_proxy_endpoints: list[:class:`huaweicloudsdkucs.v1.ConnectEndpoint`]
        """
        
        

        self._sync_mode = None
        self._cluster_group_id = None
        self._manage_type = None
        self._rule_namespaces = None
        self._api_endpoint = None
        self._secret_ref = None
        self._insecure_skip_tls_verification = None
        self._proxy_url = None
        self._provider = None
        self._type = None
        self._category = None
        self._enable_dist_mgt = None
        self._region = None
        self._country = None
        self._city = None
        self._project_id = None
        self._project_name = None
        self._zone = None
        self._taints = None
        self._is_downloaded_cert = None
        self._policy_id = None
        self._operator_namespace = None
        self._connect_proxy_endpoints = None
        self.discriminator = None

        if sync_mode is not None:
            self.sync_mode = sync_mode
        if cluster_group_id is not None:
            self.cluster_group_id = cluster_group_id
        if manage_type is not None:
            self.manage_type = manage_type
        if rule_namespaces is not None:
            self.rule_namespaces = rule_namespaces
        if api_endpoint is not None:
            self.api_endpoint = api_endpoint
        if secret_ref is not None:
            self.secret_ref = secret_ref
        if insecure_skip_tls_verification is not None:
            self.insecure_skip_tls_verification = insecure_skip_tls_verification
        if proxy_url is not None:
            self.proxy_url = proxy_url
        if provider is not None:
            self.provider = provider
        if type is not None:
            self.type = type
        if category is not None:
            self.category = category
        if enable_dist_mgt is not None:
            self.enable_dist_mgt = enable_dist_mgt
        if region is not None:
            self.region = region
        if country is not None:
            self.country = country
        if city is not None:
            self.city = city
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if zone is not None:
            self.zone = zone
        if taints is not None:
            self.taints = taints
        if is_downloaded_cert is not None:
            self.is_downloaded_cert = is_downloaded_cert
        if policy_id is not None:
            self.policy_id = policy_id
        if operator_namespace is not None:
            self.operator_namespace = operator_namespace
        if connect_proxy_endpoints is not None:
            self.connect_proxy_endpoints = connect_proxy_endpoints

    @property
    def sync_mode(self):
        r"""Gets the sync_mode of this ClusterSpec.

        集群和karmada控制面之间的同步模式

        :return: The sync_mode of this ClusterSpec.
        :rtype: str
        """
        return self._sync_mode

    @sync_mode.setter
    def sync_mode(self, sync_mode):
        r"""Sets the sync_mode of this ClusterSpec.

        集群和karmada控制面之间的同步模式

        :param sync_mode: The sync_mode of this ClusterSpec.
        :type sync_mode: str
        """
        self._sync_mode = sync_mode

    @property
    def cluster_group_id(self):
        r"""Gets the cluster_group_id of this ClusterSpec.

        容器舰队id

        :return: The cluster_group_id of this ClusterSpec.
        :rtype: str
        """
        return self._cluster_group_id

    @cluster_group_id.setter
    def cluster_group_id(self, cluster_group_id):
        r"""Sets the cluster_group_id of this ClusterSpec.

        容器舰队id

        :param cluster_group_id: The cluster_group_id of this ClusterSpec.
        :type cluster_group_id: str
        """
        self._cluster_group_id = cluster_group_id

    @property
    def manage_type(self):
        r"""Gets the manage_type of this ClusterSpec.

        集群类型，取值如下： - grouped：在舰队中纳管的集群 - discrete：未加入舰队的集群 

        :return: The manage_type of this ClusterSpec.
        :rtype: str
        """
        return self._manage_type

    @manage_type.setter
    def manage_type(self, manage_type):
        r"""Sets the manage_type of this ClusterSpec.

        集群类型，取值如下： - grouped：在舰队中纳管的集群 - discrete：未加入舰队的集群 

        :param manage_type: The manage_type of this ClusterSpec.
        :type manage_type: str
        """
        self._manage_type = manage_type

    @property
    def rule_namespaces(self):
        r"""Gets the rule_namespaces of this ClusterSpec.

        集群包含的RuleNamespace列表

        :return: The rule_namespaces of this ClusterSpec.
        :rtype: list[:class:`huaweicloudsdkucs.v1.RuleNamespace`]
        """
        return self._rule_namespaces

    @rule_namespaces.setter
    def rule_namespaces(self, rule_namespaces):
        r"""Sets the rule_namespaces of this ClusterSpec.

        集群包含的RuleNamespace列表

        :param rule_namespaces: The rule_namespaces of this ClusterSpec.
        :type rule_namespaces: list[:class:`huaweicloudsdkucs.v1.RuleNamespace`]
        """
        self._rule_namespaces = rule_namespaces

    @property
    def api_endpoint(self):
        r"""Gets the api_endpoint of this ClusterSpec.

        apiserver地址

        :return: The api_endpoint of this ClusterSpec.
        :rtype: str
        """
        return self._api_endpoint

    @api_endpoint.setter
    def api_endpoint(self, api_endpoint):
        r"""Sets the api_endpoint of this ClusterSpec.

        apiserver地址

        :param api_endpoint: The api_endpoint of this ClusterSpec.
        :type api_endpoint: str
        """
        self._api_endpoint = api_endpoint

    @property
    def secret_ref(self):
        r"""Gets the secret_ref of this ClusterSpec.

        :return: The secret_ref of this ClusterSpec.
        :rtype: :class:`huaweicloudsdkucs.v1.LocalSecretReference`
        """
        return self._secret_ref

    @secret_ref.setter
    def secret_ref(self, secret_ref):
        r"""Sets the secret_ref of this ClusterSpec.

        :param secret_ref: The secret_ref of this ClusterSpec.
        :type secret_ref: :class:`huaweicloudsdkucs.v1.LocalSecretReference`
        """
        self._secret_ref = secret_ref

    @property
    def insecure_skip_tls_verification(self):
        r"""Gets the insecure_skip_tls_verification of this ClusterSpec.

        是否跳过https校验

        :return: The insecure_skip_tls_verification of this ClusterSpec.
        :rtype: bool
        """
        return self._insecure_skip_tls_verification

    @insecure_skip_tls_verification.setter
    def insecure_skip_tls_verification(self, insecure_skip_tls_verification):
        r"""Sets the insecure_skip_tls_verification of this ClusterSpec.

        是否跳过https校验

        :param insecure_skip_tls_verification: The insecure_skip_tls_verification of this ClusterSpec.
        :type insecure_skip_tls_verification: bool
        """
        self._insecure_skip_tls_verification = insecure_skip_tls_verification

    @property
    def proxy_url(self):
        r"""Gets the proxy_url of this ClusterSpec.

        代理链接

        :return: The proxy_url of this ClusterSpec.
        :rtype: str
        """
        return self._proxy_url

    @proxy_url.setter
    def proxy_url(self, proxy_url):
        r"""Sets the proxy_url of this ClusterSpec.

        代理链接

        :param proxy_url: The proxy_url of this ClusterSpec.
        :type proxy_url: str
        """
        self._proxy_url = proxy_url

    @property
    def provider(self):
        r"""Gets the provider of this ClusterSpec.

        提供商

        :return: The provider of this ClusterSpec.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        r"""Sets the provider of this ClusterSpec.

        提供商

        :param provider: The provider of this ClusterSpec.
        :type provider: str
        """
        self._provider = provider

    @property
    def type(self):
        r"""Gets the type of this ClusterSpec.

        类型

        :return: The type of this ClusterSpec.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ClusterSpec.

        类型

        :param type: The type of this ClusterSpec.
        :type type: str
        """
        self._type = type

    @property
    def category(self):
        r"""Gets the category of this ClusterSpec.

        类别

        :return: The category of this ClusterSpec.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ClusterSpec.

        类别

        :param category: The category of this ClusterSpec.
        :type category: str
        """
        self._category = category

    @property
    def enable_dist_mgt(self):
        r"""Gets the enable_dist_mgt of this ClusterSpec.

        CCE Turbo集群是否支持管理边缘基础设施。

        :return: The enable_dist_mgt of this ClusterSpec.
        :rtype: bool
        """
        return self._enable_dist_mgt

    @enable_dist_mgt.setter
    def enable_dist_mgt(self, enable_dist_mgt):
        r"""Sets the enable_dist_mgt of this ClusterSpec.

        CCE Turbo集群是否支持管理边缘基础设施。

        :param enable_dist_mgt: The enable_dist_mgt of this ClusterSpec.
        :type enable_dist_mgt: bool
        """
        self._enable_dist_mgt = enable_dist_mgt

    @property
    def region(self):
        r"""Gets the region of this ClusterSpec.

        区域

        :return: The region of this ClusterSpec.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ClusterSpec.

        区域

        :param region: The region of this ClusterSpec.
        :type region: str
        """
        self._region = region

    @property
    def country(self):
        r"""Gets the country of this ClusterSpec.

        国家

        :return: The country of this ClusterSpec.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        r"""Sets the country of this ClusterSpec.

        国家

        :param country: The country of this ClusterSpec.
        :type country: str
        """
        self._country = country

    @property
    def city(self):
        r"""Gets the city of this ClusterSpec.

        城市

        :return: The city of this ClusterSpec.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        r"""Sets the city of this ClusterSpec.

        城市

        :param city: The city of this ClusterSpec.
        :type city: str
        """
        self._city = city

    @property
    def project_id(self):
        r"""Gets the project_id of this ClusterSpec.

        项目id

        :return: The project_id of this ClusterSpec.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ClusterSpec.

        项目id

        :param project_id: The project_id of this ClusterSpec.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        r"""Gets the project_name of this ClusterSpec.

        项目名

        :return: The project_name of this ClusterSpec.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this ClusterSpec.

        项目名

        :param project_name: The project_name of this ClusterSpec.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def zone(self):
        r"""Gets the zone of this ClusterSpec.

        地区

        :return: The zone of this ClusterSpec.
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        r"""Sets the zone of this ClusterSpec.

        地区

        :param zone: The zone of this ClusterSpec.
        :type zone: str
        """
        self._zone = zone

    @property
    def taints(self):
        r"""Gets the taints of this ClusterSpec.

        污点

        :return: The taints of this ClusterSpec.
        :rtype: list[:class:`huaweicloudsdkucs.v1.Taint`]
        """
        return self._taints

    @taints.setter
    def taints(self, taints):
        r"""Sets the taints of this ClusterSpec.

        污点

        :param taints: The taints of this ClusterSpec.
        :type taints: list[:class:`huaweicloudsdkucs.v1.Taint`]
        """
        self._taints = taints

    @property
    def is_downloaded_cert(self):
        r"""Gets the is_downloaded_cert of this ClusterSpec.

        是否已经下载过证书

        :return: The is_downloaded_cert of this ClusterSpec.
        :rtype: bool
        """
        return self._is_downloaded_cert

    @is_downloaded_cert.setter
    def is_downloaded_cert(self, is_downloaded_cert):
        r"""Sets the is_downloaded_cert of this ClusterSpec.

        是否已经下载过证书

        :param is_downloaded_cert: The is_downloaded_cert of this ClusterSpec.
        :type is_downloaded_cert: bool
        """
        self._is_downloaded_cert = is_downloaded_cert

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ClusterSpec.

        策略管理id

        :return: The policy_id of this ClusterSpec.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ClusterSpec.

        策略管理id

        :param policy_id: The policy_id of this ClusterSpec.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def operator_namespace(self):
        r"""Gets the operator_namespace of this ClusterSpec.

        集群所属domainID

        :return: The operator_namespace of this ClusterSpec.
        :rtype: str
        """
        return self._operator_namespace

    @operator_namespace.setter
    def operator_namespace(self, operator_namespace):
        r"""Sets the operator_namespace of this ClusterSpec.

        集群所属domainID

        :param operator_namespace: The operator_namespace of this ClusterSpec.
        :type operator_namespace: str
        """
        self._operator_namespace = operator_namespace

    @property
    def connect_proxy_endpoints(self):
        r"""Gets the connect_proxy_endpoints of this ClusterSpec.

        连接代理服务器的终端节点服务ID列表，仅非华为云集群返回该字段

        :return: The connect_proxy_endpoints of this ClusterSpec.
        :rtype: list[:class:`huaweicloudsdkucs.v1.ConnectEndpoint`]
        """
        return self._connect_proxy_endpoints

    @connect_proxy_endpoints.setter
    def connect_proxy_endpoints(self, connect_proxy_endpoints):
        r"""Sets the connect_proxy_endpoints of this ClusterSpec.

        连接代理服务器的终端节点服务ID列表，仅非华为云集群返回该字段

        :param connect_proxy_endpoints: The connect_proxy_endpoints of this ClusterSpec.
        :type connect_proxy_endpoints: list[:class:`huaweicloudsdkucs.v1.ConnectEndpoint`]
        """
        self._connect_proxy_endpoints = connect_proxy_endpoints

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
        if not isinstance(other, ClusterSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
