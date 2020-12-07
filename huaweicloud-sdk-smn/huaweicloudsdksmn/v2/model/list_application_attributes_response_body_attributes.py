# coding: utf-8

import pprint
import re

import six





class ListApplicationAttributesResponseBodyAttributes:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'enabled': 'str',
        'apple_certificate_expiration_date': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'apple_certificate_expiration_date': 'apple_certificate_expiration_date'
    }

    def __init__(self, enabled=None, apple_certificate_expiration_date=None):
        """ListApplicationAttributesResponseBodyAttributes - a model defined in huaweicloud sdk"""
        
        

        self._enabled = None
        self._apple_certificate_expiration_date = None
        self.discriminator = None

        self.enabled = enabled
        if apple_certificate_expiration_date is not None:
            self.apple_certificate_expiration_date = apple_certificate_expiration_date

    @property
    def enabled(self):
        """Gets the enabled of this ListApplicationAttributesResponseBodyAttributes.

        应用平台是否启用。

        :return: The enabled of this ListApplicationAttributesResponseBodyAttributes.
        :rtype: str
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ListApplicationAttributesResponseBodyAttributes.

        应用平台是否启用。

        :param enabled: The enabled of this ListApplicationAttributesResponseBodyAttributes.
        :type: str
        """
        self._enabled = enabled

    @property
    def apple_certificate_expiration_date(self):
        """Gets the apple_certificate_expiration_date of this ListApplicationAttributesResponseBodyAttributes.

        苹果证书过期时间，APNS、APNS_SANDBOX平台特有属性 时间格式为UTC时间，YYYY-MM-DDTHH:MM:SSZ。

        :return: The apple_certificate_expiration_date of this ListApplicationAttributesResponseBodyAttributes.
        :rtype: str
        """
        return self._apple_certificate_expiration_date

    @apple_certificate_expiration_date.setter
    def apple_certificate_expiration_date(self, apple_certificate_expiration_date):
        """Sets the apple_certificate_expiration_date of this ListApplicationAttributesResponseBodyAttributes.

        苹果证书过期时间，APNS、APNS_SANDBOX平台特有属性 时间格式为UTC时间，YYYY-MM-DDTHH:MM:SSZ。

        :param apple_certificate_expiration_date: The apple_certificate_expiration_date of this ListApplicationAttributesResponseBodyAttributes.
        :type: str
        """
        self._apple_certificate_expiration_date = apple_certificate_expiration_date

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
        if not isinstance(other, ListApplicationAttributesResponseBodyAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
