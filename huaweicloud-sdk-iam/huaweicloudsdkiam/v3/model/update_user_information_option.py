# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateUserInformationOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'email': 'str',
        'mobile': 'str'
    }

    attribute_map = {
        'email': 'email',
        'mobile': 'mobile'
    }

    def __init__(self, email=None, mobile=None):
        r"""UpdateUserInformationOption

        The model defined in huaweicloud sdk

        :param email: IAM用户的新邮箱，符合邮箱格式，长度小于等于255字符。
        :type email: str
        :param mobile: IAM用户的国家码+新手机号，手机号为纯数字，长度小于等于32字符。
        :type mobile: str
        """
        
        

        self._email = None
        self._mobile = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if mobile is not None:
            self.mobile = mobile

    @property
    def email(self):
        r"""Gets the email of this UpdateUserInformationOption.

        IAM用户的新邮箱，符合邮箱格式，长度小于等于255字符。

        :return: The email of this UpdateUserInformationOption.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this UpdateUserInformationOption.

        IAM用户的新邮箱，符合邮箱格式，长度小于等于255字符。

        :param email: The email of this UpdateUserInformationOption.
        :type email: str
        """
        self._email = email

    @property
    def mobile(self):
        r"""Gets the mobile of this UpdateUserInformationOption.

        IAM用户的国家码+新手机号，手机号为纯数字，长度小于等于32字符。

        :return: The mobile of this UpdateUserInformationOption.
        :rtype: str
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        r"""Sets the mobile of this UpdateUserInformationOption.

        IAM用户的国家码+新手机号，手机号为纯数字，长度小于等于32字符。

        :param mobile: The mobile of this UpdateUserInformationOption.
        :type mobile: str
        """
        self._mobile = mobile

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
        if not isinstance(other, UpdateUserInformationOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
