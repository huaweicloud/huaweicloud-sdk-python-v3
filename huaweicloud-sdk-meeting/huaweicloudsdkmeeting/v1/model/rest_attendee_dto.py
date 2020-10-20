# coding: utf-8

import pprint
import re

import six





class RestAttendeeDTO:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'user_uuid': 'str',
        'account_id': 'str',
        'name': 'str',
        'role': 'int',
        'phone': 'str',
        'phone2': 'str',
        'phone3': 'str',
        'email': 'str',
        'sms': 'str',
        'is_mute': 'int',
        'is_auto_invite': 'int',
        'type': 'str',
        'address': 'str',
        'dept_uuid': 'str',
        'dept_name': 'str',
        'app_id': 'str'
    }

    attribute_map = {
        'user_uuid': 'userUUID',
        'account_id': 'accountId',
        'name': 'name',
        'role': 'role',
        'phone': 'phone',
        'phone2': 'phone2',
        'phone3': 'phone3',
        'email': 'email',
        'sms': 'sms',
        'is_mute': 'isMute',
        'is_auto_invite': 'isAutoInvite',
        'type': 'type',
        'address': 'address',
        'dept_uuid': 'deptUUID',
        'dept_name': 'deptName',
        'app_id': 'appId'
    }

    def __init__(self, user_uuid=None, account_id=None, name=None, role=0, phone=None, phone2=None, phone3=None, email=None, sms=None, is_mute=0, is_auto_invite=1, type=None, address=None, dept_uuid=None, dept_name=None, app_id=None):
        """RestAttendeeDTO - a model defined in huaweicloud sdk"""
        
        

        self._user_uuid = None
        self._account_id = None
        self._name = None
        self._role = None
        self._phone = None
        self._phone2 = None
        self._phone3 = None
        self._email = None
        self._sms = None
        self._is_mute = None
        self._is_auto_invite = None
        self._type = None
        self._address = None
        self._dept_uuid = None
        self._dept_name = None
        self._app_id = None
        self.discriminator = None

        if user_uuid is not None:
            self.user_uuid = user_uuid
        if account_id is not None:
            self.account_id = account_id
        if name is not None:
            self.name = name
        if role is not None:
            self.role = role
        if phone is not None:
            self.phone = phone
        if phone2 is not None:
            self.phone2 = phone2
        if phone3 is not None:
            self.phone3 = phone3
        if email is not None:
            self.email = email
        if sms is not None:
            self.sms = sms
        if is_mute is not None:
            self.is_mute = is_mute
        if is_auto_invite is not None:
            self.is_auto_invite = is_auto_invite
        if type is not None:
            self.type = type
        if address is not None:
            self.address = address
        if dept_uuid is not None:
            self.dept_uuid = dept_uuid
        if dept_name is not None:
            self.dept_name = dept_name
        if app_id is not None:
            self.app_id = app_id

    @property
    def user_uuid(self):
        """Gets the user_uuid of this RestAttendeeDTO.

        与会者的用户UUID。

        :return: The user_uuid of this RestAttendeeDTO.
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """Sets the user_uuid of this RestAttendeeDTO.

        与会者的用户UUID。

        :param user_uuid: The user_uuid of this RestAttendeeDTO.
        :type: str
        """
        self._user_uuid = user_uuid

    @property
    def account_id(self):
        """Gets the account_id of this RestAttendeeDTO.

        与会者帐号，兼容终端老版本。如果没有携带userUUID，就通过accountId查询用户信息。

        :return: The account_id of this RestAttendeeDTO.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this RestAttendeeDTO.

        与会者帐号，兼容终端老版本。如果没有携带userUUID，就通过accountId查询用户信息。

        :param account_id: The account_id of this RestAttendeeDTO.
        :type: str
        """
        self._account_id = account_id

    @property
    def name(self):
        """Gets the name of this RestAttendeeDTO.

        与会者名称或昵称，长度限制为96个字符。

        :return: The name of this RestAttendeeDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RestAttendeeDTO.

        与会者名称或昵称，长度限制为96个字符。

        :param name: The name of this RestAttendeeDTO.
        :type: str
        """
        self._name = name

    @property
    def role(self):
        """Gets the role of this RestAttendeeDTO.

        会议中的角色。默认为普通与会者。 - 0: 普通与会者。 - 1: 会议主席。 - 2: 预留字段，暂不对外开放。

        :return: The role of this RestAttendeeDTO.
        :rtype: int
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this RestAttendeeDTO.

        会议中的角色。默认为普通与会者。 - 0: 普通与会者。 - 1: 会议主席。 - 2: 预留字段，暂不对外开放。

        :param role: The role of this RestAttendeeDTO.
        :type: int
        """
        self._role = role

    @property
    def phone(self):
        """Gets the phone of this RestAttendeeDTO.

        电话号码(可支持SIP、TEL号码格式)。最大不超过127个字符。phone、email和sms三者需至少填写一个。当type为telepresence时，且设备为三屏智真，则该字段填写中屏号码。

        :return: The phone of this RestAttendeeDTO.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this RestAttendeeDTO.

        电话号码(可支持SIP、TEL号码格式)。最大不超过127个字符。phone、email和sms三者需至少填写一个。当type为telepresence时，且设备为三屏智真，则该字段填写中屏号码。

        :param phone: The phone of this RestAttendeeDTO.
        :type: str
        """
        self._phone = phone

    @property
    def phone2(self):
        """Gets the phone2 of this RestAttendeeDTO.

        预留字段，取值类型同phone。当type为telepresence时，且设备为三屏智真，则该字段填写左屏号码

        :return: The phone2 of this RestAttendeeDTO.
        :rtype: str
        """
        return self._phone2

    @phone2.setter
    def phone2(self, phone2):
        """Sets the phone2 of this RestAttendeeDTO.

        预留字段，取值类型同phone。当type为telepresence时，且设备为三屏智真，则该字段填写左屏号码

        :param phone2: The phone2 of this RestAttendeeDTO.
        :type: str
        """
        self._phone2 = phone2

    @property
    def phone3(self):
        """Gets the phone3 of this RestAttendeeDTO.

        预留字段，取值类型同phone。当type为telepresence时，且设备为三屏智真，则该字段填写右屏号码

        :return: The phone3 of this RestAttendeeDTO.
        :rtype: str
        """
        return self._phone3

    @phone3.setter
    def phone3(self, phone3):
        """Sets the phone3 of this RestAttendeeDTO.

        预留字段，取值类型同phone。当type为telepresence时，且设备为三屏智真，则该字段填写右屏号码

        :param phone3: The phone3 of this RestAttendeeDTO.
        :type: str
        """
        self._phone3 = phone3

    @property
    def email(self):
        """Gets the email of this RestAttendeeDTO.

        邮件地址。最大不超过255个字符。phone、email和sms三者需至少填写一个。

        :return: The email of this RestAttendeeDTO.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this RestAttendeeDTO.

        邮件地址。最大不超过255个字符。phone、email和sms三者需至少填写一个。

        :param email: The email of this RestAttendeeDTO.
        :type: str
        """
        self._email = email

    @property
    def sms(self):
        """Gets the sms of this RestAttendeeDTO.

        短信通知的手机号码。最大不超过32个字符。phone、email和sms三者需至少填写一个。

        :return: The sms of this RestAttendeeDTO.
        :rtype: str
        """
        return self._sms

    @sms.setter
    def sms(self, sms):
        """Sets the sms of this RestAttendeeDTO.

        短信通知的手机号码。最大不超过32个字符。phone、email和sms三者需至少填写一个。

        :param sms: The sms of this RestAttendeeDTO.
        :type: str
        """
        self._sms = sms

    @property
    def is_mute(self):
        """Gets the is_mute of this RestAttendeeDTO.

        用户入会时是否需要自动静音。默认不静音。 - 0: 不需要静音。 - 1: 需要静音。

        :return: The is_mute of this RestAttendeeDTO.
        :rtype: int
        """
        return self._is_mute

    @is_mute.setter
    def is_mute(self, is_mute):
        """Sets the is_mute of this RestAttendeeDTO.

        用户入会时是否需要自动静音。默认不静音。 - 0: 不需要静音。 - 1: 需要静音。

        :param is_mute: The is_mute of this RestAttendeeDTO.
        :type: int
        """
        self._is_mute = is_mute

    @property
    def is_auto_invite(self):
        """Gets the is_auto_invite of this RestAttendeeDTO.

        会议开始时是否自动邀请该与会者。默认自动邀请。 - 0: 不自动邀请 - 1: 自动邀请

        :return: The is_auto_invite of this RestAttendeeDTO.
        :rtype: int
        """
        return self._is_auto_invite

    @is_auto_invite.setter
    def is_auto_invite(self, is_auto_invite):
        """Sets the is_auto_invite of this RestAttendeeDTO.

        会议开始时是否自动邀请该与会者。默认自动邀请。 - 0: 不自动邀请 - 1: 自动邀请

        :param is_auto_invite: The is_auto_invite of this RestAttendeeDTO.
        :type: int
        """
        self._is_auto_invite = is_auto_invite

    @property
    def type(self):
        """Gets the type of this RestAttendeeDTO.

        默认值由会议AS定义，号码类型枚举如下： - normal: 软终端。 - telepresence: 智真。单屏、三屏智真均属此类。（预留字段） - terminal: 会议室或硬终端。 - outside: 外部与会人。 - mobile: 用户手机号码。 - telephone: 软终端用户固定电话，暂不使用。

        :return: The type of this RestAttendeeDTO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RestAttendeeDTO.

        默认值由会议AS定义，号码类型枚举如下： - normal: 软终端。 - telepresence: 智真。单屏、三屏智真均属此类。（预留字段） - terminal: 会议室或硬终端。 - outside: 外部与会人。 - mobile: 用户手机号码。 - telephone: 软终端用户固定电话，暂不使用。

        :param type: The type of this RestAttendeeDTO.
        :type: str
        """
        self._type = type

    @property
    def address(self):
        """Gets the address of this RestAttendeeDTO.

        终端所在会议室信息。（预留字段）

        :return: The address of this RestAttendeeDTO.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this RestAttendeeDTO.

        终端所在会议室信息。（预留字段）

        :param address: The address of this RestAttendeeDTO.
        :type: str
        """
        self._address = address

    @property
    def dept_uuid(self):
        """Gets the dept_uuid of this RestAttendeeDTO.

        部门ID。最大不超过64个字符。

        :return: The dept_uuid of this RestAttendeeDTO.
        :rtype: str
        """
        return self._dept_uuid

    @dept_uuid.setter
    def dept_uuid(self, dept_uuid):
        """Sets the dept_uuid of this RestAttendeeDTO.

        部门ID。最大不超过64个字符。

        :param dept_uuid: The dept_uuid of this RestAttendeeDTO.
        :type: str
        """
        self._dept_uuid = dept_uuid

    @property
    def dept_name(self):
        """Gets the dept_name of this RestAttendeeDTO.

        部门名称。最大不超过128个字符。

        :return: The dept_name of this RestAttendeeDTO.
        :rtype: str
        """
        return self._dept_name

    @dept_name.setter
    def dept_name(self, dept_name):
        """Sets the dept_name of this RestAttendeeDTO.

        部门名称。最大不超过128个字符。

        :param dept_name: The dept_name of this RestAttendeeDTO.
        :type: str
        """
        self._dept_name = dept_name

    @property
    def app_id(self):
        """Gets the app_id of this RestAttendeeDTO.

        会议Paas服务APPID。

        :return: The app_id of this RestAttendeeDTO.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this RestAttendeeDTO.

        会议Paas服务APPID。

        :param app_id: The app_id of this RestAttendeeDTO.
        :type: str
        """
        self._app_id = app_id

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
        if not isinstance(other, RestAttendeeDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
