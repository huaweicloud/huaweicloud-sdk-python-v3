# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowResetPwdResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'resetpwd_flag': 'str'
    }

    attribute_map = {
        'resetpwd_flag': 'resetpwd_flag'
    }

    def __init__(self, resetpwd_flag=None):
        """ShowResetPwdResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._resetpwd_flag = None
        self.discriminator = None

        if resetpwd_flag is not None:
            self.resetpwd_flag = resetpwd_flag

    @property
    def resetpwd_flag(self):
        """Gets the resetpwd_flag of this ShowResetPwdResponse.

        是否支持重置密码。True：支持一键重置密码。False：不支持一键重置密码

        :return: The resetpwd_flag of this ShowResetPwdResponse.
        :rtype: str
        """
        return self._resetpwd_flag

    @resetpwd_flag.setter
    def resetpwd_flag(self, resetpwd_flag):
        """Sets the resetpwd_flag of this ShowResetPwdResponse.

        是否支持重置密码。True：支持一键重置密码。False：不支持一键重置密码

        :param resetpwd_flag: The resetpwd_flag of this ShowResetPwdResponse.
        :type: str
        """
        self._resetpwd_flag = resetpwd_flag

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
        if not isinstance(other, ShowResetPwdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
