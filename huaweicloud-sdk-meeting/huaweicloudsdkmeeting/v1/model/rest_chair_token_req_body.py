# coding: utf-8

import pprint
import re

import six





class RestChairTokenReqBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'apply_chair': 'int',
        'chairman_pwd': 'str'
    }

    attribute_map = {
        'apply_chair': 'applyChair',
        'chairman_pwd': 'chairmanPwd'
    }

    def __init__(self, apply_chair=None, chairman_pwd=None):
        """RestChairTokenReqBody - a model defined in huaweicloud sdk"""
        
        

        self._apply_chair = None
        self._chairman_pwd = None
        self.discriminator = None

        self.apply_chair = apply_chair
        if chairman_pwd is not None:
            self.chairman_pwd = chairman_pwd

    @property
    def apply_chair(self):
        """Gets the apply_chair of this RestChairTokenReqBody.

        - 0: 释放主持人。 - 1: 申请主持人。

        :return: The apply_chair of this RestChairTokenReqBody.
        :rtype: int
        """
        return self._apply_chair

    @apply_chair.setter
    def apply_chair(self, apply_chair):
        """Sets the apply_chair of this RestChairTokenReqBody.

        - 0: 释放主持人。 - 1: 申请主持人。

        :param apply_chair: The apply_chair of this RestChairTokenReqBody.
        :type: int
        """
        self._apply_chair = apply_chair

    @property
    def chairman_pwd(self):
        """Gets the chairman_pwd of this RestChairTokenReqBody.

        当申请主持人时，携带主持人密码。

        :return: The chairman_pwd of this RestChairTokenReqBody.
        :rtype: str
        """
        return self._chairman_pwd

    @chairman_pwd.setter
    def chairman_pwd(self, chairman_pwd):
        """Sets the chairman_pwd of this RestChairTokenReqBody.

        当申请主持人时，携带主持人密码。

        :param chairman_pwd: The chairman_pwd of this RestChairTokenReqBody.
        :type: str
        """
        self._chairman_pwd = chairman_pwd

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
        if not isinstance(other, RestChairTokenReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
