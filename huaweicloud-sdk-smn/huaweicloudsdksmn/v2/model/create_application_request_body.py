# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateApplicationRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'platform': 'str',
        'platform_principal': 'str',
        'platform_credential': 'str'
    }

    attribute_map = {
        'name': 'name',
        'platform': 'platform',
        'platform_principal': 'platform_principal',
        'platform_credential': 'platform_credential'
    }

    def __init__(self, name=None, platform=None, platform_principal=None, platform_credential=None):
        r"""CreateApplicationRequestBody

        The model defined in huaweicloud sdk

        :param name: 应用名。  最大支持64个字符，只能包含英文字母、下划线和数字。
        :type name: str
        :param platform: 应用平台。  目前仅支持HMS、APNS、APNS_SANDBOX。  HMS是为开发者提供的消息推送平台。  APNS和APNS_SANDBOX是用于推送iOS消息的服务平台。
        :type platform: str
        :param platform_principal: 对于HMS平台是APP ID，只能包含英文字母和数字，最大20个字符。 对于苹果APNS、APNS_SandBox平台是推送证书，大小不超过8K，且是Base64编码。
        :type platform_principal: str
        :param platform_credential: 对于HMS平台是APP SECRET， 只能包含英文字母和数字，32到64个字符。  对于苹果APNS、APNS_SandBox平台是推送证书的私钥（private key）， 大小不超过8K，且是Base64编码。
        :type platform_credential: str
        """
        
        

        self._name = None
        self._platform = None
        self._platform_principal = None
        self._platform_credential = None
        self.discriminator = None

        self.name = name
        self.platform = platform
        self.platform_principal = platform_principal
        self.platform_credential = platform_credential

    @property
    def name(self):
        r"""Gets the name of this CreateApplicationRequestBody.

        应用名。  最大支持64个字符，只能包含英文字母、下划线和数字。

        :return: The name of this CreateApplicationRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateApplicationRequestBody.

        应用名。  最大支持64个字符，只能包含英文字母、下划线和数字。

        :param name: The name of this CreateApplicationRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def platform(self):
        r"""Gets the platform of this CreateApplicationRequestBody.

        应用平台。  目前仅支持HMS、APNS、APNS_SANDBOX。  HMS是为开发者提供的消息推送平台。  APNS和APNS_SANDBOX是用于推送iOS消息的服务平台。

        :return: The platform of this CreateApplicationRequestBody.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        r"""Sets the platform of this CreateApplicationRequestBody.

        应用平台。  目前仅支持HMS、APNS、APNS_SANDBOX。  HMS是为开发者提供的消息推送平台。  APNS和APNS_SANDBOX是用于推送iOS消息的服务平台。

        :param platform: The platform of this CreateApplicationRequestBody.
        :type platform: str
        """
        self._platform = platform

    @property
    def platform_principal(self):
        r"""Gets the platform_principal of this CreateApplicationRequestBody.

        对于HMS平台是APP ID，只能包含英文字母和数字，最大20个字符。 对于苹果APNS、APNS_SandBox平台是推送证书，大小不超过8K，且是Base64编码。

        :return: The platform_principal of this CreateApplicationRequestBody.
        :rtype: str
        """
        return self._platform_principal

    @platform_principal.setter
    def platform_principal(self, platform_principal):
        r"""Sets the platform_principal of this CreateApplicationRequestBody.

        对于HMS平台是APP ID，只能包含英文字母和数字，最大20个字符。 对于苹果APNS、APNS_SandBox平台是推送证书，大小不超过8K，且是Base64编码。

        :param platform_principal: The platform_principal of this CreateApplicationRequestBody.
        :type platform_principal: str
        """
        self._platform_principal = platform_principal

    @property
    def platform_credential(self):
        r"""Gets the platform_credential of this CreateApplicationRequestBody.

        对于HMS平台是APP SECRET， 只能包含英文字母和数字，32到64个字符。  对于苹果APNS、APNS_SandBox平台是推送证书的私钥（private key）， 大小不超过8K，且是Base64编码。

        :return: The platform_credential of this CreateApplicationRequestBody.
        :rtype: str
        """
        return self._platform_credential

    @platform_credential.setter
    def platform_credential(self, platform_credential):
        r"""Sets the platform_credential of this CreateApplicationRequestBody.

        对于HMS平台是APP SECRET， 只能包含英文字母和数字，32到64个字符。  对于苹果APNS、APNS_SandBox平台是推送证书的私钥（private key）， 大小不超过8K，且是Base64编码。

        :param platform_credential: The platform_credential of this CreateApplicationRequestBody.
        :type platform_credential: str
        """
        self._platform_credential = platform_credential

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
        if not isinstance(other, CreateApplicationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
