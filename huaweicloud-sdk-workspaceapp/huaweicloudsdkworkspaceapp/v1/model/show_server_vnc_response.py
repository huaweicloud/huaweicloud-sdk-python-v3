# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowServerVncResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'url': 'str',
        'protocol': 'str'
    }

    attribute_map = {
        'type': 'type',
        'url': 'url',
        'protocol': 'protocol'
    }

    def __init__(self, type=None, url=None, protocol=None):
        r"""ShowServerVncResponse

        The model defined in huaweicloud sdk

        :param type: 登录类型: * &#x60;novnc&#x60; * &#x60;vnc&#x60;
        :type type: str
        :param url: 远程登录控制台地址。
        :type url: str
        :param protocol: 登录协议。
        :type protocol: str
        """
        
        super(ShowServerVncResponse, self).__init__()

        self._type = None
        self._url = None
        self._protocol = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if url is not None:
            self.url = url
        if protocol is not None:
            self.protocol = protocol

    @property
    def type(self):
        r"""Gets the type of this ShowServerVncResponse.

        登录类型: * `novnc` * `vnc`

        :return: The type of this ShowServerVncResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowServerVncResponse.

        登录类型: * `novnc` * `vnc`

        :param type: The type of this ShowServerVncResponse.
        :type type: str
        """
        self._type = type

    @property
    def url(self):
        r"""Gets the url of this ShowServerVncResponse.

        远程登录控制台地址。

        :return: The url of this ShowServerVncResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this ShowServerVncResponse.

        远程登录控制台地址。

        :param url: The url of this ShowServerVncResponse.
        :type url: str
        """
        self._url = url

    @property
    def protocol(self):
        r"""Gets the protocol of this ShowServerVncResponse.

        登录协议。

        :return: The protocol of this ShowServerVncResponse.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this ShowServerVncResponse.

        登录协议。

        :param protocol: The protocol of this ShowServerVncResponse.
        :type protocol: str
        """
        self._protocol = protocol

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
        if not isinstance(other, ShowServerVncResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
