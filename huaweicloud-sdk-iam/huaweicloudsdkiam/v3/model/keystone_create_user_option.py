# coding: utf-8

import pprint
import re

import six





class KeystoneCreateUserOption:


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
        'domain_id': 'str',
        'password': 'str',
        'enabled': 'bool',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'domain_id': 'domain_id',
        'password': 'password',
        'enabled': 'enabled',
        'description': 'description'
    }

    def __init__(self, name=None, domain_id=None, password=None, enabled=None, description=None):
        """KeystoneCreateUserOption - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._domain_id = None
        self._password = None
        self._enabled = None
        self._description = None
        self.discriminator = None

        self.name = name
        if domain_id is not None:
            self.domain_id = domain_id
        if password is not None:
            self.password = password
        if enabled is not None:
            self.enabled = enabled
        if description is not None:
            self.description = description

    @property
    def name(self):
        """Gets the name of this KeystoneCreateUserOption.

        IAM用户名，长度5~32之间，首位不能为数字，特殊字符只能包含下划线“_”、中划线“-”和空格。

        :return: The name of this KeystoneCreateUserOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this KeystoneCreateUserOption.

        IAM用户名，长度5~32之间，首位不能为数字，特殊字符只能包含下划线“_”、中划线“-”和空格。

        :param name: The name of this KeystoneCreateUserOption.
        :type: str
        """
        self._name = name

    @property
    def domain_id(self):
        """Gets the domain_id of this KeystoneCreateUserOption.

        IAM用户所属账号ID。

        :return: The domain_id of this KeystoneCreateUserOption.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this KeystoneCreateUserOption.

        IAM用户所属账号ID。

        :param domain_id: The domain_id of this KeystoneCreateUserOption.
        :type: str
        """
        self._domain_id = domain_id

    @property
    def password(self):
        """Gets the password of this KeystoneCreateUserOption.

        IAM用户密码。   - 系统默认密码最小长度为6位字符，在6-32位之间支持用户自定义密码长度。   - 至少包含以下四种字符中的两种： 大写字母、小写字母、数字和特殊字符。   - 不能包含手机号和邮箱。   - 必须满足账户设置中密码策略的要求。

        :return: The password of this KeystoneCreateUserOption.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this KeystoneCreateUserOption.

        IAM用户密码。   - 系统默认密码最小长度为6位字符，在6-32位之间支持用户自定义密码长度。   - 至少包含以下四种字符中的两种： 大写字母、小写字母、数字和特殊字符。   - 不能包含手机号和邮箱。   - 必须满足账户设置中密码策略的要求。

        :param password: The password of this KeystoneCreateUserOption.
        :type: str
        """
        self._password = password

    @property
    def enabled(self):
        """Gets the enabled of this KeystoneCreateUserOption.

        是否启用IAM用户。true为启用，false为停用，默认为true。

        :return: The enabled of this KeystoneCreateUserOption.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this KeystoneCreateUserOption.

        是否启用IAM用户。true为启用，false为停用，默认为true。

        :param enabled: The enabled of this KeystoneCreateUserOption.
        :type: bool
        """
        self._enabled = enabled

    @property
    def description(self):
        """Gets the description of this KeystoneCreateUserOption.

        IAM用户描述信息。

        :return: The description of this KeystoneCreateUserOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this KeystoneCreateUserOption.

        IAM用户描述信息。

        :param description: The description of this KeystoneCreateUserOption.
        :type: str
        """
        self._description = description

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
        if not isinstance(other, KeystoneCreateUserOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
