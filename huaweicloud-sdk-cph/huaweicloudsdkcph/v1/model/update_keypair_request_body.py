# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateKeypairRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'servers': 'list[ServerKeypair]'
    }

    attribute_map = {
        'servers': 'servers'
    }

    def __init__(self, servers=None):
        r"""UpdateKeypairRequestBody

        The model defined in huaweicloud sdk

        :param servers: 待更改密钥对的云手机服务器信息。
        :type servers: list[:class:`huaweicloudsdkcph.v1.ServerKeypair`]
        """
        
        

        self._servers = None
        self.discriminator = None

        self.servers = servers

    @property
    def servers(self):
        r"""Gets the servers of this UpdateKeypairRequestBody.

        待更改密钥对的云手机服务器信息。

        :return: The servers of this UpdateKeypairRequestBody.
        :rtype: list[:class:`huaweicloudsdkcph.v1.ServerKeypair`]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        r"""Sets the servers of this UpdateKeypairRequestBody.

        待更改密钥对的云手机服务器信息。

        :param servers: The servers of this UpdateKeypairRequestBody.
        :type servers: list[:class:`huaweicloudsdkcph.v1.ServerKeypair`]
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
        if not isinstance(other, UpdateKeypairRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
