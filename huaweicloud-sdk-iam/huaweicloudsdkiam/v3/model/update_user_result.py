# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateUserResult:

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
        'pwd_status': 'bool',
        'xuser_id': 'str',
        'xuser_type': 'str',
        'description': 'str',
        'name': 'str',
        'phone': 'str',
        'domain_id': 'str',
        'enabled': 'bool',
        'areacode': 'str',
        'email': 'str',
        'id': 'str',
        'links': 'LinksSelf',
        'password_expires_at': 'str',
        'create_time': 'str',
        'xdomain_id': 'str',
        'xdomain_type': 'str',
        'is_domain_owner': 'bool'
    }

    attribute_map = {
        'access_mode': 'access_mode',
        'pwd_status': 'pwd_status',
        'xuser_id': 'xuser_id',
        'xuser_type': 'xuser_type',
        'description': 'description',
        'name': 'name',
        'phone': 'phone',
        'domain_id': 'domain_id',
        'enabled': 'enabled',
        'areacode': 'areacode',
        'email': 'email',
        'id': 'id',
        'links': 'links',
        'password_expires_at': 'password_expires_at',
        'create_time': 'create_time',
        'xdomain_id': 'xdomain_id',
        'xdomain_type': 'xdomain_type',
        'is_domain_owner': 'is_domain_owner'
    }

    def __init__(self, access_mode=None, pwd_status=None, xuser_id=None, xuser_type=None, description=None, name=None, phone=None, domain_id=None, enabled=None, areacode=None, email=None, id=None, links=None, password_expires_at=None, create_time=None, xdomain_id=None, xdomain_type=None, is_domain_owner=None):
        r"""UpdateUserResult

        The model defined in huaweicloud sdk

        :param access_mode: IAM用户访问方式。 - default：默认访问模式，编程访问和管理控制台访问。 - programmatic：编程访问。 - console：管理控制台访问。
        :type access_mode: str
        :param pwd_status: IAM用户密码状态。true：需要修改密码，false：正常。
        :type pwd_status: bool
        :param xuser_id: IAM用户在外部系统中的ID。 &gt;外部系统指与华为云对接的外部企业管理系统，xaccount_type、xaccount_id、xdomain_type、xdomain_id、xuser_type、xuser_id等参数值，无法在华为云获取，请咨询企业管理员。
        :type xuser_id: str
        :param xuser_type: IAM用户在外部系统中的类型。 &gt;外部系统指与华为云对接的外部企业管理系统，xaccount_type、xaccount_id、xdomain_type、xdomain_id、xuser_type、xuser_id等参数值，无法在华为云获取，请咨询企业管理员。
        :type xuser_type: str
        :param description: IAM用户的新描述信息。
        :type description: str
        :param name: IAM用户新用户名，长度1~64之间，只能包含如下字符：大小写字母、空格、数字或特殊字符（-_.）且不能以数字开头。
        :type name: str
        :param phone: IAM用户新手机号，纯数字，长度小于等于32字符。必须与国家码同时存在。
        :type phone: str
        :param domain_id: IAM用户所属账号ID。
        :type domain_id: str
        :param enabled: 是否启用IAM用户。true为启用，false为停用，默认为true。
        :type enabled: bool
        :param areacode: 国家码。中国大陆为“0086”。
        :type areacode: str
        :param email: IAM用户新邮箱。
        :type email: str
        :param id: IAM用户ID。
        :type id: str
        :param links: 
        :type links: :class:`huaweicloudsdkiam.v3.LinksSelf`
        :param password_expires_at: 密码过期时间（UTC时间），“null”表示密码不过期。
        :type password_expires_at: str
        :param create_time: UTC时间，格式为YYYY-MM-DDTHH:mm:ss.ssssss，日期和时间戳格式如：2023-06-28T08:56:33.710000。
        :type create_time: str
        :param xdomain_id: IAM用户在外部系统中的ID。 &gt;外部系统指与华为云对接的外部企业管理系统，xaccount_type、xaccount_id、xdomain_type、xdomain_id、xuser_type、xuser_id等参数值，无法在华为云获取，请咨询企业管理员。
        :type xdomain_id: str
        :param xdomain_type: IAM用户在外部系统中的类型。 &gt;外部系统指与华为云对接的外部企业管理系统，xaccount_type、xaccount_id、xdomain_type、xdomain_id、xuser_type、xuser_id等参数值，无法在华为云获取，请咨询企业管理员。 
        :type xdomain_type: str
        :param is_domain_owner: IAM用户是否为账号管理员。
        :type is_domain_owner: bool
        """
        
        

        self._access_mode = None
        self._pwd_status = None
        self._xuser_id = None
        self._xuser_type = None
        self._description = None
        self._name = None
        self._phone = None
        self._domain_id = None
        self._enabled = None
        self._areacode = None
        self._email = None
        self._id = None
        self._links = None
        self._password_expires_at = None
        self._create_time = None
        self._xdomain_id = None
        self._xdomain_type = None
        self._is_domain_owner = None
        self.discriminator = None

        if access_mode is not None:
            self.access_mode = access_mode
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
        self.domain_id = domain_id
        self.enabled = enabled
        if areacode is not None:
            self.areacode = areacode
        if email is not None:
            self.email = email
        self.id = id
        self.links = links
        if password_expires_at is not None:
            self.password_expires_at = password_expires_at
        if create_time is not None:
            self.create_time = create_time
        if xdomain_id is not None:
            self.xdomain_id = xdomain_id
        if xdomain_type is not None:
            self.xdomain_type = xdomain_type
        if is_domain_owner is not None:
            self.is_domain_owner = is_domain_owner

    @property
    def access_mode(self):
        r"""Gets the access_mode of this UpdateUserResult.

        IAM用户访问方式。 - default：默认访问模式，编程访问和管理控制台访问。 - programmatic：编程访问。 - console：管理控制台访问。

        :return: The access_mode of this UpdateUserResult.
        :rtype: str
        """
        return self._access_mode

    @access_mode.setter
    def access_mode(self, access_mode):
        r"""Sets the access_mode of this UpdateUserResult.

        IAM用户访问方式。 - default：默认访问模式，编程访问和管理控制台访问。 - programmatic：编程访问。 - console：管理控制台访问。

        :param access_mode: The access_mode of this UpdateUserResult.
        :type access_mode: str
        """
        self._access_mode = access_mode

    @property
    def pwd_status(self):
        r"""Gets the pwd_status of this UpdateUserResult.

        IAM用户密码状态。true：需要修改密码，false：正常。

        :return: The pwd_status of this UpdateUserResult.
        :rtype: bool
        """
        return self._pwd_status

    @pwd_status.setter
    def pwd_status(self, pwd_status):
        r"""Sets the pwd_status of this UpdateUserResult.

        IAM用户密码状态。true：需要修改密码，false：正常。

        :param pwd_status: The pwd_status of this UpdateUserResult.
        :type pwd_status: bool
        """
        self._pwd_status = pwd_status

    @property
    def xuser_id(self):
        r"""Gets the xuser_id of this UpdateUserResult.

        IAM用户在外部系统中的ID。 >外部系统指与华为云对接的外部企业管理系统，xaccount_type、xaccount_id、xdomain_type、xdomain_id、xuser_type、xuser_id等参数值，无法在华为云获取，请咨询企业管理员。

        :return: The xuser_id of this UpdateUserResult.
        :rtype: str
        """
        return self._xuser_id

    @xuser_id.setter
    def xuser_id(self, xuser_id):
        r"""Sets the xuser_id of this UpdateUserResult.

        IAM用户在外部系统中的ID。 >外部系统指与华为云对接的外部企业管理系统，xaccount_type、xaccount_id、xdomain_type、xdomain_id、xuser_type、xuser_id等参数值，无法在华为云获取，请咨询企业管理员。

        :param xuser_id: The xuser_id of this UpdateUserResult.
        :type xuser_id: str
        """
        self._xuser_id = xuser_id

    @property
    def xuser_type(self):
        r"""Gets the xuser_type of this UpdateUserResult.

        IAM用户在外部系统中的类型。 >外部系统指与华为云对接的外部企业管理系统，xaccount_type、xaccount_id、xdomain_type、xdomain_id、xuser_type、xuser_id等参数值，无法在华为云获取，请咨询企业管理员。

        :return: The xuser_type of this UpdateUserResult.
        :rtype: str
        """
        return self._xuser_type

    @xuser_type.setter
    def xuser_type(self, xuser_type):
        r"""Sets the xuser_type of this UpdateUserResult.

        IAM用户在外部系统中的类型。 >外部系统指与华为云对接的外部企业管理系统，xaccount_type、xaccount_id、xdomain_type、xdomain_id、xuser_type、xuser_id等参数值，无法在华为云获取，请咨询企业管理员。

        :param xuser_type: The xuser_type of this UpdateUserResult.
        :type xuser_type: str
        """
        self._xuser_type = xuser_type

    @property
    def description(self):
        r"""Gets the description of this UpdateUserResult.

        IAM用户的新描述信息。

        :return: The description of this UpdateUserResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateUserResult.

        IAM用户的新描述信息。

        :param description: The description of this UpdateUserResult.
        :type description: str
        """
        self._description = description

    @property
    def name(self):
        r"""Gets the name of this UpdateUserResult.

        IAM用户新用户名，长度1~64之间，只能包含如下字符：大小写字母、空格、数字或特殊字符（-_.）且不能以数字开头。

        :return: The name of this UpdateUserResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateUserResult.

        IAM用户新用户名，长度1~64之间，只能包含如下字符：大小写字母、空格、数字或特殊字符（-_.）且不能以数字开头。

        :param name: The name of this UpdateUserResult.
        :type name: str
        """
        self._name = name

    @property
    def phone(self):
        r"""Gets the phone of this UpdateUserResult.

        IAM用户新手机号，纯数字，长度小于等于32字符。必须与国家码同时存在。

        :return: The phone of this UpdateUserResult.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        r"""Sets the phone of this UpdateUserResult.

        IAM用户新手机号，纯数字，长度小于等于32字符。必须与国家码同时存在。

        :param phone: The phone of this UpdateUserResult.
        :type phone: str
        """
        self._phone = phone

    @property
    def domain_id(self):
        r"""Gets the domain_id of this UpdateUserResult.

        IAM用户所属账号ID。

        :return: The domain_id of this UpdateUserResult.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this UpdateUserResult.

        IAM用户所属账号ID。

        :param domain_id: The domain_id of this UpdateUserResult.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def enabled(self):
        r"""Gets the enabled of this UpdateUserResult.

        是否启用IAM用户。true为启用，false为停用，默认为true。

        :return: The enabled of this UpdateUserResult.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this UpdateUserResult.

        是否启用IAM用户。true为启用，false为停用，默认为true。

        :param enabled: The enabled of this UpdateUserResult.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def areacode(self):
        r"""Gets the areacode of this UpdateUserResult.

        国家码。中国大陆为“0086”。

        :return: The areacode of this UpdateUserResult.
        :rtype: str
        """
        return self._areacode

    @areacode.setter
    def areacode(self, areacode):
        r"""Sets the areacode of this UpdateUserResult.

        国家码。中国大陆为“0086”。

        :param areacode: The areacode of this UpdateUserResult.
        :type areacode: str
        """
        self._areacode = areacode

    @property
    def email(self):
        r"""Gets the email of this UpdateUserResult.

        IAM用户新邮箱。

        :return: The email of this UpdateUserResult.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this UpdateUserResult.

        IAM用户新邮箱。

        :param email: The email of this UpdateUserResult.
        :type email: str
        """
        self._email = email

    @property
    def id(self):
        r"""Gets the id of this UpdateUserResult.

        IAM用户ID。

        :return: The id of this UpdateUserResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateUserResult.

        IAM用户ID。

        :param id: The id of this UpdateUserResult.
        :type id: str
        """
        self._id = id

    @property
    def links(self):
        r"""Gets the links of this UpdateUserResult.

        :return: The links of this UpdateUserResult.
        :rtype: :class:`huaweicloudsdkiam.v3.LinksSelf`
        """
        return self._links

    @links.setter
    def links(self, links):
        r"""Sets the links of this UpdateUserResult.

        :param links: The links of this UpdateUserResult.
        :type links: :class:`huaweicloudsdkiam.v3.LinksSelf`
        """
        self._links = links

    @property
    def password_expires_at(self):
        r"""Gets the password_expires_at of this UpdateUserResult.

        密码过期时间（UTC时间），“null”表示密码不过期。

        :return: The password_expires_at of this UpdateUserResult.
        :rtype: str
        """
        return self._password_expires_at

    @password_expires_at.setter
    def password_expires_at(self, password_expires_at):
        r"""Sets the password_expires_at of this UpdateUserResult.

        密码过期时间（UTC时间），“null”表示密码不过期。

        :param password_expires_at: The password_expires_at of this UpdateUserResult.
        :type password_expires_at: str
        """
        self._password_expires_at = password_expires_at

    @property
    def create_time(self):
        r"""Gets the create_time of this UpdateUserResult.

        UTC时间，格式为YYYY-MM-DDTHH:mm:ss.ssssss，日期和时间戳格式如：2023-06-28T08:56:33.710000。

        :return: The create_time of this UpdateUserResult.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this UpdateUserResult.

        UTC时间，格式为YYYY-MM-DDTHH:mm:ss.ssssss，日期和时间戳格式如：2023-06-28T08:56:33.710000。

        :param create_time: The create_time of this UpdateUserResult.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def xdomain_id(self):
        r"""Gets the xdomain_id of this UpdateUserResult.

        IAM用户在外部系统中的ID。 >外部系统指与华为云对接的外部企业管理系统，xaccount_type、xaccount_id、xdomain_type、xdomain_id、xuser_type、xuser_id等参数值，无法在华为云获取，请咨询企业管理员。

        :return: The xdomain_id of this UpdateUserResult.
        :rtype: str
        """
        return self._xdomain_id

    @xdomain_id.setter
    def xdomain_id(self, xdomain_id):
        r"""Sets the xdomain_id of this UpdateUserResult.

        IAM用户在外部系统中的ID。 >外部系统指与华为云对接的外部企业管理系统，xaccount_type、xaccount_id、xdomain_type、xdomain_id、xuser_type、xuser_id等参数值，无法在华为云获取，请咨询企业管理员。

        :param xdomain_id: The xdomain_id of this UpdateUserResult.
        :type xdomain_id: str
        """
        self._xdomain_id = xdomain_id

    @property
    def xdomain_type(self):
        r"""Gets the xdomain_type of this UpdateUserResult.

        IAM用户在外部系统中的类型。 >外部系统指与华为云对接的外部企业管理系统，xaccount_type、xaccount_id、xdomain_type、xdomain_id、xuser_type、xuser_id等参数值，无法在华为云获取，请咨询企业管理员。 

        :return: The xdomain_type of this UpdateUserResult.
        :rtype: str
        """
        return self._xdomain_type

    @xdomain_type.setter
    def xdomain_type(self, xdomain_type):
        r"""Sets the xdomain_type of this UpdateUserResult.

        IAM用户在外部系统中的类型。 >外部系统指与华为云对接的外部企业管理系统，xaccount_type、xaccount_id、xdomain_type、xdomain_id、xuser_type、xuser_id等参数值，无法在华为云获取，请咨询企业管理员。 

        :param xdomain_type: The xdomain_type of this UpdateUserResult.
        :type xdomain_type: str
        """
        self._xdomain_type = xdomain_type

    @property
    def is_domain_owner(self):
        r"""Gets the is_domain_owner of this UpdateUserResult.

        IAM用户是否为账号管理员。

        :return: The is_domain_owner of this UpdateUserResult.
        :rtype: bool
        """
        return self._is_domain_owner

    @is_domain_owner.setter
    def is_domain_owner(self, is_domain_owner):
        r"""Sets the is_domain_owner of this UpdateUserResult.

        IAM用户是否为账号管理员。

        :param is_domain_owner: The is_domain_owner of this UpdateUserResult.
        :type is_domain_owner: bool
        """
        self._is_domain_owner = is_domain_owner

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
        if not isinstance(other, UpdateUserResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
