# coding: utf-8

import pprint
import re

import six





class QueryAdminResultDTO:


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
        'account': 'str',
        'name': 'str',
        'admin_type': 'int',
        'email': 'str',
        'phone': 'str',
        'country': 'str'
    }

    attribute_map = {
        'id': 'id',
        'account': 'account',
        'name': 'name',
        'admin_type': 'adminType',
        'email': 'email',
        'phone': 'phone',
        'country': 'country'
    }

    def __init__(self, id=None, account=None, name=None, admin_type=None, email=None, phone=None, country=None):
        """QueryAdminResultDTO - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._account = None
        self._name = None
        self._admin_type = None
        self._email = None
        self._phone = None
        self._country = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if account is not None:
            self.account = account
        if name is not None:
            self.name = name
        if admin_type is not None:
            self.admin_type = admin_type
        if email is not None:
            self.email = email
        if phone is not None:
            self.phone = phone
        if country is not None:
            self.country = country

    @property
    def id(self):
        """Gets the id of this QueryAdminResultDTO.

        用户id

        :return: The id of this QueryAdminResultDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QueryAdminResultDTO.

        用户id

        :param id: The id of this QueryAdminResultDTO.
        :type: str
        """
        self._id = id

    @property
    def account(self):
        """Gets the account of this QueryAdminResultDTO.

        用户账号

        :return: The account of this QueryAdminResultDTO.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this QueryAdminResultDTO.

        用户账号

        :param account: The account of this QueryAdminResultDTO.
        :type: str
        """
        self._account = account

    @property
    def name(self):
        """Gets the name of this QueryAdminResultDTO.

        名称

        :return: The name of this QueryAdminResultDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this QueryAdminResultDTO.

        名称

        :param name: The name of this QueryAdminResultDTO.
        :type: str
        """
        self._name = name

    @property
    def admin_type(self):
        """Gets the admin_type of this QueryAdminResultDTO.

        管理员类型 - 0：默认管理员 - 1：普通管理员

        :return: The admin_type of this QueryAdminResultDTO.
        :rtype: int
        """
        return self._admin_type

    @admin_type.setter
    def admin_type(self, admin_type):
        """Sets the admin_type of this QueryAdminResultDTO.

        管理员类型 - 0：默认管理员 - 1：普通管理员

        :param admin_type: The admin_type of this QueryAdminResultDTO.
        :type: int
        """
        self._admin_type = admin_type

    @property
    def email(self):
        """Gets the email of this QueryAdminResultDTO.

        邮箱

        :return: The email of this QueryAdminResultDTO.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this QueryAdminResultDTO.

        邮箱

        :param email: The email of this QueryAdminResultDTO.
        :type: str
        """
        self._email = email

    @property
    def phone(self):
        """Gets the phone of this QueryAdminResultDTO.

        联系电话

        :return: The phone of this QueryAdminResultDTO.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this QueryAdminResultDTO.

        联系电话

        :param phone: The phone of this QueryAdminResultDTO.
        :type: str
        """
        self._phone = phone

    @property
    def country(self):
        """Gets the country of this QueryAdminResultDTO.

        联系电话所属的国家

        :return: The country of this QueryAdminResultDTO.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this QueryAdminResultDTO.

        联系电话所属的国家

        :param country: The country of this QueryAdminResultDTO.
        :type: str
        """
        self._country = country

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
        if not isinstance(other, QueryAdminResultDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
