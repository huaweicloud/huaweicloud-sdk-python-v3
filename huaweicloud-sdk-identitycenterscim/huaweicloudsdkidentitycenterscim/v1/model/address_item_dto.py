# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddressItemDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'formatted': 'str',
        'street_address': 'str',
        'locality': 'str',
        'region': 'str',
        'postal_code': 'str',
        'country': 'str',
        'type': 'str',
        'primary': 'bool'
    }

    attribute_map = {
        'formatted': 'formatted',
        'street_address': 'streetAddress',
        'locality': 'locality',
        'region': 'region',
        'postal_code': 'postalCode',
        'country': 'country',
        'type': 'type',
        'primary': 'primary'
    }

    def __init__(self, formatted=None, street_address=None, locality=None, region=None, postal_code=None, country=None, type=None, primary=None):
        r"""AddressItemDto

        The model defined in huaweicloud sdk

        :param formatted: 包含要显示的地址的格式化版本的字符串
        :type formatted: str
        :param street_address: 街道
        :type street_address: str
        :param locality: 地址位置
        :type locality: str
        :param region: 区域
        :type region: str
        :param postal_code: 邮政编码
        :type postal_code: str
        :param country: 国家或地区
        :type country: str
        :param type: 表示地址类型的字符串
        :type type: str
        :param primary: 一个布尔值，表示这是否是用户的主地址
        :type primary: bool
        """
        
        

        self._formatted = None
        self._street_address = None
        self._locality = None
        self._region = None
        self._postal_code = None
        self._country = None
        self._type = None
        self._primary = None
        self.discriminator = None

        if formatted is not None:
            self.formatted = formatted
        if street_address is not None:
            self.street_address = street_address
        if locality is not None:
            self.locality = locality
        if region is not None:
            self.region = region
        if postal_code is not None:
            self.postal_code = postal_code
        if country is not None:
            self.country = country
        if type is not None:
            self.type = type
        if primary is not None:
            self.primary = primary

    @property
    def formatted(self):
        r"""Gets the formatted of this AddressItemDto.

        包含要显示的地址的格式化版本的字符串

        :return: The formatted of this AddressItemDto.
        :rtype: str
        """
        return self._formatted

    @formatted.setter
    def formatted(self, formatted):
        r"""Sets the formatted of this AddressItemDto.

        包含要显示的地址的格式化版本的字符串

        :param formatted: The formatted of this AddressItemDto.
        :type formatted: str
        """
        self._formatted = formatted

    @property
    def street_address(self):
        r"""Gets the street_address of this AddressItemDto.

        街道

        :return: The street_address of this AddressItemDto.
        :rtype: str
        """
        return self._street_address

    @street_address.setter
    def street_address(self, street_address):
        r"""Sets the street_address of this AddressItemDto.

        街道

        :param street_address: The street_address of this AddressItemDto.
        :type street_address: str
        """
        self._street_address = street_address

    @property
    def locality(self):
        r"""Gets the locality of this AddressItemDto.

        地址位置

        :return: The locality of this AddressItemDto.
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        r"""Sets the locality of this AddressItemDto.

        地址位置

        :param locality: The locality of this AddressItemDto.
        :type locality: str
        """
        self._locality = locality

    @property
    def region(self):
        r"""Gets the region of this AddressItemDto.

        区域

        :return: The region of this AddressItemDto.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this AddressItemDto.

        区域

        :param region: The region of this AddressItemDto.
        :type region: str
        """
        self._region = region

    @property
    def postal_code(self):
        r"""Gets the postal_code of this AddressItemDto.

        邮政编码

        :return: The postal_code of this AddressItemDto.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        r"""Sets the postal_code of this AddressItemDto.

        邮政编码

        :param postal_code: The postal_code of this AddressItemDto.
        :type postal_code: str
        """
        self._postal_code = postal_code

    @property
    def country(self):
        r"""Gets the country of this AddressItemDto.

        国家或地区

        :return: The country of this AddressItemDto.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        r"""Sets the country of this AddressItemDto.

        国家或地区

        :param country: The country of this AddressItemDto.
        :type country: str
        """
        self._country = country

    @property
    def type(self):
        r"""Gets the type of this AddressItemDto.

        表示地址类型的字符串

        :return: The type of this AddressItemDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AddressItemDto.

        表示地址类型的字符串

        :param type: The type of this AddressItemDto.
        :type type: str
        """
        self._type = type

    @property
    def primary(self):
        r"""Gets the primary of this AddressItemDto.

        一个布尔值，表示这是否是用户的主地址

        :return: The primary of this AddressItemDto.
        :rtype: bool
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        r"""Sets the primary of this AddressItemDto.

        一个布尔值，表示这是否是用户的主地址

        :param primary: The primary of this AddressItemDto.
        :type primary: bool
        """
        self._primary = primary

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
        if not isinstance(other, AddressItemDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
