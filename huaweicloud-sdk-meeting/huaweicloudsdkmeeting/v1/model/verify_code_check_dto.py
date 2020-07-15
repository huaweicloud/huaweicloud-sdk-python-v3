# coding: utf-8

import pprint
import re

import six





class VerifyCodeCheckDTO:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'user': 'str',
        'code': 'str'
    }

    attribute_map = {
        'user': 'user',
        'code': 'code'
    }

    def __init__(self, user=None, code=None):
        """VerifyCodeCheckDTO - a model defined in huaweicloud sdk"""
        
        

        self._user = None
        self._code = None
        self.discriminator = None

        self.user = user
        self.code = code

    @property
    def user(self):
        """Gets the user of this VerifyCodeCheckDTO.

        必须和发送验证码时带的用户身份信息相同 maxLength：255 minLength：1 

        :return: The user of this VerifyCodeCheckDTO.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this VerifyCodeCheckDTO.

        必须和发送验证码时带的用户身份信息相同 maxLength：255 minLength：1 

        :param user: The user of this VerifyCodeCheckDTO.
        :type: str
        """
        self._user = user

    @property
    def code(self):
        """Gets the code of this VerifyCodeCheckDTO.

        验证码 maxLength：32 minLength：1 

        :return: The code of this VerifyCodeCheckDTO.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this VerifyCodeCheckDTO.

        验证码 maxLength：32 minLength：1 

        :param code: The code of this VerifyCodeCheckDTO.
        :type: str
        """
        self._code = code

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
        if not isinstance(other, VerifyCodeCheckDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
