# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowUserResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enabled': 'bool',
        'id': 'str',
        'domain_id': 'str',
        'name': 'str',
        'links': 'Links',
        'xuser_id': 'str',
        'xuser_type': 'str',
        'areacode': 'str',
        'email': 'str',
        'phone': 'str',
        'pwd_status': 'bool',
        'update_time': 'str',
        'create_time': 'str',
        'last_login_time': 'str',
        'pwd_strength': 'str',
        'is_domain_owner': 'bool',
        'access_mode': 'str',
        'description': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'id': 'id',
        'domain_id': 'domain_id',
        'name': 'name',
        'links': 'links',
        'xuser_id': 'xuser_id',
        'xuser_type': 'xuser_type',
        'areacode': 'areacode',
        'email': 'email',
        'phone': 'phone',
        'pwd_status': 'pwd_status',
        'update_time': 'update_time',
        'create_time': 'create_time',
        'last_login_time': 'last_login_time',
        'pwd_strength': 'pwd_strength',
        'is_domain_owner': 'is_domain_owner',
        'access_mode': 'access_mode',
        'description': 'description'
    }

    def __init__(self, enabled=None, id=None, domain_id=None, name=None, links=None, xuser_id=None, xuser_type=None, areacode=None, email=None, phone=None, pwd_status=None, update_time=None, create_time=None, last_login_time=None, pwd_strength=None, is_domain_owner=None, access_mode=None, description=None):
        """ShowUserResult

        The model defined in huaweicloud sdk

        :param enabled: IAM用户是否启用。true表示启用，false表示停用，默认为true。
        :type enabled: bool
        :param id: IAM用户ID。
        :type id: str
        :param domain_id: IAM用户所属账号ID。
        :type domain_id: str
        :param name: IAM用户名。
        :type name: str
        :param links: 
        :type links: :class:`huaweicloudsdkiam.v3.Links`
        :param xuser_id: IAM用户在外部系统中的ID。
        :type xuser_id: str
        :param xuser_type: IAM用户在外部系统中的类型。
        :type xuser_type: str
        :param areacode: IAM用户手机号的国家码。
        :type areacode: str
        :param email: IAM用户邮箱。
        :type email: str
        :param phone: IAM用户手机号。
        :type phone: str
        :param pwd_status: IAM用户密码状态。true：需要修改密码，false：正常。
        :type pwd_status: bool
        :param update_time: IAM用户更新时间。
        :type update_time: str
        :param create_time: IAM用户创建时间。
        :type create_time: str
        :param last_login_time: IAM用户最后登录时间。
        :type last_login_time: str
        :param pwd_strength: IAM用户密码强度。结果为Low/Middle/High/None，分别表示密码强度低/中/高/无。
        :type pwd_strength: str
        :param is_domain_owner: IAM用户是否为根用户。
        :type is_domain_owner: bool
        :param access_mode: IAM用户访问模式。
        :type access_mode: str
        :param description: IAM用户描述信息
        :type description: str
        """
        
        

        self._enabled = None
        self._id = None
        self._domain_id = None
        self._name = None
        self._links = None
        self._xuser_id = None
        self._xuser_type = None
        self._areacode = None
        self._email = None
        self._phone = None
        self._pwd_status = None
        self._update_time = None
        self._create_time = None
        self._last_login_time = None
        self._pwd_strength = None
        self._is_domain_owner = None
        self._access_mode = None
        self._description = None
        self.discriminator = None

        self.enabled = enabled
        self.id = id
        self.domain_id = domain_id
        self.name = name
        self.links = links
        if xuser_id is not None:
            self.xuser_id = xuser_id
        if xuser_type is not None:
            self.xuser_type = xuser_type
        if areacode is not None:
            self.areacode = areacode
        if email is not None:
            self.email = email
        if phone is not None:
            self.phone = phone
        if pwd_status is not None:
            self.pwd_status = pwd_status
        if update_time is not None:
            self.update_time = update_time
        if create_time is not None:
            self.create_time = create_time
        if last_login_time is not None:
            self.last_login_time = last_login_time
        if pwd_strength is not None:
            self.pwd_strength = pwd_strength
        self.is_domain_owner = is_domain_owner
        self.access_mode = access_mode
        self.description = description

    @property
    def enabled(self):
        """Gets the enabled of this ShowUserResult.

        IAM用户是否启用。true表示启用，false表示停用，默认为true。

        :return: The enabled of this ShowUserResult.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ShowUserResult.

        IAM用户是否启用。true表示启用，false表示停用，默认为true。

        :param enabled: The enabled of this ShowUserResult.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def id(self):
        """Gets the id of this ShowUserResult.

        IAM用户ID。

        :return: The id of this ShowUserResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowUserResult.

        IAM用户ID。

        :param id: The id of this ShowUserResult.
        :type id: str
        """
        self._id = id

    @property
    def domain_id(self):
        """Gets the domain_id of this ShowUserResult.

        IAM用户所属账号ID。

        :return: The domain_id of this ShowUserResult.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ShowUserResult.

        IAM用户所属账号ID。

        :param domain_id: The domain_id of this ShowUserResult.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def name(self):
        """Gets the name of this ShowUserResult.

        IAM用户名。

        :return: The name of this ShowUserResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowUserResult.

        IAM用户名。

        :param name: The name of this ShowUserResult.
        :type name: str
        """
        self._name = name

    @property
    def links(self):
        """Gets the links of this ShowUserResult.

        :return: The links of this ShowUserResult.
        :rtype: :class:`huaweicloudsdkiam.v3.Links`
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ShowUserResult.

        :param links: The links of this ShowUserResult.
        :type links: :class:`huaweicloudsdkiam.v3.Links`
        """
        self._links = links

    @property
    def xuser_id(self):
        """Gets the xuser_id of this ShowUserResult.

        IAM用户在外部系统中的ID。

        :return: The xuser_id of this ShowUserResult.
        :rtype: str
        """
        return self._xuser_id

    @xuser_id.setter
    def xuser_id(self, xuser_id):
        """Sets the xuser_id of this ShowUserResult.

        IAM用户在外部系统中的ID。

        :param xuser_id: The xuser_id of this ShowUserResult.
        :type xuser_id: str
        """
        self._xuser_id = xuser_id

    @property
    def xuser_type(self):
        """Gets the xuser_type of this ShowUserResult.

        IAM用户在外部系统中的类型。

        :return: The xuser_type of this ShowUserResult.
        :rtype: str
        """
        return self._xuser_type

    @xuser_type.setter
    def xuser_type(self, xuser_type):
        """Sets the xuser_type of this ShowUserResult.

        IAM用户在外部系统中的类型。

        :param xuser_type: The xuser_type of this ShowUserResult.
        :type xuser_type: str
        """
        self._xuser_type = xuser_type

    @property
    def areacode(self):
        """Gets the areacode of this ShowUserResult.

        IAM用户手机号的国家码。

        :return: The areacode of this ShowUserResult.
        :rtype: str
        """
        return self._areacode

    @areacode.setter
    def areacode(self, areacode):
        """Sets the areacode of this ShowUserResult.

        IAM用户手机号的国家码。

        :param areacode: The areacode of this ShowUserResult.
        :type areacode: str
        """
        self._areacode = areacode

    @property
    def email(self):
        """Gets the email of this ShowUserResult.

        IAM用户邮箱。

        :return: The email of this ShowUserResult.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ShowUserResult.

        IAM用户邮箱。

        :param email: The email of this ShowUserResult.
        :type email: str
        """
        self._email = email

    @property
    def phone(self):
        """Gets the phone of this ShowUserResult.

        IAM用户手机号。

        :return: The phone of this ShowUserResult.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this ShowUserResult.

        IAM用户手机号。

        :param phone: The phone of this ShowUserResult.
        :type phone: str
        """
        self._phone = phone

    @property
    def pwd_status(self):
        """Gets the pwd_status of this ShowUserResult.

        IAM用户密码状态。true：需要修改密码，false：正常。

        :return: The pwd_status of this ShowUserResult.
        :rtype: bool
        """
        return self._pwd_status

    @pwd_status.setter
    def pwd_status(self, pwd_status):
        """Sets the pwd_status of this ShowUserResult.

        IAM用户密码状态。true：需要修改密码，false：正常。

        :param pwd_status: The pwd_status of this ShowUserResult.
        :type pwd_status: bool
        """
        self._pwd_status = pwd_status

    @property
    def update_time(self):
        """Gets the update_time of this ShowUserResult.

        IAM用户更新时间。

        :return: The update_time of this ShowUserResult.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowUserResult.

        IAM用户更新时间。

        :param update_time: The update_time of this ShowUserResult.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def create_time(self):
        """Gets the create_time of this ShowUserResult.

        IAM用户创建时间。

        :return: The create_time of this ShowUserResult.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowUserResult.

        IAM用户创建时间。

        :param create_time: The create_time of this ShowUserResult.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def last_login_time(self):
        """Gets the last_login_time of this ShowUserResult.

        IAM用户最后登录时间。

        :return: The last_login_time of this ShowUserResult.
        :rtype: str
        """
        return self._last_login_time

    @last_login_time.setter
    def last_login_time(self, last_login_time):
        """Sets the last_login_time of this ShowUserResult.

        IAM用户最后登录时间。

        :param last_login_time: The last_login_time of this ShowUserResult.
        :type last_login_time: str
        """
        self._last_login_time = last_login_time

    @property
    def pwd_strength(self):
        """Gets the pwd_strength of this ShowUserResult.

        IAM用户密码强度。结果为Low/Middle/High/None，分别表示密码强度低/中/高/无。

        :return: The pwd_strength of this ShowUserResult.
        :rtype: str
        """
        return self._pwd_strength

    @pwd_strength.setter
    def pwd_strength(self, pwd_strength):
        """Sets the pwd_strength of this ShowUserResult.

        IAM用户密码强度。结果为Low/Middle/High/None，分别表示密码强度低/中/高/无。

        :param pwd_strength: The pwd_strength of this ShowUserResult.
        :type pwd_strength: str
        """
        self._pwd_strength = pwd_strength

    @property
    def is_domain_owner(self):
        """Gets the is_domain_owner of this ShowUserResult.

        IAM用户是否为根用户。

        :return: The is_domain_owner of this ShowUserResult.
        :rtype: bool
        """
        return self._is_domain_owner

    @is_domain_owner.setter
    def is_domain_owner(self, is_domain_owner):
        """Sets the is_domain_owner of this ShowUserResult.

        IAM用户是否为根用户。

        :param is_domain_owner: The is_domain_owner of this ShowUserResult.
        :type is_domain_owner: bool
        """
        self._is_domain_owner = is_domain_owner

    @property
    def access_mode(self):
        """Gets the access_mode of this ShowUserResult.

        IAM用户访问模式。

        :return: The access_mode of this ShowUserResult.
        :rtype: str
        """
        return self._access_mode

    @access_mode.setter
    def access_mode(self, access_mode):
        """Sets the access_mode of this ShowUserResult.

        IAM用户访问模式。

        :param access_mode: The access_mode of this ShowUserResult.
        :type access_mode: str
        """
        self._access_mode = access_mode

    @property
    def description(self):
        """Gets the description of this ShowUserResult.

        IAM用户描述信息

        :return: The description of this ShowUserResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowUserResult.

        IAM用户描述信息

        :param description: The description of this ShowUserResult.
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
        if not isinstance(other, ShowUserResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
