# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenAttendeeEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'user_account': 'str',
        'user_name': 'str',
        'dept_name': 'str',
        'phone': 'str',
        'email': 'str',
        'sms': 'str',
        'is_hard_terminal': 'bool'
    }

    attribute_map = {
        'app_id': 'appId',
        'user_account': 'userAccount',
        'user_name': 'userName',
        'dept_name': 'deptName',
        'phone': 'phone',
        'email': 'email',
        'sms': 'sms',
        'is_hard_terminal': 'isHardTerminal'
    }

    def __init__(self, app_id=None, user_account=None, user_name=None, dept_name=None, phone=None, email=None, sms=None, is_hard_terminal=None):
        """OpenAttendeeEntity

        The model defined in huaweicloud sdk

        :param app_id: App ID。如果是APP ID鉴权场景，此项必填。参考[[App ID的申请](https://support.huaweicloud.com/devg-meeting/meeting_20_0011.html#section1)](tag:hws)[[App ID的申请](https://support.huaweicloud.com/intl/zh-cn/devg-meeting/meeting_20_0011.html#section1)](tag:hk)。
        :type app_id: str
        :param user_account: 嘉宾的帐号。 * 如果是帐号/密码鉴权场景: 选填，表示华为云会议帐号ID * 如果是APP ID鉴权场景：必填，表示第三方的User ID，同时需要携带参数appId 
        :type user_account: str
        :param user_name: 嘉宾的名称。长度限制为96个字符。
        :type user_name: str
        :param dept_name: 部门名称，最大128字符。
        :type dept_name: str
        :param phone: 号码。支持SIP号码或者手机号码。 * 如果是帐号/密码鉴权场景：必填 * 如果是APP ID鉴权场景：选填 &gt; * 号码可以通过[[查询企业通讯](https://support.huaweicloud.com/api-meeting/meeting_21_0512.html)](tag:hws)[[查询企业通讯](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0512.html)](tag:hk)接口录获取。返回的number是SIP号码，phone是手机号码 &gt; * 填SIP号码系统会呼叫对应的软终端或者硬终端；填手机号码系统会呼叫手机 &gt; * 呼叫手机需要开通PSTN权限，否则无法呼叫 
        :type phone: str
        :param email: 邮件地址。需要发邮件通知时填写。
        :type email: str
        :param sms: 短信通知的手机号码。需要发短信通知时填写。
        :type sms: str
        :param is_hard_terminal: 是否硬终端（会议室或硬终端）。
        :type is_hard_terminal: bool
        """
        
        

        self._app_id = None
        self._user_account = None
        self._user_name = None
        self._dept_name = None
        self._phone = None
        self._email = None
        self._sms = None
        self._is_hard_terminal = None
        self.discriminator = None

        self.app_id = app_id
        if user_account is not None:
            self.user_account = user_account
        if user_name is not None:
            self.user_name = user_name
        if dept_name is not None:
            self.dept_name = dept_name
        if phone is not None:
            self.phone = phone
        if email is not None:
            self.email = email
        if sms is not None:
            self.sms = sms
        if is_hard_terminal is not None:
            self.is_hard_terminal = is_hard_terminal

    @property
    def app_id(self):
        """Gets the app_id of this OpenAttendeeEntity.

        App ID。如果是APP ID鉴权场景，此项必填。参考[[App ID的申请](https://support.huaweicloud.com/devg-meeting/meeting_20_0011.html#section1)](tag:hws)[[App ID的申请](https://support.huaweicloud.com/intl/zh-cn/devg-meeting/meeting_20_0011.html#section1)](tag:hk)。

        :return: The app_id of this OpenAttendeeEntity.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this OpenAttendeeEntity.

        App ID。如果是APP ID鉴权场景，此项必填。参考[[App ID的申请](https://support.huaweicloud.com/devg-meeting/meeting_20_0011.html#section1)](tag:hws)[[App ID的申请](https://support.huaweicloud.com/intl/zh-cn/devg-meeting/meeting_20_0011.html#section1)](tag:hk)。

        :param app_id: The app_id of this OpenAttendeeEntity.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def user_account(self):
        """Gets the user_account of this OpenAttendeeEntity.

        嘉宾的帐号。 * 如果是帐号/密码鉴权场景: 选填，表示华为云会议帐号ID * 如果是APP ID鉴权场景：必填，表示第三方的User ID，同时需要携带参数appId 

        :return: The user_account of this OpenAttendeeEntity.
        :rtype: str
        """
        return self._user_account

    @user_account.setter
    def user_account(self, user_account):
        """Sets the user_account of this OpenAttendeeEntity.

        嘉宾的帐号。 * 如果是帐号/密码鉴权场景: 选填，表示华为云会议帐号ID * 如果是APP ID鉴权场景：必填，表示第三方的User ID，同时需要携带参数appId 

        :param user_account: The user_account of this OpenAttendeeEntity.
        :type user_account: str
        """
        self._user_account = user_account

    @property
    def user_name(self):
        """Gets the user_name of this OpenAttendeeEntity.

        嘉宾的名称。长度限制为96个字符。

        :return: The user_name of this OpenAttendeeEntity.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this OpenAttendeeEntity.

        嘉宾的名称。长度限制为96个字符。

        :param user_name: The user_name of this OpenAttendeeEntity.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def dept_name(self):
        """Gets the dept_name of this OpenAttendeeEntity.

        部门名称，最大128字符。

        :return: The dept_name of this OpenAttendeeEntity.
        :rtype: str
        """
        return self._dept_name

    @dept_name.setter
    def dept_name(self, dept_name):
        """Sets the dept_name of this OpenAttendeeEntity.

        部门名称，最大128字符。

        :param dept_name: The dept_name of this OpenAttendeeEntity.
        :type dept_name: str
        """
        self._dept_name = dept_name

    @property
    def phone(self):
        """Gets the phone of this OpenAttendeeEntity.

        号码。支持SIP号码或者手机号码。 * 如果是帐号/密码鉴权场景：必填 * 如果是APP ID鉴权场景：选填 > * 号码可以通过[[查询企业通讯](https://support.huaweicloud.com/api-meeting/meeting_21_0512.html)](tag:hws)[[查询企业通讯](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0512.html)](tag:hk)接口录获取。返回的number是SIP号码，phone是手机号码 > * 填SIP号码系统会呼叫对应的软终端或者硬终端；填手机号码系统会呼叫手机 > * 呼叫手机需要开通PSTN权限，否则无法呼叫 

        :return: The phone of this OpenAttendeeEntity.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this OpenAttendeeEntity.

        号码。支持SIP号码或者手机号码。 * 如果是帐号/密码鉴权场景：必填 * 如果是APP ID鉴权场景：选填 > * 号码可以通过[[查询企业通讯](https://support.huaweicloud.com/api-meeting/meeting_21_0512.html)](tag:hws)[[查询企业通讯](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0512.html)](tag:hk)接口录获取。返回的number是SIP号码，phone是手机号码 > * 填SIP号码系统会呼叫对应的软终端或者硬终端；填手机号码系统会呼叫手机 > * 呼叫手机需要开通PSTN权限，否则无法呼叫 

        :param phone: The phone of this OpenAttendeeEntity.
        :type phone: str
        """
        self._phone = phone

    @property
    def email(self):
        """Gets the email of this OpenAttendeeEntity.

        邮件地址。需要发邮件通知时填写。

        :return: The email of this OpenAttendeeEntity.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this OpenAttendeeEntity.

        邮件地址。需要发邮件通知时填写。

        :param email: The email of this OpenAttendeeEntity.
        :type email: str
        """
        self._email = email

    @property
    def sms(self):
        """Gets the sms of this OpenAttendeeEntity.

        短信通知的手机号码。需要发短信通知时填写。

        :return: The sms of this OpenAttendeeEntity.
        :rtype: str
        """
        return self._sms

    @sms.setter
    def sms(self, sms):
        """Sets the sms of this OpenAttendeeEntity.

        短信通知的手机号码。需要发短信通知时填写。

        :param sms: The sms of this OpenAttendeeEntity.
        :type sms: str
        """
        self._sms = sms

    @property
    def is_hard_terminal(self):
        """Gets the is_hard_terminal of this OpenAttendeeEntity.

        是否硬终端（会议室或硬终端）。

        :return: The is_hard_terminal of this OpenAttendeeEntity.
        :rtype: bool
        """
        return self._is_hard_terminal

    @is_hard_terminal.setter
    def is_hard_terminal(self, is_hard_terminal):
        """Sets the is_hard_terminal of this OpenAttendeeEntity.

        是否硬终端（会议室或硬终端）。

        :param is_hard_terminal: The is_hard_terminal of this OpenAttendeeEntity.
        :type is_hard_terminal: bool
        """
        self._is_hard_terminal = is_hard_terminal

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
        if not isinstance(other, OpenAttendeeEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
