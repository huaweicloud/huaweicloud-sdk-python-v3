# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackSources:

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
        'http_port': 'int',
        'https_port': 'int'
    }

    attribute_map = {
        'sources_type': 'sources_type',
        'ip_or_domain': 'ip_or_domain',
        'obs_bucket_type': 'obs_bucket_type',
        'http_port': 'http_port',
        'https_port': 'https_port'
    }

    def __init__(self, sources_type=None, ip_or_domain=None, obs_bucket_type=None, http_port=None, https_port=None):
        """BackSources

        The model defined in huaweicloud sdk

        :param sources_type: 源站类型, ipaddr：源站IP，domain：源站域名，obs_bucket：OBS桶域名。
        :type sources_type: str
        :param ip_or_domain: 源站IP或者域名。
        :type ip_or_domain: str
        :param obs_bucket_type: OBS桶类型： - “private”， 私有桶： - “public”，公有桶。
        :type obs_bucket_type: str
        :param http_port: HTTP端口，取值范围：1-65535。
        :type http_port: int
        :param https_port: HTTPS端口，取值范围：1-65535。
        :type https_port: int
        """
        
        

        self._sources_type = None
        self._ip_or_domain = None
        self._obs_bucket_type = None
        self._http_port = None
        self._https_port = None
        self.discriminator = None

        self.sources_type = sources_type
        self.ip_or_domain = ip_or_domain
        if obs_bucket_type is not None:
            self.obs_bucket_type = obs_bucket_type
        if http_port is not None:
            self.http_port = http_port
        if https_port is not None:
            self.https_port = https_port

    @property
    def sources_type(self):
        """Gets the sources_type of this BackSources.

        源站类型, ipaddr：源站IP，domain：源站域名，obs_bucket：OBS桶域名。

        :return: The sources_type of this BackSources.
        :rtype: str
        """
        return self._sources_type

    @sources_type.setter
    def sources_type(self, sources_type):
        """Sets the sources_type of this BackSources.

        源站类型, ipaddr：源站IP，domain：源站域名，obs_bucket：OBS桶域名。

        :param sources_type: The sources_type of this BackSources.
        :type sources_type: str
        """
        self._sources_type = sources_type

    @property
    def ip_or_domain(self):
        """Gets the ip_or_domain of this BackSources.

        源站IP或者域名。

        :return: The ip_or_domain of this BackSources.
        :rtype: str
        """
        return self._ip_or_domain

    @ip_or_domain.setter
    def ip_or_domain(self, ip_or_domain):
        """Sets the ip_or_domain of this BackSources.

        源站IP或者域名。

        :param ip_or_domain: The ip_or_domain of this BackSources.
        :type ip_or_domain: str
        """
        self._ip_or_domain = ip_or_domain

    @property
    def obs_bucket_type(self):
        """Gets the obs_bucket_type of this BackSources.

        OBS桶类型： - “private”， 私有桶： - “public”，公有桶。

        :return: The obs_bucket_type of this BackSources.
        :rtype: str
        """
        return self._obs_bucket_type

    @obs_bucket_type.setter
    def obs_bucket_type(self, obs_bucket_type):
        """Sets the obs_bucket_type of this BackSources.

        OBS桶类型： - “private”， 私有桶： - “public”，公有桶。

        :param obs_bucket_type: The obs_bucket_type of this BackSources.
        :type obs_bucket_type: str
        """
        self._obs_bucket_type = obs_bucket_type

    @property
    def http_port(self):
        """Gets the http_port of this BackSources.

        HTTP端口，取值范围：1-65535。

        :return: The http_port of this BackSources.
        :rtype: int
        """
        return self._http_port

    @http_port.setter
    def http_port(self, http_port):
        """Sets the http_port of this BackSources.

        HTTP端口，取值范围：1-65535。

        :param http_port: The http_port of this BackSources.
        :type http_port: int
        """
        self._http_port = http_port

    @property
    def https_port(self):
        """Gets the https_port of this BackSources.

        HTTPS端口，取值范围：1-65535。

        :return: The https_port of this BackSources.
        :rtype: int
        """
        return self._https_port

    @https_port.setter
    def https_port(self, https_port):
        """Sets the https_port of this BackSources.

        HTTPS端口，取值范围：1-65535。

        :param https_port: The https_port of this BackSources.
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
        if not isinstance(other, BackSources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
