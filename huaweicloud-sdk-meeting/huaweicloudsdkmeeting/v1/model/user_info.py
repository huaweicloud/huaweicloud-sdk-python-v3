# coding: utf-8

import pprint
import re

import six





class UserInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'user_id': 'str',
        'uclogin_account': 'str',
        'service_account': 'str',
        'number_ha1': 'str',
        'alias1': 'str',
        'company_id': 'str',
        'sp_id': 'str',
        'company_domain': 'str',
        'realm': 'str',
        'user_type': 'int',
        'admin_type': 'int',
        'name': 'str',
        'name_en': 'str',
        'is_bind_phone': 'bool',
        'free_user': 'bool',
        'third_account': 'str',
        'vision_account': 'str',
        'head_picture_url': 'str',
        'password': 'str',
        'status': 'int',
        'paid_account': 'str',
        'paid_password': 'str',
        'we_link_user': 'bool',
        'app_id': 'str',
        'tr069_account': 'str',
        'corp_type': 'int',
        'cloud_user_id': 'str',
        'gray_user': 'bool'
    }

    attribute_map = {
        'user_id': 'userId',
        'uclogin_account': 'ucloginAccount',
        'service_account': 'serviceAccount',
        'number_ha1': 'numberHA1',
        'alias1': 'alias1',
        'company_id': 'companyId',
        'sp_id': 'spId',
        'company_domain': 'companyDomain',
        'realm': 'realm',
        'user_type': 'userType',
        'admin_type': 'adminType',
        'name': 'name',
        'name_en': 'nameEn',
        'is_bind_phone': 'isBindPhone',
        'free_user': 'freeUser',
        'third_account': 'thirdAccount',
        'vision_account': 'visionAccount',
        'head_picture_url': 'headPictureUrl',
        'password': 'password',
        'status': 'status',
        'paid_account': 'paidAccount',
        'paid_password': 'paidPassword',
        'we_link_user': 'weLinkUser',
        'app_id': 'appId',
        'tr069_account': 'tr069Account',
        'corp_type': 'corpType',
        'cloud_user_id': 'cloudUserId',
        'gray_user': 'grayUser'
    }

    def __init__(self, user_id=None, uclogin_account=None, service_account=None, number_ha1=None, alias1=None, company_id=None, sp_id=None, company_domain=None, realm=None, user_type=None, admin_type=None, name=None, name_en=None, is_bind_phone=None, free_user=None, third_account=None, vision_account=None, head_picture_url=None, password=None, status=None, paid_account=None, paid_password=None, we_link_user=None, app_id=None, tr069_account=None, corp_type=None, cloud_user_id=None, gray_user=None):
        """UserInfo - a model defined in huaweicloud sdk"""
        
        

        self._user_id = None
        self._uclogin_account = None
        self._service_account = None
        self._number_ha1 = None
        self._alias1 = None
        self._company_id = None
        self._sp_id = None
        self._company_domain = None
        self._realm = None
        self._user_type = None
        self._admin_type = None
        self._name = None
        self._name_en = None
        self._is_bind_phone = None
        self._free_user = None
        self._third_account = None
        self._vision_account = None
        self._head_picture_url = None
        self._password = None
        self._status = None
        self._paid_account = None
        self._paid_password = None
        self._we_link_user = None
        self._app_id = None
        self._tr069_account = None
        self._corp_type = None
        self._cloud_user_id = None
        self._gray_user = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        self.uclogin_account = uclogin_account
        if service_account is not None:
            self.service_account = service_account
        if number_ha1 is not None:
            self.number_ha1 = number_ha1
        if alias1 is not None:
            self.alias1 = alias1
        if company_id is not None:
            self.company_id = company_id
        if sp_id is not None:
            self.sp_id = sp_id
        if company_domain is not None:
            self.company_domain = company_domain
        if realm is not None:
            self.realm = realm
        if user_type is not None:
            self.user_type = user_type
        if admin_type is not None:
            self.admin_type = admin_type
        if name is not None:
            self.name = name
        if name_en is not None:
            self.name_en = name_en
        if is_bind_phone is not None:
            self.is_bind_phone = is_bind_phone
        if free_user is not None:
            self.free_user = free_user
        if third_account is not None:
            self.third_account = third_account
        if vision_account is not None:
            self.vision_account = vision_account
        if head_picture_url is not None:
            self.head_picture_url = head_picture_url
        if password is not None:
            self.password = password
        if status is not None:
            self.status = status
        if paid_account is not None:
            self.paid_account = paid_account
        if paid_password is not None:
            self.paid_password = paid_password
        if we_link_user is not None:
            self.we_link_user = we_link_user
        if app_id is not None:
            self.app_id = app_id
        if tr069_account is not None:
            self.tr069_account = tr069_account
        if corp_type is not None:
            self.corp_type = corp_type
        if cloud_user_id is not None:
            self.cloud_user_id = cloud_user_id
        if gray_user is not None:
            self.gray_user = gray_user

    @property
    def user_id(self):
        """Gets the user_id of this UserInfo.

        用户ID

        :return: The user_id of this UserInfo.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserInfo.

        用户ID

        :param user_id: The user_id of this UserInfo.
        :type: str
        """
        self._user_id = user_id

    @property
    def uclogin_account(self):
        """Gets the uclogin_account of this UserInfo.

        用户UC帐号

        :return: The uclogin_account of this UserInfo.
        :rtype: str
        """
        return self._uclogin_account

    @uclogin_account.setter
    def uclogin_account(self, uclogin_account):
        """Sets the uclogin_account of this UserInfo.

        用户UC帐号

        :param uclogin_account: The uclogin_account of this UserInfo.
        :type: str
        """
        self._uclogin_account = uclogin_account

    @property
    def service_account(self):
        """Gets the service_account of this UserInfo.

        用户关联的号码，sip格式。 登录类型不一样获取到的号码也不同，如软终端和硬终端客户端登录获取的号码不同。若未关联号码，则为空。 例如：sip:+8675590121000@domain5.huawei.com 

        :return: The service_account of this UserInfo.
        :rtype: str
        """
        return self._service_account

    @service_account.setter
    def service_account(self, service_account):
        """Sets the service_account of this UserInfo.

        用户关联的号码，sip格式。 登录类型不一样获取到的号码也不同，如软终端和硬终端客户端登录获取的号码不同。若未关联号码，则为空。 例如：sip:+8675590121000@domain5.huawei.com 

        :param service_account: The service_account of this UserInfo.
        :type: str
        """
        self._service_account = service_account

    @property
    def number_ha1(self):
        """Gets the number_ha1 of this UserInfo.

        号码对应的HA1

        :return: The number_ha1 of this UserInfo.
        :rtype: str
        """
        return self._number_ha1

    @number_ha1.setter
    def number_ha1(self, number_ha1):
        """Sets the number_ha1 of this UserInfo.

        号码对应的HA1

        :param number_ha1: The number_ha1 of this UserInfo.
        :type: str
        """
        self._number_ha1 = number_ha1

    @property
    def alias1(self):
        """Gets the alias1 of this UserInfo.

        用户别名1

        :return: The alias1 of this UserInfo.
        :rtype: str
        """
        return self._alias1

    @alias1.setter
    def alias1(self, alias1):
        """Sets the alias1 of this UserInfo.

        用户别名1

        :param alias1: The alias1 of this UserInfo.
        :type: str
        """
        self._alias1 = alias1

    @property
    def company_id(self):
        """Gets the company_id of this UserInfo.

        企业ID

        :return: The company_id of this UserInfo.
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this UserInfo.

        企业ID

        :param company_id: The company_id of this UserInfo.
        :type: str
        """
        self._company_id = company_id

    @property
    def sp_id(self):
        """Gets the sp_id of this UserInfo.

        SP ID

        :return: The sp_id of this UserInfo.
        :rtype: str
        """
        return self._sp_id

    @sp_id.setter
    def sp_id(self, sp_id):
        """Sets the sp_id of this UserInfo.

        SP ID

        :param sp_id: The sp_id of this UserInfo.
        :type: str
        """
        self._sp_id = sp_id

    @property
    def company_domain(self):
        """Gets the company_domain of this UserInfo.

        企业域名

        :return: The company_domain of this UserInfo.
        :rtype: str
        """
        return self._company_domain

    @company_domain.setter
    def company_domain(self, company_domain):
        """Sets the company_domain of this UserInfo.

        企业域名

        :param company_domain: The company_domain of this UserInfo.
        :type: str
        """
        self._company_domain = company_domain

    @property
    def realm(self):
        """Gets the realm of this UserInfo.

        本地鉴权：realm

        :return: The realm of this UserInfo.
        :rtype: str
        """
        return self._realm

    @realm.setter
    def realm(self, realm):
        """Sets the realm of this UserInfo.

        本地鉴权：realm

        :param realm: The realm of this UserInfo.
        :type: str
        """
        self._realm = realm

    @property
    def user_type(self):
        """Gets the user_type of this UserInfo.

        用户类型。 * 0：系统管理用户 * 1：SP管理用户 * 2：企业用户 * 3：upath用户 * 4：硬终端默认用户 * 5：TE终端用户 * 6：顾客用户 * 7：公共设备用户 * 8：集群群组用户 * 9：USM用户 

        :return: The user_type of this UserInfo.
        :rtype: int
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        """Sets the user_type of this UserInfo.

        用户类型。 * 0：系统管理用户 * 1：SP管理用户 * 2：企业用户 * 3：upath用户 * 4：硬终端默认用户 * 5：TE终端用户 * 6：顾客用户 * 7：公共设备用户 * 8：集群群组用户 * 9：USM用户 

        :param user_type: The user_type of this UserInfo.
        :type: int
        """
        self._user_type = user_type

    @property
    def admin_type(self):
        """Gets the admin_type of this UserInfo.

        管理员类型： * 0：默认管理员 * 1：普通管理员 * 2：非管理员，即普通企业成员，USERTYPE为2时有效 

        :return: The admin_type of this UserInfo.
        :rtype: int
        """
        return self._admin_type

    @admin_type.setter
    def admin_type(self, admin_type):
        """Sets the admin_type of this UserInfo.

        管理员类型： * 0：默认管理员 * 1：普通管理员 * 2：非管理员，即普通企业成员，USERTYPE为2时有效 

        :param admin_type: The admin_type of this UserInfo.
        :type: int
        """
        self._admin_type = admin_type

    @property
    def name(self):
        """Gets the name of this UserInfo.

        用户姓名

        :return: The name of this UserInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserInfo.

        用户姓名

        :param name: The name of this UserInfo.
        :type: str
        """
        self._name = name

    @property
    def name_en(self):
        """Gets the name_en of this UserInfo.

        用户英文姓名

        :return: The name_en of this UserInfo.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        """Sets the name_en of this UserInfo.

        用户英文姓名

        :param name_en: The name_en of this UserInfo.
        :type: str
        """
        self._name_en = name_en

    @property
    def is_bind_phone(self):
        """Gets the is_bind_phone of this UserInfo.

        标识是否绑定手机

        :return: The is_bind_phone of this UserInfo.
        :rtype: bool
        """
        return self._is_bind_phone

    @is_bind_phone.setter
    def is_bind_phone(self, is_bind_phone):
        """Sets the is_bind_phone of this UserInfo.

        标识是否绑定手机

        :param is_bind_phone: The is_bind_phone of this UserInfo.
        :type: bool
        """
        self._is_bind_phone = is_bind_phone

    @property
    def free_user(self):
        """Gets the free_user of this UserInfo.

        标识是否是免费试用用户

        :return: The free_user of this UserInfo.
        :rtype: bool
        """
        return self._free_user

    @free_user.setter
    def free_user(self, free_user):
        """Sets the free_user of this UserInfo.

        标识是否是免费试用用户

        :param free_user: The free_user of this UserInfo.
        :type: bool
        """
        self._free_user = free_user

    @property
    def third_account(self):
        """Gets the third_account of this UserInfo.

        用户的第三方账号，例如华为账号登录时获取到的union_id

        :return: The third_account of this UserInfo.
        :rtype: str
        """
        return self._third_account

    @third_account.setter
    def third_account(self, third_account):
        """Sets the third_account of this UserInfo.

        用户的第三方账号，例如华为账号登录时获取到的union_id

        :param third_account: The third_account of this UserInfo.
        :type: str
        """
        self._third_account = third_account

    @property
    def vision_account(self):
        """Gets the vision_account of this UserInfo.

        智慧屏设备id

        :return: The vision_account of this UserInfo.
        :rtype: str
        """
        return self._vision_account

    @vision_account.setter
    def vision_account(self, vision_account):
        """Sets the vision_account of this UserInfo.

        智慧屏设备id

        :param vision_account: The vision_account of this UserInfo.
        :type: str
        """
        self._vision_account = vision_account

    @property
    def head_picture_url(self):
        """Gets the head_picture_url of this UserInfo.

        头像链接

        :return: The head_picture_url of this UserInfo.
        :rtype: str
        """
        return self._head_picture_url

    @head_picture_url.setter
    def head_picture_url(self, head_picture_url):
        """Sets the head_picture_url of this UserInfo.

        头像链接

        :param head_picture_url: The head_picture_url of this UserInfo.
        :type: str
        """
        self._head_picture_url = head_picture_url

    @property
    def password(self):
        """Gets the password of this UserInfo.

        机机密码，用于智慧屏登录

        :return: The password of this UserInfo.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UserInfo.

        机机密码，用于智慧屏登录

        :param password: The password of this UserInfo.
        :type: str
        """
        self._password = password

    @property
    def status(self):
        """Gets the status of this UserInfo.

        用户状态。 * 0：正常 * 1：停用 

        :return: The status of this UserInfo.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UserInfo.

        用户状态。 * 0：正常 * 1：停用 

        :param status: The status of this UserInfo.
        :type: int
        """
        self._status = status

    @property
    def paid_account(self):
        """Gets the paid_account of this UserInfo.

        付费用户机机账号，用于智慧屏登录

        :return: The paid_account of this UserInfo.
        :rtype: str
        """
        return self._paid_account

    @paid_account.setter
    def paid_account(self, paid_account):
        """Sets the paid_account of this UserInfo.

        付费用户机机账号，用于智慧屏登录

        :param paid_account: The paid_account of this UserInfo.
        :type: str
        """
        self._paid_account = paid_account

    @property
    def paid_password(self):
        """Gets the paid_password of this UserInfo.

        付费用户机机密码，用于智慧屏登录

        :return: The paid_password of this UserInfo.
        :rtype: str
        """
        return self._paid_password

    @paid_password.setter
    def paid_password(self, paid_password):
        """Sets the paid_password of this UserInfo.

        付费用户机机密码，用于智慧屏登录

        :param paid_password: The paid_password of this UserInfo.
        :type: str
        """
        self._paid_password = paid_password

    @property
    def we_link_user(self):
        """Gets the we_link_user of this UserInfo.

        标识是否是WeLink用户

        :return: The we_link_user of this UserInfo.
        :rtype: bool
        """
        return self._we_link_user

    @we_link_user.setter
    def we_link_user(self, we_link_user):
        """Sets the we_link_user of this UserInfo.

        标识是否是WeLink用户

        :param we_link_user: The we_link_user of this UserInfo.
        :type: bool
        """
        self._we_link_user = we_link_user

    @property
    def app_id(self):
        """Gets the app_id of this UserInfo.

        应用ID

        :return: The app_id of this UserInfo.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this UserInfo.

        应用ID

        :param app_id: The app_id of this UserInfo.
        :type: str
        """
        self._app_id = app_id

    @property
    def tr069_account(self):
        """Gets the tr069_account of this UserInfo.

        tr069帐号

        :return: The tr069_account of this UserInfo.
        :rtype: str
        """
        return self._tr069_account

    @tr069_account.setter
    def tr069_account(self, tr069_account):
        """Sets the tr069_account of this UserInfo.

        tr069帐号

        :param tr069_account: The tr069_account of this UserInfo.
        :type: str
        """
        self._tr069_account = tr069_account

    @property
    def corp_type(self):
        """Gets the corp_type of this UserInfo.

        企业类型。 * 0：企业版 * 1：公共企业，手机、邮箱注册时会放到该企业内 * 2：公共企业，智慧屏用户自动开户时会放到该企业内 * 3：公共企业，大屏用户自动开户时会放到该企业内 * 4：公共TOC消费者企业 * 5：免费版 * 6：专业版 

        :return: The corp_type of this UserInfo.
        :rtype: int
        """
        return self._corp_type

    @corp_type.setter
    def corp_type(self, corp_type):
        """Sets the corp_type of this UserInfo.

        企业类型。 * 0：企业版 * 1：公共企业，手机、邮箱注册时会放到该企业内 * 2：公共企业，智慧屏用户自动开户时会放到该企业内 * 3：公共企业，大屏用户自动开户时会放到该企业内 * 4：公共TOC消费者企业 * 5：免费版 * 6：专业版 

        :param corp_type: The corp_type of this UserInfo.
        :type: int
        """
        self._corp_type = corp_type

    @property
    def cloud_user_id(self):
        """Gets the cloud_user_id of this UserInfo.

        华为云账号ID

        :return: The cloud_user_id of this UserInfo.
        :rtype: str
        """
        return self._cloud_user_id

    @cloud_user_id.setter
    def cloud_user_id(self, cloud_user_id):
        """Sets the cloud_user_id of this UserInfo.

        华为云账号ID

        :param cloud_user_id: The cloud_user_id of this UserInfo.
        :type: str
        """
        self._cloud_user_id = cloud_user_id

    @property
    def gray_user(self):
        """Gets the gray_user of this UserInfo.

        标识是否是灰度用户

        :return: The gray_user of this UserInfo.
        :rtype: bool
        """
        return self._gray_user

    @gray_user.setter
    def gray_user(self, gray_user):
        """Sets the gray_user of this UserInfo.

        标识是否是灰度用户

        :param gray_user: The gray_user of this UserInfo.
        :type: bool
        """
        self._gray_user = gray_user

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
        if not isinstance(other, UserInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
