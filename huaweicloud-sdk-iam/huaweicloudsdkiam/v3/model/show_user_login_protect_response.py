# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowUserLoginProtectResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'login_protect': 'LoginProtectResult'
    }

    attribute_map = {
        'login_protect': 'login_protect'
    }

    def __init__(self, login_protect=None):
        """ShowUserLoginProtectResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._login_protect = None
        self.discriminator = None

        if login_protect is not None:
            self.login_protect = login_protect

    @property
    def login_protect(self):
        """Gets the login_protect of this ShowUserLoginProtectResponse.


        :return: The login_protect of this ShowUserLoginProtectResponse.
        :rtype: LoginProtectResult
        """
        return self._login_protect

    @login_protect.setter
    def login_protect(self, login_protect):
        """Sets the login_protect of this ShowUserLoginProtectResponse.


        :param login_protect: The login_protect of this ShowUserLoginProtectResponse.
        :type: LoginProtectResult
        """
        self._login_protect = login_protect

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
        if not isinstance(other, ShowUserLoginProtectResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
