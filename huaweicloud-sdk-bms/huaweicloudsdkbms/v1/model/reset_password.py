# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResetPassword:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'new_password': 'str'
    }

    attribute_map = {
        'new_password': 'new_password'
    }

    def __init__(self, new_password=None):
        r"""ResetPassword

        The model defined in huaweicloud sdk

        :param new_password: 裸金属服务器新密码。该接口不做密码安全性校验，设置的密码复杂度请遵循密码规则。密码规则：密码长度范围为8到26位。密码至少包含以下4种字符中的3种：大写字母小写字母数字特殊字符Windows：!@$%-_&#x3D;+[]:./?Linux：!@%^-_&#x3D;+[]{}:,./?密码不能包含用户名或用户名的逆序。Windows系统的裸金属服务器，不能包含用户名中超过两个连续字符的部分。
        :type new_password: str
        """
        
        

        self._new_password = None
        self.discriminator = None

        self.new_password = new_password

    @property
    def new_password(self):
        r"""Gets the new_password of this ResetPassword.

        裸金属服务器新密码。该接口不做密码安全性校验，设置的密码复杂度请遵循密码规则。密码规则：密码长度范围为8到26位。密码至少包含以下4种字符中的3种：大写字母小写字母数字特殊字符Windows：!@$%-_=+[]:./?Linux：!@%^-_=+[]{}:,./?密码不能包含用户名或用户名的逆序。Windows系统的裸金属服务器，不能包含用户名中超过两个连续字符的部分。

        :return: The new_password of this ResetPassword.
        :rtype: str
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password):
        r"""Sets the new_password of this ResetPassword.

        裸金属服务器新密码。该接口不做密码安全性校验，设置的密码复杂度请遵循密码规则。密码规则：密码长度范围为8到26位。密码至少包含以下4种字符中的3种：大写字母小写字母数字特殊字符Windows：!@$%-_=+[]:./?Linux：!@%^-_=+[]{}:,./?密码不能包含用户名或用户名的逆序。Windows系统的裸金属服务器，不能包含用户名中超过两个连续字符的部分。

        :param new_password: The new_password of this ResetPassword.
        :type new_password: str
        """
        self._new_password = new_password

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
        if not isinstance(other, ResetPassword):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
