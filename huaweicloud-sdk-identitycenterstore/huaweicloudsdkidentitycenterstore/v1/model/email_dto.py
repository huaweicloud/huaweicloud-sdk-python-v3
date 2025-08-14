# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EmailDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('type')
    sensitive_list.append('value')

    openapi_types = {
        'primary': 'bool',
        'type': 'str',
        'value': 'str',
        'verification_status': 'str'
    }

    attribute_map = {
        'primary': 'primary',
        'type': 'type',
        'value': 'value',
        'verification_status': 'verification_status'
    }

    def __init__(self, primary=None, type=None, value=None, verification_status=None):
        r"""EmailDto

        The model defined in huaweicloud sdk

        :param primary: 一个布尔值，表示这是否是用户的主电子邮箱
        :type primary: bool
        :param type: 表示电子邮箱类型的字符串
        :type type: str
        :param value: 包含电子邮箱地址的字符串
        :type value: str
        :param verification_status: 电子邮箱地址的验证状态
        :type verification_status: str
        """
        
        

        self._primary = None
        self._type = None
        self._value = None
        self._verification_status = None
        self.discriminator = None

        self.primary = primary
        self.type = type
        self.value = value
        if verification_status is not None:
            self.verification_status = verification_status

    @property
    def primary(self):
        r"""Gets the primary of this EmailDto.

        一个布尔值，表示这是否是用户的主电子邮箱

        :return: The primary of this EmailDto.
        :rtype: bool
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        r"""Sets the primary of this EmailDto.

        一个布尔值，表示这是否是用户的主电子邮箱

        :param primary: The primary of this EmailDto.
        :type primary: bool
        """
        self._primary = primary

    @property
    def type(self):
        r"""Gets the type of this EmailDto.

        表示电子邮箱类型的字符串

        :return: The type of this EmailDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this EmailDto.

        表示电子邮箱类型的字符串

        :param type: The type of this EmailDto.
        :type type: str
        """
        self._type = type

    @property
    def value(self):
        r"""Gets the value of this EmailDto.

        包含电子邮箱地址的字符串

        :return: The value of this EmailDto.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this EmailDto.

        包含电子邮箱地址的字符串

        :param value: The value of this EmailDto.
        :type value: str
        """
        self._value = value

    @property
    def verification_status(self):
        r"""Gets the verification_status of this EmailDto.

        电子邮箱地址的验证状态

        :return: The verification_status of this EmailDto.
        :rtype: str
        """
        return self._verification_status

    @verification_status.setter
    def verification_status(self, verification_status):
        r"""Sets the verification_status of this EmailDto.

        电子邮箱地址的验证状态

        :param verification_status: The verification_status of this EmailDto.
        :type verification_status: str
        """
        self._verification_status = verification_status

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
        if not isinstance(other, EmailDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
