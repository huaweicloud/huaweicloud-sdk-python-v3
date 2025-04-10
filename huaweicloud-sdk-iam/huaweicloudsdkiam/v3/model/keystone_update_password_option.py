# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeystoneUpdatePasswordOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'password': 'str',
        'original_password': 'str'
    }

    attribute_map = {
        'password': 'password',
        'original_password': 'original_password'
    }

    def __init__(self, password=None, original_password=None):
        r"""KeystoneUpdatePasswordOption

        The model defined in huaweicloud sdk

        :param password: IAM用户的新密码。 - 系统默认密码最小长度为6位字符，在6-32位之间支持用户自定义密码长度。 - 至少包含以下四种字符中的两种： 大写字母、小写字母、数字和特殊字符。 - 不能包含手机号和邮箱。 - 必须满足用户所属账号的[密码策略](https://support.huaweicloud.com/usermanual-iam/iam_01_0607.html)要求。 - 新密码不能与当前密码相同。
        :type password: str
        :param original_password: IAM用户的原密码。
        :type original_password: str
        """
        
        

        self._password = None
        self._original_password = None
        self.discriminator = None

        self.password = password
        self.original_password = original_password

    @property
    def password(self):
        r"""Gets the password of this KeystoneUpdatePasswordOption.

        IAM用户的新密码。 - 系统默认密码最小长度为6位字符，在6-32位之间支持用户自定义密码长度。 - 至少包含以下四种字符中的两种： 大写字母、小写字母、数字和特殊字符。 - 不能包含手机号和邮箱。 - 必须满足用户所属账号的[密码策略](https://support.huaweicloud.com/usermanual-iam/iam_01_0607.html)要求。 - 新密码不能与当前密码相同。

        :return: The password of this KeystoneUpdatePasswordOption.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this KeystoneUpdatePasswordOption.

        IAM用户的新密码。 - 系统默认密码最小长度为6位字符，在6-32位之间支持用户自定义密码长度。 - 至少包含以下四种字符中的两种： 大写字母、小写字母、数字和特殊字符。 - 不能包含手机号和邮箱。 - 必须满足用户所属账号的[密码策略](https://support.huaweicloud.com/usermanual-iam/iam_01_0607.html)要求。 - 新密码不能与当前密码相同。

        :param password: The password of this KeystoneUpdatePasswordOption.
        :type password: str
        """
        self._password = password

    @property
    def original_password(self):
        r"""Gets the original_password of this KeystoneUpdatePasswordOption.

        IAM用户的原密码。

        :return: The original_password of this KeystoneUpdatePasswordOption.
        :rtype: str
        """
        return self._original_password

    @original_password.setter
    def original_password(self, original_password):
        r"""Sets the original_password of this KeystoneUpdatePasswordOption.

        IAM用户的原密码。

        :param original_password: The original_password of this KeystoneUpdatePasswordOption.
        :type original_password: str
        """
        self._original_password = original_password

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
        if not isinstance(other, KeystoneUpdatePasswordOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
