# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubscriptionExtension:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'client_id': 'str',
        'client_secret': 'str',
        'keyword': 'str',
        'sign_secret': 'str'
    }

    attribute_map = {
        'client_id': 'client_id',
        'client_secret': 'client_secret',
        'keyword': 'keyword',
        'sign_secret': 'sign_secret'
    }

    def __init__(self, client_id=None, client_secret=None, keyword=None, sign_secret=None):
        """SubscriptionExtension

        The model defined in huaweicloud sdk

        :param client_id: 该字段为welink订阅下的租户ID字段，由租户从welink方获取。当protocol值为welink时，该字段为必填字段。
        :type client_id: str
        :param client_secret: 该字段为welink订阅下的租户获取的client secret字段，由租户从welink方获取。当protocol值为welink时，该字段为必填字段。
        :type client_secret: str
        :param keyword: 该字段为关键字字段。当protocol协议为feishu时，这里的keyword字段和sign_secret字段二者必选其一。当用户在飞书或钉钉机器人端添加关键字校验的安全策略时，这里的关键字必须是飞书或钉钉端所填写的关键字之一。
        :type keyword: str
        :param sign_secret: 这是加签密钥字段。当protocol协议为feishu或dingding时，这个字段和keyword字段二者必选且只能选其一，密钥配置必须与客户在飞书或钉钉客户端的密钥配置完全一致。例如，如果在飞书端配置了密钥并且没有配置关键字，则在此处填入从飞书获取的密钥字段，如果在飞书端没有配置密钥并且配置了关键字，则不填写该字段。
        :type sign_secret: str
        """
        
        

        self._client_id = None
        self._client_secret = None
        self._keyword = None
        self._sign_secret = None
        self.discriminator = None

        if client_id is not None:
            self.client_id = client_id
        if client_secret is not None:
            self.client_secret = client_secret
        if keyword is not None:
            self.keyword = keyword
        if sign_secret is not None:
            self.sign_secret = sign_secret

    @property
    def client_id(self):
        """Gets the client_id of this SubscriptionExtension.

        该字段为welink订阅下的租户ID字段，由租户从welink方获取。当protocol值为welink时，该字段为必填字段。

        :return: The client_id of this SubscriptionExtension.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this SubscriptionExtension.

        该字段为welink订阅下的租户ID字段，由租户从welink方获取。当protocol值为welink时，该字段为必填字段。

        :param client_id: The client_id of this SubscriptionExtension.
        :type client_id: str
        """
        self._client_id = client_id

    @property
    def client_secret(self):
        """Gets the client_secret of this SubscriptionExtension.

        该字段为welink订阅下的租户获取的client secret字段，由租户从welink方获取。当protocol值为welink时，该字段为必填字段。

        :return: The client_secret of this SubscriptionExtension.
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """Sets the client_secret of this SubscriptionExtension.

        该字段为welink订阅下的租户获取的client secret字段，由租户从welink方获取。当protocol值为welink时，该字段为必填字段。

        :param client_secret: The client_secret of this SubscriptionExtension.
        :type client_secret: str
        """
        self._client_secret = client_secret

    @property
    def keyword(self):
        """Gets the keyword of this SubscriptionExtension.

        该字段为关键字字段。当protocol协议为feishu时，这里的keyword字段和sign_secret字段二者必选其一。当用户在飞书或钉钉机器人端添加关键字校验的安全策略时，这里的关键字必须是飞书或钉钉端所填写的关键字之一。

        :return: The keyword of this SubscriptionExtension.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        """Sets the keyword of this SubscriptionExtension.

        该字段为关键字字段。当protocol协议为feishu时，这里的keyword字段和sign_secret字段二者必选其一。当用户在飞书或钉钉机器人端添加关键字校验的安全策略时，这里的关键字必须是飞书或钉钉端所填写的关键字之一。

        :param keyword: The keyword of this SubscriptionExtension.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def sign_secret(self):
        """Gets the sign_secret of this SubscriptionExtension.

        这是加签密钥字段。当protocol协议为feishu或dingding时，这个字段和keyword字段二者必选且只能选其一，密钥配置必须与客户在飞书或钉钉客户端的密钥配置完全一致。例如，如果在飞书端配置了密钥并且没有配置关键字，则在此处填入从飞书获取的密钥字段，如果在飞书端没有配置密钥并且配置了关键字，则不填写该字段。

        :return: The sign_secret of this SubscriptionExtension.
        :rtype: str
        """
        return self._sign_secret

    @sign_secret.setter
    def sign_secret(self, sign_secret):
        """Sets the sign_secret of this SubscriptionExtension.

        这是加签密钥字段。当protocol协议为feishu或dingding时，这个字段和keyword字段二者必选且只能选其一，密钥配置必须与客户在飞书或钉钉客户端的密钥配置完全一致。例如，如果在飞书端配置了密钥并且没有配置关键字，则在此处填入从飞书获取的密钥字段，如果在飞书端没有配置密钥并且配置了关键字，则不填写该字段。

        :param sign_secret: The sign_secret of this SubscriptionExtension.
        :type sign_secret: str
        """
        self._sign_secret = sign_secret

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
        if not isinstance(other, SubscriptionExtension):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
