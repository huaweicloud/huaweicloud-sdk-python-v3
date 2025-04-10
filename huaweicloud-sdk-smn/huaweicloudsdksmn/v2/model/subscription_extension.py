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
        'sign_secret': 'str',
        'header': 'dict(str, str)',
        'app_key': 'str',
        'app_secret': 'str',
        'robot_code': 'str'
    }

    attribute_map = {
        'client_id': 'client_id',
        'client_secret': 'client_secret',
        'keyword': 'keyword',
        'sign_secret': 'sign_secret',
        'header': 'header',
        'app_key': 'app_key',
        'app_secret': 'app_secret',
        'robot_code': 'robot_code'
    }

    def __init__(self, client_id=None, client_secret=None, keyword=None, sign_secret=None, header=None, app_key=None, app_secret=None, robot_code=None):
        r"""SubscriptionExtension

        The model defined in huaweicloud sdk

        :param client_id: 这是应用ID字段。当protocol值为welink时，该字段为必填字段，从welink方获取。
        :type client_id: str
        :param client_secret: 该字段为应用secret字段。当protocol值为welink时，该字段为必填字段，从welink方获取。
        :type client_secret: str
        :param keyword: 该字段为关键字字段。当protocol值为feishu时，这里的keyword字段和sign_secret字段二者必选其一。当用户在飞书或钉钉自定义机器人端添加关键字校验的安全策略时，这里的关键字必须是飞书或钉钉自定义机器人中所填写的关键字之一。
        :type keyword: str
        :param sign_secret: 这是加签密钥字段。当protocol协议为feishu时，这个字段和keyword字段二者必选且只能选其一。密钥配置必须与客户在飞书或钉钉自定义机器人的密钥配置完全一致。例如，如果在飞书端配置了密钥并且没有配置关键字，则在此处填入从飞书获取的密钥字段，如果在飞书端没有配置密钥并且配置了关键字，则不填写该字段。
        :type sign_secret: str
        :param header: 该字段为http header字段，用户可以在字段限制范围内自定义http header，header字段内容以KV对形式存在。当使用主题发送时，已确认的订阅发送消息会携带用户自定义的http header。 header应满足如下要求： key值限定为：包含英文字母([A-Za-z])、数字([0-9])、中划线(-)hyphens，中划线不得作为结尾，不得连续出现。 K/V不得超过10个 key需要以\&quot;x-\&quot;开头，不能以\&quot;x-smn\&quot;开头，正确示例：x-abc-cba, x-abc 所有K/V长度总和不得超过1024个字符 key不区分大小写 key值不可重复 value值限定为ASCII码，不支持中文或其他Unicode，支持空格
        :type header: dict(str, str)
        :param app_key: 个人钉钉appKey字段，字符长度限制64个，仅支持字母、数字、中划线(-)、下划线(_)。当订阅协议为dingTalkBot时，该字段必选。
        :type app_key: str
        :param app_secret: 个人钉钉appSecret字段，字符长度限制128个，仅支持字母、数字、中划线(-)、下划线(_)。当订阅协议为dingTalkBot时，该字段必选。
        :type app_secret: str
        :param robot_code: 个人钉钉robotCode字段，名称：机器人编码，字符长度限制64个，仅支持字母、数字、中划线(-)、下划线(_)，一般与appKey一致。当订阅协议为dingTalkBot时，该字段必选。
        :type robot_code: str
        """
        
        

        self._client_id = None
        self._client_secret = None
        self._keyword = None
        self._sign_secret = None
        self._header = None
        self._app_key = None
        self._app_secret = None
        self._robot_code = None
        self.discriminator = None

        if client_id is not None:
            self.client_id = client_id
        if client_secret is not None:
            self.client_secret = client_secret
        if keyword is not None:
            self.keyword = keyword
        if sign_secret is not None:
            self.sign_secret = sign_secret
        if header is not None:
            self.header = header
        if app_key is not None:
            self.app_key = app_key
        if app_secret is not None:
            self.app_secret = app_secret
        if robot_code is not None:
            self.robot_code = robot_code

    @property
    def client_id(self):
        r"""Gets the client_id of this SubscriptionExtension.

        这是应用ID字段。当protocol值为welink时，该字段为必填字段，从welink方获取。

        :return: The client_id of this SubscriptionExtension.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        r"""Sets the client_id of this SubscriptionExtension.

        这是应用ID字段。当protocol值为welink时，该字段为必填字段，从welink方获取。

        :param client_id: The client_id of this SubscriptionExtension.
        :type client_id: str
        """
        self._client_id = client_id

    @property
    def client_secret(self):
        r"""Gets the client_secret of this SubscriptionExtension.

        该字段为应用secret字段。当protocol值为welink时，该字段为必填字段，从welink方获取。

        :return: The client_secret of this SubscriptionExtension.
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        r"""Sets the client_secret of this SubscriptionExtension.

        该字段为应用secret字段。当protocol值为welink时，该字段为必填字段，从welink方获取。

        :param client_secret: The client_secret of this SubscriptionExtension.
        :type client_secret: str
        """
        self._client_secret = client_secret

    @property
    def keyword(self):
        r"""Gets the keyword of this SubscriptionExtension.

        该字段为关键字字段。当protocol值为feishu时，这里的keyword字段和sign_secret字段二者必选其一。当用户在飞书或钉钉自定义机器人端添加关键字校验的安全策略时，这里的关键字必须是飞书或钉钉自定义机器人中所填写的关键字之一。

        :return: The keyword of this SubscriptionExtension.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        r"""Sets the keyword of this SubscriptionExtension.

        该字段为关键字字段。当protocol值为feishu时，这里的keyword字段和sign_secret字段二者必选其一。当用户在飞书或钉钉自定义机器人端添加关键字校验的安全策略时，这里的关键字必须是飞书或钉钉自定义机器人中所填写的关键字之一。

        :param keyword: The keyword of this SubscriptionExtension.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def sign_secret(self):
        r"""Gets the sign_secret of this SubscriptionExtension.

        这是加签密钥字段。当protocol协议为feishu时，这个字段和keyword字段二者必选且只能选其一。密钥配置必须与客户在飞书或钉钉自定义机器人的密钥配置完全一致。例如，如果在飞书端配置了密钥并且没有配置关键字，则在此处填入从飞书获取的密钥字段，如果在飞书端没有配置密钥并且配置了关键字，则不填写该字段。

        :return: The sign_secret of this SubscriptionExtension.
        :rtype: str
        """
        return self._sign_secret

    @sign_secret.setter
    def sign_secret(self, sign_secret):
        r"""Sets the sign_secret of this SubscriptionExtension.

        这是加签密钥字段。当protocol协议为feishu时，这个字段和keyword字段二者必选且只能选其一。密钥配置必须与客户在飞书或钉钉自定义机器人的密钥配置完全一致。例如，如果在飞书端配置了密钥并且没有配置关键字，则在此处填入从飞书获取的密钥字段，如果在飞书端没有配置密钥并且配置了关键字，则不填写该字段。

        :param sign_secret: The sign_secret of this SubscriptionExtension.
        :type sign_secret: str
        """
        self._sign_secret = sign_secret

    @property
    def header(self):
        r"""Gets the header of this SubscriptionExtension.

        该字段为http header字段，用户可以在字段限制范围内自定义http header，header字段内容以KV对形式存在。当使用主题发送时，已确认的订阅发送消息会携带用户自定义的http header。 header应满足如下要求： key值限定为：包含英文字母([A-Za-z])、数字([0-9])、中划线(-)hyphens，中划线不得作为结尾，不得连续出现。 K/V不得超过10个 key需要以\"x-\"开头，不能以\"x-smn\"开头，正确示例：x-abc-cba, x-abc 所有K/V长度总和不得超过1024个字符 key不区分大小写 key值不可重复 value值限定为ASCII码，不支持中文或其他Unicode，支持空格

        :return: The header of this SubscriptionExtension.
        :rtype: dict(str, str)
        """
        return self._header

    @header.setter
    def header(self, header):
        r"""Sets the header of this SubscriptionExtension.

        该字段为http header字段，用户可以在字段限制范围内自定义http header，header字段内容以KV对形式存在。当使用主题发送时，已确认的订阅发送消息会携带用户自定义的http header。 header应满足如下要求： key值限定为：包含英文字母([A-Za-z])、数字([0-9])、中划线(-)hyphens，中划线不得作为结尾，不得连续出现。 K/V不得超过10个 key需要以\"x-\"开头，不能以\"x-smn\"开头，正确示例：x-abc-cba, x-abc 所有K/V长度总和不得超过1024个字符 key不区分大小写 key值不可重复 value值限定为ASCII码，不支持中文或其他Unicode，支持空格

        :param header: The header of this SubscriptionExtension.
        :type header: dict(str, str)
        """
        self._header = header

    @property
    def app_key(self):
        r"""Gets the app_key of this SubscriptionExtension.

        个人钉钉appKey字段，字符长度限制64个，仅支持字母、数字、中划线(-)、下划线(_)。当订阅协议为dingTalkBot时，该字段必选。

        :return: The app_key of this SubscriptionExtension.
        :rtype: str
        """
        return self._app_key

    @app_key.setter
    def app_key(self, app_key):
        r"""Sets the app_key of this SubscriptionExtension.

        个人钉钉appKey字段，字符长度限制64个，仅支持字母、数字、中划线(-)、下划线(_)。当订阅协议为dingTalkBot时，该字段必选。

        :param app_key: The app_key of this SubscriptionExtension.
        :type app_key: str
        """
        self._app_key = app_key

    @property
    def app_secret(self):
        r"""Gets the app_secret of this SubscriptionExtension.

        个人钉钉appSecret字段，字符长度限制128个，仅支持字母、数字、中划线(-)、下划线(_)。当订阅协议为dingTalkBot时，该字段必选。

        :return: The app_secret of this SubscriptionExtension.
        :rtype: str
        """
        return self._app_secret

    @app_secret.setter
    def app_secret(self, app_secret):
        r"""Sets the app_secret of this SubscriptionExtension.

        个人钉钉appSecret字段，字符长度限制128个，仅支持字母、数字、中划线(-)、下划线(_)。当订阅协议为dingTalkBot时，该字段必选。

        :param app_secret: The app_secret of this SubscriptionExtension.
        :type app_secret: str
        """
        self._app_secret = app_secret

    @property
    def robot_code(self):
        r"""Gets the robot_code of this SubscriptionExtension.

        个人钉钉robotCode字段，名称：机器人编码，字符长度限制64个，仅支持字母、数字、中划线(-)、下划线(_)，一般与appKey一致。当订阅协议为dingTalkBot时，该字段必选。

        :return: The robot_code of this SubscriptionExtension.
        :rtype: str
        """
        return self._robot_code

    @robot_code.setter
    def robot_code(self, robot_code):
        r"""Sets the robot_code of this SubscriptionExtension.

        个人钉钉robotCode字段，名称：机器人编码，字符长度限制64个，仅支持字母、数字、中划线(-)、下划线(_)，一般与appKey一致。当订阅协议为dingTalkBot时，该字段必选。

        :param robot_code: The robot_code of this SubscriptionExtension.
        :type robot_code: str
        """
        self._robot_code = robot_code

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
