# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Sni:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'server_name': 'str'
    }

    attribute_map = {
        'status': 'status',
        'server_name': 'server_name'
    }

    def __init__(self, status=None, server_name=None):
        """Sni

        The model defined in huaweicloud sdk

        :param status: 是否开启回源SNI，on：打开，off：关闭。
        :type status: str
        :param server_name: CDN节点回源需要访问的源站域名。如test.example.com。   &gt; 1. 开启回源SNI时必填。   &gt; 2. 不支持泛域名，仅支持输入数字、“-”、“.”、英文大小写字符。
        :type server_name: str
        """
        
        

        self._status = None
        self._server_name = None
        self.discriminator = None

        self.status = status
        if server_name is not None:
            self.server_name = server_name

    @property
    def status(self):
        """Gets the status of this Sni.

        是否开启回源SNI，on：打开，off：关闭。

        :return: The status of this Sni.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Sni.

        是否开启回源SNI，on：打开，off：关闭。

        :param status: The status of this Sni.
        :type status: str
        """
        self._status = status

    @property
    def server_name(self):
        """Gets the server_name of this Sni.

        CDN节点回源需要访问的源站域名。如test.example.com。   > 1. 开启回源SNI时必填。   > 2. 不支持泛域名，仅支持输入数字、“-”、“.”、英文大小写字符。

        :return: The server_name of this Sni.
        :rtype: str
        """
        return self._server_name

    @server_name.setter
    def server_name(self, server_name):
        """Sets the server_name of this Sni.

        CDN节点回源需要访问的源站域名。如test.example.com。   > 1. 开启回源SNI时必填。   > 2. 不支持泛域名，仅支持输入数字、“-”、“.”、英文大小写字符。

        :param server_name: The server_name of this Sni.
        :type server_name: str
        """
        self._server_name = server_name

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
        if not isinstance(other, Sni):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
