# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SourcesConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'origin_type': 'str',
        'origin_addr': 'str',
        'priority': 'int',
        'weight': 'int',
        'obs_web_hosting_status': 'str',
        'http_port': 'int',
        'https_port': 'int',
        'host_name': 'str',
        'obs_bucket_type': 'str',
        'bucket_access_key': 'str',
        'bucket_secret_key': 'str',
        'bucket_region': 'str',
        'bucket_name': 'str'
    }

    attribute_map = {
        'origin_type': 'origin_type',
        'origin_addr': 'origin_addr',
        'priority': 'priority',
        'weight': 'weight',
        'obs_web_hosting_status': 'obs_web_hosting_status',
        'http_port': 'http_port',
        'https_port': 'https_port',
        'host_name': 'host_name',
        'obs_bucket_type': 'obs_bucket_type',
        'bucket_access_key': 'bucket_access_key',
        'bucket_secret_key': 'bucket_secret_key',
        'bucket_region': 'bucket_region',
        'bucket_name': 'bucket_name'
    }

    def __init__(self, origin_type=None, origin_addr=None, priority=None, weight=None, obs_web_hosting_status=None, http_port=None, https_port=None, host_name=None, obs_bucket_type=None, bucket_access_key=None, bucket_secret_key=None, bucket_region=None, bucket_name=None):
        r"""SourcesConfig

        The model defined in huaweicloud sdk

        :param origin_type: **参数解释：** 源站类型 **约束限制：** 不涉及 **取值范围：** - ipaddr: 源站IP - domain: 源站域名 - obs_bucket: OBS桶域名 - third_bucket: 第三方桶，使用该源站类型需要提交工单申请  **默认取值：** 不涉及
        :type origin_type: str
        :param origin_addr: **参数解释：** 源站IP或者域名 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type origin_addr: str
        :param priority: **参数解释：** 源站优先级 **约束限制：** 不涉及 **取值范围：** 1-1000 **默认取值：** 不涉及
        :type priority: int
        :param weight: **参数解释：** 权重 **约束限制：** 不涉及 **取值范围：** 1-100 **默认取值：** 不涉及
        :type weight: int
        :param obs_web_hosting_status: **参数解释：** 是否开启静态网站托管功能，如果您的源站是OBS桶域名且配置了静态网站托管，开启该功能后，客户端即可访问静态网站托管页面 &gt; 开启该功能后将自动给桶源站地址加上website字段，如果地址中已有website字段，该参数不生效 **约束限制：** - 源站类型为obs_bucket时需要传该参数 - 只有当源站OBS桶已经开启静态网站托管时，才可开启，否则将导致业务异常  **取值范围：** - on: 开启 - off: 关闭  **默认取值：** 不涉及
        :type obs_web_hosting_status: str
        :param http_port: **参数解释：** HTTP端口 **约束限制：** 不涉及 **取值范围：** 1-65535 **默认取值：** 80
        :type http_port: int
        :param https_port: **参数解释：** HTTPS端口 **约束限制：** 不涉及 **取值范围：** 1-65535 **默认取值：** 443
        :type https_port: int
        :param host_name: **参数解释：** 回源HOST **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 加速域名
        :type host_name: str
        :param obs_bucket_type: **参数解释：** OBS回源鉴权开关，适用于OBS桶源站场景，如果桶需要带鉴权访问，则需要打开OBS回源鉴权开关。如此，CDN节点回源时会携带鉴权信息，鉴权信息与OBS桶不匹配时，回源失败，避免非授权的请求盗刷流量 **约束限制：** 源站类型是“OBS桶域名”时需要传该参数 **取值范围：** - private: 开启回源鉴权开关 - public: 关闭回源鉴权开关  **默认取值：** public: 关闭回源鉴权开关
        :type obs_bucket_type: str
        :param bucket_access_key: **参数解释：** 第三方对象存储访问密钥ID，即AK **约束限制：** 源站类型为第三方桶时必填 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type bucket_access_key: str
        :param bucket_secret_key: **参数解释：** 第三方对象存储私密访问密钥，即SK **约束限制：** 源站类型为第三方桶时必填 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type bucket_secret_key: str
        :param bucket_region: **参数解释：** 第三方对象存储区域 **约束限制：** 源站类型为第三方桶时必填 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type bucket_region: str
        :param bucket_name: **参数解释：** 第三方对象存储名称 **约束限制：** 源站类型为第三方桶时必填 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type bucket_name: str
        """
        
        

        self._origin_type = None
        self._origin_addr = None
        self._priority = None
        self._weight = None
        self._obs_web_hosting_status = None
        self._http_port = None
        self._https_port = None
        self._host_name = None
        self._obs_bucket_type = None
        self._bucket_access_key = None
        self._bucket_secret_key = None
        self._bucket_region = None
        self._bucket_name = None
        self.discriminator = None

        self.origin_type = origin_type
        self.origin_addr = origin_addr
        self.priority = priority
        if weight is not None:
            self.weight = weight
        if obs_web_hosting_status is not None:
            self.obs_web_hosting_status = obs_web_hosting_status
        if http_port is not None:
            self.http_port = http_port
        if https_port is not None:
            self.https_port = https_port
        if host_name is not None:
            self.host_name = host_name
        if obs_bucket_type is not None:
            self.obs_bucket_type = obs_bucket_type
        if bucket_access_key is not None:
            self.bucket_access_key = bucket_access_key
        if bucket_secret_key is not None:
            self.bucket_secret_key = bucket_secret_key
        if bucket_region is not None:
            self.bucket_region = bucket_region
        if bucket_name is not None:
            self.bucket_name = bucket_name

    @property
    def origin_type(self):
        r"""Gets the origin_type of this SourcesConfig.

        **参数解释：** 源站类型 **约束限制：** 不涉及 **取值范围：** - ipaddr: 源站IP - domain: 源站域名 - obs_bucket: OBS桶域名 - third_bucket: 第三方桶，使用该源站类型需要提交工单申请  **默认取值：** 不涉及

        :return: The origin_type of this SourcesConfig.
        :rtype: str
        """
        return self._origin_type

    @origin_type.setter
    def origin_type(self, origin_type):
        r"""Sets the origin_type of this SourcesConfig.

        **参数解释：** 源站类型 **约束限制：** 不涉及 **取值范围：** - ipaddr: 源站IP - domain: 源站域名 - obs_bucket: OBS桶域名 - third_bucket: 第三方桶，使用该源站类型需要提交工单申请  **默认取值：** 不涉及

        :param origin_type: The origin_type of this SourcesConfig.
        :type origin_type: str
        """
        self._origin_type = origin_type

    @property
    def origin_addr(self):
        r"""Gets the origin_addr of this SourcesConfig.

        **参数解释：** 源站IP或者域名 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The origin_addr of this SourcesConfig.
        :rtype: str
        """
        return self._origin_addr

    @origin_addr.setter
    def origin_addr(self, origin_addr):
        r"""Sets the origin_addr of this SourcesConfig.

        **参数解释：** 源站IP或者域名 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param origin_addr: The origin_addr of this SourcesConfig.
        :type origin_addr: str
        """
        self._origin_addr = origin_addr

    @property
    def priority(self):
        r"""Gets the priority of this SourcesConfig.

        **参数解释：** 源站优先级 **约束限制：** 不涉及 **取值范围：** 1-1000 **默认取值：** 不涉及

        :return: The priority of this SourcesConfig.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this SourcesConfig.

        **参数解释：** 源站优先级 **约束限制：** 不涉及 **取值范围：** 1-1000 **默认取值：** 不涉及

        :param priority: The priority of this SourcesConfig.
        :type priority: int
        """
        self._priority = priority

    @property
    def weight(self):
        r"""Gets the weight of this SourcesConfig.

        **参数解释：** 权重 **约束限制：** 不涉及 **取值范围：** 1-100 **默认取值：** 不涉及

        :return: The weight of this SourcesConfig.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        r"""Sets the weight of this SourcesConfig.

        **参数解释：** 权重 **约束限制：** 不涉及 **取值范围：** 1-100 **默认取值：** 不涉及

        :param weight: The weight of this SourcesConfig.
        :type weight: int
        """
        self._weight = weight

    @property
    def obs_web_hosting_status(self):
        r"""Gets the obs_web_hosting_status of this SourcesConfig.

        **参数解释：** 是否开启静态网站托管功能，如果您的源站是OBS桶域名且配置了静态网站托管，开启该功能后，客户端即可访问静态网站托管页面 > 开启该功能后将自动给桶源站地址加上website字段，如果地址中已有website字段，该参数不生效 **约束限制：** - 源站类型为obs_bucket时需要传该参数 - 只有当源站OBS桶已经开启静态网站托管时，才可开启，否则将导致业务异常  **取值范围：** - on: 开启 - off: 关闭  **默认取值：** 不涉及

        :return: The obs_web_hosting_status of this SourcesConfig.
        :rtype: str
        """
        return self._obs_web_hosting_status

    @obs_web_hosting_status.setter
    def obs_web_hosting_status(self, obs_web_hosting_status):
        r"""Sets the obs_web_hosting_status of this SourcesConfig.

        **参数解释：** 是否开启静态网站托管功能，如果您的源站是OBS桶域名且配置了静态网站托管，开启该功能后，客户端即可访问静态网站托管页面 > 开启该功能后将自动给桶源站地址加上website字段，如果地址中已有website字段，该参数不生效 **约束限制：** - 源站类型为obs_bucket时需要传该参数 - 只有当源站OBS桶已经开启静态网站托管时，才可开启，否则将导致业务异常  **取值范围：** - on: 开启 - off: 关闭  **默认取值：** 不涉及

        :param obs_web_hosting_status: The obs_web_hosting_status of this SourcesConfig.
        :type obs_web_hosting_status: str
        """
        self._obs_web_hosting_status = obs_web_hosting_status

    @property
    def http_port(self):
        r"""Gets the http_port of this SourcesConfig.

        **参数解释：** HTTP端口 **约束限制：** 不涉及 **取值范围：** 1-65535 **默认取值：** 80

        :return: The http_port of this SourcesConfig.
        :rtype: int
        """
        return self._http_port

    @http_port.setter
    def http_port(self, http_port):
        r"""Sets the http_port of this SourcesConfig.

        **参数解释：** HTTP端口 **约束限制：** 不涉及 **取值范围：** 1-65535 **默认取值：** 80

        :param http_port: The http_port of this SourcesConfig.
        :type http_port: int
        """
        self._http_port = http_port

    @property
    def https_port(self):
        r"""Gets the https_port of this SourcesConfig.

        **参数解释：** HTTPS端口 **约束限制：** 不涉及 **取值范围：** 1-65535 **默认取值：** 443

        :return: The https_port of this SourcesConfig.
        :rtype: int
        """
        return self._https_port

    @https_port.setter
    def https_port(self, https_port):
        r"""Sets the https_port of this SourcesConfig.

        **参数解释：** HTTPS端口 **约束限制：** 不涉及 **取值范围：** 1-65535 **默认取值：** 443

        :param https_port: The https_port of this SourcesConfig.
        :type https_port: int
        """
        self._https_port = https_port

    @property
    def host_name(self):
        r"""Gets the host_name of this SourcesConfig.

        **参数解释：** 回源HOST **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 加速域名

        :return: The host_name of this SourcesConfig.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this SourcesConfig.

        **参数解释：** 回源HOST **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 加速域名

        :param host_name: The host_name of this SourcesConfig.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def obs_bucket_type(self):
        r"""Gets the obs_bucket_type of this SourcesConfig.

        **参数解释：** OBS回源鉴权开关，适用于OBS桶源站场景，如果桶需要带鉴权访问，则需要打开OBS回源鉴权开关。如此，CDN节点回源时会携带鉴权信息，鉴权信息与OBS桶不匹配时，回源失败，避免非授权的请求盗刷流量 **约束限制：** 源站类型是“OBS桶域名”时需要传该参数 **取值范围：** - private: 开启回源鉴权开关 - public: 关闭回源鉴权开关  **默认取值：** public: 关闭回源鉴权开关

        :return: The obs_bucket_type of this SourcesConfig.
        :rtype: str
        """
        return self._obs_bucket_type

    @obs_bucket_type.setter
    def obs_bucket_type(self, obs_bucket_type):
        r"""Sets the obs_bucket_type of this SourcesConfig.

        **参数解释：** OBS回源鉴权开关，适用于OBS桶源站场景，如果桶需要带鉴权访问，则需要打开OBS回源鉴权开关。如此，CDN节点回源时会携带鉴权信息，鉴权信息与OBS桶不匹配时，回源失败，避免非授权的请求盗刷流量 **约束限制：** 源站类型是“OBS桶域名”时需要传该参数 **取值范围：** - private: 开启回源鉴权开关 - public: 关闭回源鉴权开关  **默认取值：** public: 关闭回源鉴权开关

        :param obs_bucket_type: The obs_bucket_type of this SourcesConfig.
        :type obs_bucket_type: str
        """
        self._obs_bucket_type = obs_bucket_type

    @property
    def bucket_access_key(self):
        r"""Gets the bucket_access_key of this SourcesConfig.

        **参数解释：** 第三方对象存储访问密钥ID，即AK **约束限制：** 源站类型为第三方桶时必填 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The bucket_access_key of this SourcesConfig.
        :rtype: str
        """
        return self._bucket_access_key

    @bucket_access_key.setter
    def bucket_access_key(self, bucket_access_key):
        r"""Sets the bucket_access_key of this SourcesConfig.

        **参数解释：** 第三方对象存储访问密钥ID，即AK **约束限制：** 源站类型为第三方桶时必填 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param bucket_access_key: The bucket_access_key of this SourcesConfig.
        :type bucket_access_key: str
        """
        self._bucket_access_key = bucket_access_key

    @property
    def bucket_secret_key(self):
        r"""Gets the bucket_secret_key of this SourcesConfig.

        **参数解释：** 第三方对象存储私密访问密钥，即SK **约束限制：** 源站类型为第三方桶时必填 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The bucket_secret_key of this SourcesConfig.
        :rtype: str
        """
        return self._bucket_secret_key

    @bucket_secret_key.setter
    def bucket_secret_key(self, bucket_secret_key):
        r"""Sets the bucket_secret_key of this SourcesConfig.

        **参数解释：** 第三方对象存储私密访问密钥，即SK **约束限制：** 源站类型为第三方桶时必填 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param bucket_secret_key: The bucket_secret_key of this SourcesConfig.
        :type bucket_secret_key: str
        """
        self._bucket_secret_key = bucket_secret_key

    @property
    def bucket_region(self):
        r"""Gets the bucket_region of this SourcesConfig.

        **参数解释：** 第三方对象存储区域 **约束限制：** 源站类型为第三方桶时必填 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The bucket_region of this SourcesConfig.
        :rtype: str
        """
        return self._bucket_region

    @bucket_region.setter
    def bucket_region(self, bucket_region):
        r"""Sets the bucket_region of this SourcesConfig.

        **参数解释：** 第三方对象存储区域 **约束限制：** 源站类型为第三方桶时必填 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param bucket_region: The bucket_region of this SourcesConfig.
        :type bucket_region: str
        """
        self._bucket_region = bucket_region

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this SourcesConfig.

        **参数解释：** 第三方对象存储名称 **约束限制：** 源站类型为第三方桶时必填 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The bucket_name of this SourcesConfig.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this SourcesConfig.

        **参数解释：** 第三方对象存储名称 **约束限制：** 源站类型为第三方桶时必填 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param bucket_name: The bucket_name of this SourcesConfig.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

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
        if not isinstance(other, SourcesConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
