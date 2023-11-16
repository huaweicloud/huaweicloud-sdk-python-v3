# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DomainInfo:

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
        'domain_name': 'str',
        'cname': 'str',
        'protocol': 'list[str]',
        'real_server_type': 'int',
        'real_servers': 'str',
        'waf_status': 'int',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'domain_name': 'domain_name',
        'cname': 'cname',
        'protocol': 'protocol',
        'real_server_type': 'real_server_type',
        'real_servers': 'real_servers',
        'waf_status': 'waf_status',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, domain_id=None, domain_name=None, cname=None, protocol=None, real_server_type=None, real_servers=None, waf_status=None, enterprise_project_id=None):
        """DomainInfo

        The model defined in huaweicloud sdk

        :param domain_id: 域名ID
        :type domain_id: str
        :param domain_name: 域名
        :type domain_name: str
        :param cname: 域名cname
        :type cname: str
        :param protocol: 域名协议
        :type protocol: list[str]
        :param real_server_type: 源站类型
        :type real_server_type: int
        :param real_servers: 源站
        :type real_servers: str
        :param waf_status: waf防护状态
        :type waf_status: int
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        """
        
        

        self._domain_id = None
        self._domain_name = None
        self._cname = None
        self._protocol = None
        self._real_server_type = None
        self._real_servers = None
        self._waf_status = None
        self._enterprise_project_id = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if domain_name is not None:
            self.domain_name = domain_name
        if cname is not None:
            self.cname = cname
        if protocol is not None:
            self.protocol = protocol
        if real_server_type is not None:
            self.real_server_type = real_server_type
        if real_servers is not None:
            self.real_servers = real_servers
        if waf_status is not None:
            self.waf_status = waf_status
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def domain_id(self):
        """Gets the domain_id of this DomainInfo.

        域名ID

        :return: The domain_id of this DomainInfo.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this DomainInfo.

        域名ID

        :param domain_id: The domain_id of this DomainInfo.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def domain_name(self):
        """Gets the domain_name of this DomainInfo.

        域名

        :return: The domain_name of this DomainInfo.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this DomainInfo.

        域名

        :param domain_name: The domain_name of this DomainInfo.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def cname(self):
        """Gets the cname of this DomainInfo.

        域名cname

        :return: The cname of this DomainInfo.
        :rtype: str
        """
        return self._cname

    @cname.setter
    def cname(self, cname):
        """Sets the cname of this DomainInfo.

        域名cname

        :param cname: The cname of this DomainInfo.
        :type cname: str
        """
        self._cname = cname

    @property
    def protocol(self):
        """Gets the protocol of this DomainInfo.

        域名协议

        :return: The protocol of this DomainInfo.
        :rtype: list[str]
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this DomainInfo.

        域名协议

        :param protocol: The protocol of this DomainInfo.
        :type protocol: list[str]
        """
        self._protocol = protocol

    @property
    def real_server_type(self):
        """Gets the real_server_type of this DomainInfo.

        源站类型

        :return: The real_server_type of this DomainInfo.
        :rtype: int
        """
        return self._real_server_type

    @real_server_type.setter
    def real_server_type(self, real_server_type):
        """Sets the real_server_type of this DomainInfo.

        源站类型

        :param real_server_type: The real_server_type of this DomainInfo.
        :type real_server_type: int
        """
        self._real_server_type = real_server_type

    @property
    def real_servers(self):
        """Gets the real_servers of this DomainInfo.

        源站

        :return: The real_servers of this DomainInfo.
        :rtype: str
        """
        return self._real_servers

    @real_servers.setter
    def real_servers(self, real_servers):
        """Sets the real_servers of this DomainInfo.

        源站

        :param real_servers: The real_servers of this DomainInfo.
        :type real_servers: str
        """
        self._real_servers = real_servers

    @property
    def waf_status(self):
        """Gets the waf_status of this DomainInfo.

        waf防护状态

        :return: The waf_status of this DomainInfo.
        :rtype: int
        """
        return self._waf_status

    @waf_status.setter
    def waf_status(self, waf_status):
        """Sets the waf_status of this DomainInfo.

        waf防护状态

        :param waf_status: The waf_status of this DomainInfo.
        :type waf_status: int
        """
        self._waf_status = waf_status

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this DomainInfo.

        企业项目ID

        :return: The enterprise_project_id of this DomainInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this DomainInfo.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this DomainInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, DomainInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
