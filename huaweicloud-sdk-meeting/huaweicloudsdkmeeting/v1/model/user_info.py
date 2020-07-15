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
        'name_en': 'str'
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
        'name_en': 'nameEn'
    }

    def __init__(self, user_id=None, uclogin_account=None, service_account=None, number_ha1=None, alias1=None, company_id=None, sp_id=None, company_domain=None, realm=None, user_type=None, admin_type=None, name=None, name_en=None):
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
