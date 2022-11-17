# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Attendee:

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
        'type': 'str',
        'dept_uuid': 'str',
        'dept_name': 'str'
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
        'type': 'type',
        'dept_uuid': 'deptUUID',
        'dept_name': 'deptName'
    }

    def __init__(self, user_uuid=None, account_id=None, name=None, role=None, phone=None, phone2=None, phone3=None, email=None, sms=None, type=None, dept_uuid=None, dept_name=None):
        """Attendee

        The model defined in huaweicloud sdk

        :param user_uuid: 与会者的用户UUID。
        :type user_uuid: str
        :param account_id: 与会者的华为云会议帐号。
        :type account_id: str
        :param name: 与会者名称，长度限制为96个字符。
        :type name: str
        :param role: 会议中的角色。默认为普通与会者。 - 0: 普通与会者 - 1: 会议主持人
        :type role: int
        :param phone: 号码。支持SIP号码或者手机号码。 &gt; * 号码可以通过[[查询企业通讯](https://support.huaweicloud.com/api-meeting/meeting_21_0512.html)](tag:hws)[[查询企业通讯](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0512.html)](tag:hk)接口录获取。返回的number是SIP号码，phone是手机号码 &gt; * 填SIP号码系统会呼叫对应的软终端或者硬终端；填手机号码系统会呼叫手机 &gt; * 呼叫手机需要开通PSTN权限，否则无法呼叫 
        :type phone: str
        :param phone2: 预留字段，取值类型同参数“phone”。
        :type phone2: str
        :param phone3: 预留字段，取值类型同参数“phone”。
        :type phone3: str
        :param email: 邮件地址。 &gt; 会中邀请不发会议通知，不用填写。 
        :type email: str
        :param sms: 短信通知的手机号码。 &gt; 会中邀请不发会议通知，不用填写。 
        :type sms: str
        :param type: 终端类型，类型枚举如下： * normal：软终端 * terminal：硬终端 * outside：外部与会人 * mobile：用户手机号码 * ideahub：ideahub * board: 电子白板（SmartRooms）。含Maxhub、海信大屏、IdeaHub B2hwvision：华为智慧屏TV
        :type type: str
        :param dept_uuid: 部门编码。
        :type dept_uuid: str
        :param dept_name: 部门名称。
        :type dept_name: str
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
        self._type = None
        self._dept_uuid = None
        self._dept_name = None
        self.discriminator = None

        if user_uuid is not None:
            self.user_uuid = user_uuid
        if account_id is not None:
            self.account_id = account_id
        self.name = name
        if role is not None:
            self.role = role
        self.phone = phone
        if phone2 is not None:
            self.phone2 = phone2
        if phone3 is not None:
            self.phone3 = phone3
        if email is not None:
            self.email = email
        if sms is not None:
            self.sms = sms
        self.type = type
        if dept_uuid is not None:
            self.dept_uuid = dept_uuid
        if dept_name is not None:
            self.dept_name = dept_name

    @property
    def user_uuid(self):
        """Gets the user_uuid of this Attendee.

        与会者的用户UUID。

        :return: The user_uuid of this Attendee.
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """Sets the user_uuid of this Attendee.

        与会者的用户UUID。

        :param user_uuid: The user_uuid of this Attendee.
        :type user_uuid: str
        """
        self._user_uuid = user_uuid

    @property
    def account_id(self):
        """Gets the account_id of this Attendee.

        与会者的华为云会议帐号。

        :return: The account_id of this Attendee.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Attendee.

        与会者的华为云会议帐号。

        :param account_id: The account_id of this Attendee.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def name(self):
        """Gets the name of this Attendee.

        与会者名称，长度限制为96个字符。

        :return: The name of this Attendee.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Attendee.

        与会者名称，长度限制为96个字符。

        :param name: The name of this Attendee.
        :type name: str
        """
        self._name = name

    @property
    def role(self):
        """Gets the role of this Attendee.

        会议中的角色。默认为普通与会者。 - 0: 普通与会者 - 1: 会议主持人

        :return: The role of this Attendee.
        :rtype: int
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this Attendee.

        会议中的角色。默认为普通与会者。 - 0: 普通与会者 - 1: 会议主持人

        :param role: The role of this Attendee.
        :type role: int
        """
        self._role = role

    @property
    def phone(self):
        """Gets the phone of this Attendee.

        号码。支持SIP号码或者手机号码。 > * 号码可以通过[[查询企业通讯](https://support.huaweicloud.com/api-meeting/meeting_21_0512.html)](tag:hws)[[查询企业通讯](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0512.html)](tag:hk)接口录获取。返回的number是SIP号码，phone是手机号码 > * 填SIP号码系统会呼叫对应的软终端或者硬终端；填手机号码系统会呼叫手机 > * 呼叫手机需要开通PSTN权限，否则无法呼叫 

        :return: The phone of this Attendee.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Attendee.

        号码。支持SIP号码或者手机号码。 > * 号码可以通过[[查询企业通讯](https://support.huaweicloud.com/api-meeting/meeting_21_0512.html)](tag:hws)[[查询企业通讯](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0512.html)](tag:hk)接口录获取。返回的number是SIP号码，phone是手机号码 > * 填SIP号码系统会呼叫对应的软终端或者硬终端；填手机号码系统会呼叫手机 > * 呼叫手机需要开通PSTN权限，否则无法呼叫 

        :param phone: The phone of this Attendee.
        :type phone: str
        """
        self._phone = phone

    @property
    def phone2(self):
        """Gets the phone2 of this Attendee.

        预留字段，取值类型同参数“phone”。

        :return: The phone2 of this Attendee.
        :rtype: str
        """
        return self._phone2

    @phone2.setter
    def phone2(self, phone2):
        """Sets the phone2 of this Attendee.

        预留字段，取值类型同参数“phone”。

        :param phone2: The phone2 of this Attendee.
        :type phone2: str
        """
        self._phone2 = phone2

    @property
    def phone3(self):
        """Gets the phone3 of this Attendee.

        预留字段，取值类型同参数“phone”。

        :return: The phone3 of this Attendee.
        :rtype: str
        """
        return self._phone3

    @phone3.setter
    def phone3(self, phone3):
        """Sets the phone3 of this Attendee.

        预留字段，取值类型同参数“phone”。

        :param phone3: The phone3 of this Attendee.
        :type phone3: str
        """
        self._phone3 = phone3

    @property
    def email(self):
        """Gets the email of this Attendee.

        邮件地址。 > 会中邀请不发会议通知，不用填写。 

        :return: The email of this Attendee.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Attendee.

        邮件地址。 > 会中邀请不发会议通知，不用填写。 

        :param email: The email of this Attendee.
        :type email: str
        """
        self._email = email

    @property
    def sms(self):
        """Gets the sms of this Attendee.

        短信通知的手机号码。 > 会中邀请不发会议通知，不用填写。 

        :return: The sms of this Attendee.
        :rtype: str
        """
        return self._sms

    @sms.setter
    def sms(self, sms):
        """Sets the sms of this Attendee.

        短信通知的手机号码。 > 会中邀请不发会议通知，不用填写。 

        :param sms: The sms of this Attendee.
        :type sms: str
        """
        self._sms = sms

    @property
    def type(self):
        """Gets the type of this Attendee.

        终端类型，类型枚举如下： * normal：软终端 * terminal：硬终端 * outside：外部与会人 * mobile：用户手机号码 * ideahub：ideahub * board: 电子白板（SmartRooms）。含Maxhub、海信大屏、IdeaHub B2hwvision：华为智慧屏TV

        :return: The type of this Attendee.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Attendee.

        终端类型，类型枚举如下： * normal：软终端 * terminal：硬终端 * outside：外部与会人 * mobile：用户手机号码 * ideahub：ideahub * board: 电子白板（SmartRooms）。含Maxhub、海信大屏、IdeaHub B2hwvision：华为智慧屏TV

        :param type: The type of this Attendee.
        :type type: str
        """
        self._type = type

    @property
    def dept_uuid(self):
        """Gets the dept_uuid of this Attendee.

        部门编码。

        :return: The dept_uuid of this Attendee.
        :rtype: str
        """
        return self._dept_uuid

    @dept_uuid.setter
    def dept_uuid(self, dept_uuid):
        """Sets the dept_uuid of this Attendee.

        部门编码。

        :param dept_uuid: The dept_uuid of this Attendee.
        :type dept_uuid: str
        """
        self._dept_uuid = dept_uuid

    @property
    def dept_name(self):
        """Gets the dept_name of this Attendee.

        部门名称。

        :return: The dept_name of this Attendee.
        :rtype: str
        """
        return self._dept_name

    @dept_name.setter
    def dept_name(self, dept_name):
        """Sets the dept_name of this Attendee.

        部门名称。

        :param dept_name: The dept_name of this Attendee.
        :type dept_name: str
        """
        self._dept_name = dept_name

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
        if not isinstance(other, Attendee):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
