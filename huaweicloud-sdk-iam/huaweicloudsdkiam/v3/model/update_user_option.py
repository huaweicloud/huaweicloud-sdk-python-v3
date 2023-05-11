# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateUserOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_mode': 'str',
        'name': 'str',
        'password': 'str',
        'email': 'str',
        'areacode': 'str',
        'phone': 'str',
        'enabled': 'bool',
        'pwd_status': 'bool',
        'xuser_type': 'str',
        'xuser_id': 'str',
        'description': 'str'
    }

    attribute_map = {
        'access_mode': 'access_mode',
        'name': 'name',
        'password': 'password',
        'email': 'email',
        'areacode': 'areacode',
        'phone': 'phone',
        'enabled': 'enabled',
        'pwd_status': 'pwd_status',
        'xuser_type': 'xuser_type',
        'xuser_id': 'xuser_id',
        'description': 'description'
    }

    def __init__(self, access_mode=None, name=None, password=None, email=None, areacode=None, phone=None, enabled=None, pwd_status=None, xuser_type=None, xuser_id=None, description=None):
        """UpdateUserOption

        The model defined in huaweicloud sdk

        :param access_mode: IAM用户访问方式。 - default：默认访问模式，编程访问和管理控制台访问。 - programmatic：编程访问。 - console：管理控制台访问。
        :type access_mode: str
        :param name: 新IAM用户名，长度1~64之间，只能包含如下字符：大小写字母、空格、数字或特殊字符（-_.）且不能以数字开头。
        :type name: str
        :param password: IAM用户新密码。 - 系统默认密码最小长度为6字符，在6-32字符之间支持用户自定义密码长度。 - 至少包含以下四种字符中的两种： 大写字母、小写字母、数字和特殊字符。 - 必须满足账户设置中[密码策略](https://support.huaweicloud.com/usermanual-iam/iam_01_0607.html)的要求。 - 新密码不能与当前密码相同。 
        :type password: str
        :param email: IAM用户新邮箱，需符合邮箱格式，长度小于等于255字符。
        :type email: str
        :param areacode: 国家码。必须与手机号同时存在。中国大陆为“0086”。
        :type areacode: str
        :param phone: IAM用户新手机号，纯数字，长度小于等于32字符。必须与国家码同时存在。
        :type phone: str
        :param enabled: 是否启用IAM用户。true为启用，false为停用，默认为true。
        :type enabled: bool
        :param pwd_status: IAM用户密码状态。true：需要修改密码，false：正常。
        :type pwd_status: bool
        :param xuser_type: IAM用户在外部系统中的类型。长度小于等于64字符。xuser_type如果存在，则需要与同一租户中的xaccount_type、xdomain_type校验，须与xuser_id同时存在。 &gt;外部系统指与华为云对接的外部企业管理系统，xaccount_type、xaccount_id、xdomain_type、xdomain_id、xuser_type、xuser_id等参数值，无法在华为云获取，请咨询企业管理员。
        :type xuser_type: str
        :param xuser_id: IAM用户在外部系统中的ID。长度小于等于128字符，必须与xuser_type同时存在。 &gt;外部系统指与华为云对接的外部企业管理系统，xaccount_type、xaccount_id、xdomain_type、xdomain_id、xuser_type、xuser_id等参数值，无法在华为云获取，请咨询企业管理员。
        :type xuser_id: str
        :param description: IAM用户新描述信息。
        :type description: str
        """
        
        

        self._access_mode = None
        self._name = None
        self._password = None
        self._email = None
        self._areacode = None
        self._phone = None
        self._enabled = None
        self._pwd_status = None
        self._xuser_type = None
        self._xuser_id = None
        self._description = None
        self.discriminator = None

        if access_mode is not None:
            self.access_mode = access_mode
        if name is not None:
            self.name = name
        if password is not None:
            self.password = password
        if email is not None:
            self.email = email
        if areacode is not None:
            self.areacode = areacode
        if phone is not None:
            self.phone = phone
        if enabled is not None:
            self.enabled = enabled
        if pwd_status is not None:
            self.pwd_status = pwd_status
        if xuser_type is not None:
            self.xuser_type = xuser_type
        if xuser_id is not None:
            self.xuser_id = xuser_id
        if description is not None:
            self.description = description

    @property
    def access_mode(self):
        """Gets the access_mode of this UpdateUserOption.

        IAM用户访问方式。 - default：默认访问模式，编程访问和管理控制台访问。 - programmatic：编程访问。 - console：管理控制台访问。

        :return: The access_mode of this UpdateUserOption.
        :rtype: str
        """
        return self._access_mode

    @access_mode.setter
    def access_mode(self, access_mode):
        """Sets the access_mode of this UpdateUserOption.

        IAM用户访问方式。 - default：默认访问模式，编程访问和管理控制台访问。 - programmatic：编程访问。 - console：管理控制台访问。

        :param access_mode: The access_mode of this UpdateUserOption.
        :type access_mode: str
        """
        self._access_mode = access_mode

    @property
    def name(self):
        """Gets the name of this UpdateUserOption.

        新IAM用户名，长度1~64之间，只能包含如下字符：大小写字母、空格、数字或特殊字符（-_.）且不能以数字开头。

        :return: The name of this UpdateUserOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateUserOption.

        新IAM用户名，长度1~64之间，只能包含如下字符：大小写字母、空格、数字或特殊字符（-_.）且不能以数字开头。

        :param name: The name of this UpdateUserOption.
        :type name: str
        """
        self._name = name

    @property
    def password(self):
        """Gets the password of this UpdateUserOption.

        IAM用户新密码。 - 系统默认密码最小长度为6字符，在6-32字符之间支持用户自定义密码长度。 - 至少包含以下四种字符中的两种： 大写字母、小写字母、数字和特殊字符。 - 必须满足账户设置中[密码策略](https://support.huaweicloud.com/usermanual-iam/iam_01_0607.html)的要求。 - 新密码不能与当前密码相同。 

        :return: The password of this UpdateUserOption.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UpdateUserOption.

        IAM用户新密码。 - 系统默认密码最小长度为6字符，在6-32字符之间支持用户自定义密码长度。 - 至少包含以下四种字符中的两种： 大写字母、小写字母、数字和特殊字符。 - 必须满足账户设置中[密码策略](https://support.huaweicloud.com/usermanual-iam/iam_01_0607.html)的要求。 - 新密码不能与当前密码相同。 

        :param password: The password of this UpdateUserOption.
        :type password: str
        """
        self._password = password

    @property
    def email(self):
        """Gets the email of this UpdateUserOption.

        IAM用户新邮箱，需符合邮箱格式，长度小于等于255字符。

        :return: The email of this UpdateUserOption.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UpdateUserOption.

        IAM用户新邮箱，需符合邮箱格式，长度小于等于255字符。

        :param email: The email of this UpdateUserOption.
        :type email: str
        """
        self._email = email

    @property
    def areacode(self):
        """Gets the areacode of this UpdateUserOption.

        国家码。必须与手机号同时存在。中国大陆为“0086”。

        :return: The areacode of this UpdateUserOption.
        :rtype: str
        """
        return self._areacode

    @areacode.setter
    def areacode(self, areacode):
        """Sets the areacode of this UpdateUserOption.

        国家码。必须与手机号同时存在。中国大陆为“0086”。

        :param areacode: The areacode of this UpdateUserOption.
        :type areacode: str
        """
        self._areacode = areacode

    @property
    def phone(self):
        """Gets the phone of this UpdateUserOption.

        IAM用户新手机号，纯数字，长度小于等于32字符。必须与国家码同时存在。

        :return: The phone of this UpdateUserOption.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this UpdateUserOption.

        IAM用户新手机号，纯数字，长度小于等于32字符。必须与国家码同时存在。

        :param phone: The phone of this UpdateUserOption.
        :type phone: str
        """
        self._phone = phone

    @property
    def enabled(self):
        """Gets the enabled of this UpdateUserOption.

        是否启用IAM用户。true为启用，false为停用，默认为true。

        :return: The enabled of this UpdateUserOption.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this UpdateUserOption.

        是否启用IAM用户。true为启用，false为停用，默认为true。

        :param enabled: The enabled of this UpdateUserOption.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def pwd_status(self):
        """Gets the pwd_status of this UpdateUserOption.

        IAM用户密码状态。true：需要修改密码，false：正常。

        :return: The pwd_status of this UpdateUserOption.
        :rtype: bool
        """
        return self._pwd_status

    @pwd_status.setter
    def pwd_status(self, pwd_status):
        """Sets the pwd_status of this UpdateUserOption.

        IAM用户密码状态。true：需要修改密码，false：正常。

        :param pwd_status: The pwd_status of this UpdateUserOption.
        :type pwd_status: bool
        """
        self._pwd_status = pwd_status

    @property
    def xuser_type(self):
        """Gets the xuser_type of this UpdateUserOption.

        IAM用户在外部系统中的类型。长度小于等于64字符。xuser_type如果存在，则需要与同一租户中的xaccount_type、xdomain_type校验，须与xuser_id同时存在。 >外部系统指与华为云对接的外部企业管理系统，xaccount_type、xaccount_id、xdomain_type、xdomain_id、xuser_type、xuser_id等参数值，无法在华为云获取，请咨询企业管理员。

        :return: The xuser_type of this UpdateUserOption.
        :rtype: str
        """
        return self._xuser_type

    @xuser_type.setter
    def xuser_type(self, xuser_type):
        """Sets the xuser_type of this UpdateUserOption.

        IAM用户在外部系统中的类型。长度小于等于64字符。xuser_type如果存在，则需要与同一租户中的xaccount_type、xdomain_type校验，须与xuser_id同时存在。 >外部系统指与华为云对接的外部企业管理系统，xaccount_type、xaccount_id、xdomain_type、xdomain_id、xuser_type、xuser_id等参数值，无法在华为云获取，请咨询企业管理员。

        :param xuser_type: The xuser_type of this UpdateUserOption.
        :type xuser_type: str
        """
        self._xuser_type = xuser_type

    @property
    def xuser_id(self):
        """Gets the xuser_id of this UpdateUserOption.

        IAM用户在外部系统中的ID。长度小于等于128字符，必须与xuser_type同时存在。 >外部系统指与华为云对接的外部企业管理系统，xaccount_type、xaccount_id、xdomain_type、xdomain_id、xuser_type、xuser_id等参数值，无法在华为云获取，请咨询企业管理员。

        :return: The xuser_id of this UpdateUserOption.
        :rtype: str
        """
        return self._xuser_id

    @xuser_id.setter
    def xuser_id(self, xuser_id):
        """Sets the xuser_id of this UpdateUserOption.

        IAM用户在外部系统中的ID。长度小于等于128字符，必须与xuser_type同时存在。 >外部系统指与华为云对接的外部企业管理系统，xaccount_type、xaccount_id、xdomain_type、xdomain_id、xuser_type、xuser_id等参数值，无法在华为云获取，请咨询企业管理员。

        :param xuser_id: The xuser_id of this UpdateUserOption.
        :type xuser_id: str
        """
        self._xuser_id = xuser_id

    @property
    def description(self):
        """Gets the description of this UpdateUserOption.

        IAM用户新描述信息。

        :return: The description of this UpdateUserOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateUserOption.

        IAM用户新描述信息。

        :param description: The description of this UpdateUserOption.
        :type description: str
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
        if not isinstance(other, UpdateUserOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
