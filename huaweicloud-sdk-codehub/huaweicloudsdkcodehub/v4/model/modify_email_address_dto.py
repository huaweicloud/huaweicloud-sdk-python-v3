# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyEmailAddressDto:

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
        'verify_code': 'str'
    }

    attribute_map = {
        'email': 'email',
        'verify_code': 'verify_code'
    }

    def __init__(self, email=None, verify_code=None):
        r"""ModifyEmailAddressDto

        The model defined in huaweicloud sdk

        :param email: **参数解释：** 邮箱。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type email: str
        :param verify_code: **参数解释：** 验证码。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type verify_code: str
        """
        
        

        self._email = None
        self._verify_code = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if verify_code is not None:
            self.verify_code = verify_code

    @property
    def email(self):
        r"""Gets the email of this ModifyEmailAddressDto.

        **参数解释：** 邮箱。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The email of this ModifyEmailAddressDto.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this ModifyEmailAddressDto.

        **参数解释：** 邮箱。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param email: The email of this ModifyEmailAddressDto.
        :type email: str
        """
        self._email = email

    @property
    def verify_code(self):
        r"""Gets the verify_code of this ModifyEmailAddressDto.

        **参数解释：** 验证码。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The verify_code of this ModifyEmailAddressDto.
        :rtype: str
        """
        return self._verify_code

    @verify_code.setter
    def verify_code(self, verify_code):
        r"""Sets the verify_code of this ModifyEmailAddressDto.

        **参数解释：** 验证码。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param verify_code: The verify_code of this ModifyEmailAddressDto.
        :type verify_code: str
        """
        self._verify_code = verify_code

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
        if not isinstance(other, ModifyEmailAddressDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
