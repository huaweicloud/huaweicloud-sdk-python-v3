# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSubscriptionUserRequestDingdingEndpointInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'endpoint': 'str',
        'keyword': 'str',
        'sign_secret': 'str'
    }

    attribute_map = {
        'endpoint': 'endpoint',
        'keyword': 'keyword',
        'sign_secret': 'sign_secret'
    }

    def __init__(self, endpoint=None, keyword=None, sign_secret=None):
        r"""CreateSubscriptionUserRequestDingdingEndpointInfo

        The model defined in huaweicloud sdk

        :param endpoint: 终端地址。必须是一个钉钉群机器人的地址。
        :type endpoint: str
        :param keyword: dingding协议订阅用户的关键字。dingding协议订阅用户必须指定keyword和sign_secret二者之一。当用户在钉钉机器人端添加关键字校验的安全策略时，这里的关键字必须是钉钉端所填写的关键字之一。
        :type keyword: str
        :param sign_secret: dingding协议订阅用户的加签密钥字段。dingding协议订阅用户必须指定keyword和sign_secret二者之一。当用户在钉钉机器人端添加关键字校验的安全策略时，这里的关键字必须是钉钉端所填写的关键字之一。
        :type sign_secret: str
        """
        
        

        self._endpoint = None
        self._keyword = None
        self._sign_secret = None
        self.discriminator = None

        self.endpoint = endpoint
        if keyword is not None:
            self.keyword = keyword
        if sign_secret is not None:
            self.sign_secret = sign_secret

    @property
    def endpoint(self):
        r"""Gets the endpoint of this CreateSubscriptionUserRequestDingdingEndpointInfo.

        终端地址。必须是一个钉钉群机器人的地址。

        :return: The endpoint of this CreateSubscriptionUserRequestDingdingEndpointInfo.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        r"""Sets the endpoint of this CreateSubscriptionUserRequestDingdingEndpointInfo.

        终端地址。必须是一个钉钉群机器人的地址。

        :param endpoint: The endpoint of this CreateSubscriptionUserRequestDingdingEndpointInfo.
        :type endpoint: str
        """
        self._endpoint = endpoint

    @property
    def keyword(self):
        r"""Gets the keyword of this CreateSubscriptionUserRequestDingdingEndpointInfo.

        dingding协议订阅用户的关键字。dingding协议订阅用户必须指定keyword和sign_secret二者之一。当用户在钉钉机器人端添加关键字校验的安全策略时，这里的关键字必须是钉钉端所填写的关键字之一。

        :return: The keyword of this CreateSubscriptionUserRequestDingdingEndpointInfo.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        r"""Sets the keyword of this CreateSubscriptionUserRequestDingdingEndpointInfo.

        dingding协议订阅用户的关键字。dingding协议订阅用户必须指定keyword和sign_secret二者之一。当用户在钉钉机器人端添加关键字校验的安全策略时，这里的关键字必须是钉钉端所填写的关键字之一。

        :param keyword: The keyword of this CreateSubscriptionUserRequestDingdingEndpointInfo.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def sign_secret(self):
        r"""Gets the sign_secret of this CreateSubscriptionUserRequestDingdingEndpointInfo.

        dingding协议订阅用户的加签密钥字段。dingding协议订阅用户必须指定keyword和sign_secret二者之一。当用户在钉钉机器人端添加关键字校验的安全策略时，这里的关键字必须是钉钉端所填写的关键字之一。

        :return: The sign_secret of this CreateSubscriptionUserRequestDingdingEndpointInfo.
        :rtype: str
        """
        return self._sign_secret

    @sign_secret.setter
    def sign_secret(self, sign_secret):
        r"""Sets the sign_secret of this CreateSubscriptionUserRequestDingdingEndpointInfo.

        dingding协议订阅用户的加签密钥字段。dingding协议订阅用户必须指定keyword和sign_secret二者之一。当用户在钉钉机器人端添加关键字校验的安全策略时，这里的关键字必须是钉钉端所填写的关键字之一。

        :param sign_secret: The sign_secret of this CreateSubscriptionUserRequestDingdingEndpointInfo.
        :type sign_secret: str
        """
        self._sign_secret = sign_secret

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateSubscriptionUserRequestDingdingEndpointInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
