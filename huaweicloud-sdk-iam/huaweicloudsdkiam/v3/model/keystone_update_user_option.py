# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeystoneUpdateUserOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'name': 'str',
        'password': 'str',
        'enabled': 'bool',
        'description': 'str',
        'pwd_status': 'bool'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'name': 'name',
        'password': 'password',
        'enabled': 'enabled',
        'description': 'description',
        'pwd_status': 'pwd_status'
    }

    def __init__(self, domain_id=None, name=None, password=None, enabled=None, description=None, pwd_status=None):
        """KeystoneUpdateUserOption

        The model defined in huaweicloud sdk

        :param domain_id: IAM用户所属账号ID。
        :type domain_id: str
        :param name: 新IAM用户名，长度1~64之间，只能包含如下字符：大小写字母、空格、数字或特殊字符（-_.）且不能以数字开头
        :type name: str
        :param password: IAM用户密码。 - 系统默认密码最小长度为6位字符，在6-32位之间支持用户自定义密码长度。 - 至少包含以下四种字符中的两种： 大写字母、小写字母、数字和特殊字符。 - 不能包含手机号和邮箱。 - 必须满足账户设置中密码策略的要求。 - 新密码不能与当前密码相同。
        :type password: str
        :param enabled: 是否启用IAM用户。true为启用，false为停用，默认为true。
        :type enabled: bool
        :param description: IAM用户新描述信息。
        :type description: str
        :param pwd_status: IAM用户密码状态。true:需要修改密码,false:正常。
        :type pwd_status: bool
        """
        
        

        self._domain_id = None
        self._name = None
        self._password = None
        self._enabled = None
        self._description = None
        self._pwd_status = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if name is not None:
            self.name = name
        if password is not None:
            self.password = password
        if enabled is not None:
            self.enabled = enabled
        if description is not None:
            self.description = description
        if pwd_status is not None:
            self.pwd_status = pwd_status

    @property
    def domain_id(self):
        """Gets the domain_id of this KeystoneUpdateUserOption.

        IAM用户所属账号ID。

        :return: The domain_id of this KeystoneUpdateUserOption.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this KeystoneUpdateUserOption.

        IAM用户所属账号ID。

        :param domain_id: The domain_id of this KeystoneUpdateUserOption.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def name(self):
        """Gets the name of this KeystoneUpdateUserOption.

        新IAM用户名，长度1~64之间，只能包含如下字符：大小写字母、空格、数字或特殊字符（-_.）且不能以数字开头

        :return: The name of this KeystoneUpdateUserOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this KeystoneUpdateUserOption.

        新IAM用户名，长度1~64之间，只能包含如下字符：大小写字母、空格、数字或特殊字符（-_.）且不能以数字开头

        :param name: The name of this KeystoneUpdateUserOption.
        :type name: str
        """
        self._name = name

    @property
    def password(self):
        """Gets the password of this KeystoneUpdateUserOption.

        IAM用户密码。 - 系统默认密码最小长度为6位字符，在6-32位之间支持用户自定义密码长度。 - 至少包含以下四种字符中的两种： 大写字母、小写字母、数字和特殊字符。 - 不能包含手机号和邮箱。 - 必须满足账户设置中密码策略的要求。 - 新密码不能与当前密码相同。

        :return: The password of this KeystoneUpdateUserOption.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this KeystoneUpdateUserOption.

        IAM用户密码。 - 系统默认密码最小长度为6位字符，在6-32位之间支持用户自定义密码长度。 - 至少包含以下四种字符中的两种： 大写字母、小写字母、数字和特殊字符。 - 不能包含手机号和邮箱。 - 必须满足账户设置中密码策略的要求。 - 新密码不能与当前密码相同。

        :param password: The password of this KeystoneUpdateUserOption.
        :type password: str
        """
        self._password = password

    @property
    def enabled(self):
        """Gets the enabled of this KeystoneUpdateUserOption.

        是否启用IAM用户。true为启用，false为停用，默认为true。

        :return: The enabled of this KeystoneUpdateUserOption.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this KeystoneUpdateUserOption.

        是否启用IAM用户。true为启用，false为停用，默认为true。

        :param enabled: The enabled of this KeystoneUpdateUserOption.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def description(self):
        """Gets the description of this KeystoneUpdateUserOption.

        IAM用户新描述信息。

        :return: The description of this KeystoneUpdateUserOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this KeystoneUpdateUserOption.

        IAM用户新描述信息。

        :param description: The description of this KeystoneUpdateUserOption.
        :type description: str
        """
        self._description = description

    @property
    def pwd_status(self):
        """Gets the pwd_status of this KeystoneUpdateUserOption.

        IAM用户密码状态。true:需要修改密码,false:正常。

        :return: The pwd_status of this KeystoneUpdateUserOption.
        :rtype: bool
        """
        return self._pwd_status

    @pwd_status.setter
    def pwd_status(self, pwd_status):
        """Sets the pwd_status of this KeystoneUpdateUserOption.

        IAM用户密码状态。true:需要修改密码,false:正常。

        :param pwd_status: The pwd_status of this KeystoneUpdateUserOption.
        :type pwd_status: bool
        """
        self._pwd_status = pwd_status

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
        if not isinstance(other, KeystoneUpdateUserOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
