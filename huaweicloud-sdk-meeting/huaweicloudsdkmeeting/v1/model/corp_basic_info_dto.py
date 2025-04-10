# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CorpBasicInfoDTO:

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
        'address': 'str',
        'admin_name': 'str',
        'account': 'str',
        'phone': 'str',
        'country': 'str',
        'email': 'str',
        'enable_sms': 'bool',
        'enable_cloud_disk': 'bool',
        'enable_pstn': 'bool',
        'auto_user_create': 'bool',
        'corp_type': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'address': 'address',
        'admin_name': 'adminName',
        'account': 'account',
        'phone': 'phone',
        'country': 'country',
        'email': 'email',
        'enable_sms': 'enableSMS',
        'enable_cloud_disk': 'enableCloudDisk',
        'enable_pstn': 'enablePstn',
        'auto_user_create': 'autoUserCreate',
        'corp_type': 'corpType'
    }

    def __init__(self, id=None, name=None, address=None, admin_name=None, account=None, phone=None, country=None, email=None, enable_sms=None, enable_cloud_disk=None, enable_pstn=None, auto_user_create=None, corp_type=None):
        r"""CorpBasicInfoDTO

        The model defined in huaweicloud sdk

        :param id: 企业id。
        :type id: str
        :param name: 企业名称。
        :type name: str
        :param address: 企业所在地。
        :type address: str
        :param admin_name: 管理员名称。
        :type admin_name: str
        :param account: 管理员的华为云会议帐号。
        :type account: str
        :param phone: 管理员手机。
        :type phone: str
        :param country: [[手机号所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 
        :type country: str
        :param email: 管理员邮箱。
        :type email: str
        :param enable_sms: 是否通过短信形式发送会议通知。
        :type enable_sms: bool
        :param enable_cloud_disk: 是否开启云盘。
        :type enable_cloud_disk: bool
        :param enable_pstn: 是否具有pstn功能。
        :type enable_pstn: bool
        :param auto_user_create: 是否支持自动开户。
        :type auto_user_create: bool
        :param corp_type: 企业类型。 * 0：旗舰版 * 5：免费版 * 6：标准版 
        :type corp_type: int
        """
        
        

        self._id = None
        self._name = None
        self._address = None
        self._admin_name = None
        self._account = None
        self._phone = None
        self._country = None
        self._email = None
        self._enable_sms = None
        self._enable_cloud_disk = None
        self._enable_pstn = None
        self._auto_user_create = None
        self._corp_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if address is not None:
            self.address = address
        if admin_name is not None:
            self.admin_name = admin_name
        if account is not None:
            self.account = account
        if phone is not None:
            self.phone = phone
        if country is not None:
            self.country = country
        if email is not None:
            self.email = email
        if enable_sms is not None:
            self.enable_sms = enable_sms
        if enable_cloud_disk is not None:
            self.enable_cloud_disk = enable_cloud_disk
        if enable_pstn is not None:
            self.enable_pstn = enable_pstn
        if auto_user_create is not None:
            self.auto_user_create = auto_user_create
        if corp_type is not None:
            self.corp_type = corp_type

    @property
    def id(self):
        r"""Gets the id of this CorpBasicInfoDTO.

        企业id。

        :return: The id of this CorpBasicInfoDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CorpBasicInfoDTO.

        企业id。

        :param id: The id of this CorpBasicInfoDTO.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CorpBasicInfoDTO.

        企业名称。

        :return: The name of this CorpBasicInfoDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CorpBasicInfoDTO.

        企业名称。

        :param name: The name of this CorpBasicInfoDTO.
        :type name: str
        """
        self._name = name

    @property
    def address(self):
        r"""Gets the address of this CorpBasicInfoDTO.

        企业所在地。

        :return: The address of this CorpBasicInfoDTO.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this CorpBasicInfoDTO.

        企业所在地。

        :param address: The address of this CorpBasicInfoDTO.
        :type address: str
        """
        self._address = address

    @property
    def admin_name(self):
        r"""Gets the admin_name of this CorpBasicInfoDTO.

        管理员名称。

        :return: The admin_name of this CorpBasicInfoDTO.
        :rtype: str
        """
        return self._admin_name

    @admin_name.setter
    def admin_name(self, admin_name):
        r"""Sets the admin_name of this CorpBasicInfoDTO.

        管理员名称。

        :param admin_name: The admin_name of this CorpBasicInfoDTO.
        :type admin_name: str
        """
        self._admin_name = admin_name

    @property
    def account(self):
        r"""Gets the account of this CorpBasicInfoDTO.

        管理员的华为云会议帐号。

        :return: The account of this CorpBasicInfoDTO.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        r"""Sets the account of this CorpBasicInfoDTO.

        管理员的华为云会议帐号。

        :param account: The account of this CorpBasicInfoDTO.
        :type account: str
        """
        self._account = account

    @property
    def phone(self):
        r"""Gets the phone of this CorpBasicInfoDTO.

        管理员手机。

        :return: The phone of this CorpBasicInfoDTO.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        r"""Sets the phone of this CorpBasicInfoDTO.

        管理员手机。

        :param phone: The phone of this CorpBasicInfoDTO.
        :type phone: str
        """
        self._phone = phone

    @property
    def country(self):
        r"""Gets the country of this CorpBasicInfoDTO.

        [[手机号所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 

        :return: The country of this CorpBasicInfoDTO.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        r"""Sets the country of this CorpBasicInfoDTO.

        [[手机号所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 

        :param country: The country of this CorpBasicInfoDTO.
        :type country: str
        """
        self._country = country

    @property
    def email(self):
        r"""Gets the email of this CorpBasicInfoDTO.

        管理员邮箱。

        :return: The email of this CorpBasicInfoDTO.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this CorpBasicInfoDTO.

        管理员邮箱。

        :param email: The email of this CorpBasicInfoDTO.
        :type email: str
        """
        self._email = email

    @property
    def enable_sms(self):
        r"""Gets the enable_sms of this CorpBasicInfoDTO.

        是否通过短信形式发送会议通知。

        :return: The enable_sms of this CorpBasicInfoDTO.
        :rtype: bool
        """
        return self._enable_sms

    @enable_sms.setter
    def enable_sms(self, enable_sms):
        r"""Sets the enable_sms of this CorpBasicInfoDTO.

        是否通过短信形式发送会议通知。

        :param enable_sms: The enable_sms of this CorpBasicInfoDTO.
        :type enable_sms: bool
        """
        self._enable_sms = enable_sms

    @property
    def enable_cloud_disk(self):
        r"""Gets the enable_cloud_disk of this CorpBasicInfoDTO.

        是否开启云盘。

        :return: The enable_cloud_disk of this CorpBasicInfoDTO.
        :rtype: bool
        """
        return self._enable_cloud_disk

    @enable_cloud_disk.setter
    def enable_cloud_disk(self, enable_cloud_disk):
        r"""Sets the enable_cloud_disk of this CorpBasicInfoDTO.

        是否开启云盘。

        :param enable_cloud_disk: The enable_cloud_disk of this CorpBasicInfoDTO.
        :type enable_cloud_disk: bool
        """
        self._enable_cloud_disk = enable_cloud_disk

    @property
    def enable_pstn(self):
        r"""Gets the enable_pstn of this CorpBasicInfoDTO.

        是否具有pstn功能。

        :return: The enable_pstn of this CorpBasicInfoDTO.
        :rtype: bool
        """
        return self._enable_pstn

    @enable_pstn.setter
    def enable_pstn(self, enable_pstn):
        r"""Sets the enable_pstn of this CorpBasicInfoDTO.

        是否具有pstn功能。

        :param enable_pstn: The enable_pstn of this CorpBasicInfoDTO.
        :type enable_pstn: bool
        """
        self._enable_pstn = enable_pstn

    @property
    def auto_user_create(self):
        r"""Gets the auto_user_create of this CorpBasicInfoDTO.

        是否支持自动开户。

        :return: The auto_user_create of this CorpBasicInfoDTO.
        :rtype: bool
        """
        return self._auto_user_create

    @auto_user_create.setter
    def auto_user_create(self, auto_user_create):
        r"""Sets the auto_user_create of this CorpBasicInfoDTO.

        是否支持自动开户。

        :param auto_user_create: The auto_user_create of this CorpBasicInfoDTO.
        :type auto_user_create: bool
        """
        self._auto_user_create = auto_user_create

    @property
    def corp_type(self):
        r"""Gets the corp_type of this CorpBasicInfoDTO.

        企业类型。 * 0：旗舰版 * 5：免费版 * 6：标准版 

        :return: The corp_type of this CorpBasicInfoDTO.
        :rtype: int
        """
        return self._corp_type

    @corp_type.setter
    def corp_type(self, corp_type):
        r"""Sets the corp_type of this CorpBasicInfoDTO.

        企业类型。 * 0：旗舰版 * 5：免费版 * 6：标准版 

        :param corp_type: The corp_type of this CorpBasicInfoDTO.
        :type corp_type: int
        """
        self._corp_type = corp_type

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
        if not isinstance(other, CorpBasicInfoDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
