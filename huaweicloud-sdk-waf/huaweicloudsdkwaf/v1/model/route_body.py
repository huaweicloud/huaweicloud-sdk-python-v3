# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RouteBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cname': 'str',
        'name': 'str',
        'servers': 'list[RouteServerBody]'
    }

    attribute_map = {
        'cname': 'cname',
        'name': 'name',
        'servers': 'servers'
    }

    def __init__(self, cname=None, name=None, servers=None):
        """RouteBody

        The model defined in huaweicloud sdk

        :param cname: WAF集群的cname后缀
        :type cname: str
        :param name: WAF集群名称
        :type name: str
        :param servers: 防护域名源站服务器信息列表
        :type servers: list[:class:`huaweicloudsdkwaf.v1.RouteServerBody`]
        """
        
        

        self._cname = None
        self._name = None
        self._servers = None
        self.discriminator = None

        if cname is not None:
            self.cname = cname
        if name is not None:
            self.name = name
        if servers is not None:
            self.servers = servers

    @property
    def cname(self):
        """Gets the cname of this RouteBody.

        WAF集群的cname后缀

        :return: The cname of this RouteBody.
        :rtype: str
        """
        return self._cname

    @cname.setter
    def cname(self, cname):
        """Sets the cname of this RouteBody.

        WAF集群的cname后缀

        :param cname: The cname of this RouteBody.
        :type cname: str
        """
        self._cname = cname

    @property
    def name(self):
        """Gets the name of this RouteBody.

        WAF集群名称

        :return: The name of this RouteBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RouteBody.

        WAF集群名称

        :param name: The name of this RouteBody.
        :type name: str
        """
        self._name = name

    @property
    def servers(self):
        """Gets the servers of this RouteBody.

        防护域名源站服务器信息列表

        :return: The servers of this RouteBody.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.RouteServerBody`]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """Sets the servers of this RouteBody.

        防护域名源站服务器信息列表

        :param servers: The servers of this RouteBody.
        :type servers: list[:class:`huaweicloudsdkwaf.v1.RouteServerBody`]
        """
        self._servers = servers

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
        if not isinstance(other, RouteBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
