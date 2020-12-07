# coding: utf-8

import pprint
import re

import six





class UpdateApplicationRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'platform_principal': 'str',
        'platform_credential': 'str'
    }

    attribute_map = {
        'platform_principal': 'platform_principal',
        'platform_credential': 'platform_credential'
    }

    def __init__(self, platform_principal=None, platform_credential=None):
        """UpdateApplicationRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._platform_principal = None
        self._platform_credential = None
        self.discriminator = None

        self.platform_principal = platform_principal
        self.platform_credential = platform_credential

    @property
    def platform_principal(self):
        """Gets the platform_principal of this UpdateApplicationRequestBody.

        对于HMS平台是APP ID，只能包含英文字母和数字，最大20个字符。  对于苹果APNS、APNS_SandBox平台是推送证书，大小不超过8K，且是Base64编码。

        :return: The platform_principal of this UpdateApplicationRequestBody.
        :rtype: str
        """
        return self._platform_principal

    @platform_principal.setter
    def platform_principal(self, platform_principal):
        """Sets the platform_principal of this UpdateApplicationRequestBody.

        对于HMS平台是APP ID，只能包含英文字母和数字，最大20个字符。  对于苹果APNS、APNS_SandBox平台是推送证书，大小不超过8K，且是Base64编码。

        :param platform_principal: The platform_principal of this UpdateApplicationRequestBody.
        :type: str
        """
        self._platform_principal = platform_principal

    @property
    def platform_credential(self):
        """Gets the platform_credential of this UpdateApplicationRequestBody.

        对于HMS平台是APP SECRET， 只能包含英文字母和数字，32到64个字符。  对于苹果APNS、APNS_SandBox平台是推送证书的私钥（private key）， 大小不超过8K，且是Base64编码。

        :return: The platform_credential of this UpdateApplicationRequestBody.
        :rtype: str
        """
        return self._platform_credential

    @platform_credential.setter
    def platform_credential(self, platform_credential):
        """Sets the platform_credential of this UpdateApplicationRequestBody.

        对于HMS平台是APP SECRET， 只能包含英文字母和数字，32到64个字符。  对于苹果APNS、APNS_SandBox平台是推送证书的私钥（private key）， 大小不超过8K，且是Base64编码。

        :param platform_credential: The platform_credential of this UpdateApplicationRequestBody.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateApplicationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
