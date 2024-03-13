# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HostBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_name': 'str',
        'enterprise_project_id': 'str',
        'vips': 'list[str]',
        'real_server_type': 'int',
        'port_http': 'list[int]',
        'port_https': 'list[int]',
        'real_server': 'str'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'enterprise_project_id': 'enterprise_project_id',
        'vips': 'vips',
        'real_server_type': 'real_server_type',
        'port_http': 'port_http',
        'port_https': 'port_https',
        'real_server': 'real_server'
    }

    def __init__(self, domain_name=None, enterprise_project_id=None, vips=None, real_server_type=None, port_http=None, port_https=None, real_server=None):
        """HostBody

        The model defined in huaweicloud sdk

        :param domain_name: 域名
        :type domain_name: str
        :param enterprise_project_id: 企业项目id，与接入的高防实例所属企业项目保持一致。可在华为云EPS服务中查看企业项目id，default企业项目id为\&quot;0\&quot;。
        :type enterprise_project_id: str
        :param vips: 高防实例ip列表。多个高防实例ip必须属于同一企业项目。
        :type vips: list[str]
        :param real_server_type: 源站类型。 0 - 源站IP， 1 - 源站域名。
        :type real_server_type: int
        :param port_http: HTTP端口，与port_https不能同时为空。DDoS高防支持的HTTP端口可在控制台查看。
        :type port_http: list[int]
        :param port_https: HTTPS端口，与port_http不能同时为空。DDoS高防支持的HTTPS端口可在控制台查看。
        :type port_https: list[int]
        :param real_server: 源站ip/源站域名
        :type real_server: str
        """
        
        

        self._domain_name = None
        self._enterprise_project_id = None
        self._vips = None
        self._real_server_type = None
        self._port_http = None
        self._port_https = None
        self._real_server = None
        self.discriminator = None

        self.domain_name = domain_name
        self.enterprise_project_id = enterprise_project_id
        self.vips = vips
        self.real_server_type = real_server_type
        if port_http is not None:
            self.port_http = port_http
        if port_https is not None:
            self.port_https = port_https
        self.real_server = real_server

    @property
    def domain_name(self):
        """Gets the domain_name of this HostBody.

        域名

        :return: The domain_name of this HostBody.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this HostBody.

        域名

        :param domain_name: The domain_name of this HostBody.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this HostBody.

        企业项目id，与接入的高防实例所属企业项目保持一致。可在华为云EPS服务中查看企业项目id，default企业项目id为\"0\"。

        :return: The enterprise_project_id of this HostBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this HostBody.

        企业项目id，与接入的高防实例所属企业项目保持一致。可在华为云EPS服务中查看企业项目id，default企业项目id为\"0\"。

        :param enterprise_project_id: The enterprise_project_id of this HostBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def vips(self):
        """Gets the vips of this HostBody.

        高防实例ip列表。多个高防实例ip必须属于同一企业项目。

        :return: The vips of this HostBody.
        :rtype: list[str]
        """
        return self._vips

    @vips.setter
    def vips(self, vips):
        """Sets the vips of this HostBody.

        高防实例ip列表。多个高防实例ip必须属于同一企业项目。

        :param vips: The vips of this HostBody.
        :type vips: list[str]
        """
        self._vips = vips

    @property
    def real_server_type(self):
        """Gets the real_server_type of this HostBody.

        源站类型。 0 - 源站IP， 1 - 源站域名。

        :return: The real_server_type of this HostBody.
        :rtype: int
        """
        return self._real_server_type

    @real_server_type.setter
    def real_server_type(self, real_server_type):
        """Sets the real_server_type of this HostBody.

        源站类型。 0 - 源站IP， 1 - 源站域名。

        :param real_server_type: The real_server_type of this HostBody.
        :type real_server_type: int
        """
        self._real_server_type = real_server_type

    @property
    def port_http(self):
        """Gets the port_http of this HostBody.

        HTTP端口，与port_https不能同时为空。DDoS高防支持的HTTP端口可在控制台查看。

        :return: The port_http of this HostBody.
        :rtype: list[int]
        """
        return self._port_http

    @port_http.setter
    def port_http(self, port_http):
        """Sets the port_http of this HostBody.

        HTTP端口，与port_https不能同时为空。DDoS高防支持的HTTP端口可在控制台查看。

        :param port_http: The port_http of this HostBody.
        :type port_http: list[int]
        """
        self._port_http = port_http

    @property
    def port_https(self):
        """Gets the port_https of this HostBody.

        HTTPS端口，与port_http不能同时为空。DDoS高防支持的HTTPS端口可在控制台查看。

        :return: The port_https of this HostBody.
        :rtype: list[int]
        """
        return self._port_https

    @port_https.setter
    def port_https(self, port_https):
        """Sets the port_https of this HostBody.

        HTTPS端口，与port_http不能同时为空。DDoS高防支持的HTTPS端口可在控制台查看。

        :param port_https: The port_https of this HostBody.
        :type port_https: list[int]
        """
        self._port_https = port_https

    @property
    def real_server(self):
        """Gets the real_server of this HostBody.

        源站ip/源站域名

        :return: The real_server of this HostBody.
        :rtype: str
        """
        return self._real_server

    @real_server.setter
    def real_server(self, real_server):
        """Sets the real_server of this HostBody.

        源站ip/源站域名

        :param real_server: The real_server of this HostBody.
        :type real_server: str
        """
        self._real_server = real_server

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
        if not isinstance(other, HostBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
