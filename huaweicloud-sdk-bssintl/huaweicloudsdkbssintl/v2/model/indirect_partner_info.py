# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IndirectPartnerInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'indirect_partner_id': 'str',
        'mobile_phone': 'str',
        'email': 'str',
        'account_name': 'str',
        'name': 'str',
        'associated_on': 'str',
        'account_manager_id': 'str',
        'account_manager_name': 'str'
    }

    attribute_map = {
        'indirect_partner_id': 'indirect_partner_id',
        'mobile_phone': 'mobile_phone',
        'email': 'email',
        'account_name': 'account_name',
        'name': 'name',
        'associated_on': 'associated_on',
        'account_manager_id': 'account_manager_id',
        'account_manager_name': 'account_manager_name'
    }

    def __init__(self, indirect_partner_id=None, mobile_phone=None, email=None, account_name=None, name=None, associated_on=None, account_manager_id=None, account_manager_name=None):
        """IndirectPartnerInfo

        The model defined in huaweicloud sdk

        :param indirect_partner_id: 云经销商ID。
        :type indirect_partner_id: str
        :param mobile_phone: 云经销商的手机号码。
        :type mobile_phone: str
        :param email: 云经销商的邮箱。
        :type email: str
        :param account_name: 云经销商的账户名。
        :type account_name: str
        :param name: 云经销商的名称。
        :type name: str
        :param associated_on: 云经销商关联华为云总经销商的时间。 UTC时间（包括时区），例如2016-03-28T00:00:00Z。
        :type associated_on: str
        :param account_manager_id: 客户经理登录账户名。
        :type account_manager_id: str
        :param account_manager_name: 客户经理的名称。
        :type account_manager_name: str
        """
        
        

        self._indirect_partner_id = None
        self._mobile_phone = None
        self._email = None
        self._account_name = None
        self._name = None
        self._associated_on = None
        self._account_manager_id = None
        self._account_manager_name = None
        self.discriminator = None

        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id
        if mobile_phone is not None:
            self.mobile_phone = mobile_phone
        if email is not None:
            self.email = email
        if account_name is not None:
            self.account_name = account_name
        if name is not None:
            self.name = name
        if associated_on is not None:
            self.associated_on = associated_on
        if account_manager_id is not None:
            self.account_manager_id = account_manager_id
        if account_manager_name is not None:
            self.account_manager_name = account_manager_name

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this IndirectPartnerInfo.

        云经销商ID。

        :return: The indirect_partner_id of this IndirectPartnerInfo.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this IndirectPartnerInfo.

        云经销商ID。

        :param indirect_partner_id: The indirect_partner_id of this IndirectPartnerInfo.
        :type indirect_partner_id: str
        """
        self._indirect_partner_id = indirect_partner_id

    @property
    def mobile_phone(self):
        """Gets the mobile_phone of this IndirectPartnerInfo.

        云经销商的手机号码。

        :return: The mobile_phone of this IndirectPartnerInfo.
        :rtype: str
        """
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        """Sets the mobile_phone of this IndirectPartnerInfo.

        云经销商的手机号码。

        :param mobile_phone: The mobile_phone of this IndirectPartnerInfo.
        :type mobile_phone: str
        """
        self._mobile_phone = mobile_phone

    @property
    def email(self):
        """Gets the email of this IndirectPartnerInfo.

        云经销商的邮箱。

        :return: The email of this IndirectPartnerInfo.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this IndirectPartnerInfo.

        云经销商的邮箱。

        :param email: The email of this IndirectPartnerInfo.
        :type email: str
        """
        self._email = email

    @property
    def account_name(self):
        """Gets the account_name of this IndirectPartnerInfo.

        云经销商的账户名。

        :return: The account_name of this IndirectPartnerInfo.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this IndirectPartnerInfo.

        云经销商的账户名。

        :param account_name: The account_name of this IndirectPartnerInfo.
        :type account_name: str
        """
        self._account_name = account_name

    @property
    def name(self):
        """Gets the name of this IndirectPartnerInfo.

        云经销商的名称。

        :return: The name of this IndirectPartnerInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IndirectPartnerInfo.

        云经销商的名称。

        :param name: The name of this IndirectPartnerInfo.
        :type name: str
        """
        self._name = name

    @property
    def associated_on(self):
        """Gets the associated_on of this IndirectPartnerInfo.

        云经销商关联华为云总经销商的时间。 UTC时间（包括时区），例如2016-03-28T00:00:00Z。

        :return: The associated_on of this IndirectPartnerInfo.
        :rtype: str
        """
        return self._associated_on

    @associated_on.setter
    def associated_on(self, associated_on):
        """Sets the associated_on of this IndirectPartnerInfo.

        云经销商关联华为云总经销商的时间。 UTC时间（包括时区），例如2016-03-28T00:00:00Z。

        :param associated_on: The associated_on of this IndirectPartnerInfo.
        :type associated_on: str
        """
        self._associated_on = associated_on

    @property
    def account_manager_id(self):
        """Gets the account_manager_id of this IndirectPartnerInfo.

        客户经理登录账户名。

        :return: The account_manager_id of this IndirectPartnerInfo.
        :rtype: str
        """
        return self._account_manager_id

    @account_manager_id.setter
    def account_manager_id(self, account_manager_id):
        """Sets the account_manager_id of this IndirectPartnerInfo.

        客户经理登录账户名。

        :param account_manager_id: The account_manager_id of this IndirectPartnerInfo.
        :type account_manager_id: str
        """
        self._account_manager_id = account_manager_id

    @property
    def account_manager_name(self):
        """Gets the account_manager_name of this IndirectPartnerInfo.

        客户经理的名称。

        :return: The account_manager_name of this IndirectPartnerInfo.
        :rtype: str
        """
        return self._account_manager_name

    @account_manager_name.setter
    def account_manager_name(self, account_manager_name):
        """Sets the account_manager_name of this IndirectPartnerInfo.

        客户经理的名称。

        :param account_manager_name: The account_manager_name of this IndirectPartnerInfo.
        :type account_manager_name: str
        """
        self._account_manager_name = account_manager_name

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
        if not isinstance(other, IndirectPartnerInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
