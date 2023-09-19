# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddressDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('country')
    sensitive_list.append('formatted')
    sensitive_list.append('locality')
    sensitive_list.append('postal_code')
    sensitive_list.append('region')
    sensitive_list.append('street_address')
    sensitive_list.append('type')

    openapi_types = {
        'country': 'str',
        'formatted': 'str',
        'locality': 'str',
        'postal_code': 'str',
        'primary': 'bool',
        'region': 'str',
        'street_address': 'str',
        'type': 'str'
    }

    attribute_map = {
        'country': 'country',
        'formatted': 'formatted',
        'locality': 'locality',
        'postal_code': 'postal_code',
        'primary': 'primary',
        'region': 'region',
        'street_address': 'street_address',
        'type': 'type'
    }

    def __init__(self, country=None, formatted=None, locality=None, postal_code=None, primary=None, region=None, street_address=None, type=None):
        """AddressDto

        The model defined in huaweicloud sdk

        :param country: 国家/地区
        :type country: str
        :param formatted: 包含要显示的地址的格式化版本的字符串
        :type formatted: str
        :param locality: 地址位置
        :type locality: str
        :param postal_code: 邮政编码
        :type postal_code: str
        :param primary: 一个布尔值，表示这是否是用户的主地址
        :type primary: bool
        :param region: 区域
        :type region: str
        :param street_address: 街道
        :type street_address: str
        :param type: 表示地址类型的字符串
        :type type: str
        """
        
        

        self._country = None
        self._formatted = None
        self._locality = None
        self._postal_code = None
        self._primary = None
        self._region = None
        self._street_address = None
        self._type = None
        self.discriminator = None

        if country is not None:
            self.country = country
        if formatted is not None:
            self.formatted = formatted
        if locality is not None:
            self.locality = locality
        if postal_code is not None:
            self.postal_code = postal_code
        if primary is not None:
            self.primary = primary
        if region is not None:
            self.region = region
        if street_address is not None:
            self.street_address = street_address
        if type is not None:
            self.type = type

    @property
    def country(self):
        """Gets the country of this AddressDto.

        国家/地区

        :return: The country of this AddressDto.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this AddressDto.

        国家/地区

        :param country: The country of this AddressDto.
        :type country: str
        """
        self._country = country

    @property
    def formatted(self):
        """Gets the formatted of this AddressDto.

        包含要显示的地址的格式化版本的字符串

        :return: The formatted of this AddressDto.
        :rtype: str
        """
        return self._formatted

    @formatted.setter
    def formatted(self, formatted):
        """Sets the formatted of this AddressDto.

        包含要显示的地址的格式化版本的字符串

        :param formatted: The formatted of this AddressDto.
        :type formatted: str
        """
        self._formatted = formatted

    @property
    def locality(self):
        """Gets the locality of this AddressDto.

        地址位置

        :return: The locality of this AddressDto.
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """Sets the locality of this AddressDto.

        地址位置

        :param locality: The locality of this AddressDto.
        :type locality: str
        """
        self._locality = locality

    @property
    def postal_code(self):
        """Gets the postal_code of this AddressDto.

        邮政编码

        :return: The postal_code of this AddressDto.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this AddressDto.

        邮政编码

        :param postal_code: The postal_code of this AddressDto.
        :type postal_code: str
        """
        self._postal_code = postal_code

    @property
    def primary(self):
        """Gets the primary of this AddressDto.

        一个布尔值，表示这是否是用户的主地址

        :return: The primary of this AddressDto.
        :rtype: bool
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        """Sets the primary of this AddressDto.

        一个布尔值，表示这是否是用户的主地址

        :param primary: The primary of this AddressDto.
        :type primary: bool
        """
        self._primary = primary

    @property
    def region(self):
        """Gets the region of this AddressDto.

        区域

        :return: The region of this AddressDto.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this AddressDto.

        区域

        :param region: The region of this AddressDto.
        :type region: str
        """
        self._region = region

    @property
    def street_address(self):
        """Gets the street_address of this AddressDto.

        街道

        :return: The street_address of this AddressDto.
        :rtype: str
        """
        return self._street_address

    @street_address.setter
    def street_address(self, street_address):
        """Sets the street_address of this AddressDto.

        街道

        :param street_address: The street_address of this AddressDto.
        :type street_address: str
        """
        self._street_address = street_address

    @property
    def type(self):
        """Gets the type of this AddressDto.

        表示地址类型的字符串

        :return: The type of this AddressDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AddressDto.

        表示地址类型的字符串

        :param type: The type of this AddressDto.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, AddressDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
