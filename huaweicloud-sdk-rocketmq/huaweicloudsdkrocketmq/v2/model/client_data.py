# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClientData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'language': 'str',
        'version': 'str',
        'client_id': 'str',
        'client_addr': 'str',
        'subscriptions': 'list[Subscription]'
    }

    attribute_map = {
        'language': 'language',
        'version': 'version',
        'client_id': 'client_id',
        'client_addr': 'client_addr',
        'subscriptions': 'subscriptions'
    }

    def __init__(self, language=None, version=None, client_id=None, client_addr=None, subscriptions=None):
        r"""ClientData

        The model defined in huaweicloud sdk

        :param language: 客户端语言。
        :type language: str
        :param version: 客户端版本。
        :type version: str
        :param client_id: 客户端ID。
        :type client_id: str
        :param client_addr: 客户端地址。
        :type client_addr: str
        :param subscriptions: 订阅关系列表。
        :type subscriptions: list[:class:`huaweicloudsdkrocketmq.v2.Subscription`]
        """
        
        

        self._language = None
        self._version = None
        self._client_id = None
        self._client_addr = None
        self._subscriptions = None
        self.discriminator = None

        if language is not None:
            self.language = language
        if version is not None:
            self.version = version
        if client_id is not None:
            self.client_id = client_id
        if client_addr is not None:
            self.client_addr = client_addr
        if subscriptions is not None:
            self.subscriptions = subscriptions

    @property
    def language(self):
        r"""Gets the language of this ClientData.

        客户端语言。

        :return: The language of this ClientData.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this ClientData.

        客户端语言。

        :param language: The language of this ClientData.
        :type language: str
        """
        self._language = language

    @property
    def version(self):
        r"""Gets the version of this ClientData.

        客户端版本。

        :return: The version of this ClientData.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ClientData.

        客户端版本。

        :param version: The version of this ClientData.
        :type version: str
        """
        self._version = version

    @property
    def client_id(self):
        r"""Gets the client_id of this ClientData.

        客户端ID。

        :return: The client_id of this ClientData.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        r"""Sets the client_id of this ClientData.

        客户端ID。

        :param client_id: The client_id of this ClientData.
        :type client_id: str
        """
        self._client_id = client_id

    @property
    def client_addr(self):
        r"""Gets the client_addr of this ClientData.

        客户端地址。

        :return: The client_addr of this ClientData.
        :rtype: str
        """
        return self._client_addr

    @client_addr.setter
    def client_addr(self, client_addr):
        r"""Sets the client_addr of this ClientData.

        客户端地址。

        :param client_addr: The client_addr of this ClientData.
        :type client_addr: str
        """
        self._client_addr = client_addr

    @property
    def subscriptions(self):
        r"""Gets the subscriptions of this ClientData.

        订阅关系列表。

        :return: The subscriptions of this ClientData.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.Subscription`]
        """
        return self._subscriptions

    @subscriptions.setter
    def subscriptions(self, subscriptions):
        r"""Sets the subscriptions of this ClientData.

        订阅关系列表。

        :param subscriptions: The subscriptions of this ClientData.
        :type subscriptions: list[:class:`huaweicloudsdkrocketmq.v2.Subscription`]
        """
        self._subscriptions = subscriptions

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
        if not isinstance(other, ClientData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
