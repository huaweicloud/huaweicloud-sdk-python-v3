# coding: utf-8

import six

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
        """SourcesConfig

        The model defined in huaweicloud sdk

        :param origin_type: 源站类型， - ipaddr：源站IP； - domain：源站域名； - obs_bucket：OBS桶域名； - third_bucket：第三方桶。
        :type origin_type: str
        :param origin_addr: 源站IP或者域名。
        :type origin_addr: str
        :param priority: 源站优先级，70：主，30：备。
        :type priority: int
        :param weight: 权重，取值范围1-100。
        :type weight: int
        :param obs_web_hosting_status: 是否开启OBS静态网站托管，源站类型为obs_bucket时传递，off：关闭，on：开启。
        :type obs_web_hosting_status: str
        :param http_port: HTTP端口，默认80,端口取值取值范围1-65535。
        :type http_port: int
        :param https_port: HTTPS端口，默认443,端口取值取值范围1-65535。
        :type https_port: int
        :param host_name: 回源HOST，默认加速域名。
        :type host_name: str
        :param obs_bucket_type: OBS桶源站类型： - “private” 私有桶； - “public” 公有桶，默认为公有桶。
        :type obs_bucket_type: str
        :param bucket_access_key: 第三方对象存储访问密钥。  &gt; 源站类型为第三方桶时必填
        :type bucket_access_key: str
        :param bucket_secret_key: 第三方对象存储密钥。  &gt; 源站类型为第三方桶时必填
        :type bucket_secret_key: str
        :param bucket_region: 第三方对象存储区域。  &gt; 源站类型为第三方桶时必填
        :type bucket_region: str
        :param bucket_name: 第三方对象存储名称。  &gt; 源站类型为第三方桶时必填
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
        """Gets the origin_type of this SourcesConfig.

        源站类型， - ipaddr：源站IP； - domain：源站域名； - obs_bucket：OBS桶域名； - third_bucket：第三方桶。

        :return: The origin_type of this SourcesConfig.
        :rtype: str
        """
        return self._origin_type

    @origin_type.setter
    def origin_type(self, origin_type):
        """Sets the origin_type of this SourcesConfig.

        源站类型， - ipaddr：源站IP； - domain：源站域名； - obs_bucket：OBS桶域名； - third_bucket：第三方桶。

        :param origin_type: The origin_type of this SourcesConfig.
        :type origin_type: str
        """
        self._origin_type = origin_type

    @property
    def origin_addr(self):
        """Gets the origin_addr of this SourcesConfig.

        源站IP或者域名。

        :return: The origin_addr of this SourcesConfig.
        :rtype: str
        """
        return self._origin_addr

    @origin_addr.setter
    def origin_addr(self, origin_addr):
        """Sets the origin_addr of this SourcesConfig.

        源站IP或者域名。

        :param origin_addr: The origin_addr of this SourcesConfig.
        :type origin_addr: str
        """
        self._origin_addr = origin_addr

    @property
    def priority(self):
        """Gets the priority of this SourcesConfig.

        源站优先级，70：主，30：备。

        :return: The priority of this SourcesConfig.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this SourcesConfig.

        源站优先级，70：主，30：备。

        :param priority: The priority of this SourcesConfig.
        :type priority: int
        """
        self._priority = priority

    @property
    def weight(self):
        """Gets the weight of this SourcesConfig.

        权重，取值范围1-100。

        :return: The weight of this SourcesConfig.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this SourcesConfig.

        权重，取值范围1-100。

        :param weight: The weight of this SourcesConfig.
        :type weight: int
        """
        self._weight = weight

    @property
    def obs_web_hosting_status(self):
        """Gets the obs_web_hosting_status of this SourcesConfig.

        是否开启OBS静态网站托管，源站类型为obs_bucket时传递，off：关闭，on：开启。

        :return: The obs_web_hosting_status of this SourcesConfig.
        :rtype: str
        """
        return self._obs_web_hosting_status

    @obs_web_hosting_status.setter
    def obs_web_hosting_status(self, obs_web_hosting_status):
        """Sets the obs_web_hosting_status of this SourcesConfig.

        是否开启OBS静态网站托管，源站类型为obs_bucket时传递，off：关闭，on：开启。

        :param obs_web_hosting_status: The obs_web_hosting_status of this SourcesConfig.
        :type obs_web_hosting_status: str
        """
        self._obs_web_hosting_status = obs_web_hosting_status

    @property
    def http_port(self):
        """Gets the http_port of this SourcesConfig.

        HTTP端口，默认80,端口取值取值范围1-65535。

        :return: The http_port of this SourcesConfig.
        :rtype: int
        """
        return self._http_port

    @http_port.setter
    def http_port(self, http_port):
        """Sets the http_port of this SourcesConfig.

        HTTP端口，默认80,端口取值取值范围1-65535。

        :param http_port: The http_port of this SourcesConfig.
        :type http_port: int
        """
        self._http_port = http_port

    @property
    def https_port(self):
        """Gets the https_port of this SourcesConfig.

        HTTPS端口，默认443,端口取值取值范围1-65535。

        :return: The https_port of this SourcesConfig.
        :rtype: int
        """
        return self._https_port

    @https_port.setter
    def https_port(self, https_port):
        """Sets the https_port of this SourcesConfig.

        HTTPS端口，默认443,端口取值取值范围1-65535。

        :param https_port: The https_port of this SourcesConfig.
        :type https_port: int
        """
        self._https_port = https_port

    @property
    def host_name(self):
        """Gets the host_name of this SourcesConfig.

        回源HOST，默认加速域名。

        :return: The host_name of this SourcesConfig.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this SourcesConfig.

        回源HOST，默认加速域名。

        :param host_name: The host_name of this SourcesConfig.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def obs_bucket_type(self):
        """Gets the obs_bucket_type of this SourcesConfig.

        OBS桶源站类型： - “private” 私有桶； - “public” 公有桶，默认为公有桶。

        :return: The obs_bucket_type of this SourcesConfig.
        :rtype: str
        """
        return self._obs_bucket_type

    @obs_bucket_type.setter
    def obs_bucket_type(self, obs_bucket_type):
        """Sets the obs_bucket_type of this SourcesConfig.

        OBS桶源站类型： - “private” 私有桶； - “public” 公有桶，默认为公有桶。

        :param obs_bucket_type: The obs_bucket_type of this SourcesConfig.
        :type obs_bucket_type: str
        """
        self._obs_bucket_type = obs_bucket_type

    @property
    def bucket_access_key(self):
        """Gets the bucket_access_key of this SourcesConfig.

        第三方对象存储访问密钥。  > 源站类型为第三方桶时必填

        :return: The bucket_access_key of this SourcesConfig.
        :rtype: str
        """
        return self._bucket_access_key

    @bucket_access_key.setter
    def bucket_access_key(self, bucket_access_key):
        """Sets the bucket_access_key of this SourcesConfig.

        第三方对象存储访问密钥。  > 源站类型为第三方桶时必填

        :param bucket_access_key: The bucket_access_key of this SourcesConfig.
        :type bucket_access_key: str
        """
        self._bucket_access_key = bucket_access_key

    @property
    def bucket_secret_key(self):
        """Gets the bucket_secret_key of this SourcesConfig.

        第三方对象存储密钥。  > 源站类型为第三方桶时必填

        :return: The bucket_secret_key of this SourcesConfig.
        :rtype: str
        """
        return self._bucket_secret_key

    @bucket_secret_key.setter
    def bucket_secret_key(self, bucket_secret_key):
        """Sets the bucket_secret_key of this SourcesConfig.

        第三方对象存储密钥。  > 源站类型为第三方桶时必填

        :param bucket_secret_key: The bucket_secret_key of this SourcesConfig.
        :type bucket_secret_key: str
        """
        self._bucket_secret_key = bucket_secret_key

    @property
    def bucket_region(self):
        """Gets the bucket_region of this SourcesConfig.

        第三方对象存储区域。  > 源站类型为第三方桶时必填

        :return: The bucket_region of this SourcesConfig.
        :rtype: str
        """
        return self._bucket_region

    @bucket_region.setter
    def bucket_region(self, bucket_region):
        """Sets the bucket_region of this SourcesConfig.

        第三方对象存储区域。  > 源站类型为第三方桶时必填

        :param bucket_region: The bucket_region of this SourcesConfig.
        :type bucket_region: str
        """
        self._bucket_region = bucket_region

    @property
    def bucket_name(self):
        """Gets the bucket_name of this SourcesConfig.

        第三方对象存储名称。  > 源站类型为第三方桶时必填

        :return: The bucket_name of this SourcesConfig.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this SourcesConfig.

        第三方对象存储名称。  > 源站类型为第三方桶时必填

        :param bucket_name: The bucket_name of this SourcesConfig.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

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
        if not isinstance(other, SourcesConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
