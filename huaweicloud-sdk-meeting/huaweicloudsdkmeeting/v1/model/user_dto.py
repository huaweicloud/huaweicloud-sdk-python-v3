# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserDTO:

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
        'status_code': 'int',
        'account': 'str',
        'name': 'str',
        'english_name': 'str',
        'email': 'str',
        'phone': 'str',
        'dept_name': 'str',
        'number': 'str',
        'update_time': 'int',
        'is_hard_terminal': 'bool',
        'vmr_id': 'str',
        'signature': 'str',
        'title': 'str',
        'description': 'str',
        'hide_phone': 'bool',
        'type': 'str',
        'dept_codes': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'status_code': 'statusCode',
        'account': 'account',
        'name': 'name',
        'english_name': 'englishName',
        'email': 'email',
        'phone': 'phone',
        'dept_name': 'deptName',
        'number': 'number',
        'update_time': 'updateTime',
        'is_hard_terminal': 'isHardTerminal',
        'vmr_id': 'vmrId',
        'signature': 'signature',
        'title': 'title',
        'description': 'description',
        'hide_phone': 'hidePhone',
        'type': 'type',
        'dept_codes': 'deptCodes'
    }

    def __init__(self, id=None, status_code=None, account=None, name=None, english_name=None, email=None, phone=None, dept_name=None, number=None, update_time=None, is_hard_terminal=None, vmr_id=None, signature=None, title=None, description=None, hide_phone=None, type=None, dept_codes=None):
        """UserDTO

        The model defined in huaweicloud sdk

        :param id: 用户ID。
        :type id: str
        :param status_code: 查询用户详情时, 根据不同情况，响应不同。 * 0： 查询成功且用户信息有变化， 响应会把新的信息都返回回去 * 1 ：查询成功且用户信息没有变化，响应只会返回用户ID * 2 ：用户不存在 * 3 ：无权限查询这个用户 
        :type status_code: int
        :param account: 用户帐号。
        :type account: str
        :param name: 用户名。
        :type name: str
        :param english_name: 英文名。
        :type english_name: str
        :param email: 邮箱地址。
        :type email: str
        :param phone: 用户手机。
        :type phone: str
        :param dept_name: 用户部门。
        :type dept_name: str
        :param number: 用户SIP号码。
        :type number: str
        :param update_time: 用户信息最后更新时间。
        :type update_time: int
        :param is_hard_terminal: 是否为硬终端。 &gt; 该参数将被废弃，请勿使用。 
        :type is_hard_terminal: bool
        :param vmr_id: 用户虚拟会议室ID。
        :type vmr_id: str
        :param signature: 用户签名。
        :type signature: str
        :param title: 职位。
        :type title: str
        :param description: 描述信息。
        :type description: str
        :param hide_phone: 是否隐藏手机号（如果为true，其他人查询该用户时，不会返回该用户的手机号。自己查自己是可见的）
        :type hide_phone: bool
        :param type: 类型： * NORMAL_USER&#x3D;普通用户 * HARD_TERMINAL&#x3D;硬终端用户 * WHITE_BOARD&#x3D;第三方白板 * HW_VISION_MEMBER&#x3D;智慧屏 
        :type type: str
        :param dept_codes: 部门编码列表。
        :type dept_codes: list[str]
        """
        
        

        self._id = None
        self._status_code = None
        self._account = None
        self._name = None
        self._english_name = None
        self._email = None
        self._phone = None
        self._dept_name = None
        self._number = None
        self._update_time = None
        self._is_hard_terminal = None
        self._vmr_id = None
        self._signature = None
        self._title = None
        self._description = None
        self._hide_phone = None
        self._type = None
        self._dept_codes = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status_code is not None:
            self.status_code = status_code
        if account is not None:
            self.account = account
        if name is not None:
            self.name = name
        if english_name is not None:
            self.english_name = english_name
        if email is not None:
            self.email = email
        if phone is not None:
            self.phone = phone
        if dept_name is not None:
            self.dept_name = dept_name
        if number is not None:
            self.number = number
        if update_time is not None:
            self.update_time = update_time
        if is_hard_terminal is not None:
            self.is_hard_terminal = is_hard_terminal
        if vmr_id is not None:
            self.vmr_id = vmr_id
        if signature is not None:
            self.signature = signature
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if hide_phone is not None:
            self.hide_phone = hide_phone
        if type is not None:
            self.type = type
        if dept_codes is not None:
            self.dept_codes = dept_codes

    @property
    def id(self):
        """Gets the id of this UserDTO.

        用户ID。

        :return: The id of this UserDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserDTO.

        用户ID。

        :param id: The id of this UserDTO.
        :type id: str
        """
        self._id = id

    @property
    def status_code(self):
        """Gets the status_code of this UserDTO.

        查询用户详情时, 根据不同情况，响应不同。 * 0： 查询成功且用户信息有变化， 响应会把新的信息都返回回去 * 1 ：查询成功且用户信息没有变化，响应只会返回用户ID * 2 ：用户不存在 * 3 ：无权限查询这个用户 

        :return: The status_code of this UserDTO.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this UserDTO.

        查询用户详情时, 根据不同情况，响应不同。 * 0： 查询成功且用户信息有变化， 响应会把新的信息都返回回去 * 1 ：查询成功且用户信息没有变化，响应只会返回用户ID * 2 ：用户不存在 * 3 ：无权限查询这个用户 

        :param status_code: The status_code of this UserDTO.
        :type status_code: int
        """
        self._status_code = status_code

    @property
    def account(self):
        """Gets the account of this UserDTO.

        用户帐号。

        :return: The account of this UserDTO.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this UserDTO.

        用户帐号。

        :param account: The account of this UserDTO.
        :type account: str
        """
        self._account = account

    @property
    def name(self):
        """Gets the name of this UserDTO.

        用户名。

        :return: The name of this UserDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserDTO.

        用户名。

        :param name: The name of this UserDTO.
        :type name: str
        """
        self._name = name

    @property
    def english_name(self):
        """Gets the english_name of this UserDTO.

        英文名。

        :return: The english_name of this UserDTO.
        :rtype: str
        """
        return self._english_name

    @english_name.setter
    def english_name(self, english_name):
        """Sets the english_name of this UserDTO.

        英文名。

        :param english_name: The english_name of this UserDTO.
        :type english_name: str
        """
        self._english_name = english_name

    @property
    def email(self):
        """Gets the email of this UserDTO.

        邮箱地址。

        :return: The email of this UserDTO.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserDTO.

        邮箱地址。

        :param email: The email of this UserDTO.
        :type email: str
        """
        self._email = email

    @property
    def phone(self):
        """Gets the phone of this UserDTO.

        用户手机。

        :return: The phone of this UserDTO.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this UserDTO.

        用户手机。

        :param phone: The phone of this UserDTO.
        :type phone: str
        """
        self._phone = phone

    @property
    def dept_name(self):
        """Gets the dept_name of this UserDTO.

        用户部门。

        :return: The dept_name of this UserDTO.
        :rtype: str
        """
        return self._dept_name

    @dept_name.setter
    def dept_name(self, dept_name):
        """Sets the dept_name of this UserDTO.

        用户部门。

        :param dept_name: The dept_name of this UserDTO.
        :type dept_name: str
        """
        self._dept_name = dept_name

    @property
    def number(self):
        """Gets the number of this UserDTO.

        用户SIP号码。

        :return: The number of this UserDTO.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this UserDTO.

        用户SIP号码。

        :param number: The number of this UserDTO.
        :type number: str
        """
        self._number = number

    @property
    def update_time(self):
        """Gets the update_time of this UserDTO.

        用户信息最后更新时间。

        :return: The update_time of this UserDTO.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this UserDTO.

        用户信息最后更新时间。

        :param update_time: The update_time of this UserDTO.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def is_hard_terminal(self):
        """Gets the is_hard_terminal of this UserDTO.

        是否为硬终端。 > 该参数将被废弃，请勿使用。 

        :return: The is_hard_terminal of this UserDTO.
        :rtype: bool
        """
        return self._is_hard_terminal

    @is_hard_terminal.setter
    def is_hard_terminal(self, is_hard_terminal):
        """Sets the is_hard_terminal of this UserDTO.

        是否为硬终端。 > 该参数将被废弃，请勿使用。 

        :param is_hard_terminal: The is_hard_terminal of this UserDTO.
        :type is_hard_terminal: bool
        """
        self._is_hard_terminal = is_hard_terminal

    @property
    def vmr_id(self):
        """Gets the vmr_id of this UserDTO.

        用户虚拟会议室ID。

        :return: The vmr_id of this UserDTO.
        :rtype: str
        """
        return self._vmr_id

    @vmr_id.setter
    def vmr_id(self, vmr_id):
        """Sets the vmr_id of this UserDTO.

        用户虚拟会议室ID。

        :param vmr_id: The vmr_id of this UserDTO.
        :type vmr_id: str
        """
        self._vmr_id = vmr_id

    @property
    def signature(self):
        """Gets the signature of this UserDTO.

        用户签名。

        :return: The signature of this UserDTO.
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this UserDTO.

        用户签名。

        :param signature: The signature of this UserDTO.
        :type signature: str
        """
        self._signature = signature

    @property
    def title(self):
        """Gets the title of this UserDTO.

        职位。

        :return: The title of this UserDTO.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this UserDTO.

        职位。

        :param title: The title of this UserDTO.
        :type title: str
        """
        self._title = title

    @property
    def description(self):
        """Gets the description of this UserDTO.

        描述信息。

        :return: The description of this UserDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UserDTO.

        描述信息。

        :param description: The description of this UserDTO.
        :type description: str
        """
        self._description = description

    @property
    def hide_phone(self):
        """Gets the hide_phone of this UserDTO.

        是否隐藏手机号（如果为true，其他人查询该用户时，不会返回该用户的手机号。自己查自己是可见的）

        :return: The hide_phone of this UserDTO.
        :rtype: bool
        """
        return self._hide_phone

    @hide_phone.setter
    def hide_phone(self, hide_phone):
        """Sets the hide_phone of this UserDTO.

        是否隐藏手机号（如果为true，其他人查询该用户时，不会返回该用户的手机号。自己查自己是可见的）

        :param hide_phone: The hide_phone of this UserDTO.
        :type hide_phone: bool
        """
        self._hide_phone = hide_phone

    @property
    def type(self):
        """Gets the type of this UserDTO.

        类型： * NORMAL_USER=普通用户 * HARD_TERMINAL=硬终端用户 * WHITE_BOARD=第三方白板 * HW_VISION_MEMBER=智慧屏 

        :return: The type of this UserDTO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UserDTO.

        类型： * NORMAL_USER=普通用户 * HARD_TERMINAL=硬终端用户 * WHITE_BOARD=第三方白板 * HW_VISION_MEMBER=智慧屏 

        :param type: The type of this UserDTO.
        :type type: str
        """
        self._type = type

    @property
    def dept_codes(self):
        """Gets the dept_codes of this UserDTO.

        部门编码列表。

        :return: The dept_codes of this UserDTO.
        :rtype: list[str]
        """
        return self._dept_codes

    @dept_codes.setter
    def dept_codes(self, dept_codes):
        """Sets the dept_codes of this UserDTO.

        部门编码列表。

        :param dept_codes: The dept_codes of this UserDTO.
        :type dept_codes: list[str]
        """
        self._dept_codes = dept_codes

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
        if not isinstance(other, UserDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
