# coding: utf-8

import pprint
import re

import six





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
        'auto_user_create': 'bool'
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
        'auto_user_create': 'autoUserCreate'
    }

    def __init__(self, id=None, name=None, address=None, admin_name=None, account=None, phone=None, country=None, email=None, enable_sms=None, enable_cloud_disk=None, enable_pstn=None, auto_user_create=None):
        """CorpBasicInfoDTO - a model defined in huaweicloud sdk"""
        
        

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

    @property
    def id(self):
        """Gets the id of this CorpBasicInfoDTO.

        企业id

        :return: The id of this CorpBasicInfoDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CorpBasicInfoDTO.

        企业id

        :param id: The id of this CorpBasicInfoDTO.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CorpBasicInfoDTO.

        企业名称

        :return: The name of this CorpBasicInfoDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CorpBasicInfoDTO.

        企业名称

        :param name: The name of this CorpBasicInfoDTO.
        :type: str
        """
        self._name = name

    @property
    def address(self):
        """Gets the address of this CorpBasicInfoDTO.

        企业所在地

        :return: The address of this CorpBasicInfoDTO.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this CorpBasicInfoDTO.

        企业所在地

        :param address: The address of this CorpBasicInfoDTO.
        :type: str
        """
        self._address = address

    @property
    def admin_name(self):
        """Gets the admin_name of this CorpBasicInfoDTO.

        管理员名称

        :return: The admin_name of this CorpBasicInfoDTO.
        :rtype: str
        """
        return self._admin_name

    @admin_name.setter
    def admin_name(self, admin_name):
        """Sets the admin_name of this CorpBasicInfoDTO.

        管理员名称

        :param admin_name: The admin_name of this CorpBasicInfoDTO.
        :type: str
        """
        self._admin_name = admin_name

    @property
    def account(self):
        """Gets the account of this CorpBasicInfoDTO.

        管理员账号

        :return: The account of this CorpBasicInfoDTO.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this CorpBasicInfoDTO.

        管理员账号

        :param account: The account of this CorpBasicInfoDTO.
        :type: str
        """
        self._account = account

    @property
    def phone(self):
        """Gets the phone of this CorpBasicInfoDTO.

        管理员手机

        :return: The phone of this CorpBasicInfoDTO.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this CorpBasicInfoDTO.

        管理员手机

        :param phone: The phone of this CorpBasicInfoDTO.
        :type: str
        """
        self._phone = phone

    @property
    def country(self):
        """Gets the country of this CorpBasicInfoDTO.

        管理员手机所属的国家

        :return: The country of this CorpBasicInfoDTO.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this CorpBasicInfoDTO.

        管理员手机所属的国家

        :param country: The country of this CorpBasicInfoDTO.
        :type: str
        """
        self._country = country

    @property
    def email(self):
        """Gets the email of this CorpBasicInfoDTO.

        管理员邮箱

        :return: The email of this CorpBasicInfoDTO.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CorpBasicInfoDTO.

        管理员邮箱

        :param email: The email of this CorpBasicInfoDTO.
        :type: str
        """
        self._email = email

    @property
    def enable_sms(self):
        """Gets the enable_sms of this CorpBasicInfoDTO.

        是否发送短信

        :return: The enable_sms of this CorpBasicInfoDTO.
        :rtype: bool
        """
        return self._enable_sms

    @enable_sms.setter
    def enable_sms(self, enable_sms):
        """Sets the enable_sms of this CorpBasicInfoDTO.

        是否发送短信

        :param enable_sms: The enable_sms of this CorpBasicInfoDTO.
        :type: bool
        """
        self._enable_sms = enable_sms

    @property
    def enable_cloud_disk(self):
        """Gets the enable_cloud_disk of this CorpBasicInfoDTO.

        是否开启云盘

        :return: The enable_cloud_disk of this CorpBasicInfoDTO.
        :rtype: bool
        """
        return self._enable_cloud_disk

    @enable_cloud_disk.setter
    def enable_cloud_disk(self, enable_cloud_disk):
        """Sets the enable_cloud_disk of this CorpBasicInfoDTO.

        是否开启云盘

        :param enable_cloud_disk: The enable_cloud_disk of this CorpBasicInfoDTO.
        :type: bool
        """
        self._enable_cloud_disk = enable_cloud_disk

    @property
    def enable_pstn(self):
        """Gets the enable_pstn of this CorpBasicInfoDTO.

        是否具有pstn功能

        :return: The enable_pstn of this CorpBasicInfoDTO.
        :rtype: bool
        """
        return self._enable_pstn

    @enable_pstn.setter
    def enable_pstn(self, enable_pstn):
        """Sets the enable_pstn of this CorpBasicInfoDTO.

        是否具有pstn功能

        :param enable_pstn: The enable_pstn of this CorpBasicInfoDTO.
        :type: bool
        """
        self._enable_pstn = enable_pstn

    @property
    def auto_user_create(self):
        """Gets the auto_user_create of this CorpBasicInfoDTO.

        是否支持自动开户

        :return: The auto_user_create of this CorpBasicInfoDTO.
        :rtype: bool
        """
        return self._auto_user_create

    @auto_user_create.setter
    def auto_user_create(self, auto_user_create):
        """Sets the auto_user_create of this CorpBasicInfoDTO.

        是否支持自动开户

        :param auto_user_create: The auto_user_create of this CorpBasicInfoDTO.
        :type: bool
        """
        self._auto_user_create = auto_user_create

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
        if not isinstance(other, CorpBasicInfoDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
