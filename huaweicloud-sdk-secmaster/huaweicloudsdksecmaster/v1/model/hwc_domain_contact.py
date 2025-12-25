# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HwcDomainContact:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'email': 'str',
        'register': 'str',
        'contact_name': 'str',
        'phone_num': 'str',
        'province': 'str',
        'city': 'str',
        'address': 'str',
        'zip_code': 'str'
    }

    attribute_map = {
        'email': 'email',
        'register': 'register',
        'contact_name': 'contact_name',
        'phone_num': 'phone_num',
        'province': 'province',
        'city': 'city',
        'address': 'address',
        'zip_code': 'zip_code'
    }

    def __init__(self, email=None, register=None, contact_name=None, phone_num=None, province=None, city=None, address=None, zip_code=None):
        r"""HwcDomainContact

        The model defined in huaweicloud sdk

        :param email: 邮箱地址
        :type email: str
        :param register: 域名所有者
        :type register: str
        :param contact_name: 联系人
        :type contact_name: str
        :param phone_num: 联系电话
        :type phone_num: str
        :param province: 省份
        :type province: str
        :param city: 城市
        :type city: str
        :param address: 通讯地址
        :type address: str
        :param zip_code: 邮编
        :type zip_code: str
        """
        
        

        self._email = None
        self._register = None
        self._contact_name = None
        self._phone_num = None
        self._province = None
        self._city = None
        self._address = None
        self._zip_code = None
        self.discriminator = None

        self.email = email
        self.register = register
        self.contact_name = contact_name
        self.phone_num = phone_num
        self.province = province
        self.city = city
        self.address = address
        self.zip_code = zip_code

    @property
    def email(self):
        r"""Gets the email of this HwcDomainContact.

        邮箱地址

        :return: The email of this HwcDomainContact.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this HwcDomainContact.

        邮箱地址

        :param email: The email of this HwcDomainContact.
        :type email: str
        """
        self._email = email

    @property
    def register(self):
        r"""Gets the register of this HwcDomainContact.

        域名所有者

        :return: The register of this HwcDomainContact.
        :rtype: str
        """
        return self._register

    @register.setter
    def register(self, register):
        r"""Sets the register of this HwcDomainContact.

        域名所有者

        :param register: The register of this HwcDomainContact.
        :type register: str
        """
        self._register = register

    @property
    def contact_name(self):
        r"""Gets the contact_name of this HwcDomainContact.

        联系人

        :return: The contact_name of this HwcDomainContact.
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        r"""Sets the contact_name of this HwcDomainContact.

        联系人

        :param contact_name: The contact_name of this HwcDomainContact.
        :type contact_name: str
        """
        self._contact_name = contact_name

    @property
    def phone_num(self):
        r"""Gets the phone_num of this HwcDomainContact.

        联系电话

        :return: The phone_num of this HwcDomainContact.
        :rtype: str
        """
        return self._phone_num

    @phone_num.setter
    def phone_num(self, phone_num):
        r"""Sets the phone_num of this HwcDomainContact.

        联系电话

        :param phone_num: The phone_num of this HwcDomainContact.
        :type phone_num: str
        """
        self._phone_num = phone_num

    @property
    def province(self):
        r"""Gets the province of this HwcDomainContact.

        省份

        :return: The province of this HwcDomainContact.
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        r"""Sets the province of this HwcDomainContact.

        省份

        :param province: The province of this HwcDomainContact.
        :type province: str
        """
        self._province = province

    @property
    def city(self):
        r"""Gets the city of this HwcDomainContact.

        城市

        :return: The city of this HwcDomainContact.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        r"""Sets the city of this HwcDomainContact.

        城市

        :param city: The city of this HwcDomainContact.
        :type city: str
        """
        self._city = city

    @property
    def address(self):
        r"""Gets the address of this HwcDomainContact.

        通讯地址

        :return: The address of this HwcDomainContact.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this HwcDomainContact.

        通讯地址

        :param address: The address of this HwcDomainContact.
        :type address: str
        """
        self._address = address

    @property
    def zip_code(self):
        r"""Gets the zip_code of this HwcDomainContact.

        邮编

        :return: The zip_code of this HwcDomainContact.
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        r"""Sets the zip_code of this HwcDomainContact.

        邮编

        :param zip_code: The zip_code of this HwcDomainContact.
        :type zip_code: str
        """
        self._zip_code = zip_code

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HwcDomainContact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
