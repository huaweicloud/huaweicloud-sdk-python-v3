# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SourceWithPort:

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
        'ip_or_domain': 'str',
        'origin_type': 'str',
        'obs_bucket_type': 'str',
        'active_standby': 'int',
        'enable_obs_web_hosting': 'int',
        'http_port': 'int',
        'https_port': 'int',
        'weight': 'int'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'ip_or_domain': 'ip_or_domain',
        'origin_type': 'origin_type',
        'obs_bucket_type': 'obs_bucket_type',
        'active_standby': 'active_standby',
        'enable_obs_web_hosting': 'enable_obs_web_hosting',
        'http_port': 'http_port',
        'https_port': 'https_port',
        'weight': 'weight'
    }

    def __init__(self, domain_id=None, ip_or_domain=None, origin_type=None, obs_bucket_type=None, active_standby=None, enable_obs_web_hosting=None, http_port=None, https_port=None, weight=None):
        r"""SourceWithPort

        The model defined in huaweicloud sdk

        :param domain_id: **参数解释：** 加速域名id。 **约束限制：** 不涉及 **取值范围：** 不涉及
        :type domain_id: str
        :param ip_or_domain: **参数解释：** 源站IP（非内网IP）或者域名。 **约束限制：** 不涉及 **取值范围：** 不涉及
        :type ip_or_domain: str
        :param origin_type: 源站类型，ipaddr：源站IP、 domain：源站域名、obs_bucket：OBS桶域名。
        :type origin_type: str
        :param obs_bucket_type: OBS桶类型。   - private: 私有桶（除桶ACL授权外的其他用户无桶的访问权限）。   - public: 公有桶（任何用户都可以对桶内对象进行读操作）。
        :type obs_bucket_type: str
        :param active_standby: 主备状态（1代表主源站；0代表备源站）。
        :type active_standby: int
        :param enable_obs_web_hosting: **参数解释：** 是否开启静态网站托管功能，如果您的源站是OBS桶域名且配置了静态网站托管，开启该功能后，客户端即可访问静态网站托管页面 &gt; 开启该功能后将自动给桶源站地址加上website字段，如果地址中已有website字段，该参数不生效 **约束限制：** - 源站类型为obs_bucket时需要传该参数 - 只有当源站OBS桶已经开启静态网站托管时，才可开启，否则将导致业务异常  **取值范围：** - 0: 关闭 - 1: 开启  **默认取值：** 0: 关闭
        :type enable_obs_web_hosting: int
        :param http_port: **参数解释：** HTTP端口，默认80 **约束限制：** 不涉及 **取值范围：** 不涉及
        :type http_port: int
        :param https_port: **参数解释：** HTTPS端口，默认443 **约束限制：** 不涉及 **取值范围：** 不涉及
        :type https_port: int
        :param weight: **参数解释：** 权重，值越大回源到该源站的次数越多。多个优先级相同的源站，由权重决定回源到各个源站的比例 **约束限制：** 不涉及 **取值范围：** 1-100 **默认取值：** 50
        :type weight: int
        """
        
        

        self._domain_id = None
        self._ip_or_domain = None
        self._origin_type = None
        self._obs_bucket_type = None
        self._active_standby = None
        self._enable_obs_web_hosting = None
        self._http_port = None
        self._https_port = None
        self._weight = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        self.ip_or_domain = ip_or_domain
        self.origin_type = origin_type
        if obs_bucket_type is not None:
            self.obs_bucket_type = obs_bucket_type
        self.active_standby = active_standby
        if enable_obs_web_hosting is not None:
            self.enable_obs_web_hosting = enable_obs_web_hosting
        if http_port is not None:
            self.http_port = http_port
        if https_port is not None:
            self.https_port = https_port
        if weight is not None:
            self.weight = weight

    @property
    def domain_id(self):
        r"""Gets the domain_id of this SourceWithPort.

        **参数解释：** 加速域名id。 **约束限制：** 不涉及 **取值范围：** 不涉及

        :return: The domain_id of this SourceWithPort.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this SourceWithPort.

        **参数解释：** 加速域名id。 **约束限制：** 不涉及 **取值范围：** 不涉及

        :param domain_id: The domain_id of this SourceWithPort.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def ip_or_domain(self):
        r"""Gets the ip_or_domain of this SourceWithPort.

        **参数解释：** 源站IP（非内网IP）或者域名。 **约束限制：** 不涉及 **取值范围：** 不涉及

        :return: The ip_or_domain of this SourceWithPort.
        :rtype: str
        """
        return self._ip_or_domain

    @ip_or_domain.setter
    def ip_or_domain(self, ip_or_domain):
        r"""Sets the ip_or_domain of this SourceWithPort.

        **参数解释：** 源站IP（非内网IP）或者域名。 **约束限制：** 不涉及 **取值范围：** 不涉及

        :param ip_or_domain: The ip_or_domain of this SourceWithPort.
        :type ip_or_domain: str
        """
        self._ip_or_domain = ip_or_domain

    @property
    def origin_type(self):
        r"""Gets the origin_type of this SourceWithPort.

        源站类型，ipaddr：源站IP、 domain：源站域名、obs_bucket：OBS桶域名。

        :return: The origin_type of this SourceWithPort.
        :rtype: str
        """
        return self._origin_type

    @origin_type.setter
    def origin_type(self, origin_type):
        r"""Sets the origin_type of this SourceWithPort.

        源站类型，ipaddr：源站IP、 domain：源站域名、obs_bucket：OBS桶域名。

        :param origin_type: The origin_type of this SourceWithPort.
        :type origin_type: str
        """
        self._origin_type = origin_type

    @property
    def obs_bucket_type(self):
        r"""Gets the obs_bucket_type of this SourceWithPort.

        OBS桶类型。   - private: 私有桶（除桶ACL授权外的其他用户无桶的访问权限）。   - public: 公有桶（任何用户都可以对桶内对象进行读操作）。

        :return: The obs_bucket_type of this SourceWithPort.
        :rtype: str
        """
        return self._obs_bucket_type

    @obs_bucket_type.setter
    def obs_bucket_type(self, obs_bucket_type):
        r"""Sets the obs_bucket_type of this SourceWithPort.

        OBS桶类型。   - private: 私有桶（除桶ACL授权外的其他用户无桶的访问权限）。   - public: 公有桶（任何用户都可以对桶内对象进行读操作）。

        :param obs_bucket_type: The obs_bucket_type of this SourceWithPort.
        :type obs_bucket_type: str
        """
        self._obs_bucket_type = obs_bucket_type

    @property
    def active_standby(self):
        r"""Gets the active_standby of this SourceWithPort.

        主备状态（1代表主源站；0代表备源站）。

        :return: The active_standby of this SourceWithPort.
        :rtype: int
        """
        return self._active_standby

    @active_standby.setter
    def active_standby(self, active_standby):
        r"""Sets the active_standby of this SourceWithPort.

        主备状态（1代表主源站；0代表备源站）。

        :param active_standby: The active_standby of this SourceWithPort.
        :type active_standby: int
        """
        self._active_standby = active_standby

    @property
    def enable_obs_web_hosting(self):
        r"""Gets the enable_obs_web_hosting of this SourceWithPort.

        **参数解释：** 是否开启静态网站托管功能，如果您的源站是OBS桶域名且配置了静态网站托管，开启该功能后，客户端即可访问静态网站托管页面 > 开启该功能后将自动给桶源站地址加上website字段，如果地址中已有website字段，该参数不生效 **约束限制：** - 源站类型为obs_bucket时需要传该参数 - 只有当源站OBS桶已经开启静态网站托管时，才可开启，否则将导致业务异常  **取值范围：** - 0: 关闭 - 1: 开启  **默认取值：** 0: 关闭

        :return: The enable_obs_web_hosting of this SourceWithPort.
        :rtype: int
        """
        return self._enable_obs_web_hosting

    @enable_obs_web_hosting.setter
    def enable_obs_web_hosting(self, enable_obs_web_hosting):
        r"""Sets the enable_obs_web_hosting of this SourceWithPort.

        **参数解释：** 是否开启静态网站托管功能，如果您的源站是OBS桶域名且配置了静态网站托管，开启该功能后，客户端即可访问静态网站托管页面 > 开启该功能后将自动给桶源站地址加上website字段，如果地址中已有website字段，该参数不生效 **约束限制：** - 源站类型为obs_bucket时需要传该参数 - 只有当源站OBS桶已经开启静态网站托管时，才可开启，否则将导致业务异常  **取值范围：** - 0: 关闭 - 1: 开启  **默认取值：** 0: 关闭

        :param enable_obs_web_hosting: The enable_obs_web_hosting of this SourceWithPort.
        :type enable_obs_web_hosting: int
        """
        self._enable_obs_web_hosting = enable_obs_web_hosting

    @property
    def http_port(self):
        r"""Gets the http_port of this SourceWithPort.

        **参数解释：** HTTP端口，默认80 **约束限制：** 不涉及 **取值范围：** 不涉及

        :return: The http_port of this SourceWithPort.
        :rtype: int
        """
        return self._http_port

    @http_port.setter
    def http_port(self, http_port):
        r"""Sets the http_port of this SourceWithPort.

        **参数解释：** HTTP端口，默认80 **约束限制：** 不涉及 **取值范围：** 不涉及

        :param http_port: The http_port of this SourceWithPort.
        :type http_port: int
        """
        self._http_port = http_port

    @property
    def https_port(self):
        r"""Gets the https_port of this SourceWithPort.

        **参数解释：** HTTPS端口，默认443 **约束限制：** 不涉及 **取值范围：** 不涉及

        :return: The https_port of this SourceWithPort.
        :rtype: int
        """
        return self._https_port

    @https_port.setter
    def https_port(self, https_port):
        r"""Sets the https_port of this SourceWithPort.

        **参数解释：** HTTPS端口，默认443 **约束限制：** 不涉及 **取值范围：** 不涉及

        :param https_port: The https_port of this SourceWithPort.
        :type https_port: int
        """
        self._https_port = https_port

    @property
    def weight(self):
        r"""Gets the weight of this SourceWithPort.

        **参数解释：** 权重，值越大回源到该源站的次数越多。多个优先级相同的源站，由权重决定回源到各个源站的比例 **约束限制：** 不涉及 **取值范围：** 1-100 **默认取值：** 50

        :return: The weight of this SourceWithPort.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        r"""Sets the weight of this SourceWithPort.

        **参数解释：** 权重，值越大回源到该源站的次数越多。多个优先级相同的源站，由权重决定回源到各个源站的比例 **约束限制：** 不涉及 **取值范围：** 1-100 **默认取值：** 50

        :param weight: The weight of this SourceWithPort.
        :type weight: int
        """
        self._weight = weight

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
        if not isinstance(other, SourceWithPort):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
