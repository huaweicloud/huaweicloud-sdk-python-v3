# coding: utf-8

import pprint
import re

import six





class CreateCredentialOption:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'user_id': 'str',
        'description': 'str'
    }

    attribute_map = {
        'user_id': 'user_id',
        'description': 'description'
    }

    def __init__(self, user_id=None, description=None):
        """CreateCredentialOption - a model defined in huaweicloud sdk"""
        
        

        self._user_id = None
        self._description = None
        self.discriminator = None

        self.user_id = user_id
        if description is not None:
            self.description = description

    @property
    def user_id(self):
        """Gets the user_id of this CreateCredentialOption.

        待创建访问秘钥（AK/SK）的IAM用户ID，获取方式请参见：[获取账号、IAM用户、项目、用户组、委托的名称和ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)。

        :return: The user_id of this CreateCredentialOption.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this CreateCredentialOption.

        待创建访问秘钥（AK/SK）的IAM用户ID，获取方式请参见：[获取账号、IAM用户、项目、用户组、委托的名称和ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)。

        :param user_id: The user_id of this CreateCredentialOption.
        :type: str
        """
        self._user_id = user_id

    @property
    def description(self):
        """Gets the description of this CreateCredentialOption.

        访问密钥描述信息。

        :return: The description of this CreateCredentialOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateCredentialOption.

        访问密钥描述信息。

        :param description: The description of this CreateCredentialOption.
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
        if not isinstance(other, CreateCredentialOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
