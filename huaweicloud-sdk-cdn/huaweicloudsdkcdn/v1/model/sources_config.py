# coding: utf-8

import re
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
        'origin_addr': 'str',
        'origin_type': 'str',
        'priority': 'int',
        'obs_web_hosting_status': 'str',
        'http_port': 'int',
        'https_port': 'int',
        'host_name': 'str'
    }

    attribute_map = {
        'origin_addr': 'origin_addr',
        'origin_type': 'origin_type',
        'priority': 'priority',
        'obs_web_hosting_status': 'obs_web_hosting_status',
        'http_port': 'http_port',
        'https_port': 'https_port',
        'host_name': 'host_name'
    }

    def __init__(self, origin_addr=None, origin_type=None, priority=None, obs_web_hosting_status=None, http_port=None, https_port=None, host_name=None):
        """SourcesConfig

        The model defined in huaweicloud sdk

        :param origin_addr: 源站IP或者域名。
        :type origin_addr: str
        :param origin_type: 源站类型（\&quot;ipaddr\&quot;：\&quot;IP源站\&quot;，\&quot;domain\&quot;：\&quot;域名源站\&quot;，\&quot;obs_bucket\&quot;：\&quot;OBS Bucket源站\&quot;）。
        :type origin_type: str
        :param priority: 源站优先级（70：主，30：备）。
        :type priority: int
        :param obs_web_hosting_status: 是否开启Obs静态网站托管，源站类型为obs_bucket时传递(off：关闭，on：开启)。
        :type obs_web_hosting_status: str
        :param http_port: HTTP端口，默认80。
        :type http_port: int
        :param https_port: HTTPS端口，默认443。
        :type https_port: int
        :param host_name: 回源HOST，默认加速域名。
        :type host_name: str
        """
        
        

        self._origin_addr = None
        self._origin_type = None
        self._priority = None
        self._obs_web_hosting_status = None
        self._http_port = None
        self._https_port = None
        self._host_name = None
        self.discriminator = None

        self.origin_addr = origin_addr
        self.origin_type = origin_type
        self.priority = priority
        if obs_web_hosting_status is not None:
            self.obs_web_hosting_status = obs_web_hosting_status
        if http_port is not None:
            self.http_port = http_port
        if https_port is not None:
            self.https_port = https_port
        if host_name is not None:
            self.host_name = host_name

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
    def origin_type(self):
        """Gets the origin_type of this SourcesConfig.

        源站类型（\"ipaddr\"：\"IP源站\"，\"domain\"：\"域名源站\"，\"obs_bucket\"：\"OBS Bucket源站\"）。

        :return: The origin_type of this SourcesConfig.
        :rtype: str
        """
        return self._origin_type

    @origin_type.setter
    def origin_type(self, origin_type):
        """Sets the origin_type of this SourcesConfig.

        源站类型（\"ipaddr\"：\"IP源站\"，\"domain\"：\"域名源站\"，\"obs_bucket\"：\"OBS Bucket源站\"）。

        :param origin_type: The origin_type of this SourcesConfig.
        :type origin_type: str
        """
        self._origin_type = origin_type

    @property
    def priority(self):
        """Gets the priority of this SourcesConfig.

        源站优先级（70：主，30：备）。

        :return: The priority of this SourcesConfig.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this SourcesConfig.

        源站优先级（70：主，30：备）。

        :param priority: The priority of this SourcesConfig.
        :type priority: int
        """
        self._priority = priority

    @property
    def obs_web_hosting_status(self):
        """Gets the obs_web_hosting_status of this SourcesConfig.

        是否开启Obs静态网站托管，源站类型为obs_bucket时传递(off：关闭，on：开启)。

        :return: The obs_web_hosting_status of this SourcesConfig.
        :rtype: str
        """
        return self._obs_web_hosting_status

    @obs_web_hosting_status.setter
    def obs_web_hosting_status(self, obs_web_hosting_status):
        """Sets the obs_web_hosting_status of this SourcesConfig.

        是否开启Obs静态网站托管，源站类型为obs_bucket时传递(off：关闭，on：开启)。

        :param obs_web_hosting_status: The obs_web_hosting_status of this SourcesConfig.
        :type obs_web_hosting_status: str
        """
        self._obs_web_hosting_status = obs_web_hosting_status

    @property
    def http_port(self):
        """Gets the http_port of this SourcesConfig.

        HTTP端口，默认80。

        :return: The http_port of this SourcesConfig.
        :rtype: int
        """
        return self._http_port

    @http_port.setter
    def http_port(self, http_port):
        """Sets the http_port of this SourcesConfig.

        HTTP端口，默认80。

        :param http_port: The http_port of this SourcesConfig.
        :type http_port: int
        """
        self._http_port = http_port

    @property
    def https_port(self):
        """Gets the https_port of this SourcesConfig.

        HTTPS端口，默认443。

        :return: The https_port of this SourcesConfig.
        :rtype: int
        """
        return self._https_port

    @https_port.setter
    def https_port(self, https_port):
        """Sets the https_port of this SourcesConfig.

        HTTPS端口，默认443。

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
