# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server': 'list[ResponseServer]',
        'total': 'int'
    }

    attribute_map = {
        'server': 'server',
        'total': 'total'
    }

    def __init__(self, server=None, total=None):
        r"""ServerList

        The model defined in huaweicloud sdk

        :param server: server列表
        :type server: list[:class:`huaweicloudsdkdbss.v1.ResponseServer`]
        :param total: 数量
        :type total: int
        """
        
        

        self._server = None
        self._total = None
        self.discriminator = None

        if server is not None:
            self.server = server
        if total is not None:
            self.total = total

    @property
    def server(self):
        r"""Gets the server of this ServerList.

        server列表

        :return: The server of this ServerList.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.ResponseServer`]
        """
        return self._server

    @server.setter
    def server(self, server):
        r"""Sets the server of this ServerList.

        server列表

        :param server: The server of this ServerList.
        :type server: list[:class:`huaweicloudsdkdbss.v1.ResponseServer`]
        """
        self._server = server

    @property
    def total(self):
        r"""Gets the total of this ServerList.

        数量

        :return: The total of this ServerList.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ServerList.

        数量

        :param total: The total of this ServerList.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ServerList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
