# coding: utf-8

import pprint
import re

import six





class UpdateLoginProject:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'enabled': 'bool',
        'verification_method': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'verification_method': 'verification_method'
    }

    def __init__(self, enabled=None, verification_method=None):
        """UpdateLoginProject - a model defined in huaweicloud sdk"""
        
        

        self._enabled = None
        self._verification_method = None
        self.discriminator = None

        self.enabled = enabled
        self.verification_method = verification_method

    @property
    def enabled(self):
        """Gets the enabled of this UpdateLoginProject.

        IAM用户是否开启登录保护，开启为\"true\"，未开启为\"false\"。

        :return: The enabled of this UpdateLoginProject.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this UpdateLoginProject.

        IAM用户是否开启登录保护，开启为\"true\"，未开启为\"false\"。

        :param enabled: The enabled of this UpdateLoginProject.
        :type: bool
        """
        self._enabled = enabled

    @property
    def verification_method(self):
        """Gets the verification_method of this UpdateLoginProject.

        IAM用户登录验证方式。手机验证为“sms”,邮箱验证为“email”,MFA验证为“vmfa”。

        :return: The verification_method of this UpdateLoginProject.
        :rtype: str
        """
        return self._verification_method

    @verification_method.setter
    def verification_method(self, verification_method):
        """Sets the verification_method of this UpdateLoginProject.

        IAM用户登录验证方式。手机验证为“sms”,邮箱验证为“email”,MFA验证为“vmfa”。

        :param verification_method: The verification_method of this UpdateLoginProject.
        :type: str
        """
        self._verification_method = verification_method

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
        if not isinstance(other, UpdateLoginProject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
