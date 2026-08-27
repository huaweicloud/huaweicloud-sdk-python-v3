# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImChannelConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'platform': 'str',
        'enabled': 'bool',
        'client_id': 'str',
        'client_secret': 'str',
        'platform_specific': 'dict(str, str)'
    }

    attribute_map = {
        'platform': 'platform',
        'enabled': 'enabled',
        'client_id': 'client_id',
        'client_secret': 'client_secret',
        'platform_specific': 'platform_specific'
    }

    def __init__(self, platform=None, enabled=None, client_id=None, client_secret=None, platform_specific=None):
        r"""ImChannelConfig

        The model defined in huaweicloud sdk

        :param platform: IM 平台类型：wecom / feishu / dingtalk-connector
        :type platform: str
        :param enabled: 是否启用
        :type enabled: bool
        :param client_id: 客户端 ID
        :type client_id: str
        :param client_secret: 客户端密钥
        :type client_secret: str
        :param platform_specific: 平台扩展配置
        :type platform_specific: dict(str, str)
        """
        
        

        self._platform = None
        self._enabled = None
        self._client_id = None
        self._client_secret = None
        self._platform_specific = None
        self.discriminator = None

        self.platform = platform
        if enabled is not None:
            self.enabled = enabled
        if client_id is not None:
            self.client_id = client_id
        if client_secret is not None:
            self.client_secret = client_secret
        if platform_specific is not None:
            self.platform_specific = platform_specific

    @property
    def platform(self):
        r"""Gets the platform of this ImChannelConfig.

        IM 平台类型：wecom / feishu / dingtalk-connector

        :return: The platform of this ImChannelConfig.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        r"""Sets the platform of this ImChannelConfig.

        IM 平台类型：wecom / feishu / dingtalk-connector

        :param platform: The platform of this ImChannelConfig.
        :type platform: str
        """
        self._platform = platform

    @property
    def enabled(self):
        r"""Gets the enabled of this ImChannelConfig.

        是否启用

        :return: The enabled of this ImChannelConfig.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this ImChannelConfig.

        是否启用

        :param enabled: The enabled of this ImChannelConfig.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def client_id(self):
        r"""Gets the client_id of this ImChannelConfig.

        客户端 ID

        :return: The client_id of this ImChannelConfig.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        r"""Sets the client_id of this ImChannelConfig.

        客户端 ID

        :param client_id: The client_id of this ImChannelConfig.
        :type client_id: str
        """
        self._client_id = client_id

    @property
    def client_secret(self):
        r"""Gets the client_secret of this ImChannelConfig.

        客户端密钥

        :return: The client_secret of this ImChannelConfig.
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        r"""Sets the client_secret of this ImChannelConfig.

        客户端密钥

        :param client_secret: The client_secret of this ImChannelConfig.
        :type client_secret: str
        """
        self._client_secret = client_secret

    @property
    def platform_specific(self):
        r"""Gets the platform_specific of this ImChannelConfig.

        平台扩展配置

        :return: The platform_specific of this ImChannelConfig.
        :rtype: dict(str, str)
        """
        return self._platform_specific

    @platform_specific.setter
    def platform_specific(self, platform_specific):
        r"""Sets the platform_specific of this ImChannelConfig.

        平台扩展配置

        :param platform_specific: The platform_specific of this ImChannelConfig.
        :type platform_specific: dict(str, str)
        """
        self._platform_specific = platform_specific

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
        if not isinstance(other, ImChannelConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
