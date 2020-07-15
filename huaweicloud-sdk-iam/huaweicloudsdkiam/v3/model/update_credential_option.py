# coding: utf-8

import pprint
import re

import six





class UpdateCredentialOption:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'description': 'str'
    }

    attribute_map = {
        'status': 'status',
        'description': 'description'
    }

    def __init__(self, status=None, description=None):
        """UpdateCredentialOption - a model defined in huaweicloud sdk"""
        
        

        self._status = None
        self._description = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if description is not None:
            self.description = description

    @property
    def status(self):
        """Gets the status of this UpdateCredentialOption.

        访问密钥状态。取值为：“active”（启用）或者 “inactive”（停用）。status与description至少填写一个。

        :return: The status of this UpdateCredentialOption.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateCredentialOption.

        访问密钥状态。取值为：“active”（启用）或者 “inactive”（停用）。status与description至少填写一个。

        :param status: The status of this UpdateCredentialOption.
        :type: str
        """
        self._status = status

    @property
    def description(self):
        """Gets the description of this UpdateCredentialOption.

        访问密钥描述信息。status与description至少填写一个。

        :return: The description of this UpdateCredentialOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateCredentialOption.

        访问密钥描述信息。status与description至少填写一个。

        :param description: The description of this UpdateCredentialOption.
        :type: str
        """
        self._description = description

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
        if not isinstance(other, UpdateCredentialOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
