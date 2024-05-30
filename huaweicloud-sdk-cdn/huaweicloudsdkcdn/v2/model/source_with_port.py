# coding: utf-8

import six

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
        'https_port': 'int'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'ip_or_domain': 'ip_or_domain',
        'origin_type': 'origin_type',
        'obs_bucket_type': 'obs_bucket_type',
        'active_standby': 'active_standby',
        'enable_obs_web_hosting': 'enable_obs_web_hosting',
        'http_port': 'http_port',
        'https_port': 'https_port'
    }

    def __init__(self, domain_id=None, ip_or_domain=None, origin_type=None, obs_bucket_type=None, active_standby=None, enable_obs_web_hosting=None, http_port=None, https_port=None):
        """SourceWithPort

        The model defined in huaweicloud sdk

        :param domain_id: 加速域名id。
        :type domain_id: str
        :param ip_or_domain: 源站IP（非内网IP）或者域名。
        :type ip_or_domain: str
        :param origin_type: 源站类型，ipaddr：源站IP、 domain：源站域名、obs_bucket：OBS桶域名。
        :type origin_type: str
        :param obs_bucket_type: OBS桶类型。   - private: 私有桶（除桶ACL授权外的其他用户无桶的访问权限）。   - public: 公有桶（任何用户都可以对桶内对象进行读操作）。
        :type obs_bucket_type: str
        :param active_standby: 主备状态（1代表主源站；0代表备源站）。
        :type active_standby: int
        :param enable_obs_web_hosting: 是否开OBS托管(0表示关闭,1表示则为开启)，源站类型为obs_bucket时传递。
        :type enable_obs_web_hosting: int
        :param http_port: HTTP端口，默认80
        :type http_port: int
        :param https_port: HTTPS端口，默认443
        :type https_port: int
        """
        
        

        self._domain_id = None
        self._ip_or_domain = None
        self._origin_type = None
        self._obs_bucket_type = None
        self._active_standby = None
        self._enable_obs_web_hosting = None
        self._http_port = None
        self._https_port = None
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

    @property
    def domain_id(self):
        """Gets the domain_id of this SourceWithPort.

        加速域名id。

        :return: The domain_id of this SourceWithPort.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this SourceWithPort.

        加速域名id。

        :param domain_id: The domain_id of this SourceWithPort.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def ip_or_domain(self):
        """Gets the ip_or_domain of this SourceWithPort.

        源站IP（非内网IP）或者域名。

        :return: The ip_or_domain of this SourceWithPort.
        :rtype: str
        """
        return self._ip_or_domain

    @ip_or_domain.setter
    def ip_or_domain(self, ip_or_domain):
        """Sets the ip_or_domain of this SourceWithPort.

        源站IP（非内网IP）或者域名。

        :param ip_or_domain: The ip_or_domain of this SourceWithPort.
        :type ip_or_domain: str
        """
        self._ip_or_domain = ip_or_domain

    @property
    def origin_type(self):
        """Gets the origin_type of this SourceWithPort.

        源站类型，ipaddr：源站IP、 domain：源站域名、obs_bucket：OBS桶域名。

        :return: The origin_type of this SourceWithPort.
        :rtype: str
        """
        return self._origin_type

    @origin_type.setter
    def origin_type(self, origin_type):
        """Sets the origin_type of this SourceWithPort.

        源站类型，ipaddr：源站IP、 domain：源站域名、obs_bucket：OBS桶域名。

        :param origin_type: The origin_type of this SourceWithPort.
        :type origin_type: str
        """
        self._origin_type = origin_type

    @property
    def obs_bucket_type(self):
        """Gets the obs_bucket_type of this SourceWithPort.

        OBS桶类型。   - private: 私有桶（除桶ACL授权外的其他用户无桶的访问权限）。   - public: 公有桶（任何用户都可以对桶内对象进行读操作）。

        :return: The obs_bucket_type of this SourceWithPort.
        :rtype: str
        """
        return self._obs_bucket_type

    @obs_bucket_type.setter
    def obs_bucket_type(self, obs_bucket_type):
        """Sets the obs_bucket_type of this SourceWithPort.

        OBS桶类型。   - private: 私有桶（除桶ACL授权外的其他用户无桶的访问权限）。   - public: 公有桶（任何用户都可以对桶内对象进行读操作）。

        :param obs_bucket_type: The obs_bucket_type of this SourceWithPort.
        :type obs_bucket_type: str
        """
        self._obs_bucket_type = obs_bucket_type

    @property
    def active_standby(self):
        """Gets the active_standby of this SourceWithPort.

        主备状态（1代表主源站；0代表备源站）。

        :return: The active_standby of this SourceWithPort.
        :rtype: int
        """
        return self._active_standby

    @active_standby.setter
    def active_standby(self, active_standby):
        """Sets the active_standby of this SourceWithPort.

        主备状态（1代表主源站；0代表备源站）。

        :param active_standby: The active_standby of this SourceWithPort.
        :type active_standby: int
        """
        self._active_standby = active_standby

    @property
    def enable_obs_web_hosting(self):
        """Gets the enable_obs_web_hosting of this SourceWithPort.

        是否开OBS托管(0表示关闭,1表示则为开启)，源站类型为obs_bucket时传递。

        :return: The enable_obs_web_hosting of this SourceWithPort.
        :rtype: int
        """
        return self._enable_obs_web_hosting

    @enable_obs_web_hosting.setter
    def enable_obs_web_hosting(self, enable_obs_web_hosting):
        """Sets the enable_obs_web_hosting of this SourceWithPort.

        是否开OBS托管(0表示关闭,1表示则为开启)，源站类型为obs_bucket时传递。

        :param enable_obs_web_hosting: The enable_obs_web_hosting of this SourceWithPort.
        :type enable_obs_web_hosting: int
        """
        self._enable_obs_web_hosting = enable_obs_web_hosting

    @property
    def http_port(self):
        """Gets the http_port of this SourceWithPort.

        HTTP端口，默认80

        :return: The http_port of this SourceWithPort.
        :rtype: int
        """
        return self._http_port

    @http_port.setter
    def http_port(self, http_port):
        """Sets the http_port of this SourceWithPort.

        HTTP端口，默认80

        :param http_port: The http_port of this SourceWithPort.
        :type http_port: int
        """
        self._http_port = http_port

    @property
    def https_port(self):
        """Gets the https_port of this SourceWithPort.

        HTTPS端口，默认443

        :return: The https_port of this SourceWithPort.
        :rtype: int
        """
        return self._https_port

    @https_port.setter
    def https_port(self, https_port):
        """Sets the https_port of this SourceWithPort.

        HTTPS端口，默认443

        :param https_port: The https_port of this SourceWithPort.
        :type https_port: int
        """
        self._https_port = https_port

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
        if not isinstance(other, SourceWithPort):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
