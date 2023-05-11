# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateUserResponse(SdkResponse):

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
        'user_account': 'str',
        'name': 'str',
        'english_name': 'str',
        'phone': 'str',
        'country': 'str',
        'email': 'str',
        'sip_num': 'str',
        'vmr_list': 'list[UserVmrDTO]',
        'dept_code': 'str',
        'dept_name': 'str',
        'dept_name_path': 'str',
        'user_type': 'int',
        'admin_type': 'int',
        'signature': 'str',
        'title': 'str',
        'desc': 'str',
        'corp': 'CorpBasicInfoDTO',
        'function': 'UserFunctionDTO',
        'dev_type': 'QueryDeviceInfoResultDTO',
        'status': 'int',
        'sort_level': 'int',
        'hide_phone': 'bool',
        'vision_account': 'str',
        'third_account': 'str',
        'license': 'int',
        'active_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'user_account': 'userAccount',
        'name': 'name',
        'english_name': 'englishName',
        'phone': 'phone',
        'country': 'country',
        'email': 'email',
        'sip_num': 'sipNum',
        'vmr_list': 'vmrList',
        'dept_code': 'deptCode',
        'dept_name': 'deptName',
        'dept_name_path': 'deptNamePath',
        'user_type': 'userType',
        'admin_type': 'adminType',
        'signature': 'signature',
        'title': 'title',
        'desc': 'desc',
        'corp': 'corp',
        'function': 'function',
        'dev_type': 'devType',
        'status': 'status',
        'sort_level': 'sortLevel',
        'hide_phone': 'hidePhone',
        'vision_account': 'visionAccount',
        'third_account': 'thirdAccount',
        'license': 'license',
        'active_time': 'activeTime'
    }

    def __init__(self, id=None, user_account=None, name=None, english_name=None, phone=None, country=None, email=None, sip_num=None, vmr_list=None, dept_code=None, dept_name=None, dept_name_path=None, user_type=None, admin_type=None, signature=None, title=None, desc=None, corp=None, function=None, dev_type=None, status=None, sort_level=None, hide_phone=None, vision_account=None, third_account=None, license=None, active_time=None):
        """UpdateUserResponse

        The model defined in huaweicloud sdk

        :param id: 用户UUID。
        :type id: str
        :param user_account: 华为云会议帐号。
        :type user_account: str
        :param name: 名称。
        :type name: str
        :param english_name: 英文名称。
        :type english_name: str
        :param phone: 联系电话。
        :type phone: str
        :param country: [[手机号所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 
        :type country: str
        :param email: 邮箱地址。
        :type email: str
        :param sip_num: SIP号码。
        :type sip_num: str
        :param vmr_list: 云会议室列表。
        :type vmr_list: list[:class:`huaweicloudsdkmeeting.v1.UserVmrDTO`]
        :param dept_code: 部门编码。
        :type dept_code: str
        :param dept_name: 部门名称。
        :type dept_name: str
        :param dept_name_path: 部门完整名称。
        :type dept_name_path: str
        :param user_type: 用户类型。 - 2：企业成员账户
        :type user_type: int
        :param admin_type: 管理员类型。 - 0：默认（超级）管理员 - 1：普通管理员 - 2：非管理员（即为普通企业成员，UserType是2时有效）
        :type admin_type: int
        :param signature: 签名。
        :type signature: str
        :param title: 职位。
        :type title: str
        :param desc: 备注。
        :type desc: str
        :param corp: 
        :type corp: :class:`huaweicloudsdkmeeting.v1.CorpBasicInfoDTO`
        :param function: 
        :type function: :class:`huaweicloudsdkmeeting.v1.UserFunctionDTO`
        :param dev_type: 
        :type dev_type: :class:`huaweicloudsdkmeeting.v1.QueryDeviceInfoResultDTO`
        :param status: 用户状态。 * 0：正常 * 1：停用 
        :type status: int
        :param sort_level: 通讯录排序等级，序号越低优先级越高。
        :type sort_level: int
        :param hide_phone: 是否隐藏手机号码。
        :type hide_phone: bool
        :param vision_account: 智慧屏唯一帐号。
        :type vision_account: str
        :param third_account: 第三方User ID。
        :type third_account: str
        :param license: 许可证。 * 0：商用 * 1：免费试用 
        :type license: int
        :param active_time: 激活时间，utc时间戳。
        :type active_time: int
        """
        
        super(UpdateUserResponse, self).__init__()

        self._id = None
        self._user_account = None
        self._name = None
        self._english_name = None
        self._phone = None
        self._country = None
        self._email = None
        self._sip_num = None
        self._vmr_list = None
        self._dept_code = None
        self._dept_name = None
        self._dept_name_path = None
        self._user_type = None
        self._admin_type = None
        self._signature = None
        self._title = None
        self._desc = None
        self._corp = None
        self._function = None
        self._dev_type = None
        self._status = None
        self._sort_level = None
        self._hide_phone = None
        self._vision_account = None
        self._third_account = None
        self._license = None
        self._active_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if user_account is not None:
            self.user_account = user_account
        if name is not None:
            self.name = name
        if english_name is not None:
            self.english_name = english_name
        if phone is not None:
            self.phone = phone
        if country is not None:
            self.country = country
        if email is not None:
            self.email = email
        if sip_num is not None:
            self.sip_num = sip_num
        if vmr_list is not None:
            self.vmr_list = vmr_list
        if dept_code is not None:
            self.dept_code = dept_code
        if dept_name is not None:
            self.dept_name = dept_name
        if dept_name_path is not None:
            self.dept_name_path = dept_name_path
        if user_type is not None:
            self.user_type = user_type
        if admin_type is not None:
            self.admin_type = admin_type
        if signature is not None:
            self.signature = signature
        if title is not None:
            self.title = title
        if desc is not None:
            self.desc = desc
        if corp is not None:
            self.corp = corp
        if function is not None:
            self.function = function
        if dev_type is not None:
            self.dev_type = dev_type
        if status is not None:
            self.status = status
        if sort_level is not None:
            self.sort_level = sort_level
        if hide_phone is not None:
            self.hide_phone = hide_phone
        if vision_account is not None:
            self.vision_account = vision_account
        if third_account is not None:
            self.third_account = third_account
        if license is not None:
            self.license = license
        if active_time is not None:
            self.active_time = active_time

    @property
    def id(self):
        """Gets the id of this UpdateUserResponse.

        用户UUID。

        :return: The id of this UpdateUserResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateUserResponse.

        用户UUID。

        :param id: The id of this UpdateUserResponse.
        :type id: str
        """
        self._id = id

    @property
    def user_account(self):
        """Gets the user_account of this UpdateUserResponse.

        华为云会议帐号。

        :return: The user_account of this UpdateUserResponse.
        :rtype: str
        """
        return self._user_account

    @user_account.setter
    def user_account(self, user_account):
        """Sets the user_account of this UpdateUserResponse.

        华为云会议帐号。

        :param user_account: The user_account of this UpdateUserResponse.
        :type user_account: str
        """
        self._user_account = user_account

    @property
    def name(self):
        """Gets the name of this UpdateUserResponse.

        名称。

        :return: The name of this UpdateUserResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateUserResponse.

        名称。

        :param name: The name of this UpdateUserResponse.
        :type name: str
        """
        self._name = name

    @property
    def english_name(self):
        """Gets the english_name of this UpdateUserResponse.

        英文名称。

        :return: The english_name of this UpdateUserResponse.
        :rtype: str
        """
        return self._english_name

    @english_name.setter
    def english_name(self, english_name):
        """Sets the english_name of this UpdateUserResponse.

        英文名称。

        :param english_name: The english_name of this UpdateUserResponse.
        :type english_name: str
        """
        self._english_name = english_name

    @property
    def phone(self):
        """Gets the phone of this UpdateUserResponse.

        联系电话。

        :return: The phone of this UpdateUserResponse.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this UpdateUserResponse.

        联系电话。

        :param phone: The phone of this UpdateUserResponse.
        :type phone: str
        """
        self._phone = phone

    @property
    def country(self):
        """Gets the country of this UpdateUserResponse.

        [[手机号所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 

        :return: The country of this UpdateUserResponse.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this UpdateUserResponse.

        [[手机号所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 

        :param country: The country of this UpdateUserResponse.
        :type country: str
        """
        self._country = country

    @property
    def email(self):
        """Gets the email of this UpdateUserResponse.

        邮箱地址。

        :return: The email of this UpdateUserResponse.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UpdateUserResponse.

        邮箱地址。

        :param email: The email of this UpdateUserResponse.
        :type email: str
        """
        self._email = email

    @property
    def sip_num(self):
        """Gets the sip_num of this UpdateUserResponse.

        SIP号码。

        :return: The sip_num of this UpdateUserResponse.
        :rtype: str
        """
        return self._sip_num

    @sip_num.setter
    def sip_num(self, sip_num):
        """Sets the sip_num of this UpdateUserResponse.

        SIP号码。

        :param sip_num: The sip_num of this UpdateUserResponse.
        :type sip_num: str
        """
        self._sip_num = sip_num

    @property
    def vmr_list(self):
        """Gets the vmr_list of this UpdateUserResponse.

        云会议室列表。

        :return: The vmr_list of this UpdateUserResponse.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.UserVmrDTO`]
        """
        return self._vmr_list

    @vmr_list.setter
    def vmr_list(self, vmr_list):
        """Sets the vmr_list of this UpdateUserResponse.

        云会议室列表。

        :param vmr_list: The vmr_list of this UpdateUserResponse.
        :type vmr_list: list[:class:`huaweicloudsdkmeeting.v1.UserVmrDTO`]
        """
        self._vmr_list = vmr_list

    @property
    def dept_code(self):
        """Gets the dept_code of this UpdateUserResponse.

        部门编码。

        :return: The dept_code of this UpdateUserResponse.
        :rtype: str
        """
        return self._dept_code

    @dept_code.setter
    def dept_code(self, dept_code):
        """Sets the dept_code of this UpdateUserResponse.

        部门编码。

        :param dept_code: The dept_code of this UpdateUserResponse.
        :type dept_code: str
        """
        self._dept_code = dept_code

    @property
    def dept_name(self):
        """Gets the dept_name of this UpdateUserResponse.

        部门名称。

        :return: The dept_name of this UpdateUserResponse.
        :rtype: str
        """
        return self._dept_name

    @dept_name.setter
    def dept_name(self, dept_name):
        """Sets the dept_name of this UpdateUserResponse.

        部门名称。

        :param dept_name: The dept_name of this UpdateUserResponse.
        :type dept_name: str
        """
        self._dept_name = dept_name

    @property
    def dept_name_path(self):
        """Gets the dept_name_path of this UpdateUserResponse.

        部门完整名称。

        :return: The dept_name_path of this UpdateUserResponse.
        :rtype: str
        """
        return self._dept_name_path

    @dept_name_path.setter
    def dept_name_path(self, dept_name_path):
        """Sets the dept_name_path of this UpdateUserResponse.

        部门完整名称。

        :param dept_name_path: The dept_name_path of this UpdateUserResponse.
        :type dept_name_path: str
        """
        self._dept_name_path = dept_name_path

    @property
    def user_type(self):
        """Gets the user_type of this UpdateUserResponse.

        用户类型。 - 2：企业成员账户

        :return: The user_type of this UpdateUserResponse.
        :rtype: int
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        """Sets the user_type of this UpdateUserResponse.

        用户类型。 - 2：企业成员账户

        :param user_type: The user_type of this UpdateUserResponse.
        :type user_type: int
        """
        self._user_type = user_type

    @property
    def admin_type(self):
        """Gets the admin_type of this UpdateUserResponse.

        管理员类型。 - 0：默认（超级）管理员 - 1：普通管理员 - 2：非管理员（即为普通企业成员，UserType是2时有效）

        :return: The admin_type of this UpdateUserResponse.
        :rtype: int
        """
        return self._admin_type

    @admin_type.setter
    def admin_type(self, admin_type):
        """Sets the admin_type of this UpdateUserResponse.

        管理员类型。 - 0：默认（超级）管理员 - 1：普通管理员 - 2：非管理员（即为普通企业成员，UserType是2时有效）

        :param admin_type: The admin_type of this UpdateUserResponse.
        :type admin_type: int
        """
        self._admin_type = admin_type

    @property
    def signature(self):
        """Gets the signature of this UpdateUserResponse.

        签名。

        :return: The signature of this UpdateUserResponse.
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this UpdateUserResponse.

        签名。

        :param signature: The signature of this UpdateUserResponse.
        :type signature: str
        """
        self._signature = signature

    @property
    def title(self):
        """Gets the title of this UpdateUserResponse.

        职位。

        :return: The title of this UpdateUserResponse.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this UpdateUserResponse.

        职位。

        :param title: The title of this UpdateUserResponse.
        :type title: str
        """
        self._title = title

    @property
    def desc(self):
        """Gets the desc of this UpdateUserResponse.

        备注。

        :return: The desc of this UpdateUserResponse.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this UpdateUserResponse.

        备注。

        :param desc: The desc of this UpdateUserResponse.
        :type desc: str
        """
        self._desc = desc

    @property
    def corp(self):
        """Gets the corp of this UpdateUserResponse.

        :return: The corp of this UpdateUserResponse.
        :rtype: :class:`huaweicloudsdkmeeting.v1.CorpBasicInfoDTO`
        """
        return self._corp

    @corp.setter
    def corp(self, corp):
        """Sets the corp of this UpdateUserResponse.

        :param corp: The corp of this UpdateUserResponse.
        :type corp: :class:`huaweicloudsdkmeeting.v1.CorpBasicInfoDTO`
        """
        self._corp = corp

    @property
    def function(self):
        """Gets the function of this UpdateUserResponse.

        :return: The function of this UpdateUserResponse.
        :rtype: :class:`huaweicloudsdkmeeting.v1.UserFunctionDTO`
        """
        return self._function

    @function.setter
    def function(self, function):
        """Sets the function of this UpdateUserResponse.

        :param function: The function of this UpdateUserResponse.
        :type function: :class:`huaweicloudsdkmeeting.v1.UserFunctionDTO`
        """
        self._function = function

    @property
    def dev_type(self):
        """Gets the dev_type of this UpdateUserResponse.

        :return: The dev_type of this UpdateUserResponse.
        :rtype: :class:`huaweicloudsdkmeeting.v1.QueryDeviceInfoResultDTO`
        """
        return self._dev_type

    @dev_type.setter
    def dev_type(self, dev_type):
        """Sets the dev_type of this UpdateUserResponse.

        :param dev_type: The dev_type of this UpdateUserResponse.
        :type dev_type: :class:`huaweicloudsdkmeeting.v1.QueryDeviceInfoResultDTO`
        """
        self._dev_type = dev_type

    @property
    def status(self):
        """Gets the status of this UpdateUserResponse.

        用户状态。 * 0：正常 * 1：停用 

        :return: The status of this UpdateUserResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateUserResponse.

        用户状态。 * 0：正常 * 1：停用 

        :param status: The status of this UpdateUserResponse.
        :type status: int
        """
        self._status = status

    @property
    def sort_level(self):
        """Gets the sort_level of this UpdateUserResponse.

        通讯录排序等级，序号越低优先级越高。

        :return: The sort_level of this UpdateUserResponse.
        :rtype: int
        """
        return self._sort_level

    @sort_level.setter
    def sort_level(self, sort_level):
        """Sets the sort_level of this UpdateUserResponse.

        通讯录排序等级，序号越低优先级越高。

        :param sort_level: The sort_level of this UpdateUserResponse.
        :type sort_level: int
        """
        self._sort_level = sort_level

    @property
    def hide_phone(self):
        """Gets the hide_phone of this UpdateUserResponse.

        是否隐藏手机号码。

        :return: The hide_phone of this UpdateUserResponse.
        :rtype: bool
        """
        return self._hide_phone

    @hide_phone.setter
    def hide_phone(self, hide_phone):
        """Sets the hide_phone of this UpdateUserResponse.

        是否隐藏手机号码。

        :param hide_phone: The hide_phone of this UpdateUserResponse.
        :type hide_phone: bool
        """
        self._hide_phone = hide_phone

    @property
    def vision_account(self):
        """Gets the vision_account of this UpdateUserResponse.

        智慧屏唯一帐号。

        :return: The vision_account of this UpdateUserResponse.
        :rtype: str
        """
        return self._vision_account

    @vision_account.setter
    def vision_account(self, vision_account):
        """Sets the vision_account of this UpdateUserResponse.

        智慧屏唯一帐号。

        :param vision_account: The vision_account of this UpdateUserResponse.
        :type vision_account: str
        """
        self._vision_account = vision_account

    @property
    def third_account(self):
        """Gets the third_account of this UpdateUserResponse.

        第三方User ID。

        :return: The third_account of this UpdateUserResponse.
        :rtype: str
        """
        return self._third_account

    @third_account.setter
    def third_account(self, third_account):
        """Sets the third_account of this UpdateUserResponse.

        第三方User ID。

        :param third_account: The third_account of this UpdateUserResponse.
        :type third_account: str
        """
        self._third_account = third_account

    @property
    def license(self):
        """Gets the license of this UpdateUserResponse.

        许可证。 * 0：商用 * 1：免费试用 

        :return: The license of this UpdateUserResponse.
        :rtype: int
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this UpdateUserResponse.

        许可证。 * 0：商用 * 1：免费试用 

        :param license: The license of this UpdateUserResponse.
        :type license: int
        """
        self._license = license

    @property
    def active_time(self):
        """Gets the active_time of this UpdateUserResponse.

        激活时间，utc时间戳。

        :return: The active_time of this UpdateUserResponse.
        :rtype: int
        """
        return self._active_time

    @active_time.setter
    def active_time(self, active_time):
        """Sets the active_time of this UpdateUserResponse.

        激活时间，utc时间戳。

        :param active_time: The active_time of this UpdateUserResponse.
        :type active_time: int
        """
        self._active_time = active_time

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
        if not isinstance(other, UpdateUserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
