# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddUserDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'english_name': 'str',
        'account': 'str',
        'third_account': 'str',
        'phone': 'str',
        'country': 'str',
        'pwd': 'str',
        'email': 'str',
        'dept_code': 'str',
        'signature': 'str',
        'title': 'str',
        'desc': 'str',
        'status': 'int',
        'function': 'UserFunctionDTO',
        'send_notify': 'str',
        'sort_level': 'int',
        'hide_phone': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'english_name': 'englishName',
        'account': 'account',
        'third_account': 'thirdAccount',
        'phone': 'phone',
        'country': 'country',
        'pwd': 'pwd',
        'email': 'email',
        'dept_code': 'deptCode',
        'signature': 'signature',
        'title': 'title',
        'desc': 'desc',
        'status': 'status',
        'function': 'function',
        'send_notify': 'sendNotify',
        'sort_level': 'sortLevel',
        'hide_phone': 'hidePhone'
    }

    def __init__(self, name=None, english_name=None, account=None, third_account=None, phone=None, country=None, pwd=None, email=None, dept_code=None, signature=None, title=None, desc=None, status=None, function=None, send_notify=None, sort_level=None, hide_phone=None):
        """AddUserDTO

        The model defined in huaweicloud sdk

        :param name: 企业用户名称。
        :type name: str
        :param english_name: 企业用户的英文名称。
        :type english_name: str
        :param account: 企业用户帐号，若携带则以携带为准，否则后台自动生成。帐号整系统唯一。 帐号只能包含大小写字母、数字、_、-、.、@符号，不能为纯数字和@后面带.号。 &gt; 帐号/密码鉴权方式时需要填写。
        :type account: str
        :param third_account: 第三方User ID。 &gt; App ID鉴权方式时需要填写。第三方User ID需要企业内唯一。
        :type third_account: str
        :param phone: 手机号，必须加上国家码。 例如中国大陆手机+86xxxxxxx。当填写手机号时 “country”参数必填。 手机号只允许输入纯数字。 说明：手机号或者邮箱至少填写一个
        :type phone: str
        :param country: [[手机号所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 
        :type country: str
        :param pwd: 企业用户帐号的密码。若携带则以实际携带为准，否则后台默认生成，密码必须满足： 1、8-32位 2、不能和帐号的正序和倒序一致 3、至少包含两种字符类型：小写字母、大写字母、数字、特殊字符（&#x60; ~ ! @ # $ % ^ &amp; * ( ) - _ &#x3D; + | [ { } ] ; : \&quot; ,’ &lt; . &gt; / ?）
        :type pwd: str
        :param email: 邮箱地址。
        :type email: str
        :param dept_code: 部门编码，若不携带则默认根部门。 默认值：1
        :type dept_code: str
        :param signature: 签名。
        :type signature: str
        :param title: 职位。
        :type title: str
        :param desc: 备注。
        :type desc: str
        :param status: 用户状态。默认值：0 * 0：正常 * 1：停用
        :type status: int
        :param function: 
        :type function: :class:`huaweicloudsdkmeeting.v1.UserFunctionDTO`
        :param send_notify: 是否发送开户的邮件和短信通知。 - 0 不发送 - 不填或者其他值就发送, 默认发送
        :type send_notify: str
        :param sort_level: 通讯录排序等级，序号越低优先级越高。 默认值：10000
        :type sort_level: int
        :param hide_phone: 是否隐藏手机号码。默认值：false。 * true：在通讯录和会议中不显示手机号码 * false：在通讯录和会议中显示手机号码 
        :type hide_phone: bool
        """
        
        

        self._name = None
        self._english_name = None
        self._account = None
        self._third_account = None
        self._phone = None
        self._country = None
        self._pwd = None
        self._email = None
        self._dept_code = None
        self._signature = None
        self._title = None
        self._desc = None
        self._status = None
        self._function = None
        self._send_notify = None
        self._sort_level = None
        self._hide_phone = None
        self.discriminator = None

        self.name = name
        if english_name is not None:
            self.english_name = english_name
        if account is not None:
            self.account = account
        if third_account is not None:
            self.third_account = third_account
        if phone is not None:
            self.phone = phone
        if country is not None:
            self.country = country
        if pwd is not None:
            self.pwd = pwd
        if email is not None:
            self.email = email
        if dept_code is not None:
            self.dept_code = dept_code
        if signature is not None:
            self.signature = signature
        if title is not None:
            self.title = title
        if desc is not None:
            self.desc = desc
        if status is not None:
            self.status = status
        if function is not None:
            self.function = function
        if send_notify is not None:
            self.send_notify = send_notify
        if sort_level is not None:
            self.sort_level = sort_level
        if hide_phone is not None:
            self.hide_phone = hide_phone

    @property
    def name(self):
        """Gets the name of this AddUserDTO.

        企业用户名称。

        :return: The name of this AddUserDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddUserDTO.

        企业用户名称。

        :param name: The name of this AddUserDTO.
        :type name: str
        """
        self._name = name

    @property
    def english_name(self):
        """Gets the english_name of this AddUserDTO.

        企业用户的英文名称。

        :return: The english_name of this AddUserDTO.
        :rtype: str
        """
        return self._english_name

    @english_name.setter
    def english_name(self, english_name):
        """Sets the english_name of this AddUserDTO.

        企业用户的英文名称。

        :param english_name: The english_name of this AddUserDTO.
        :type english_name: str
        """
        self._english_name = english_name

    @property
    def account(self):
        """Gets the account of this AddUserDTO.

        企业用户帐号，若携带则以携带为准，否则后台自动生成。帐号整系统唯一。 帐号只能包含大小写字母、数字、_、-、.、@符号，不能为纯数字和@后面带.号。 > 帐号/密码鉴权方式时需要填写。

        :return: The account of this AddUserDTO.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this AddUserDTO.

        企业用户帐号，若携带则以携带为准，否则后台自动生成。帐号整系统唯一。 帐号只能包含大小写字母、数字、_、-、.、@符号，不能为纯数字和@后面带.号。 > 帐号/密码鉴权方式时需要填写。

        :param account: The account of this AddUserDTO.
        :type account: str
        """
        self._account = account

    @property
    def third_account(self):
        """Gets the third_account of this AddUserDTO.

        第三方User ID。 > App ID鉴权方式时需要填写。第三方User ID需要企业内唯一。

        :return: The third_account of this AddUserDTO.
        :rtype: str
        """
        return self._third_account

    @third_account.setter
    def third_account(self, third_account):
        """Sets the third_account of this AddUserDTO.

        第三方User ID。 > App ID鉴权方式时需要填写。第三方User ID需要企业内唯一。

        :param third_account: The third_account of this AddUserDTO.
        :type third_account: str
        """
        self._third_account = third_account

    @property
    def phone(self):
        """Gets the phone of this AddUserDTO.

        手机号，必须加上国家码。 例如中国大陆手机+86xxxxxxx。当填写手机号时 “country”参数必填。 手机号只允许输入纯数字。 说明：手机号或者邮箱至少填写一个

        :return: The phone of this AddUserDTO.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this AddUserDTO.

        手机号，必须加上国家码。 例如中国大陆手机+86xxxxxxx。当填写手机号时 “country”参数必填。 手机号只允许输入纯数字。 说明：手机号或者邮箱至少填写一个

        :param phone: The phone of this AddUserDTO.
        :type phone: str
        """
        self._phone = phone

    @property
    def country(self):
        """Gets the country of this AddUserDTO.

        [[手机号所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 

        :return: The country of this AddUserDTO.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this AddUserDTO.

        [[手机号所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 

        :param country: The country of this AddUserDTO.
        :type country: str
        """
        self._country = country

    @property
    def pwd(self):
        """Gets the pwd of this AddUserDTO.

        企业用户帐号的密码。若携带则以实际携带为准，否则后台默认生成，密码必须满足： 1、8-32位 2、不能和帐号的正序和倒序一致 3、至少包含两种字符类型：小写字母、大写字母、数字、特殊字符（` ~ ! @ # $ % ^ & * ( ) - _ = + | [ { } ] ; : \" ,’ < . > / ?）

        :return: The pwd of this AddUserDTO.
        :rtype: str
        """
        return self._pwd

    @pwd.setter
    def pwd(self, pwd):
        """Sets the pwd of this AddUserDTO.

        企业用户帐号的密码。若携带则以实际携带为准，否则后台默认生成，密码必须满足： 1、8-32位 2、不能和帐号的正序和倒序一致 3、至少包含两种字符类型：小写字母、大写字母、数字、特殊字符（` ~ ! @ # $ % ^ & * ( ) - _ = + | [ { } ] ; : \" ,’ < . > / ?）

        :param pwd: The pwd of this AddUserDTO.
        :type pwd: str
        """
        self._pwd = pwd

    @property
    def email(self):
        """Gets the email of this AddUserDTO.

        邮箱地址。

        :return: The email of this AddUserDTO.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this AddUserDTO.

        邮箱地址。

        :param email: The email of this AddUserDTO.
        :type email: str
        """
        self._email = email

    @property
    def dept_code(self):
        """Gets the dept_code of this AddUserDTO.

        部门编码，若不携带则默认根部门。 默认值：1

        :return: The dept_code of this AddUserDTO.
        :rtype: str
        """
        return self._dept_code

    @dept_code.setter
    def dept_code(self, dept_code):
        """Sets the dept_code of this AddUserDTO.

        部门编码，若不携带则默认根部门。 默认值：1

        :param dept_code: The dept_code of this AddUserDTO.
        :type dept_code: str
        """
        self._dept_code = dept_code

    @property
    def signature(self):
        """Gets the signature of this AddUserDTO.

        签名。

        :return: The signature of this AddUserDTO.
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this AddUserDTO.

        签名。

        :param signature: The signature of this AddUserDTO.
        :type signature: str
        """
        self._signature = signature

    @property
    def title(self):
        """Gets the title of this AddUserDTO.

        职位。

        :return: The title of this AddUserDTO.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this AddUserDTO.

        职位。

        :param title: The title of this AddUserDTO.
        :type title: str
        """
        self._title = title

    @property
    def desc(self):
        """Gets the desc of this AddUserDTO.

        备注。

        :return: The desc of this AddUserDTO.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this AddUserDTO.

        备注。

        :param desc: The desc of this AddUserDTO.
        :type desc: str
        """
        self._desc = desc

    @property
    def status(self):
        """Gets the status of this AddUserDTO.

        用户状态。默认值：0 * 0：正常 * 1：停用

        :return: The status of this AddUserDTO.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AddUserDTO.

        用户状态。默认值：0 * 0：正常 * 1：停用

        :param status: The status of this AddUserDTO.
        :type status: int
        """
        self._status = status

    @property
    def function(self):
        """Gets the function of this AddUserDTO.

        :return: The function of this AddUserDTO.
        :rtype: :class:`huaweicloudsdkmeeting.v1.UserFunctionDTO`
        """
        return self._function

    @function.setter
    def function(self, function):
        """Sets the function of this AddUserDTO.

        :param function: The function of this AddUserDTO.
        :type function: :class:`huaweicloudsdkmeeting.v1.UserFunctionDTO`
        """
        self._function = function

    @property
    def send_notify(self):
        """Gets the send_notify of this AddUserDTO.

        是否发送开户的邮件和短信通知。 - 0 不发送 - 不填或者其他值就发送, 默认发送

        :return: The send_notify of this AddUserDTO.
        :rtype: str
        """
        return self._send_notify

    @send_notify.setter
    def send_notify(self, send_notify):
        """Sets the send_notify of this AddUserDTO.

        是否发送开户的邮件和短信通知。 - 0 不发送 - 不填或者其他值就发送, 默认发送

        :param send_notify: The send_notify of this AddUserDTO.
        :type send_notify: str
        """
        self._send_notify = send_notify

    @property
    def sort_level(self):
        """Gets the sort_level of this AddUserDTO.

        通讯录排序等级，序号越低优先级越高。 默认值：10000

        :return: The sort_level of this AddUserDTO.
        :rtype: int
        """
        return self._sort_level

    @sort_level.setter
    def sort_level(self, sort_level):
        """Sets the sort_level of this AddUserDTO.

        通讯录排序等级，序号越低优先级越高。 默认值：10000

        :param sort_level: The sort_level of this AddUserDTO.
        :type sort_level: int
        """
        self._sort_level = sort_level

    @property
    def hide_phone(self):
        """Gets the hide_phone of this AddUserDTO.

        是否隐藏手机号码。默认值：false。 * true：在通讯录和会议中不显示手机号码 * false：在通讯录和会议中显示手机号码 

        :return: The hide_phone of this AddUserDTO.
        :rtype: bool
        """
        return self._hide_phone

    @hide_phone.setter
    def hide_phone(self, hide_phone):
        """Sets the hide_phone of this AddUserDTO.

        是否隐藏手机号码。默认值：false。 * true：在通讯录和会议中不显示手机号码 * false：在通讯录和会议中显示手机号码 

        :param hide_phone: The hide_phone of this AddUserDTO.
        :type hide_phone: bool
        """
        self._hide_phone = hide_phone

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
        if not isinstance(other, AddUserDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
