# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        r"""ModPwdReqDTO

        The model defined in huaweicloud sdk

        :param account: 帐号，必须是携带域名的帐号。 
        :type account: str
        :param old_pwd: 用户旧的登录密码。 
        :type old_pwd: str
        :param new_pwd: 用户新的登录密码。 密码要求： * 长度范围要求8~32 * 至少包含两种字符类型：小写字母、大写字母、数字、特殊字符（&#x60; ~ ! @ # $ % ^ &amp; * ( ) - _ &#x3D; + \\ | [ { } ] ; : \&quot; ,&#39; &lt; . &gt; / ?） * 旧密码和新密码不能相同 * 上次修改密码后5分钟内不能更新密码 * 不能与最近使用的旧密码相同 * 不能包含3个以上重复字符 * 密码不能包含与其对应的用户名（不区分大小写）以及逆序的用户名（不区分大小写） * 新密码与旧密码之间允许的最少不相同字符数为2个 
        :type new_pwd: str
        """
        
        

        self._account = None
        self._old_pwd = None
        self._new_pwd = None
        self.discriminator = None

        self.account = account
        self.old_pwd = old_pwd
        self.new_pwd = new_pwd

    @property
    def account(self):
        r"""Gets the account of this ModPwdReqDTO.

        帐号，必须是携带域名的帐号。 

        :return: The account of this ModPwdReqDTO.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        r"""Sets the account of this ModPwdReqDTO.

        帐号，必须是携带域名的帐号。 

        :param account: The account of this ModPwdReqDTO.
        :type account: str
        """
        self._account = account

    @property
    def old_pwd(self):
        r"""Gets the old_pwd of this ModPwdReqDTO.

        用户旧的登录密码。 

        :return: The old_pwd of this ModPwdReqDTO.
        :rtype: str
        """
        return self._old_pwd

    @old_pwd.setter
    def old_pwd(self, old_pwd):
        r"""Sets the old_pwd of this ModPwdReqDTO.

        用户旧的登录密码。 

        :param old_pwd: The old_pwd of this ModPwdReqDTO.
        :type old_pwd: str
        """
        self._old_pwd = old_pwd

    @property
    def new_pwd(self):
        r"""Gets the new_pwd of this ModPwdReqDTO.

        用户新的登录密码。 密码要求： * 长度范围要求8~32 * 至少包含两种字符类型：小写字母、大写字母、数字、特殊字符（` ~ ! @ # $ % ^ & * ( ) - _ = + \\ | [ { } ] ; : \" ,' < . > / ?） * 旧密码和新密码不能相同 * 上次修改密码后5分钟内不能更新密码 * 不能与最近使用的旧密码相同 * 不能包含3个以上重复字符 * 密码不能包含与其对应的用户名（不区分大小写）以及逆序的用户名（不区分大小写） * 新密码与旧密码之间允许的最少不相同字符数为2个 

        :return: The new_pwd of this ModPwdReqDTO.
        :rtype: str
        """
        return self._new_pwd

    @new_pwd.setter
    def new_pwd(self, new_pwd):
        r"""Sets the new_pwd of this ModPwdReqDTO.

        用户新的登录密码。 密码要求： * 长度范围要求8~32 * 至少包含两种字符类型：小写字母、大写字母、数字、特殊字符（` ~ ! @ # $ % ^ & * ( ) - _ = + \\ | [ { } ] ; : \" ,' < . > / ?） * 旧密码和新密码不能相同 * 上次修改密码后5分钟内不能更新密码 * 不能与最近使用的旧密码相同 * 不能包含3个以上重复字符 * 密码不能包含与其对应的用户名（不区分大小写）以及逆序的用户名（不区分大小写） * 新密码与旧密码之间允许的最少不相同字符数为2个 

        :param new_pwd: The new_pwd of this ModPwdReqDTO.
        :type new_pwd: str
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
        if not isinstance(other, ModPwdReqDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
