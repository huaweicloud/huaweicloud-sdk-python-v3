# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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

    def __init__(self, user_uuid=None, account_id=None, name=None, role=None, phone=None, phone2=None, phone3=None, email=None, sms=None, is_mute=None, is_auto_invite=None, type=None, address=None, dept_uuid=None, dept_name=None, app_id=None):
        """RestAttendeeDTO

        The model defined in huaweicloud sdk

        :param user_uuid: 与会者的用户UUID。
        :type user_uuid: str
        :param account_id: 与会者的帐号。 * 如果是帐号/密码鉴权场景：选填，表示华为云会议帐号 * 如果是APPID鉴权场景：必填，表示第三方的User ID，同时需要携带参数appId
        :type account_id: str
        :param name: 与会者名称。长度限制为96个字符。
        :type name: str
        :param role: 会议中的角色。默认为普通与会者。 - 0: 普通与会者 - 1: 会议主持人
        :type role: int
        :param phone: 号码。支持SIP号码或者手机号码。 * 如果是帐号/密码鉴权场景：必填 * 如果是APP ID鉴权场景：选填 &gt; * 号码可以通过[[查询企业通讯](https://support.huaweicloud.com/api-meeting/meeting_21_0512.html)](tag:hws)[[查询企业通讯](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0512.html)](tag:hk)接口录获取。返回的number是SIP号码，phone是手机号码 &gt; * 填SIP号码系统会呼叫对应的软终端或者硬终端；填手机号码系统会呼叫手机 &gt; * 呼叫手机需要开通PSTN权限，否则无法呼叫
        :type phone: str
        :param phone2: 预留字段，取值类型同phone。
        :type phone2: str
        :param phone3: 预留字段，取值类型同phone。
        :type phone3: str
        :param email: 邮箱地址。需要发邮件通知时填写。
        :type email: str
        :param sms: 短信通知的手机号码。需要发短信通知时填写。
        :type sms: str
        :param is_mute: 用户入会时是否需要自动静音。默认不静音。 - 0: 不需要静音 - 1: 需要静音 &gt; 仅会中邀请与会者时生效。
        :type is_mute: int
        :param is_auto_invite: 会议开始时是否自动邀请该与会者。默认值由企业级配置决定。 - 0: 不自动邀请 - 1: 自动邀请 &gt; 仅并发会议资源的随机会议ID会议才生效。
        :type is_auto_invite: int
        :param type: 终端类型，类型枚举如下： * normal: 软终端 * terminal: 会议室或硬终端 * outside: 外部与会人 * mobile: 用户手机号码 * ideahub：ideahub * board: 电子白板（SmartRooms），含Maxhub、海信大屏、IdeaHub B2 * hwvision：华为智慧屏TV
        :type type: str
        :param address: 预留字段，终端所在会议室信息。
        :type address: str
        :param dept_uuid: 部门ID。
        :type dept_uuid: str
        :param dept_name: 部门名称。最大不超过128个字符。
        :type dept_name: str
        :param app_id: App ID。如果是APP ID鉴权场景，此项必填。参考[[App ID的申请](https://support.huaweicloud.com/devg-meeting/meeting_20_0011.html#section1)](tag:hws)[[App ID的申请](https://support.huaweicloud.com/intl/zh-cn/devg-meeting/meeting_20_0011.html#section1)](tag:hk)。
        :type app_id: str
        """
        
        

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
        :type user_uuid: str
        """
        self._user_uuid = user_uuid

    @property
    def account_id(self):
        """Gets the account_id of this RestAttendeeDTO.

        与会者的帐号。 * 如果是帐号/密码鉴权场景：选填，表示华为云会议帐号 * 如果是APPID鉴权场景：必填，表示第三方的User ID，同时需要携带参数appId

        :return: The account_id of this RestAttendeeDTO.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this RestAttendeeDTO.

        与会者的帐号。 * 如果是帐号/密码鉴权场景：选填，表示华为云会议帐号 * 如果是APPID鉴权场景：必填，表示第三方的User ID，同时需要携带参数appId

        :param account_id: The account_id of this RestAttendeeDTO.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def name(self):
        """Gets the name of this RestAttendeeDTO.

        与会者名称。长度限制为96个字符。

        :return: The name of this RestAttendeeDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RestAttendeeDTO.

        与会者名称。长度限制为96个字符。

        :param name: The name of this RestAttendeeDTO.
        :type name: str
        """
        self._name = name

    @property
    def role(self):
        """Gets the role of this RestAttendeeDTO.

        会议中的角色。默认为普通与会者。 - 0: 普通与会者 - 1: 会议主持人

        :return: The role of this RestAttendeeDTO.
        :rtype: int
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this RestAttendeeDTO.

        会议中的角色。默认为普通与会者。 - 0: 普通与会者 - 1: 会议主持人

        :param role: The role of this RestAttendeeDTO.
        :type role: int
        """
        self._role = role

    @property
    def phone(self):
        """Gets the phone of this RestAttendeeDTO.

        号码。支持SIP号码或者手机号码。 * 如果是帐号/密码鉴权场景：必填 * 如果是APP ID鉴权场景：选填 > * 号码可以通过[[查询企业通讯](https://support.huaweicloud.com/api-meeting/meeting_21_0512.html)](tag:hws)[[查询企业通讯](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0512.html)](tag:hk)接口录获取。返回的number是SIP号码，phone是手机号码 > * 填SIP号码系统会呼叫对应的软终端或者硬终端；填手机号码系统会呼叫手机 > * 呼叫手机需要开通PSTN权限，否则无法呼叫

        :return: The phone of this RestAttendeeDTO.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this RestAttendeeDTO.

        号码。支持SIP号码或者手机号码。 * 如果是帐号/密码鉴权场景：必填 * 如果是APP ID鉴权场景：选填 > * 号码可以通过[[查询企业通讯](https://support.huaweicloud.com/api-meeting/meeting_21_0512.html)](tag:hws)[[查询企业通讯](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0512.html)](tag:hk)接口录获取。返回的number是SIP号码，phone是手机号码 > * 填SIP号码系统会呼叫对应的软终端或者硬终端；填手机号码系统会呼叫手机 > * 呼叫手机需要开通PSTN权限，否则无法呼叫

        :param phone: The phone of this RestAttendeeDTO.
        :type phone: str
        """
        self._phone = phone

    @property
    def phone2(self):
        """Gets the phone2 of this RestAttendeeDTO.

        预留字段，取值类型同phone。

        :return: The phone2 of this RestAttendeeDTO.
        :rtype: str
        """
        return self._phone2

    @phone2.setter
    def phone2(self, phone2):
        """Sets the phone2 of this RestAttendeeDTO.

        预留字段，取值类型同phone。

        :param phone2: The phone2 of this RestAttendeeDTO.
        :type phone2: str
        """
        self._phone2 = phone2

    @property
    def phone3(self):
        """Gets the phone3 of this RestAttendeeDTO.

        预留字段，取值类型同phone。

        :return: The phone3 of this RestAttendeeDTO.
        :rtype: str
        """
        return self._phone3

    @phone3.setter
    def phone3(self, phone3):
        """Sets the phone3 of this RestAttendeeDTO.

        预留字段，取值类型同phone。

        :param phone3: The phone3 of this RestAttendeeDTO.
        :type phone3: str
        """
        self._phone3 = phone3

    @property
    def email(self):
        """Gets the email of this RestAttendeeDTO.

        邮箱地址。需要发邮件通知时填写。

        :return: The email of this RestAttendeeDTO.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this RestAttendeeDTO.

        邮箱地址。需要发邮件通知时填写。

        :param email: The email of this RestAttendeeDTO.
        :type email: str
        """
        self._email = email

    @property
    def sms(self):
        """Gets the sms of this RestAttendeeDTO.

        短信通知的手机号码。需要发短信通知时填写。

        :return: The sms of this RestAttendeeDTO.
        :rtype: str
        """
        return self._sms

    @sms.setter
    def sms(self, sms):
        """Sets the sms of this RestAttendeeDTO.

        短信通知的手机号码。需要发短信通知时填写。

        :param sms: The sms of this RestAttendeeDTO.
        :type sms: str
        """
        self._sms = sms

    @property
    def is_mute(self):
        """Gets the is_mute of this RestAttendeeDTO.

        用户入会时是否需要自动静音。默认不静音。 - 0: 不需要静音 - 1: 需要静音 > 仅会中邀请与会者时生效。

        :return: The is_mute of this RestAttendeeDTO.
        :rtype: int
        """
        return self._is_mute

    @is_mute.setter
    def is_mute(self, is_mute):
        """Sets the is_mute of this RestAttendeeDTO.

        用户入会时是否需要自动静音。默认不静音。 - 0: 不需要静音 - 1: 需要静音 > 仅会中邀请与会者时生效。

        :param is_mute: The is_mute of this RestAttendeeDTO.
        :type is_mute: int
        """
        self._is_mute = is_mute

    @property
    def is_auto_invite(self):
        """Gets the is_auto_invite of this RestAttendeeDTO.

        会议开始时是否自动邀请该与会者。默认值由企业级配置决定。 - 0: 不自动邀请 - 1: 自动邀请 > 仅并发会议资源的随机会议ID会议才生效。

        :return: The is_auto_invite of this RestAttendeeDTO.
        :rtype: int
        """
        return self._is_auto_invite

    @is_auto_invite.setter
    def is_auto_invite(self, is_auto_invite):
        """Sets the is_auto_invite of this RestAttendeeDTO.

        会议开始时是否自动邀请该与会者。默认值由企业级配置决定。 - 0: 不自动邀请 - 1: 自动邀请 > 仅并发会议资源的随机会议ID会议才生效。

        :param is_auto_invite: The is_auto_invite of this RestAttendeeDTO.
        :type is_auto_invite: int
        """
        self._is_auto_invite = is_auto_invite

    @property
    def type(self):
        """Gets the type of this RestAttendeeDTO.

        终端类型，类型枚举如下： * normal: 软终端 * terminal: 会议室或硬终端 * outside: 外部与会人 * mobile: 用户手机号码 * ideahub：ideahub * board: 电子白板（SmartRooms），含Maxhub、海信大屏、IdeaHub B2 * hwvision：华为智慧屏TV

        :return: The type of this RestAttendeeDTO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RestAttendeeDTO.

        终端类型，类型枚举如下： * normal: 软终端 * terminal: 会议室或硬终端 * outside: 外部与会人 * mobile: 用户手机号码 * ideahub：ideahub * board: 电子白板（SmartRooms），含Maxhub、海信大屏、IdeaHub B2 * hwvision：华为智慧屏TV

        :param type: The type of this RestAttendeeDTO.
        :type type: str
        """
        self._type = type

    @property
    def address(self):
        """Gets the address of this RestAttendeeDTO.

        预留字段，终端所在会议室信息。

        :return: The address of this RestAttendeeDTO.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this RestAttendeeDTO.

        预留字段，终端所在会议室信息。

        :param address: The address of this RestAttendeeDTO.
        :type address: str
        """
        self._address = address

    @property
    def dept_uuid(self):
        """Gets the dept_uuid of this RestAttendeeDTO.

        部门ID。

        :return: The dept_uuid of this RestAttendeeDTO.
        :rtype: str
        """
        return self._dept_uuid

    @dept_uuid.setter
    def dept_uuid(self, dept_uuid):
        """Sets the dept_uuid of this RestAttendeeDTO.

        部门ID。

        :param dept_uuid: The dept_uuid of this RestAttendeeDTO.
        :type dept_uuid: str
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
        :type dept_name: str
        """
        self._dept_name = dept_name

    @property
    def app_id(self):
        """Gets the app_id of this RestAttendeeDTO.

        App ID。如果是APP ID鉴权场景，此项必填。参考[[App ID的申请](https://support.huaweicloud.com/devg-meeting/meeting_20_0011.html#section1)](tag:hws)[[App ID的申请](https://support.huaweicloud.com/intl/zh-cn/devg-meeting/meeting_20_0011.html#section1)](tag:hk)。

        :return: The app_id of this RestAttendeeDTO.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this RestAttendeeDTO.

        App ID。如果是APP ID鉴权场景，此项必填。参考[[App ID的申请](https://support.huaweicloud.com/devg-meeting/meeting_20_0011.html#section1)](tag:hws)[[App ID的申请](https://support.huaweicloud.com/intl/zh-cn/devg-meeting/meeting_20_0011.html#section1)](tag:hk)。

        :param app_id: The app_id of this RestAttendeeDTO.
        :type app_id: str
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
        if not isinstance(other, RestAttendeeDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
