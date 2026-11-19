# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateKeyStoreRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'keystore_alias': 'str',
        'hsm_cluster_id': 'str',
        'hsm_ca_cert': 'str',
        'cluster_id': 'str',
        'keystore_type': 'str',
        'proxy_uri_endpoint': 'str',
        'proxy_uri_path': 'str',
        'proxy_access_key_id': 'str',
        'proxy_secret_access_key': 'str',
        'proxy_vpc_endpoint_service_name': 'str',
        'proxy_vpc_endpoint_service_owner': 'str'
    }

    attribute_map = {
        'keystore_alias': 'keystore_alias',
        'hsm_cluster_id': 'hsm_cluster_id',
        'hsm_ca_cert': 'hsm_ca_cert',
        'cluster_id': 'cluster_id',
        'keystore_type': 'keystore_type',
        'proxy_uri_endpoint': 'proxy_uri_endpoint',
        'proxy_uri_path': 'proxy_uri_path',
        'proxy_access_key_id': 'proxy_access_key_id',
        'proxy_secret_access_key': 'proxy_secret_access_key',
        'proxy_vpc_endpoint_service_name': 'proxy_vpc_endpoint_service_name',
        'proxy_vpc_endpoint_service_owner': 'proxy_vpc_endpoint_service_owner'
    }

    def __init__(self, keystore_alias=None, hsm_cluster_id=None, hsm_ca_cert=None, cluster_id=None, keystore_type=None, proxy_uri_endpoint=None, proxy_uri_path=None, proxy_access_key_id=None, proxy_secret_access_key=None, proxy_vpc_endpoint_service_name=None, proxy_vpc_endpoint_service_owner=None):
        r"""CreateKeyStoreRequestBody

        The model defined in huaweicloud sdk

        :param keystore_alias: 专属密钥库别名，取值范围为1到255个字符，满足正则匹配“^[a-zA-Z0-9:/_-]{1,255}$”，且不与已有的专属密钥库别名重名。
        :type keystore_alias: str
        :param hsm_cluster_id: DHSM集群Id，要求集群当前未创建专属密钥库。
        :type hsm_cluster_id: str
        :param hsm_ca_cert: DHSM集群的CA证书
        :type hsm_ca_cert: str
        :param cluster_id: 集群ID。当类型为DHSM时，cluster_id为hsm_cluster_id。当类型为CDMS时，为cdms_cluster_id
        :type cluster_id: str
        :param keystore_type: 专属密钥库集群类型。DHSM表示专属加密服务集群，CDMS表示密码卡集群,DEFAULT表示KMS原有集群
        :type keystore_type: str
        :param proxy_uri_endpoint: **参数解释：** 仅XKS类型的密钥库支持；可选，表示Xks-Proxy的域名信息 **约束限制：** ^https://[^\\s]+ **取值范围：** 不涉及 **默认取值：** 不涉及
        :type proxy_uri_endpoint: str
        :param proxy_uri_path: **参数解释：** 仅XKS类型的密钥库支持；必选，Xks-Proxy的路径前缀 **约束限制：** ^/(?:[a-zA-Z0-9/_-]{0,127})$ **取值范围：** 不涉及 **默认取值：** 不涉及
        :type proxy_uri_path: str
        :param proxy_access_key_id: **参数解释：** 仅XKS类型的密钥库支持；必选，访问XKS-Proxy的凭据ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type proxy_access_key_id: str
        :param proxy_secret_access_key: **参数解释：** 仅XKS类型的密钥库支持；必选，访问XKS-Proxy的凭据Key **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type proxy_secret_access_key: str
        :param proxy_vpc_endpoint_service_name: **参数解释：** 仅XKS类型的密钥库支持；必选，Xks-Proxy的终端节点服务名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type proxy_vpc_endpoint_service_name: str
        :param proxy_vpc_endpoint_service_owner: **参数解释：** 仅XKS类型的密钥库支持；必选，终端节点服务所属账号 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type proxy_vpc_endpoint_service_owner: str
        """
        
        

        self._keystore_alias = None
        self._hsm_cluster_id = None
        self._hsm_ca_cert = None
        self._cluster_id = None
        self._keystore_type = None
        self._proxy_uri_endpoint = None
        self._proxy_uri_path = None
        self._proxy_access_key_id = None
        self._proxy_secret_access_key = None
        self._proxy_vpc_endpoint_service_name = None
        self._proxy_vpc_endpoint_service_owner = None
        self.discriminator = None

        self.keystore_alias = keystore_alias
        if hsm_cluster_id is not None:
            self.hsm_cluster_id = hsm_cluster_id
        if hsm_ca_cert is not None:
            self.hsm_ca_cert = hsm_ca_cert
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if keystore_type is not None:
            self.keystore_type = keystore_type
        if proxy_uri_endpoint is not None:
            self.proxy_uri_endpoint = proxy_uri_endpoint
        if proxy_uri_path is not None:
            self.proxy_uri_path = proxy_uri_path
        if proxy_access_key_id is not None:
            self.proxy_access_key_id = proxy_access_key_id
        if proxy_secret_access_key is not None:
            self.proxy_secret_access_key = proxy_secret_access_key
        if proxy_vpc_endpoint_service_name is not None:
            self.proxy_vpc_endpoint_service_name = proxy_vpc_endpoint_service_name
        if proxy_vpc_endpoint_service_owner is not None:
            self.proxy_vpc_endpoint_service_owner = proxy_vpc_endpoint_service_owner

    @property
    def keystore_alias(self):
        r"""Gets the keystore_alias of this CreateKeyStoreRequestBody.

        专属密钥库别名，取值范围为1到255个字符，满足正则匹配“^[a-zA-Z0-9:/_-]{1,255}$”，且不与已有的专属密钥库别名重名。

        :return: The keystore_alias of this CreateKeyStoreRequestBody.
        :rtype: str
        """
        return self._keystore_alias

    @keystore_alias.setter
    def keystore_alias(self, keystore_alias):
        r"""Sets the keystore_alias of this CreateKeyStoreRequestBody.

        专属密钥库别名，取值范围为1到255个字符，满足正则匹配“^[a-zA-Z0-9:/_-]{1,255}$”，且不与已有的专属密钥库别名重名。

        :param keystore_alias: The keystore_alias of this CreateKeyStoreRequestBody.
        :type keystore_alias: str
        """
        self._keystore_alias = keystore_alias

    @property
    def hsm_cluster_id(self):
        r"""Gets the hsm_cluster_id of this CreateKeyStoreRequestBody.

        DHSM集群Id，要求集群当前未创建专属密钥库。

        :return: The hsm_cluster_id of this CreateKeyStoreRequestBody.
        :rtype: str
        """
        return self._hsm_cluster_id

    @hsm_cluster_id.setter
    def hsm_cluster_id(self, hsm_cluster_id):
        r"""Sets the hsm_cluster_id of this CreateKeyStoreRequestBody.

        DHSM集群Id，要求集群当前未创建专属密钥库。

        :param hsm_cluster_id: The hsm_cluster_id of this CreateKeyStoreRequestBody.
        :type hsm_cluster_id: str
        """
        self._hsm_cluster_id = hsm_cluster_id

    @property
    def hsm_ca_cert(self):
        r"""Gets the hsm_ca_cert of this CreateKeyStoreRequestBody.

        DHSM集群的CA证书

        :return: The hsm_ca_cert of this CreateKeyStoreRequestBody.
        :rtype: str
        """
        return self._hsm_ca_cert

    @hsm_ca_cert.setter
    def hsm_ca_cert(self, hsm_ca_cert):
        r"""Sets the hsm_ca_cert of this CreateKeyStoreRequestBody.

        DHSM集群的CA证书

        :param hsm_ca_cert: The hsm_ca_cert of this CreateKeyStoreRequestBody.
        :type hsm_ca_cert: str
        """
        self._hsm_ca_cert = hsm_ca_cert

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this CreateKeyStoreRequestBody.

        集群ID。当类型为DHSM时，cluster_id为hsm_cluster_id。当类型为CDMS时，为cdms_cluster_id

        :return: The cluster_id of this CreateKeyStoreRequestBody.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this CreateKeyStoreRequestBody.

        集群ID。当类型为DHSM时，cluster_id为hsm_cluster_id。当类型为CDMS时，为cdms_cluster_id

        :param cluster_id: The cluster_id of this CreateKeyStoreRequestBody.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def keystore_type(self):
        r"""Gets the keystore_type of this CreateKeyStoreRequestBody.

        专属密钥库集群类型。DHSM表示专属加密服务集群，CDMS表示密码卡集群,DEFAULT表示KMS原有集群

        :return: The keystore_type of this CreateKeyStoreRequestBody.
        :rtype: str
        """
        return self._keystore_type

    @keystore_type.setter
    def keystore_type(self, keystore_type):
        r"""Sets the keystore_type of this CreateKeyStoreRequestBody.

        专属密钥库集群类型。DHSM表示专属加密服务集群，CDMS表示密码卡集群,DEFAULT表示KMS原有集群

        :param keystore_type: The keystore_type of this CreateKeyStoreRequestBody.
        :type keystore_type: str
        """
        self._keystore_type = keystore_type

    @property
    def proxy_uri_endpoint(self):
        r"""Gets the proxy_uri_endpoint of this CreateKeyStoreRequestBody.

        **参数解释：** 仅XKS类型的密钥库支持；可选，表示Xks-Proxy的域名信息 **约束限制：** ^https://[^\\s]+ **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The proxy_uri_endpoint of this CreateKeyStoreRequestBody.
        :rtype: str
        """
        return self._proxy_uri_endpoint

    @proxy_uri_endpoint.setter
    def proxy_uri_endpoint(self, proxy_uri_endpoint):
        r"""Sets the proxy_uri_endpoint of this CreateKeyStoreRequestBody.

        **参数解释：** 仅XKS类型的密钥库支持；可选，表示Xks-Proxy的域名信息 **约束限制：** ^https://[^\\s]+ **取值范围：** 不涉及 **默认取值：** 不涉及

        :param proxy_uri_endpoint: The proxy_uri_endpoint of this CreateKeyStoreRequestBody.
        :type proxy_uri_endpoint: str
        """
        self._proxy_uri_endpoint = proxy_uri_endpoint

    @property
    def proxy_uri_path(self):
        r"""Gets the proxy_uri_path of this CreateKeyStoreRequestBody.

        **参数解释：** 仅XKS类型的密钥库支持；必选，Xks-Proxy的路径前缀 **约束限制：** ^/(?:[a-zA-Z0-9/_-]{0,127})$ **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The proxy_uri_path of this CreateKeyStoreRequestBody.
        :rtype: str
        """
        return self._proxy_uri_path

    @proxy_uri_path.setter
    def proxy_uri_path(self, proxy_uri_path):
        r"""Sets the proxy_uri_path of this CreateKeyStoreRequestBody.

        **参数解释：** 仅XKS类型的密钥库支持；必选，Xks-Proxy的路径前缀 **约束限制：** ^/(?:[a-zA-Z0-9/_-]{0,127})$ **取值范围：** 不涉及 **默认取值：** 不涉及

        :param proxy_uri_path: The proxy_uri_path of this CreateKeyStoreRequestBody.
        :type proxy_uri_path: str
        """
        self._proxy_uri_path = proxy_uri_path

    @property
    def proxy_access_key_id(self):
        r"""Gets the proxy_access_key_id of this CreateKeyStoreRequestBody.

        **参数解释：** 仅XKS类型的密钥库支持；必选，访问XKS-Proxy的凭据ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The proxy_access_key_id of this CreateKeyStoreRequestBody.
        :rtype: str
        """
        return self._proxy_access_key_id

    @proxy_access_key_id.setter
    def proxy_access_key_id(self, proxy_access_key_id):
        r"""Sets the proxy_access_key_id of this CreateKeyStoreRequestBody.

        **参数解释：** 仅XKS类型的密钥库支持；必选，访问XKS-Proxy的凭据ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param proxy_access_key_id: The proxy_access_key_id of this CreateKeyStoreRequestBody.
        :type proxy_access_key_id: str
        """
        self._proxy_access_key_id = proxy_access_key_id

    @property
    def proxy_secret_access_key(self):
        r"""Gets the proxy_secret_access_key of this CreateKeyStoreRequestBody.

        **参数解释：** 仅XKS类型的密钥库支持；必选，访问XKS-Proxy的凭据Key **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The proxy_secret_access_key of this CreateKeyStoreRequestBody.
        :rtype: str
        """
        return self._proxy_secret_access_key

    @proxy_secret_access_key.setter
    def proxy_secret_access_key(self, proxy_secret_access_key):
        r"""Sets the proxy_secret_access_key of this CreateKeyStoreRequestBody.

        **参数解释：** 仅XKS类型的密钥库支持；必选，访问XKS-Proxy的凭据Key **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param proxy_secret_access_key: The proxy_secret_access_key of this CreateKeyStoreRequestBody.
        :type proxy_secret_access_key: str
        """
        self._proxy_secret_access_key = proxy_secret_access_key

    @property
    def proxy_vpc_endpoint_service_name(self):
        r"""Gets the proxy_vpc_endpoint_service_name of this CreateKeyStoreRequestBody.

        **参数解释：** 仅XKS类型的密钥库支持；必选，Xks-Proxy的终端节点服务名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The proxy_vpc_endpoint_service_name of this CreateKeyStoreRequestBody.
        :rtype: str
        """
        return self._proxy_vpc_endpoint_service_name

    @proxy_vpc_endpoint_service_name.setter
    def proxy_vpc_endpoint_service_name(self, proxy_vpc_endpoint_service_name):
        r"""Sets the proxy_vpc_endpoint_service_name of this CreateKeyStoreRequestBody.

        **参数解释：** 仅XKS类型的密钥库支持；必选，Xks-Proxy的终端节点服务名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param proxy_vpc_endpoint_service_name: The proxy_vpc_endpoint_service_name of this CreateKeyStoreRequestBody.
        :type proxy_vpc_endpoint_service_name: str
        """
        self._proxy_vpc_endpoint_service_name = proxy_vpc_endpoint_service_name

    @property
    def proxy_vpc_endpoint_service_owner(self):
        r"""Gets the proxy_vpc_endpoint_service_owner of this CreateKeyStoreRequestBody.

        **参数解释：** 仅XKS类型的密钥库支持；必选，终端节点服务所属账号 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The proxy_vpc_endpoint_service_owner of this CreateKeyStoreRequestBody.
        :rtype: str
        """
        return self._proxy_vpc_endpoint_service_owner

    @proxy_vpc_endpoint_service_owner.setter
    def proxy_vpc_endpoint_service_owner(self, proxy_vpc_endpoint_service_owner):
        r"""Sets the proxy_vpc_endpoint_service_owner of this CreateKeyStoreRequestBody.

        **参数解释：** 仅XKS类型的密钥库支持；必选，终端节点服务所属账号 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param proxy_vpc_endpoint_service_owner: The proxy_vpc_endpoint_service_owner of this CreateKeyStoreRequestBody.
        :type proxy_vpc_endpoint_service_owner: str
        """
        self._proxy_vpc_endpoint_service_owner = proxy_vpc_endpoint_service_owner

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
        if not isinstance(other, CreateKeyStoreRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
