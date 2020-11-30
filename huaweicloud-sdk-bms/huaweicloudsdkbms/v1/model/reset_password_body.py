# coding: utf-8

import pprint
import re

import six





class ResetPasswordBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'reset_password': 'ResetPassword'
    }

    attribute_map = {
        'reset_password': 'reset-password'
    }

    def __init__(self, reset_password=None):
        """ResetPasswordBody - a model defined in huaweicloud sdk"""
        
        

        self._reset_password = None
        self.discriminator = None

        self.reset_password = reset_password

    @property
    def reset_password(self):
        """Gets the reset_password of this ResetPasswordBody.


        :return: The reset_password of this ResetPasswordBody.
        :rtype: ResetPassword
        """
        return self._reset_password

    @reset_password.setter
    def reset_password(self, reset_password):
        """Sets the reset_password of this ResetPasswordBody.


        :param reset_password: The reset_password of this ResetPasswordBody.
        :type: ResetPassword
        """
        self._reset_password = reset_password

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
        if not isinstance(other, ResetPasswordBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
