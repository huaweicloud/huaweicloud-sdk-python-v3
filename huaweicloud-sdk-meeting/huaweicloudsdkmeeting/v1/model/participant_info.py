# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ParticipantInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'participant_id': 'str',
        'name': 'str',
        'subscriber_id': 'str',
        'role': 'int',
        'state': 'str',
        'address': 'str',
        'attendee_type': 'str',
        'account_id': 'str',
        'phone2': 'str',
        'phone3': 'str',
        'email': 'str',
        'sms': 'str',
        'dept_name': 'str',
        'user_uuid': 'str',
        'app_id': 'str',
        'is_auto_invite': 'int',
        'is_not_overlay_pid_name': 'bool'
    }

    attribute_map = {
        'participant_id': 'participantID',
        'name': 'name',
        'subscriber_id': 'subscriberID',
        'role': 'role',
        'state': 'state',
        'address': 'address',
        'attendee_type': 'attendeeType',
        'account_id': 'accountId',
        'phone2': 'phone2',
        'phone3': 'phone3',
        'email': 'email',
        'sms': 'sms',
        'dept_name': 'deptName',
        'user_uuid': 'userUUID',
        'app_id': 'appId',
        'is_auto_invite': 'isAutoInvite',
        'is_not_overlay_pid_name': 'isNotOverlayPidName'
    }

    def __init__(self, participant_id=None, name=None, subscriber_id=None, role=None, state=None, address=None, attendee_type=None, account_id=None, phone2=None, phone3=None, email=None, sms=None, dept_name=None, user_uuid=None, app_id=None, is_auto_invite=None, is_not_overlay_pid_name=None):
        """ParticipantInfo

        The model defined in huaweicloud sdk

        :param participant_id: 与会者的号码。
        :type participant_id: str
        :param name: 与会者的名称。
        :type name: str
        :param subscriber_id: 与会者的号码（预留字段）。
        :type subscriber_id: str
        :param role: 与会者的角色。 - 1: 会议主持人 - 0: 普通与会者
        :type role: int
        :param state: 用户状态。目前固定返回MEETTING。
        :type state: str
        :param address: 终端所在会议室信息（预留字段）。
        :type address: str
        :param attendee_type: 与会者终端类型。 - normal: 软终端。 - terminal: 会议室或硬终端。 - outside: 外部与会人。 - mobile: 用户手机号码。
        :type attendee_type: str
        :param account_id: 预订者的帐号。 * 如果是帐号/密码鉴权场景，表示华为云会议帐号 * 如果是APP ID鉴权场景，表示第三方的User ID 
        :type account_id: str
        :param phone2: 预留字段。
        :type phone2: str
        :param phone3: 预留字段。
        :type phone3: str
        :param email: 邮箱地址。
        :type email: str
        :param sms: 短信通知的手机号码。
        :type sms: str
        :param dept_name: 部门名称。
        :type dept_name: str
        :param user_uuid: 预订者的用户UUID。
        :type user_uuid: str
        :param app_id: App ID。参考[[App ID的申请](https://support.huaweicloud.com/devg-meeting/meeting_20_0011.html#section1)](tag:hws)[[App ID的申请](https://support.huaweicloud.com/intl/zh-cn/devg-meeting/meeting_20_0011.html#section1)](tag:hk)。
        :type app_id: str
        :param is_auto_invite: 会议开始时是否自动邀请该与会者。默认值由企业级配置决定。 * 0： 不自动邀请 * 1： 自动邀请 
        :type is_auto_invite: int
        :param is_not_overlay_pid_name: 是否不叠加会场名（VDC场景下适用）。
        :type is_not_overlay_pid_name: bool
        """
        
        

        self._participant_id = None
        self._name = None
        self._subscriber_id = None
        self._role = None
        self._state = None
        self._address = None
        self._attendee_type = None
        self._account_id = None
        self._phone2 = None
        self._phone3 = None
        self._email = None
        self._sms = None
        self._dept_name = None
        self._user_uuid = None
        self._app_id = None
        self._is_auto_invite = None
        self._is_not_overlay_pid_name = None
        self.discriminator = None

        if participant_id is not None:
            self.participant_id = participant_id
        if name is not None:
            self.name = name
        if subscriber_id is not None:
            self.subscriber_id = subscriber_id
        if role is not None:
            self.role = role
        if state is not None:
            self.state = state
        if address is not None:
            self.address = address
        if attendee_type is not None:
            self.attendee_type = attendee_type
        if account_id is not None:
            self.account_id = account_id
        if phone2 is not None:
            self.phone2 = phone2
        if phone3 is not None:
            self.phone3 = phone3
        if email is not None:
            self.email = email
        if sms is not None:
            self.sms = sms
        if dept_name is not None:
            self.dept_name = dept_name
        if user_uuid is not None:
            self.user_uuid = user_uuid
        if app_id is not None:
            self.app_id = app_id
        if is_auto_invite is not None:
            self.is_auto_invite = is_auto_invite
        if is_not_overlay_pid_name is not None:
            self.is_not_overlay_pid_name = is_not_overlay_pid_name

    @property
    def participant_id(self):
        """Gets the participant_id of this ParticipantInfo.

        与会者的号码。

        :return: The participant_id of this ParticipantInfo.
        :rtype: str
        """
        return self._participant_id

    @participant_id.setter
    def participant_id(self, participant_id):
        """Sets the participant_id of this ParticipantInfo.

        与会者的号码。

        :param participant_id: The participant_id of this ParticipantInfo.
        :type participant_id: str
        """
        self._participant_id = participant_id

    @property
    def name(self):
        """Gets the name of this ParticipantInfo.

        与会者的名称。

        :return: The name of this ParticipantInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ParticipantInfo.

        与会者的名称。

        :param name: The name of this ParticipantInfo.
        :type name: str
        """
        self._name = name

    @property
    def subscriber_id(self):
        """Gets the subscriber_id of this ParticipantInfo.

        与会者的号码（预留字段）。

        :return: The subscriber_id of this ParticipantInfo.
        :rtype: str
        """
        return self._subscriber_id

    @subscriber_id.setter
    def subscriber_id(self, subscriber_id):
        """Sets the subscriber_id of this ParticipantInfo.

        与会者的号码（预留字段）。

        :param subscriber_id: The subscriber_id of this ParticipantInfo.
        :type subscriber_id: str
        """
        self._subscriber_id = subscriber_id

    @property
    def role(self):
        """Gets the role of this ParticipantInfo.

        与会者的角色。 - 1: 会议主持人 - 0: 普通与会者

        :return: The role of this ParticipantInfo.
        :rtype: int
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this ParticipantInfo.

        与会者的角色。 - 1: 会议主持人 - 0: 普通与会者

        :param role: The role of this ParticipantInfo.
        :type role: int
        """
        self._role = role

    @property
    def state(self):
        """Gets the state of this ParticipantInfo.

        用户状态。目前固定返回MEETTING。

        :return: The state of this ParticipantInfo.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ParticipantInfo.

        用户状态。目前固定返回MEETTING。

        :param state: The state of this ParticipantInfo.
        :type state: str
        """
        self._state = state

    @property
    def address(self):
        """Gets the address of this ParticipantInfo.

        终端所在会议室信息（预留字段）。

        :return: The address of this ParticipantInfo.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ParticipantInfo.

        终端所在会议室信息（预留字段）。

        :param address: The address of this ParticipantInfo.
        :type address: str
        """
        self._address = address

    @property
    def attendee_type(self):
        """Gets the attendee_type of this ParticipantInfo.

        与会者终端类型。 - normal: 软终端。 - terminal: 会议室或硬终端。 - outside: 外部与会人。 - mobile: 用户手机号码。

        :return: The attendee_type of this ParticipantInfo.
        :rtype: str
        """
        return self._attendee_type

    @attendee_type.setter
    def attendee_type(self, attendee_type):
        """Sets the attendee_type of this ParticipantInfo.

        与会者终端类型。 - normal: 软终端。 - terminal: 会议室或硬终端。 - outside: 外部与会人。 - mobile: 用户手机号码。

        :param attendee_type: The attendee_type of this ParticipantInfo.
        :type attendee_type: str
        """
        self._attendee_type = attendee_type

    @property
    def account_id(self):
        """Gets the account_id of this ParticipantInfo.

        预订者的帐号。 * 如果是帐号/密码鉴权场景，表示华为云会议帐号 * 如果是APP ID鉴权场景，表示第三方的User ID 

        :return: The account_id of this ParticipantInfo.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this ParticipantInfo.

        预订者的帐号。 * 如果是帐号/密码鉴权场景，表示华为云会议帐号 * 如果是APP ID鉴权场景，表示第三方的User ID 

        :param account_id: The account_id of this ParticipantInfo.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def phone2(self):
        """Gets the phone2 of this ParticipantInfo.

        预留字段。

        :return: The phone2 of this ParticipantInfo.
        :rtype: str
        """
        return self._phone2

    @phone2.setter
    def phone2(self, phone2):
        """Sets the phone2 of this ParticipantInfo.

        预留字段。

        :param phone2: The phone2 of this ParticipantInfo.
        :type phone2: str
        """
        self._phone2 = phone2

    @property
    def phone3(self):
        """Gets the phone3 of this ParticipantInfo.

        预留字段。

        :return: The phone3 of this ParticipantInfo.
        :rtype: str
        """
        return self._phone3

    @phone3.setter
    def phone3(self, phone3):
        """Sets the phone3 of this ParticipantInfo.

        预留字段。

        :param phone3: The phone3 of this ParticipantInfo.
        :type phone3: str
        """
        self._phone3 = phone3

    @property
    def email(self):
        """Gets the email of this ParticipantInfo.

        邮箱地址。

        :return: The email of this ParticipantInfo.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ParticipantInfo.

        邮箱地址。

        :param email: The email of this ParticipantInfo.
        :type email: str
        """
        self._email = email

    @property
    def sms(self):
        """Gets the sms of this ParticipantInfo.

        短信通知的手机号码。

        :return: The sms of this ParticipantInfo.
        :rtype: str
        """
        return self._sms

    @sms.setter
    def sms(self, sms):
        """Sets the sms of this ParticipantInfo.

        短信通知的手机号码。

        :param sms: The sms of this ParticipantInfo.
        :type sms: str
        """
        self._sms = sms

    @property
    def dept_name(self):
        """Gets the dept_name of this ParticipantInfo.

        部门名称。

        :return: The dept_name of this ParticipantInfo.
        :rtype: str
        """
        return self._dept_name

    @dept_name.setter
    def dept_name(self, dept_name):
        """Sets the dept_name of this ParticipantInfo.

        部门名称。

        :param dept_name: The dept_name of this ParticipantInfo.
        :type dept_name: str
        """
        self._dept_name = dept_name

    @property
    def user_uuid(self):
        """Gets the user_uuid of this ParticipantInfo.

        预订者的用户UUID。

        :return: The user_uuid of this ParticipantInfo.
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """Sets the user_uuid of this ParticipantInfo.

        预订者的用户UUID。

        :param user_uuid: The user_uuid of this ParticipantInfo.
        :type user_uuid: str
        """
        self._user_uuid = user_uuid

    @property
    def app_id(self):
        """Gets the app_id of this ParticipantInfo.

        App ID。参考[[App ID的申请](https://support.huaweicloud.com/devg-meeting/meeting_20_0011.html#section1)](tag:hws)[[App ID的申请](https://support.huaweicloud.com/intl/zh-cn/devg-meeting/meeting_20_0011.html#section1)](tag:hk)。

        :return: The app_id of this ParticipantInfo.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ParticipantInfo.

        App ID。参考[[App ID的申请](https://support.huaweicloud.com/devg-meeting/meeting_20_0011.html#section1)](tag:hws)[[App ID的申请](https://support.huaweicloud.com/intl/zh-cn/devg-meeting/meeting_20_0011.html#section1)](tag:hk)。

        :param app_id: The app_id of this ParticipantInfo.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def is_auto_invite(self):
        """Gets the is_auto_invite of this ParticipantInfo.

        会议开始时是否自动邀请该与会者。默认值由企业级配置决定。 * 0： 不自动邀请 * 1： 自动邀请 

        :return: The is_auto_invite of this ParticipantInfo.
        :rtype: int
        """
        return self._is_auto_invite

    @is_auto_invite.setter
    def is_auto_invite(self, is_auto_invite):
        """Sets the is_auto_invite of this ParticipantInfo.

        会议开始时是否自动邀请该与会者。默认值由企业级配置决定。 * 0： 不自动邀请 * 1： 自动邀请 

        :param is_auto_invite: The is_auto_invite of this ParticipantInfo.
        :type is_auto_invite: int
        """
        self._is_auto_invite = is_auto_invite

    @property
    def is_not_overlay_pid_name(self):
        """Gets the is_not_overlay_pid_name of this ParticipantInfo.

        是否不叠加会场名（VDC场景下适用）。

        :return: The is_not_overlay_pid_name of this ParticipantInfo.
        :rtype: bool
        """
        return self._is_not_overlay_pid_name

    @is_not_overlay_pid_name.setter
    def is_not_overlay_pid_name(self, is_not_overlay_pid_name):
        """Sets the is_not_overlay_pid_name of this ParticipantInfo.

        是否不叠加会场名（VDC场景下适用）。

        :param is_not_overlay_pid_name: The is_not_overlay_pid_name of this ParticipantInfo.
        :type is_not_overlay_pid_name: bool
        """
        self._is_not_overlay_pid_name = is_not_overlay_pid_name

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
        if not isinstance(other, ParticipantInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
