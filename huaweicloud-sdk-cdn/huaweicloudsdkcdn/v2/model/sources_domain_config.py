# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SourcesDomainConfig:

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
        'obs_web_hosting_status': 'str',
        'http_port': 'int',
        'https_port': 'int',
        'host_name': 'str',
        'obs_bucket_type': 'str'
    }

    attribute_map = {
        'origin_type': 'origin_type',
        'origin_addr': 'origin_addr',
        'priority': 'priority',
        'obs_web_hosting_status': 'obs_web_hosting_status',
        'http_port': 'http_port',
        'https_port': 'https_port',
        'host_name': 'host_name',
        'obs_bucket_type': 'obs_bucket_type'
    }

    def __init__(self, origin_type=None, origin_addr=None, priority=None, obs_web_hosting_status=None, http_port=None, https_port=None, host_name=None, obs_bucket_type=None):
        """SourcesDomainConfig

        The model defined in huaweicloud sdk

        :param origin_type: 源站类型。 - ipaddr：源站IP； - domain：源站域名； - obs_bucket：OBS桶域名； - third_bucket：第三方桶。
        :type origin_type: str
        :param origin_addr: 源站IP或者域名。
        :type origin_addr: str
        :param priority: 源站优先级，70：主，30：备。
        :type priority: int
        :param obs_web_hosting_status: 是否开启OBS静态网站托管，源站类型为obs_bucket时传递，off：关闭，on：开启。
        :type obs_web_hosting_status: str
        :param http_port: HTTP端口，默认80,端口取值取值范围1-65535。
        :type http_port: int
        :param https_port: HTTPS端口，默认443,端口取值取值范围1-65535。
        :type https_port: int
        :param host_name: 回源HOST，默认加速域名。
        :type host_name: str
        :param obs_bucket_type: OBS桶类型。   - private: 私有桶（除桶ACL授权外的其他用户无桶的访问权限）。   - public: 公有桶（任何用户都可以对桶内对象进行读操作）。
        :type obs_bucket_type: str
        """
        
        

        self._origin_type = None
        self._origin_addr = None
        self._priority = None
        self._obs_web_hosting_status = None
        self._http_port = None
        self._https_port = None
        self._host_name = None
        self._obs_bucket_type = None
        self.discriminator = None

        self.origin_type = origin_type
        self.origin_addr = origin_addr
        self.priority = priority
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

    @property
    def origin_type(self):
        """Gets the origin_type of this SourcesDomainConfig.

        源站类型。 - ipaddr：源站IP； - domain：源站域名； - obs_bucket：OBS桶域名； - third_bucket：第三方桶。

        :return: The origin_type of this SourcesDomainConfig.
        :rtype: str
        """
        return self._origin_type

    @origin_type.setter
    def origin_type(self, origin_type):
        """Sets the origin_type of this SourcesDomainConfig.

        源站类型。 - ipaddr：源站IP； - domain：源站域名； - obs_bucket：OBS桶域名； - third_bucket：第三方桶。

        :param origin_type: The origin_type of this SourcesDomainConfig.
        :type origin_type: str
        """
        self._origin_type = origin_type

    @property
    def origin_addr(self):
        """Gets the origin_addr of this SourcesDomainConfig.

        源站IP或者域名。

        :return: The origin_addr of this SourcesDomainConfig.
        :rtype: str
        """
        return self._origin_addr

    @origin_addr.setter
    def origin_addr(self, origin_addr):
        """Sets the origin_addr of this SourcesDomainConfig.

        源站IP或者域名。

        :param origin_addr: The origin_addr of this SourcesDomainConfig.
        :type origin_addr: str
        """
        self._origin_addr = origin_addr

    @property
    def priority(self):
        """Gets the priority of this SourcesDomainConfig.

        源站优先级，70：主，30：备。

        :return: The priority of this SourcesDomainConfig.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this SourcesDomainConfig.

        源站优先级，70：主，30：备。

        :param priority: The priority of this SourcesDomainConfig.
        :type priority: int
        """
        self._priority = priority

    @property
    def obs_web_hosting_status(self):
        """Gets the obs_web_hosting_status of this SourcesDomainConfig.

        是否开启OBS静态网站托管，源站类型为obs_bucket时传递，off：关闭，on：开启。

        :return: The obs_web_hosting_status of this SourcesDomainConfig.
        :rtype: str
        """
        return self._obs_web_hosting_status

    @obs_web_hosting_status.setter
    def obs_web_hosting_status(self, obs_web_hosting_status):
        """Sets the obs_web_hosting_status of this SourcesDomainConfig.

        是否开启OBS静态网站托管，源站类型为obs_bucket时传递，off：关闭，on：开启。

        :param obs_web_hosting_status: The obs_web_hosting_status of this SourcesDomainConfig.
        :type obs_web_hosting_status: str
        """
        self._obs_web_hosting_status = obs_web_hosting_status

    @property
    def http_port(self):
        """Gets the http_port of this SourcesDomainConfig.

        HTTP端口，默认80,端口取值取值范围1-65535。

        :return: The http_port of this SourcesDomainConfig.
        :rtype: int
        """
        return self._http_port

    @http_port.setter
    def http_port(self, http_port):
        """Sets the http_port of this SourcesDomainConfig.

        HTTP端口，默认80,端口取值取值范围1-65535。

        :param http_port: The http_port of this SourcesDomainConfig.
        :type http_port: int
        """
        self._http_port = http_port

    @property
    def https_port(self):
        """Gets the https_port of this SourcesDomainConfig.

        HTTPS端口，默认443,端口取值取值范围1-65535。

        :return: The https_port of this SourcesDomainConfig.
        :rtype: int
        """
        return self._https_port

    @https_port.setter
    def https_port(self, https_port):
        """Sets the https_port of this SourcesDomainConfig.

        HTTPS端口，默认443,端口取值取值范围1-65535。

        :param https_port: The https_port of this SourcesDomainConfig.
        :type https_port: int
        """
        self._https_port = https_port

    @property
    def host_name(self):
        """Gets the host_name of this SourcesDomainConfig.

        回源HOST，默认加速域名。

        :return: The host_name of this SourcesDomainConfig.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this SourcesDomainConfig.

        回源HOST，默认加速域名。

        :param host_name: The host_name of this SourcesDomainConfig.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def obs_bucket_type(self):
        """Gets the obs_bucket_type of this SourcesDomainConfig.

        OBS桶类型。   - private: 私有桶（除桶ACL授权外的其他用户无桶的访问权限）。   - public: 公有桶（任何用户都可以对桶内对象进行读操作）。

        :return: The obs_bucket_type of this SourcesDomainConfig.
        :rtype: str
        """
        return self._obs_bucket_type

    @obs_bucket_type.setter
    def obs_bucket_type(self, obs_bucket_type):
        """Sets the obs_bucket_type of this SourcesDomainConfig.

        OBS桶类型。   - private: 私有桶（除桶ACL授权外的其他用户无桶的访问权限）。   - public: 公有桶（任何用户都可以对桶内对象进行读操作）。

        :param obs_bucket_type: The obs_bucket_type of this SourcesDomainConfig.
        :type obs_bucket_type: str
        """
        self._obs_bucket_type = obs_bucket_type

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
        if not isinstance(other, SourcesDomainConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
