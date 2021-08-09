# coding: utf-8

import re
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
        'name': 'str',
        'servers': 'list[RouteServerBody]'
    }

    attribute_map = {
        'name': 'name',
        'servers': 'servers'
    }

    def __init__(self, name=None, servers=None):
        """RouteBody - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._servers = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if servers is not None:
            self.servers = servers

    @property
    def name(self):
        """Gets the name of this RouteBody.

        名称

        :return: The name of this RouteBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RouteBody.

        名称

        :param name: The name of this RouteBody.
        :type: str
        """
        self._name = name

    @property
    def servers(self):
        """Gets the servers of this RouteBody.

        路由信息

        :return: The servers of this RouteBody.
        :rtype: list[RouteServerBody]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """Sets the servers of this RouteBody.

        路由信息

        :param servers: The servers of this RouteBody.
        :type: list[RouteServerBody]
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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RouteBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other