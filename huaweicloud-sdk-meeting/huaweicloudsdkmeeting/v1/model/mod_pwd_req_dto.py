# coding: utf-8

import pprint
import re

import six





class ModPwdReqDTO:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'account': 'str',
        'old_pwd': 'str',
        'new_pwd': 'str'
    }

    attribute_map = {
        'account': 'account',
        'old_pwd': 'oldPwd',
        'new_pwd': 'newPwd'
    }

    def __init__(self, account=None, old_pwd=None, new_pwd=None):
        """ModPwdReqDTO - a model defined in huaweicloud sdk"""
        
        

        self._account = None
        self._old_pwd = None
        self._new_pwd = None
        self.discriminator = None

        self.account = account
        self.old_pwd = old_pwd
        self.new_pwd = new_pwd

    @property
    def account(self):
        """Gets the account of this ModPwdReqDTO.

        帐号，必须是携带域名的帐号 maxLength: 255 minLength: 1 

        :return: The account of this ModPwdReqDTO.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this ModPwdReqDTO.

        帐号，必须是携带域名的帐号 maxLength: 255 minLength: 1 

        :param account: The account of this ModPwdReqDTO.
        :type: str
        """
        self._account = account

    @property
    def old_pwd(self):
        """Gets the old_pwd of this ModPwdReqDTO.

        用户旧的登录密码 maxLength: 255 minLength: 1 

        :return: The old_pwd of this ModPwdReqDTO.
        :rtype: str
        """
        return self._old_pwd

    @old_pwd.setter
    def old_pwd(self, old_pwd):
        """Sets the old_pwd of this ModPwdReqDTO.

        用户旧的登录密码 maxLength: 255 minLength: 1 

        :param old_pwd: The old_pwd of this ModPwdReqDTO.
        :type: str
        """
        self._old_pwd = old_pwd

    @property
    def new_pwd(self):
        """Gets the new_pwd of this ModPwdReqDTO.

        用户新的登录密码 密码要求： * 长度范围要求8~32 * 至少包含大小写字母、数字 * 旧密码和新密码不能相同 * 上次修改密码后5分钟内不能更新密码 * 不能与最近使用的旧密码相同 * 不能包含3个以上重复字符 * 密码不能包含与其对应的用户名（不区分大小写）以及逆序的用户名（不区分大小写） * 新密码与旧密码之间允许的最少不相同字符数为2个 

        :return: The new_pwd of this ModPwdReqDTO.
        :rtype: str
        """
        return self._new_pwd

    @new_pwd.setter
    def new_pwd(self, new_pwd):
        """Sets the new_pwd of this ModPwdReqDTO.

        用户新的登录密码 密码要求： * 长度范围要求8~32 * 至少包含大小写字母、数字 * 旧密码和新密码不能相同 * 上次修改密码后5分钟内不能更新密码 * 不能与最近使用的旧密码相同 * 不能包含3个以上重复字符 * 密码不能包含与其对应的用户名（不区分大小写）以及逆序的用户名（不区分大小写） * 新密码与旧密码之间允许的最少不相同字符数为2个 

        :param new_pwd: The new_pwd of this ModPwdReqDTO.
        :type: str
        """
        self._new_pwd = new_pwd

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
        if not isinstance(other, ModPwdReqDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
