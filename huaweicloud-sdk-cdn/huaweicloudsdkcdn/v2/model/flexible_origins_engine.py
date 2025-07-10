# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlexibleOriginsEngine:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sources_type': 'str',
        'ip_or_domain': 'str',
        'obs_bucket_type': 'str',
        'bucket_access_key': 'str',
        'bucket_secret_key': 'str',
        'bucket_region': 'str',
        'bucket_name': 'str',
        'host_name': 'str',
        'origin_protocol': 'str',
        'http_port': 'int',
        'https_port': 'int',
        'priority': 'int',
        'weight': 'int'
    }

    attribute_map = {
        'sources_type': 'sources_type',
        'ip_or_domain': 'ip_or_domain',
        'obs_bucket_type': 'obs_bucket_type',
        'bucket_access_key': 'bucket_access_key',
        'bucket_secret_key': 'bucket_secret_key',
        'bucket_region': 'bucket_region',
        'bucket_name': 'bucket_name',
        'host_name': 'host_name',
        'origin_protocol': 'origin_protocol',
        'http_port': 'http_port',
        'https_port': 'https_port',
        'priority': 'priority',
        'weight': 'weight'
    }

    def __init__(self, sources_type=None, ip_or_domain=None, obs_bucket_type=None, bucket_access_key=None, bucket_secret_key=None, bucket_region=None, bucket_name=None, host_name=None, origin_protocol=None, http_port=None, https_port=None, priority=None, weight=None):
        r"""FlexibleOriginsEngine

        The model defined in huaweicloud sdk

        :param sources_type: **参数解释：** 源站类型 **约束限制：** 不涉及 **取值范围：** - ipaddr: 源站IP - domain: 源站域名 - obs_bucket: OBS桶域名 - third_bucket: 第三方桶域名 **默认取值：** 不涉及
        :type sources_type: str
        :param ip_or_domain: **参数解释：** 源站IP或者域名 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type ip_or_domain: str
        :param obs_bucket_type: **参数解释：** OBS桶类型 **约束限制：** 源站类型是“OBS桶域名”时需要传该参数 **取值范围：** - private: 私有桶 - public: 公有桶 **默认取值：** public: 公有桶
        :type obs_bucket_type: str
        :param bucket_access_key: **参数解释：** 第三方对象存储访问密钥 **约束限制：** 源站类型为第三方桶时必填 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type bucket_access_key: str
        :param bucket_secret_key: **参数解释：** 第三方对象存储密钥 **约束限制：** 源站类型为第三方桶时必填 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type bucket_secret_key: str
        :param bucket_region: **参数解释：** 第三方对象存储区域 **约束限制：** 源站类型为第三方桶时必填 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type bucket_region: str
        :param bucket_name: **参数解释：** 第三方对象存储名称 **约束限制：** 源站类型为第三方桶时必填 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type bucket_name: str
        :param host_name: **参数解释：** 回源HOST **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 加速域名
        :type host_name: str
        :param origin_protocol: **参数解释：** 指定CDN回源时的请求协议 **约束限制：** 不涉及 **取值范围：** - follow: 协议跟随 - http: http协议 - https: https协议 **默认取值：** http: http协议
        :type origin_protocol: str
        :param http_port: **参数解释：** HTTP端口 **约束限制：** 不涉及 **取值范围：** 1-65535 **默认取值：** 80
        :type http_port: int
        :param https_port: **参数解释：** HTTPS端口 **约束限制：** 不涉及 **取值范围：** 1-65535 **默认取值：** 443
        :type https_port: int
        :param priority: **参数解释：** 优先级，值越大优先级越高 **约束限制：** 不涉及 **取值范围：** 1-100 **默认取值：** 不涉及
        :type priority: int
        :param weight: **参数解释：** 权重，值越大回源到该源站的次数越多。多个优先级相同的源站，由权重决定回源到各个源站的比例 **约束限制：** 不涉及 **取值范围：** 1-100 **默认取值：** 不涉及
        :type weight: int
        """
        
        

        self._sources_type = None
        self._ip_or_domain = None
        self._obs_bucket_type = None
        self._bucket_access_key = None
        self._bucket_secret_key = None
        self._bucket_region = None
        self._bucket_name = None
        self._host_name = None
        self._origin_protocol = None
        self._http_port = None
        self._https_port = None
        self._priority = None
        self._weight = None
        self.discriminator = None

        self.sources_type = sources_type
        self.ip_or_domain = ip_or_domain
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
        if host_name is not None:
            self.host_name = host_name
        if origin_protocol is not None:
            self.origin_protocol = origin_protocol
        if http_port is not None:
            self.http_port = http_port
        if https_port is not None:
            self.https_port = https_port
        self.priority = priority
        self.weight = weight

    @property
    def sources_type(self):
        r"""Gets the sources_type of this FlexibleOriginsEngine.

        **参数解释：** 源站类型 **约束限制：** 不涉及 **取值范围：** - ipaddr: 源站IP - domain: 源站域名 - obs_bucket: OBS桶域名 - third_bucket: 第三方桶域名 **默认取值：** 不涉及

        :return: The sources_type of this FlexibleOriginsEngine.
        :rtype: str
        """
        return self._sources_type

    @sources_type.setter
    def sources_type(self, sources_type):
        r"""Sets the sources_type of this FlexibleOriginsEngine.

        **参数解释：** 源站类型 **约束限制：** 不涉及 **取值范围：** - ipaddr: 源站IP - domain: 源站域名 - obs_bucket: OBS桶域名 - third_bucket: 第三方桶域名 **默认取值：** 不涉及

        :param sources_type: The sources_type of this FlexibleOriginsEngine.
        :type sources_type: str
        """
        self._sources_type = sources_type

    @property
    def ip_or_domain(self):
        r"""Gets the ip_or_domain of this FlexibleOriginsEngine.

        **参数解释：** 源站IP或者域名 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The ip_or_domain of this FlexibleOriginsEngine.
        :rtype: str
        """
        return self._ip_or_domain

    @ip_or_domain.setter
    def ip_or_domain(self, ip_or_domain):
        r"""Sets the ip_or_domain of this FlexibleOriginsEngine.

        **参数解释：** 源站IP或者域名 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param ip_or_domain: The ip_or_domain of this FlexibleOriginsEngine.
        :type ip_or_domain: str
        """
        self._ip_or_domain = ip_or_domain

    @property
    def obs_bucket_type(self):
        r"""Gets the obs_bucket_type of this FlexibleOriginsEngine.

        **参数解释：** OBS桶类型 **约束限制：** 源站类型是“OBS桶域名”时需要传该参数 **取值范围：** - private: 私有桶 - public: 公有桶 **默认取值：** public: 公有桶

        :return: The obs_bucket_type of this FlexibleOriginsEngine.
        :rtype: str
        """
        return self._obs_bucket_type

    @obs_bucket_type.setter
    def obs_bucket_type(self, obs_bucket_type):
        r"""Sets the obs_bucket_type of this FlexibleOriginsEngine.

        **参数解释：** OBS桶类型 **约束限制：** 源站类型是“OBS桶域名”时需要传该参数 **取值范围：** - private: 私有桶 - public: 公有桶 **默认取值：** public: 公有桶

        :param obs_bucket_type: The obs_bucket_type of this FlexibleOriginsEngine.
        :type obs_bucket_type: str
        """
        self._obs_bucket_type = obs_bucket_type

    @property
    def bucket_access_key(self):
        r"""Gets the bucket_access_key of this FlexibleOriginsEngine.

        **参数解释：** 第三方对象存储访问密钥 **约束限制：** 源站类型为第三方桶时必填 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The bucket_access_key of this FlexibleOriginsEngine.
        :rtype: str
        """
        return self._bucket_access_key

    @bucket_access_key.setter
    def bucket_access_key(self, bucket_access_key):
        r"""Sets the bucket_access_key of this FlexibleOriginsEngine.

        **参数解释：** 第三方对象存储访问密钥 **约束限制：** 源站类型为第三方桶时必填 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param bucket_access_key: The bucket_access_key of this FlexibleOriginsEngine.
        :type bucket_access_key: str
        """
        self._bucket_access_key = bucket_access_key

    @property
    def bucket_secret_key(self):
        r"""Gets the bucket_secret_key of this FlexibleOriginsEngine.

        **参数解释：** 第三方对象存储密钥 **约束限制：** 源站类型为第三方桶时必填 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The bucket_secret_key of this FlexibleOriginsEngine.
        :rtype: str
        """
        return self._bucket_secret_key

    @bucket_secret_key.setter
    def bucket_secret_key(self, bucket_secret_key):
        r"""Sets the bucket_secret_key of this FlexibleOriginsEngine.

        **参数解释：** 第三方对象存储密钥 **约束限制：** 源站类型为第三方桶时必填 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param bucket_secret_key: The bucket_secret_key of this FlexibleOriginsEngine.
        :type bucket_secret_key: str
        """
        self._bucket_secret_key = bucket_secret_key

    @property
    def bucket_region(self):
        r"""Gets the bucket_region of this FlexibleOriginsEngine.

        **参数解释：** 第三方对象存储区域 **约束限制：** 源站类型为第三方桶时必填 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The bucket_region of this FlexibleOriginsEngine.
        :rtype: str
        """
        return self._bucket_region

    @bucket_region.setter
    def bucket_region(self, bucket_region):
        r"""Sets the bucket_region of this FlexibleOriginsEngine.

        **参数解释：** 第三方对象存储区域 **约束限制：** 源站类型为第三方桶时必填 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param bucket_region: The bucket_region of this FlexibleOriginsEngine.
        :type bucket_region: str
        """
        self._bucket_region = bucket_region

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this FlexibleOriginsEngine.

        **参数解释：** 第三方对象存储名称 **约束限制：** 源站类型为第三方桶时必填 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The bucket_name of this FlexibleOriginsEngine.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this FlexibleOriginsEngine.

        **参数解释：** 第三方对象存储名称 **约束限制：** 源站类型为第三方桶时必填 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param bucket_name: The bucket_name of this FlexibleOriginsEngine.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def host_name(self):
        r"""Gets the host_name of this FlexibleOriginsEngine.

        **参数解释：** 回源HOST **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 加速域名

        :return: The host_name of this FlexibleOriginsEngine.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this FlexibleOriginsEngine.

        **参数解释：** 回源HOST **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 加速域名

        :param host_name: The host_name of this FlexibleOriginsEngine.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def origin_protocol(self):
        r"""Gets the origin_protocol of this FlexibleOriginsEngine.

        **参数解释：** 指定CDN回源时的请求协议 **约束限制：** 不涉及 **取值范围：** - follow: 协议跟随 - http: http协议 - https: https协议 **默认取值：** http: http协议

        :return: The origin_protocol of this FlexibleOriginsEngine.
        :rtype: str
        """
        return self._origin_protocol

    @origin_protocol.setter
    def origin_protocol(self, origin_protocol):
        r"""Sets the origin_protocol of this FlexibleOriginsEngine.

        **参数解释：** 指定CDN回源时的请求协议 **约束限制：** 不涉及 **取值范围：** - follow: 协议跟随 - http: http协议 - https: https协议 **默认取值：** http: http协议

        :param origin_protocol: The origin_protocol of this FlexibleOriginsEngine.
        :type origin_protocol: str
        """
        self._origin_protocol = origin_protocol

    @property
    def http_port(self):
        r"""Gets the http_port of this FlexibleOriginsEngine.

        **参数解释：** HTTP端口 **约束限制：** 不涉及 **取值范围：** 1-65535 **默认取值：** 80

        :return: The http_port of this FlexibleOriginsEngine.
        :rtype: int
        """
        return self._http_port

    @http_port.setter
    def http_port(self, http_port):
        r"""Sets the http_port of this FlexibleOriginsEngine.

        **参数解释：** HTTP端口 **约束限制：** 不涉及 **取值范围：** 1-65535 **默认取值：** 80

        :param http_port: The http_port of this FlexibleOriginsEngine.
        :type http_port: int
        """
        self._http_port = http_port

    @property
    def https_port(self):
        r"""Gets the https_port of this FlexibleOriginsEngine.

        **参数解释：** HTTPS端口 **约束限制：** 不涉及 **取值范围：** 1-65535 **默认取值：** 443

        :return: The https_port of this FlexibleOriginsEngine.
        :rtype: int
        """
        return self._https_port

    @https_port.setter
    def https_port(self, https_port):
        r"""Sets the https_port of this FlexibleOriginsEngine.

        **参数解释：** HTTPS端口 **约束限制：** 不涉及 **取值范围：** 1-65535 **默认取值：** 443

        :param https_port: The https_port of this FlexibleOriginsEngine.
        :type https_port: int
        """
        self._https_port = https_port

    @property
    def priority(self):
        r"""Gets the priority of this FlexibleOriginsEngine.

        **参数解释：** 优先级，值越大优先级越高 **约束限制：** 不涉及 **取值范围：** 1-100 **默认取值：** 不涉及

        :return: The priority of this FlexibleOriginsEngine.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this FlexibleOriginsEngine.

        **参数解释：** 优先级，值越大优先级越高 **约束限制：** 不涉及 **取值范围：** 1-100 **默认取值：** 不涉及

        :param priority: The priority of this FlexibleOriginsEngine.
        :type priority: int
        """
        self._priority = priority

    @property
    def weight(self):
        r"""Gets the weight of this FlexibleOriginsEngine.

        **参数解释：** 权重，值越大回源到该源站的次数越多。多个优先级相同的源站，由权重决定回源到各个源站的比例 **约束限制：** 不涉及 **取值范围：** 1-100 **默认取值：** 不涉及

        :return: The weight of this FlexibleOriginsEngine.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        r"""Sets the weight of this FlexibleOriginsEngine.

        **参数解释：** 权重，值越大回源到该源站的次数越多。多个优先级相同的源站，由权重决定回源到各个源站的比例 **约束限制：** 不涉及 **取值范围：** 1-100 **默认取值：** 不涉及

        :param weight: The weight of this FlexibleOriginsEngine.
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
        if not isinstance(other, FlexibleOriginsEngine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
