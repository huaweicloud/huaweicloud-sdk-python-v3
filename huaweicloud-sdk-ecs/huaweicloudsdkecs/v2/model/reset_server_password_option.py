# coding: utf-8

import pprint
import re

import six





class ResetServerPasswordOption:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'new_password': 'str',
        'is_check_password': 'bool'
    }

    attribute_map = {
        'new_password': 'new_password',
        'is_check_password': 'is_check_password'
    }

    def __init__(self, new_password=None, is_check_password=None):
        """ResetServerPasswordOption - a model defined in huaweicloud sdk"""
        
        

        self._new_password = None
        self._is_check_password = None
        self.discriminator = None

        self.new_password = new_password
        if is_check_password is not None:
            self.is_check_password = is_check_password

    @property
    def new_password(self):
        """Gets the new_password of this ResetServerPasswordOption.

        弹性云服务器新密码。  该接口默认不做密码安全性校验；如需校验，请指定字段“is_check_password”为true。  新密码的校验规则： - 密码长度范围为8到26位。 - 允许输入的字符包括：!@%-_=+[]:./? - 禁止输入的字符包括：汉字及【】：；“”‘’、，。《》？￥…（）—— ·！~`#&^,{}*();\"'<>|\\ $ - 复杂度上必须包含大写字母（A-Z）、小写字母（a-z）、数字（0-9）、以及允许的特殊字符中的3种以上搭配 - 不能包含用户名 \"Administrator\" 和“root”及逆序字符 - 不能包含用户名 \"Administrator\" 中连续3个字符

        :return: The new_password of this ResetServerPasswordOption.
        :rtype: str
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password):
        """Sets the new_password of this ResetServerPasswordOption.

        弹性云服务器新密码。  该接口默认不做密码安全性校验；如需校验，请指定字段“is_check_password”为true。  新密码的校验规则： - 密码长度范围为8到26位。 - 允许输入的字符包括：!@%-_=+[]:./? - 禁止输入的字符包括：汉字及【】：；“”‘’、，。《》？￥…（）—— ·！~`#&^,{}*();\"'<>|\\ $ - 复杂度上必须包含大写字母（A-Z）、小写字母（a-z）、数字（0-9）、以及允许的特殊字符中的3种以上搭配 - 不能包含用户名 \"Administrator\" 和“root”及逆序字符 - 不能包含用户名 \"Administrator\" 中连续3个字符

        :param new_password: The new_password of this ResetServerPasswordOption.
        :type: str
        """
        self._new_password = new_password

    @property
    def is_check_password(self):
        """Gets the is_check_password of this ResetServerPasswordOption.

        是否检查密码的复杂度。

        :return: The is_check_password of this ResetServerPasswordOption.
        :rtype: bool
        """
        return self._is_check_password

    @is_check_password.setter
    def is_check_password(self, is_check_password):
        """Sets the is_check_password of this ResetServerPasswordOption.

        是否检查密码的复杂度。

        :param is_check_password: The is_check_password of this ResetServerPasswordOption.
        :type: bool
        """
        self._is_check_password = is_check_password

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
        if not isinstance(other, ResetServerPasswordOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
