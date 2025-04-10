# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetUserRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'role': 'str',
        'status': 'str',
        'email': 'str',
        'phone': 'str',
        'areacode': 'str',
        'is_domain_owner': 'bool',
        'create_time': 'str',
        'pwd_status': 'bool',
        'update_time': 'str',
        'source': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'role': 'role',
        'status': 'status',
        'email': 'email',
        'phone': 'phone',
        'areacode': 'areacode',
        'is_domain_owner': 'is_domain_owner',
        'create_time': 'create_time',
        'pwd_status': 'pwd_status',
        'update_time': 'update_time',
        'source': 'source'
    }

    def __init__(self, id=None, name=None, role=None, status=None, email=None, phone=None, areacode=None, is_domain_owner=None, create_time=None, pwd_status=None, update_time=None, source=None):
        r"""GetUserRsp

        The model defined in huaweicloud sdk

        :param id: 用户id
        :type id: str
        :param name: 用户名，长度4~31之间，首位不能为数字，特殊字符只能包含下划线“_”、中划线“-”和空格
        :type name: str
        :param role: 角色类型：管理员(ADMIN)、操作者(OPERATOR)
        :type role: str
        :param status: 状态
        :type status: str
        :param email: 用户邮箱，需符合邮箱格式
        :type email: str
        :param phone: 用户手机号，纯数字，长度小于等于32位。必须与国家码同时存在。
        :type phone: str
        :param areacode: 国家码。中国大陆为“0086”
        :type areacode: str
        :param is_domain_owner: 是否domain用户
        :type is_domain_owner: bool
        :param create_time: 用户创建时间，UTC时间
        :type create_time: str
        :param pwd_status: 是否需要修改密码
        :type pwd_status: bool
        :param update_time: 更新时间，UTC时间
        :type update_time: str
        :param source: 来源，PLATFORM或者IAM
        :type source: str
        """
        
        

        self._id = None
        self._name = None
        self._role = None
        self._status = None
        self._email = None
        self._phone = None
        self._areacode = None
        self._is_domain_owner = None
        self._create_time = None
        self._pwd_status = None
        self._update_time = None
        self._source = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if role is not None:
            self.role = role
        if status is not None:
            self.status = status
        if email is not None:
            self.email = email
        if phone is not None:
            self.phone = phone
        if areacode is not None:
            self.areacode = areacode
        if is_domain_owner is not None:
            self.is_domain_owner = is_domain_owner
        if create_time is not None:
            self.create_time = create_time
        if pwd_status is not None:
            self.pwd_status = pwd_status
        if update_time is not None:
            self.update_time = update_time
        if source is not None:
            self.source = source

    @property
    def id(self):
        r"""Gets the id of this GetUserRsp.

        用户id

        :return: The id of this GetUserRsp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GetUserRsp.

        用户id

        :param id: The id of this GetUserRsp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this GetUserRsp.

        用户名，长度4~31之间，首位不能为数字，特殊字符只能包含下划线“_”、中划线“-”和空格

        :return: The name of this GetUserRsp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GetUserRsp.

        用户名，长度4~31之间，首位不能为数字，特殊字符只能包含下划线“_”、中划线“-”和空格

        :param name: The name of this GetUserRsp.
        :type name: str
        """
        self._name = name

    @property
    def role(self):
        r"""Gets the role of this GetUserRsp.

        角色类型：管理员(ADMIN)、操作者(OPERATOR)

        :return: The role of this GetUserRsp.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this GetUserRsp.

        角色类型：管理员(ADMIN)、操作者(OPERATOR)

        :param role: The role of this GetUserRsp.
        :type role: str
        """
        self._role = role

    @property
    def status(self):
        r"""Gets the status of this GetUserRsp.

        状态

        :return: The status of this GetUserRsp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this GetUserRsp.

        状态

        :param status: The status of this GetUserRsp.
        :type status: str
        """
        self._status = status

    @property
    def email(self):
        r"""Gets the email of this GetUserRsp.

        用户邮箱，需符合邮箱格式

        :return: The email of this GetUserRsp.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this GetUserRsp.

        用户邮箱，需符合邮箱格式

        :param email: The email of this GetUserRsp.
        :type email: str
        """
        self._email = email

    @property
    def phone(self):
        r"""Gets the phone of this GetUserRsp.

        用户手机号，纯数字，长度小于等于32位。必须与国家码同时存在。

        :return: The phone of this GetUserRsp.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        r"""Sets the phone of this GetUserRsp.

        用户手机号，纯数字，长度小于等于32位。必须与国家码同时存在。

        :param phone: The phone of this GetUserRsp.
        :type phone: str
        """
        self._phone = phone

    @property
    def areacode(self):
        r"""Gets the areacode of this GetUserRsp.

        国家码。中国大陆为“0086”

        :return: The areacode of this GetUserRsp.
        :rtype: str
        """
        return self._areacode

    @areacode.setter
    def areacode(self, areacode):
        r"""Sets the areacode of this GetUserRsp.

        国家码。中国大陆为“0086”

        :param areacode: The areacode of this GetUserRsp.
        :type areacode: str
        """
        self._areacode = areacode

    @property
    def is_domain_owner(self):
        r"""Gets the is_domain_owner of this GetUserRsp.

        是否domain用户

        :return: The is_domain_owner of this GetUserRsp.
        :rtype: bool
        """
        return self._is_domain_owner

    @is_domain_owner.setter
    def is_domain_owner(self, is_domain_owner):
        r"""Sets the is_domain_owner of this GetUserRsp.

        是否domain用户

        :param is_domain_owner: The is_domain_owner of this GetUserRsp.
        :type is_domain_owner: bool
        """
        self._is_domain_owner = is_domain_owner

    @property
    def create_time(self):
        r"""Gets the create_time of this GetUserRsp.

        用户创建时间，UTC时间

        :return: The create_time of this GetUserRsp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this GetUserRsp.

        用户创建时间，UTC时间

        :param create_time: The create_time of this GetUserRsp.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def pwd_status(self):
        r"""Gets the pwd_status of this GetUserRsp.

        是否需要修改密码

        :return: The pwd_status of this GetUserRsp.
        :rtype: bool
        """
        return self._pwd_status

    @pwd_status.setter
    def pwd_status(self, pwd_status):
        r"""Sets the pwd_status of this GetUserRsp.

        是否需要修改密码

        :param pwd_status: The pwd_status of this GetUserRsp.
        :type pwd_status: bool
        """
        self._pwd_status = pwd_status

    @property
    def update_time(self):
        r"""Gets the update_time of this GetUserRsp.

        更新时间，UTC时间

        :return: The update_time of this GetUserRsp.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this GetUserRsp.

        更新时间，UTC时间

        :param update_time: The update_time of this GetUserRsp.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def source(self):
        r"""Gets the source of this GetUserRsp.

        来源，PLATFORM或者IAM

        :return: The source of this GetUserRsp.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this GetUserRsp.

        来源，PLATFORM或者IAM

        :param source: The source of this GetUserRsp.
        :type source: str
        """
        self._source = source

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
        if not isinstance(other, GetUserRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
