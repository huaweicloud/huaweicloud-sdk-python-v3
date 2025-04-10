# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResetPwdReqDTOV1:

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
        'new_pwd': 'str',
        'pass_word_type': 'int'
    }

    attribute_map = {
        'user': 'user',
        'new_pwd': 'newPwd',
        'pass_word_type': 'passWordType'
    }

    def __init__(self, user=None, new_pwd=None, pass_word_type=None):
        r"""ResetPwdReqDTOV1

        The model defined in huaweicloud sdk

        :param user: 用户身份信息（手机号码或邮箱帐号或用户真实帐号）。 
        :type user: str
        :param new_pwd: 用户新的登录密码。 密码要求： * 长度范围要求8~32 * 至少包含大小写字母、数字 * 不能包含3个以上重复字符 * 密码不能包含与其对应的用户名（不区分大小写）以及逆序的用户名（不区分大小写） 
        :type new_pwd: str
        :param pass_word_type: * 1：临时密码，重置完密码后登录Web Portal根据配置可能需要强制修改密码 * 非1：正式密码，重置完密码后登录Web Portal不需要强制修改密码 
        :type pass_word_type: int
        """
        
        

        self._user = None
        self._new_pwd = None
        self._pass_word_type = None
        self.discriminator = None

        self.user = user
        self.new_pwd = new_pwd
        if pass_word_type is not None:
            self.pass_word_type = pass_word_type

    @property
    def user(self):
        r"""Gets the user of this ResetPwdReqDTOV1.

        用户身份信息（手机号码或邮箱帐号或用户真实帐号）。 

        :return: The user of this ResetPwdReqDTOV1.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this ResetPwdReqDTOV1.

        用户身份信息（手机号码或邮箱帐号或用户真实帐号）。 

        :param user: The user of this ResetPwdReqDTOV1.
        :type user: str
        """
        self._user = user

    @property
    def new_pwd(self):
        r"""Gets the new_pwd of this ResetPwdReqDTOV1.

        用户新的登录密码。 密码要求： * 长度范围要求8~32 * 至少包含大小写字母、数字 * 不能包含3个以上重复字符 * 密码不能包含与其对应的用户名（不区分大小写）以及逆序的用户名（不区分大小写） 

        :return: The new_pwd of this ResetPwdReqDTOV1.
        :rtype: str
        """
        return self._new_pwd

    @new_pwd.setter
    def new_pwd(self, new_pwd):
        r"""Sets the new_pwd of this ResetPwdReqDTOV1.

        用户新的登录密码。 密码要求： * 长度范围要求8~32 * 至少包含大小写字母、数字 * 不能包含3个以上重复字符 * 密码不能包含与其对应的用户名（不区分大小写）以及逆序的用户名（不区分大小写） 

        :param new_pwd: The new_pwd of this ResetPwdReqDTOV1.
        :type new_pwd: str
        """
        self._new_pwd = new_pwd

    @property
    def pass_word_type(self):
        r"""Gets the pass_word_type of this ResetPwdReqDTOV1.

        * 1：临时密码，重置完密码后登录Web Portal根据配置可能需要强制修改密码 * 非1：正式密码，重置完密码后登录Web Portal不需要强制修改密码 

        :return: The pass_word_type of this ResetPwdReqDTOV1.
        :rtype: int
        """
        return self._pass_word_type

    @pass_word_type.setter
    def pass_word_type(self, pass_word_type):
        r"""Sets the pass_word_type of this ResetPwdReqDTOV1.

        * 1：临时密码，重置完密码后登录Web Portal根据配置可能需要强制修改密码 * 非1：正式密码，重置完密码后登录Web Portal不需要强制修改密码 

        :param pass_word_type: The pass_word_type of this ResetPwdReqDTOV1.
        :type pass_word_type: int
        """
        self._pass_word_type = pass_word_type

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
        if not isinstance(other, ResetPwdReqDTOV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
