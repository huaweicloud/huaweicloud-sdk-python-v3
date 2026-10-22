# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RequestInspectionDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'payload_type': 'str',
        'username': 'str',
        'password': 'str',
        'email': 'str',
        'phone': 'str'
    }

    attribute_map = {
        'payload_type': 'payload_type',
        'username': 'username',
        'password': 'password',
        'email': 'email',
        'phone': 'phone'
    }

    def __init__(self, payload_type=None, username=None, password=None, email=None, phone=None):
        r"""RequestInspectionDTO

        The model defined in huaweicloud sdk

        :param payload_type: 请求的 Payload 类型（JSON/FORM_URLENCODED）
        :type payload_type: str
        :param username: 用户名字段路径
        :type username: str
        :param password: 密码字段路径
        :type password: str
        :param email: 邮箱字段路径（可选）
        :type email: str
        :param phone: 手机号字段路径（可选）
        :type phone: str
        """
        
        

        self._payload_type = None
        self._username = None
        self._password = None
        self._email = None
        self._phone = None
        self.discriminator = None

        self.payload_type = payload_type
        self.username = username
        self.password = password
        if email is not None:
            self.email = email
        if phone is not None:
            self.phone = phone

    @property
    def payload_type(self):
        r"""Gets the payload_type of this RequestInspectionDTO.

        请求的 Payload 类型（JSON/FORM_URLENCODED）

        :return: The payload_type of this RequestInspectionDTO.
        :rtype: str
        """
        return self._payload_type

    @payload_type.setter
    def payload_type(self, payload_type):
        r"""Sets the payload_type of this RequestInspectionDTO.

        请求的 Payload 类型（JSON/FORM_URLENCODED）

        :param payload_type: The payload_type of this RequestInspectionDTO.
        :type payload_type: str
        """
        self._payload_type = payload_type

    @property
    def username(self):
        r"""Gets the username of this RequestInspectionDTO.

        用户名字段路径

        :return: The username of this RequestInspectionDTO.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this RequestInspectionDTO.

        用户名字段路径

        :param username: The username of this RequestInspectionDTO.
        :type username: str
        """
        self._username = username

    @property
    def password(self):
        r"""Gets the password of this RequestInspectionDTO.

        密码字段路径

        :return: The password of this RequestInspectionDTO.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this RequestInspectionDTO.

        密码字段路径

        :param password: The password of this RequestInspectionDTO.
        :type password: str
        """
        self._password = password

    @property
    def email(self):
        r"""Gets the email of this RequestInspectionDTO.

        邮箱字段路径（可选）

        :return: The email of this RequestInspectionDTO.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this RequestInspectionDTO.

        邮箱字段路径（可选）

        :param email: The email of this RequestInspectionDTO.
        :type email: str
        """
        self._email = email

    @property
    def phone(self):
        r"""Gets the phone of this RequestInspectionDTO.

        手机号字段路径（可选）

        :return: The phone of this RequestInspectionDTO.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        r"""Sets the phone of this RequestInspectionDTO.

        手机号字段路径（可选）

        :param phone: The phone of this RequestInspectionDTO.
        :type phone: str
        """
        self._phone = phone

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RequestInspectionDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
