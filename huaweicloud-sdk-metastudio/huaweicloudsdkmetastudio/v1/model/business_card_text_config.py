# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BusinessCardTextConfig:

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
        'company': 'str',
        'title': 'str',
        'mobile_phone': 'str',
        'phone': 'str',
        'mail': 'str',
        'address': 'str',
        'other1': 'str',
        'other2': 'str',
        'other3': 'str'
    }

    attribute_map = {
        'name': 'name',
        'company': 'company',
        'title': 'title',
        'mobile_phone': 'mobile_phone',
        'phone': 'phone',
        'mail': 'mail',
        'address': 'address',
        'other1': 'other1',
        'other2': 'other2',
        'other3': 'other3'
    }

    def __init__(self, name=None, company=None, title=None, mobile_phone=None, phone=None, mail=None, address=None, other1=None, other2=None, other3=None):
        r"""BusinessCardTextConfig

        The model defined in huaweicloud sdk

        :param name: 姓名。
        :type name: str
        :param company: 企业或组织名称。
        :type company: str
        :param title: 职位名称。
        :type title: str
        :param mobile_phone: 手机号码。
        :type mobile_phone: str
        :param phone: 固话号码。
        :type phone: str
        :param mail: 电子邮件地址。
        :type mail: str
        :param address: 地址。
        :type address: str
        :param other1: 其他信息1。可填写一些公司广告语等
        :type other1: str
        :param other2: 其他信息2。可填写一些公司广告语等
        :type other2: str
        :param other3: 其他信息3。可填写一些公司广告语等
        :type other3: str
        """
        
        

        self._name = None
        self._company = None
        self._title = None
        self._mobile_phone = None
        self._phone = None
        self._mail = None
        self._address = None
        self._other1 = None
        self._other2 = None
        self._other3 = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if company is not None:
            self.company = company
        if title is not None:
            self.title = title
        if mobile_phone is not None:
            self.mobile_phone = mobile_phone
        if phone is not None:
            self.phone = phone
        if mail is not None:
            self.mail = mail
        if address is not None:
            self.address = address
        if other1 is not None:
            self.other1 = other1
        if other2 is not None:
            self.other2 = other2
        if other3 is not None:
            self.other3 = other3

    @property
    def name(self):
        r"""Gets the name of this BusinessCardTextConfig.

        姓名。

        :return: The name of this BusinessCardTextConfig.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BusinessCardTextConfig.

        姓名。

        :param name: The name of this BusinessCardTextConfig.
        :type name: str
        """
        self._name = name

    @property
    def company(self):
        r"""Gets the company of this BusinessCardTextConfig.

        企业或组织名称。

        :return: The company of this BusinessCardTextConfig.
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        r"""Sets the company of this BusinessCardTextConfig.

        企业或组织名称。

        :param company: The company of this BusinessCardTextConfig.
        :type company: str
        """
        self._company = company

    @property
    def title(self):
        r"""Gets the title of this BusinessCardTextConfig.

        职位名称。

        :return: The title of this BusinessCardTextConfig.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this BusinessCardTextConfig.

        职位名称。

        :param title: The title of this BusinessCardTextConfig.
        :type title: str
        """
        self._title = title

    @property
    def mobile_phone(self):
        r"""Gets the mobile_phone of this BusinessCardTextConfig.

        手机号码。

        :return: The mobile_phone of this BusinessCardTextConfig.
        :rtype: str
        """
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        r"""Sets the mobile_phone of this BusinessCardTextConfig.

        手机号码。

        :param mobile_phone: The mobile_phone of this BusinessCardTextConfig.
        :type mobile_phone: str
        """
        self._mobile_phone = mobile_phone

    @property
    def phone(self):
        r"""Gets the phone of this BusinessCardTextConfig.

        固话号码。

        :return: The phone of this BusinessCardTextConfig.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        r"""Sets the phone of this BusinessCardTextConfig.

        固话号码。

        :param phone: The phone of this BusinessCardTextConfig.
        :type phone: str
        """
        self._phone = phone

    @property
    def mail(self):
        r"""Gets the mail of this BusinessCardTextConfig.

        电子邮件地址。

        :return: The mail of this BusinessCardTextConfig.
        :rtype: str
        """
        return self._mail

    @mail.setter
    def mail(self, mail):
        r"""Sets the mail of this BusinessCardTextConfig.

        电子邮件地址。

        :param mail: The mail of this BusinessCardTextConfig.
        :type mail: str
        """
        self._mail = mail

    @property
    def address(self):
        r"""Gets the address of this BusinessCardTextConfig.

        地址。

        :return: The address of this BusinessCardTextConfig.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this BusinessCardTextConfig.

        地址。

        :param address: The address of this BusinessCardTextConfig.
        :type address: str
        """
        self._address = address

    @property
    def other1(self):
        r"""Gets the other1 of this BusinessCardTextConfig.

        其他信息1。可填写一些公司广告语等

        :return: The other1 of this BusinessCardTextConfig.
        :rtype: str
        """
        return self._other1

    @other1.setter
    def other1(self, other1):
        r"""Sets the other1 of this BusinessCardTextConfig.

        其他信息1。可填写一些公司广告语等

        :param other1: The other1 of this BusinessCardTextConfig.
        :type other1: str
        """
        self._other1 = other1

    @property
    def other2(self):
        r"""Gets the other2 of this BusinessCardTextConfig.

        其他信息2。可填写一些公司广告语等

        :return: The other2 of this BusinessCardTextConfig.
        :rtype: str
        """
        return self._other2

    @other2.setter
    def other2(self, other2):
        r"""Sets the other2 of this BusinessCardTextConfig.

        其他信息2。可填写一些公司广告语等

        :param other2: The other2 of this BusinessCardTextConfig.
        :type other2: str
        """
        self._other2 = other2

    @property
    def other3(self):
        r"""Gets the other3 of this BusinessCardTextConfig.

        其他信息3。可填写一些公司广告语等

        :return: The other3 of this BusinessCardTextConfig.
        :rtype: str
        """
        return self._other3

    @other3.setter
    def other3(self, other3):
        r"""Sets the other3 of this BusinessCardTextConfig.

        其他信息3。可填写一些公司广告语等

        :param other3: The other3 of this BusinessCardTextConfig.
        :type other3: str
        """
        self._other3 = other3

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
        if not isinstance(other, BusinessCardTextConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
