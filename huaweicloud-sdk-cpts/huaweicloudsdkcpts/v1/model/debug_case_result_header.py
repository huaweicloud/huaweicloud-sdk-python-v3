# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DebugCaseResultHeader:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connection': 'str',
        'content_type': 'str',
        'host': 'str'
    }

    attribute_map = {
        'connection': 'Connection',
        'content_type': 'Content-Type',
        'host': 'Host'
    }

    def __init__(self, connection=None, content_type=None, host=None):
        r"""DebugCaseResultHeader

        The model defined in huaweicloud sdk

        :param connection: 连接
        :type connection: str
        :param content_type: 内容类型
        :type content_type: str
        :param host: 主机
        :type host: str
        """
        
        

        self._connection = None
        self._content_type = None
        self._host = None
        self.discriminator = None

        if connection is not None:
            self.connection = connection
        if content_type is not None:
            self.content_type = content_type
        if host is not None:
            self.host = host

    @property
    def connection(self):
        r"""Gets the connection of this DebugCaseResultHeader.

        连接

        :return: The connection of this DebugCaseResultHeader.
        :rtype: str
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        r"""Sets the connection of this DebugCaseResultHeader.

        连接

        :param connection: The connection of this DebugCaseResultHeader.
        :type connection: str
        """
        self._connection = connection

    @property
    def content_type(self):
        r"""Gets the content_type of this DebugCaseResultHeader.

        内容类型

        :return: The content_type of this DebugCaseResultHeader.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        r"""Sets the content_type of this DebugCaseResultHeader.

        内容类型

        :param content_type: The content_type of this DebugCaseResultHeader.
        :type content_type: str
        """
        self._content_type = content_type

    @property
    def host(self):
        r"""Gets the host of this DebugCaseResultHeader.

        主机

        :return: The host of this DebugCaseResultHeader.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this DebugCaseResultHeader.

        主机

        :param host: The host of this DebugCaseResultHeader.
        :type host: str
        """
        self._host = host

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
        if not isinstance(other, DebugCaseResultHeader):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
