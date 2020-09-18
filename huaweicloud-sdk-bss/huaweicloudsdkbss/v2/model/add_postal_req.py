# coding: utf-8

import pprint
import re

import six





class AddPostalReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'recipient': 'str',
        'province': 'str',
        'city': 'str',
        'district': 'str',
        'address': 'str',
        'zipcode': 'str',
        'mobile_phone': 'str',
        'is_default': 'int'
    }

    attribute_map = {
        'recipient': 'recipient',
        'province': 'province',
        'city': 'city',
        'district': 'district',
        'address': 'address',
        'zipcode': 'zipcode',
        'mobile_phone': 'mobile_phone',
        'is_default': 'is_default'
    }

    def __init__(self, recipient=None, province=None, city=None, district=None, address=None, zipcode=None, mobile_phone=None, is_default=0):
        """AddPostalReq - a model defined in huaweicloud sdk"""
        
        

        self._recipient = None
        self._province = None
        self._city = None
        self._district = None
        self._address = None
        self._zipcode = None
        self._mobile_phone = None
        self._is_default = None
        self.discriminator = None

        self.recipient = recipient
        self.province = province
        self.city = city
        self.district = district
        self.address = address
        if zipcode is not None:
            self.zipcode = zipcode
        self.mobile_phone = mobile_phone
        if is_default is not None:
            self.is_default = is_default

    @property
    def recipient(self):
        """Gets the recipient of this AddPostalReq.

        |参数名称：收件人姓名| |参数约束及描述：收件人姓名|

        :return: The recipient of this AddPostalReq.
        :rtype: str
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        """Sets the recipient of this AddPostalReq.

        |参数名称：收件人姓名| |参数约束及描述：收件人姓名|

        :param recipient: The recipient of this AddPostalReq.
        :type: str
        """
        self._recipient = recipient

    @property
    def province(self):
        """Gets the province of this AddPostalReq.

        |参数名称：省/自治区/直辖市。例如：江苏，不要写成：江苏省| |参数约束及描述：省/自治区/直辖市。例如：江苏，不要写成：江苏省|

        :return: The province of this AddPostalReq.
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        """Sets the province of this AddPostalReq.

        |参数名称：省/自治区/直辖市。例如：江苏，不要写成：江苏省| |参数约束及描述：省/自治区/直辖市。例如：江苏，不要写成：江苏省|

        :param province: The province of this AddPostalReq.
        :type: str
        """
        self._province = province

    @property
    def city(self):
        """Gets the city of this AddPostalReq.

        |参数名称：市/区。例如：南京。| |参数约束及描述：市/区。例如：南京。|

        :return: The city of this AddPostalReq.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this AddPostalReq.

        |参数名称：市/区。例如：南京。| |参数约束及描述：市/区。例如：南京。|

        :param city: The city of this AddPostalReq.
        :type: str
        """
        self._city = city

    @property
    def district(self):
        """Gets the district of this AddPostalReq.

        |参数名称：区。例如：雨花。| |参数约束及描述：区。例如：雨花。|

        :return: The district of this AddPostalReq.
        :rtype: str
        """
        return self._district

    @district.setter
    def district(self, district):
        """Sets the district of this AddPostalReq.

        |参数名称：区。例如：雨花。| |参数约束及描述：区。例如：雨花。|

        :param district: The district of this AddPostalReq.
        :type: str
        """
        self._district = district

    @property
    def address(self):
        """Gets the address of this AddPostalReq.

        |参数名称：邮寄详细地址。| |参数约束及描述：邮寄详细地址。|

        :return: The address of this AddPostalReq.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this AddPostalReq.

        |参数名称：邮寄详细地址。| |参数约束及描述：邮寄详细地址。|

        :param address: The address of this AddPostalReq.
        :type: str
        """
        self._address = address

    @property
    def zipcode(self):
        """Gets the zipcode of this AddPostalReq.

        |参数名称：邮编| |参数约束及描述：邮编|

        :return: The zipcode of this AddPostalReq.
        :rtype: str
        """
        return self._zipcode

    @zipcode.setter
    def zipcode(self, zipcode):
        """Sets the zipcode of this AddPostalReq.

        |参数名称：邮编| |参数约束及描述：邮编|

        :param zipcode: The zipcode of this AddPostalReq.
        :type: str
        """
        self._zipcode = zipcode

    @property
    def mobile_phone(self):
        """Gets the mobile_phone of this AddPostalReq.

        |参数名称：手机号码，不带国家码| |参数约束及描述：手机号码，不带国家码|

        :return: The mobile_phone of this AddPostalReq.
        :rtype: str
        """
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        """Sets the mobile_phone of this AddPostalReq.

        |参数名称：手机号码，不带国家码| |参数约束及描述：手机号码，不带国家码|

        :param mobile_phone: The mobile_phone of this AddPostalReq.
        :type: str
        """
        self._mobile_phone = mobile_phone

    @property
    def is_default(self):
        """Gets the is_default of this AddPostalReq.

        |参数名称：是否默认地址| |参数约束及描述：是否默认地址，默认为0。1：默认地址0：非默认地址|

        :return: The is_default of this AddPostalReq.
        :rtype: int
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this AddPostalReq.

        |参数名称：是否默认地址| |参数约束及描述：是否默认地址，默认为0。1：默认地址0：非默认地址|

        :param is_default: The is_default of this AddPostalReq.
        :type: int
        """
        self._is_default = is_default

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
        if not isinstance(other, AddPostalReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
