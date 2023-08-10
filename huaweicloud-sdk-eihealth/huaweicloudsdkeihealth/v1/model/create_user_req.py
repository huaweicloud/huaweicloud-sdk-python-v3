# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateUserReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'password': 'str',
        'role': 'str',
        'email': 'str',
        'phone': 'str',
        'areacode': 'str',
        'settings': 'UserSettingDto'
    }

    attribute_map = {
        'name': 'name',
        'password': 'password',
        'role': 'role',
        'email': 'email',
        'phone': 'phone',
        'areacode': 'areacode',
        'settings': 'settings'
    }

    def __init__(self, name=None, password=None, role=None, email=None, phone=None, areacode=None, settings=None):
        """CreateUserReq

        The model defined in huaweicloud sdk

        :param name: 用户名，长度5~31之间，首位不能为数字，特殊字符只能包含下划线“_”、中划线“-”和空格
        :type name: str
        :param password: 用户密码，在8-32位之间支持用户自定义密码长度，至少包含以下四种字符中的两种： 大写字母、小写字母、数字和特殊字符。
        :type password: str
        :param role: 角色类型：管理员(ADMIN)、操作者(OPERATOR)
        :type role: str
        :param email: 用户邮箱，需符合邮箱格式
        :type email: str
        :param phone: 用户手机号，纯数字，长度小于等于32位。必须与国家码同时存在。
        :type phone: str
        :param areacode: 国家码。中国大陆为“0086”
        :type areacode: str
        :param settings: 
        :type settings: :class:`huaweicloudsdkeihealth.v1.UserSettingDto`
        """
        
        

        self._name = None
        self._password = None
        self._role = None
        self._email = None
        self._phone = None
        self._areacode = None
        self._settings = None
        self.discriminator = None

        self.name = name
        self.password = password
        self.role = role
        if email is not None:
            self.email = email
        if phone is not None:
            self.phone = phone
        if areacode is not None:
            self.areacode = areacode
        if settings is not None:
            self.settings = settings

    @property
    def name(self):
        """Gets the name of this CreateUserReq.

        用户名，长度5~31之间，首位不能为数字，特殊字符只能包含下划线“_”、中划线“-”和空格

        :return: The name of this CreateUserReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateUserReq.

        用户名，长度5~31之间，首位不能为数字，特殊字符只能包含下划线“_”、中划线“-”和空格

        :param name: The name of this CreateUserReq.
        :type name: str
        """
        self._name = name

    @property
    def password(self):
        """Gets the password of this CreateUserReq.

        用户密码，在8-32位之间支持用户自定义密码长度，至少包含以下四种字符中的两种： 大写字母、小写字母、数字和特殊字符。

        :return: The password of this CreateUserReq.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CreateUserReq.

        用户密码，在8-32位之间支持用户自定义密码长度，至少包含以下四种字符中的两种： 大写字母、小写字母、数字和特殊字符。

        :param password: The password of this CreateUserReq.
        :type password: str
        """
        self._password = password

    @property
    def role(self):
        """Gets the role of this CreateUserReq.

        角色类型：管理员(ADMIN)、操作者(OPERATOR)

        :return: The role of this CreateUserReq.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this CreateUserReq.

        角色类型：管理员(ADMIN)、操作者(OPERATOR)

        :param role: The role of this CreateUserReq.
        :type role: str
        """
        self._role = role

    @property
    def email(self):
        """Gets the email of this CreateUserReq.

        用户邮箱，需符合邮箱格式

        :return: The email of this CreateUserReq.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CreateUserReq.

        用户邮箱，需符合邮箱格式

        :param email: The email of this CreateUserReq.
        :type email: str
        """
        self._email = email

    @property
    def phone(self):
        """Gets the phone of this CreateUserReq.

        用户手机号，纯数字，长度小于等于32位。必须与国家码同时存在。

        :return: The phone of this CreateUserReq.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this CreateUserReq.

        用户手机号，纯数字，长度小于等于32位。必须与国家码同时存在。

        :param phone: The phone of this CreateUserReq.
        :type phone: str
        """
        self._phone = phone

    @property
    def areacode(self):
        """Gets the areacode of this CreateUserReq.

        国家码。中国大陆为“0086”

        :return: The areacode of this CreateUserReq.
        :rtype: str
        """
        return self._areacode

    @areacode.setter
    def areacode(self, areacode):
        """Sets the areacode of this CreateUserReq.

        国家码。中国大陆为“0086”

        :param areacode: The areacode of this CreateUserReq.
        :type areacode: str
        """
        self._areacode = areacode

    @property
    def settings(self):
        """Gets the settings of this CreateUserReq.

        :return: The settings of this CreateUserReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.UserSettingDto`
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this CreateUserReq.

        :param settings: The settings of this CreateUserReq.
        :type settings: :class:`huaweicloudsdkeihealth.v1.UserSettingDto`
        """
        self._settings = settings

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
        if not isinstance(other, CreateUserReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
