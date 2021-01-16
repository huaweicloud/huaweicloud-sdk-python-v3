# coding: utf-8

import pprint
import re

import six





class CreateUserResult:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'status': 'int',
        'pwd_status': 'bool',
        'xuser_id': 'str',
        'xuser_type': 'str',
        'description': 'str',
        'name': 'str',
        'phone': 'str',
        'is_domain_owner': 'bool',
        'domain_id': 'str',
        'enabled': 'bool',
        'areacode': 'str',
        'email': 'str',
        'create_time': 'str',
        'xdomain_id': 'str',
        'xdomain_type': 'str',
        'id': 'str',
        'password_expires_at': 'str'
    }

    attribute_map = {
        'status': 'status',
        'pwd_status': 'pwd_status',
        'xuser_id': 'xuser_id',
        'xuser_type': 'xuser_type',
        'description': 'description',
        'name': 'name',
        'phone': 'phone',
        'is_domain_owner': 'is_domain_owner',
        'domain_id': 'domain_id',
        'enabled': 'enabled',
        'areacode': 'areacode',
        'email': 'email',
        'create_time': 'create_time',
        'xdomain_id': 'xdomain_id',
        'xdomain_type': 'xdomain_type',
        'id': 'id',
        'password_expires_at': 'password_expires_at'
    }

    def __init__(self, status=None, pwd_status=None, xuser_id=None, xuser_type=None, description=None, name=None, phone=None, is_domain_owner=None, domain_id=None, enabled=None, areacode=None, email=None, create_time=None, xdomain_id=None, xdomain_type=None, id=None, password_expires_at=None):
        """CreateUserResult - a model defined in huaweicloud sdk"""
        
        

        self._status = None
        self._pwd_status = None
        self._xuser_id = None
        self._xuser_type = None
        self._description = None
        self._name = None
        self._phone = None
        self._is_domain_owner = None
        self._domain_id = None
        self._enabled = None
        self._areacode = None
        self._email = None
        self._create_time = None
        self._xdomain_id = None
        self._xdomain_type = None
        self._id = None
        self._password_expires_at = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if pwd_status is not None:
            self.pwd_status = pwd_status
        if xuser_id is not None:
            self.xuser_id = xuser_id
        if xuser_type is not None:
            self.xuser_type = xuser_type
        if description is not None:
            self.description = description
        self.name = name
        if phone is not None:
            self.phone = phone
        if is_domain_owner is not None:
            self.is_domain_owner = is_domain_owner
        self.domain_id = domain_id
        self.enabled = enabled
        if areacode is not None:
            self.areacode = areacode
        if email is not None:
            self.email = email
        if create_time is not None:
            self.create_time = create_time
        if xdomain_id is not None:
            self.xdomain_id = xdomain_id
        if xdomain_type is not None:
            self.xdomain_type = xdomain_type
        self.id = id
        if password_expires_at is not None:
            self.password_expires_at = password_expires_at

    @property
    def status(self):
        """Gets the status of this CreateUserResult.

        IAM用户状态信息。

        :return: The status of this CreateUserResult.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateUserResult.

        IAM用户状态信息。

        :param status: The status of this CreateUserResult.
        :type: int
        """
        self._status = status

    @property
    def pwd_status(self):
        """Gets the pwd_status of this CreateUserResult.

        IAM用户首次登录是否重置密码。

        :return: The pwd_status of this CreateUserResult.
        :rtype: bool
        """
        return self._pwd_status

    @pwd_status.setter
    def pwd_status(self, pwd_status):
        """Sets the pwd_status of this CreateUserResult.

        IAM用户首次登录是否重置密码。

        :param pwd_status: The pwd_status of this CreateUserResult.
        :type: bool
        """
        self._pwd_status = pwd_status

    @property
    def xuser_id(self):
        """Gets the xuser_id of this CreateUserResult.

        IAM用户在外部系统中的ID。 >外部系统指与华为云对接的外部企业管理系统，xaccount_type、xaccount_id、xdomain_type、xdomain_id、xuser_type、xuser_id等参数值，无法在华为云获取，请咨询企业管理员。

        :return: The xuser_id of this CreateUserResult.
        :rtype: str
        """
        return self._xuser_id

    @xuser_id.setter
    def xuser_id(self, xuser_id):
        """Sets the xuser_id of this CreateUserResult.

        IAM用户在外部系统中的ID。 >外部系统指与华为云对接的外部企业管理系统，xaccount_type、xaccount_id、xdomain_type、xdomain_id、xuser_type、xuser_id等参数值，无法在华为云获取，请咨询企业管理员。

        :param xuser_id: The xuser_id of this CreateUserResult.
        :type: str
        """
        self._xuser_id = xuser_id

    @property
    def xuser_type(self):
        """Gets the xuser_type of this CreateUserResult.

        用户在外部系统中的类型。 >外部系统指与华为云对接的外部企业管理系统，xaccount_type、xaccount_id、xdomain_type、xdomain_id、xuser_type、xuser_id等参数值，无法在华为云获取，请咨询企业管理员。

        :return: The xuser_type of this CreateUserResult.
        :rtype: str
        """
        return self._xuser_type

    @xuser_type.setter
    def xuser_type(self, xuser_type):
        """Sets the xuser_type of this CreateUserResult.

        用户在外部系统中的类型。 >外部系统指与华为云对接的外部企业管理系统，xaccount_type、xaccount_id、xdomain_type、xdomain_id、xuser_type、xuser_id等参数值，无法在华为云获取，请咨询企业管理员。

        :param xuser_type: The xuser_type of this CreateUserResult.
        :type: str
        """
        self._xuser_type = xuser_type

    @property
    def description(self):
        """Gets the description of this CreateUserResult.

        IAM用户描述信息。

        :return: The description of this CreateUserResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateUserResult.

        IAM用户描述信息。

        :param description: The description of this CreateUserResult.
        :type: str
        """
        self._description = description

    @property
    def name(self):
        """Gets the name of this CreateUserResult.

        IAM用户名，长度5~32字符之间，首位不能为数字，特殊字符只能包含下划线“_”、中划线“-”和空格。

        :return: The name of this CreateUserResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateUserResult.

        IAM用户名，长度5~32字符之间，首位不能为数字，特殊字符只能包含下划线“_”、中划线“-”和空格。

        :param name: The name of this CreateUserResult.
        :type: str
        """
        self._name = name

    @property
    def phone(self):
        """Gets the phone of this CreateUserResult.

        IAM用户手机号，纯数字，长度小于等于32字符。必须与国家码同时存在。

        :return: The phone of this CreateUserResult.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this CreateUserResult.

        IAM用户手机号，纯数字，长度小于等于32字符。必须与国家码同时存在。

        :param phone: The phone of this CreateUserResult.
        :type: str
        """
        self._phone = phone

    @property
    def is_domain_owner(self):
        """Gets the is_domain_owner of this CreateUserResult.

        IAM用户是否为账号管理员。

        :return: The is_domain_owner of this CreateUserResult.
        :rtype: bool
        """
        return self._is_domain_owner

    @is_domain_owner.setter
    def is_domain_owner(self, is_domain_owner):
        """Sets the is_domain_owner of this CreateUserResult.

        IAM用户是否为账号管理员。

        :param is_domain_owner: The is_domain_owner of this CreateUserResult.
        :type: bool
        """
        self._is_domain_owner = is_domain_owner

    @property
    def domain_id(self):
        """Gets the domain_id of this CreateUserResult.

        IAM用户所属账号ID。

        :return: The domain_id of this CreateUserResult.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this CreateUserResult.

        IAM用户所属账号ID。

        :param domain_id: The domain_id of this CreateUserResult.
        :type: str
        """
        self._domain_id = domain_id

    @property
    def enabled(self):
        """Gets the enabled of this CreateUserResult.

        是否启用IAM用户。true为启用，false为停用，默认为true。

        :return: The enabled of this CreateUserResult.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this CreateUserResult.

        是否启用IAM用户。true为启用，false为停用，默认为true。

        :param enabled: The enabled of this CreateUserResult.
        :type: bool
        """
        self._enabled = enabled

    @property
    def areacode(self):
        """Gets the areacode of this CreateUserResult.

        国家码。中国大陆为“0086”。

        :return: The areacode of this CreateUserResult.
        :rtype: str
        """
        return self._areacode

    @areacode.setter
    def areacode(self, areacode):
        """Sets the areacode of this CreateUserResult.

        国家码。中国大陆为“0086”。

        :param areacode: The areacode of this CreateUserResult.
        :type: str
        """
        self._areacode = areacode

    @property
    def email(self):
        """Gets the email of this CreateUserResult.

        IAM用户邮箱。

        :return: The email of this CreateUserResult.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CreateUserResult.

        IAM用户邮箱。

        :param email: The email of this CreateUserResult.
        :type: str
        """
        self._email = email

    @property
    def create_time(self):
        """Gets the create_time of this CreateUserResult.

        IAM用户创建时间。

        :return: The create_time of this CreateUserResult.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CreateUserResult.

        IAM用户创建时间。

        :param create_time: The create_time of this CreateUserResult.
        :type: str
        """
        self._create_time = create_time

    @property
    def xdomain_id(self):
        """Gets the xdomain_id of this CreateUserResult.

        运营主体的客户编码。

        :return: The xdomain_id of this CreateUserResult.
        :rtype: str
        """
        return self._xdomain_id

    @xdomain_id.setter
    def xdomain_id(self, xdomain_id):
        """Sets the xdomain_id of this CreateUserResult.

        运营主体的客户编码。

        :param xdomain_id: The xdomain_id of this CreateUserResult.
        :type: str
        """
        self._xdomain_id = xdomain_id

    @property
    def xdomain_type(self):
        """Gets the xdomain_type of this CreateUserResult.

        运营主体。

        :return: The xdomain_type of this CreateUserResult.
        :rtype: str
        """
        return self._xdomain_type

    @xdomain_type.setter
    def xdomain_type(self, xdomain_type):
        """Sets the xdomain_type of this CreateUserResult.

        运营主体。

        :param xdomain_type: The xdomain_type of this CreateUserResult.
        :type: str
        """
        self._xdomain_type = xdomain_type

    @property
    def id(self):
        """Gets the id of this CreateUserResult.

        IAM用户ID。

        :return: The id of this CreateUserResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateUserResult.

        IAM用户ID。

        :param id: The id of this CreateUserResult.
        :type: str
        """
        self._id = id

    @property
    def password_expires_at(self):
        """Gets the password_expires_at of this CreateUserResult.

        密码过期时间（UTC时间），“null”表示密码不过期。

        :return: The password_expires_at of this CreateUserResult.
        :rtype: str
        """
        return self._password_expires_at

    @password_expires_at.setter
    def password_expires_at(self, password_expires_at):
        """Sets the password_expires_at of this CreateUserResult.

        密码过期时间（UTC时间），“null”表示密码不过期。

        :param password_expires_at: The password_expires_at of this CreateUserResult.
        :type: str
        """
        self._password_expires_at = password_expires_at

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
        if not isinstance(other, CreateUserResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
