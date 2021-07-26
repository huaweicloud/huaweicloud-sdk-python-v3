# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModCorpBasicDTO:


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
        'phone': 'str',
        'country': 'str',
        'fax': 'str',
        'email': 'str',
        'address': 'str',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'phone': 'phone',
        'country': 'country',
        'fax': 'fax',
        'email': 'email',
        'address': 'address',
        'description': 'description'
    }

    def __init__(self, name=None, phone=None, country=None, fax=None, email=None, address=None, description=None):
        """ModCorpBasicDTO - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._phone = None
        self._country = None
        self._fax = None
        self._email = None
        self._address = None
        self._description = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if phone is not None:
            self.phone = phone
        if country is not None:
            self.country = country
        if fax is not None:
            self.fax = fax
        if email is not None:
            self.email = email
        if address is not None:
            self.address = address
        if description is not None:
            self.description = description

    @property
    def name(self):
        """Gets the name of this ModCorpBasicDTO.

        企业名称，格式必须满足^[^#%&'+;<>=\"'？?\\\\……/]*$

        :return: The name of this ModCorpBasicDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModCorpBasicDTO.

        企业名称，格式必须满足^[^#%&'+;<>=\"'？?\\\\……/]*$

        :param name: The name of this ModCorpBasicDTO.
        :type: str
        """
        self._name = name

    @property
    def phone(self):
        """Gets the phone of this ModCorpBasicDTO.

        手机号，必须加上国家码，例如中国大陆手机+86xxxxxxx，当填写手机号时 “country”参数必填,手机格式必须满足(^$|^[+]?[0-9]+$)

        :return: The phone of this ModCorpBasicDTO.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this ModCorpBasicDTO.

        手机号，必须加上国家码，例如中国大陆手机+86xxxxxxx，当填写手机号时 “country”参数必填,手机格式必须满足(^$|^[+]?[0-9]+$)

        :param phone: The phone of this ModCorpBasicDTO.
        :type: str
        """
        self._phone = phone

    @property
    def country(self):
        """Gets the country of this ModCorpBasicDTO.

        若smsNumber为手机号,则需带上手机号所属的国家。 例如国家为中国大陆则country参数取值为chinaPR 国家和国家码的对应关系请参考：https://support.huaweicloud.com/api-meeting/meeting_21_0109.html 

        :return: The country of this ModCorpBasicDTO.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this ModCorpBasicDTO.

        若smsNumber为手机号,则需带上手机号所属的国家。 例如国家为中国大陆则country参数取值为chinaPR 国家和国家码的对应关系请参考：https://support.huaweicloud.com/api-meeting/meeting_21_0109.html 

        :param country: The country of this ModCorpBasicDTO.
        :type: str
        """
        self._country = country

    @property
    def fax(self):
        """Gets the fax of this ModCorpBasicDTO.

        传真号码,格式必须满足(^$|^[+]?[0-9]+$)

        :return: The fax of this ModCorpBasicDTO.
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """Sets the fax of this ModCorpBasicDTO.

        传真号码,格式必须满足(^$|^[+]?[0-9]+$)

        :param fax: The fax of this ModCorpBasicDTO.
        :type: str
        """
        self._fax = fax

    @property
    def email(self):
        """Gets the email of this ModCorpBasicDTO.

        邮箱地址,格式必须满足(^$|^[\\w-+]+(\\.[\\w-+]+)*@[\\w-]+(\\.[\\w-]+)*(\\.[\\w-]{1,})$)

        :return: The email of this ModCorpBasicDTO.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ModCorpBasicDTO.

        邮箱地址,格式必须满足(^$|^[\\w-+]+(\\.[\\w-+]+)*@[\\w-]+(\\.[\\w-]+)*(\\.[\\w-]{1,})$)

        :param email: The email of this ModCorpBasicDTO.
        :type: str
        """
        self._email = email

    @property
    def address(self):
        """Gets the address of this ModCorpBasicDTO.

        地址

        :return: The address of this ModCorpBasicDTO.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ModCorpBasicDTO.

        地址

        :param address: The address of this ModCorpBasicDTO.
        :type: str
        """
        self._address = address

    @property
    def description(self):
        """Gets the description of this ModCorpBasicDTO.

        备注

        :return: The description of this ModCorpBasicDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModCorpBasicDTO.

        备注

        :param description: The description of this ModCorpBasicDTO.
        :type: str
        """
        self._description = description

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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ModCorpBasicDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
