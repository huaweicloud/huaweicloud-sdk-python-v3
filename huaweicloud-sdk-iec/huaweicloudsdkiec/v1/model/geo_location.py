# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GeoLocation:

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
        'area': 'str',
        'city': 'str',
        'country': 'str',
        'i18n_area': 'str',
        'i18n_city': 'str',
        'i18n_country': 'str',
        'i18n_province': 'str',
        'province': 'str'
    }

    attribute_map = {
        'id': 'id',
        'area': 'area',
        'city': 'city',
        'country': 'country',
        'i18n_area': 'i18n_area',
        'i18n_city': 'i18n_city',
        'i18n_country': 'i18n_country',
        'i18n_province': 'i18n_province',
        'province': 'province'
    }

    def __init__(self, id=None, area=None, city=None, country=None, i18n_area=None, i18n_city=None, i18n_country=None, i18n_province=None, province=None):
        r"""GeoLocation

        The model defined in huaweicloud sdk

        :param id: 地理位置信息ID。
        :type id: str
        :param area: 所在大区。
        :type area: str
        :param city: 所在城市。
        :type city: str
        :param country: 所在的国家。
        :type country: str
        :param i18n_area: 区域的国际化名称。
        :type i18n_area: str
        :param i18n_city: 城市的国际化名称。
        :type i18n_city: str
        :param i18n_country: 国家的国际化名称。
        :type i18n_country: str
        :param i18n_province: 省份的国际化名称。
        :type i18n_province: str
        :param province: 所在省份。
        :type province: str
        """
        
        

        self._id = None
        self._area = None
        self._city = None
        self._country = None
        self._i18n_area = None
        self._i18n_city = None
        self._i18n_country = None
        self._i18n_province = None
        self._province = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if area is not None:
            self.area = area
        if city is not None:
            self.city = city
        if country is not None:
            self.country = country
        if i18n_area is not None:
            self.i18n_area = i18n_area
        if i18n_city is not None:
            self.i18n_city = i18n_city
        if i18n_country is not None:
            self.i18n_country = i18n_country
        if i18n_province is not None:
            self.i18n_province = i18n_province
        if province is not None:
            self.province = province

    @property
    def id(self):
        r"""Gets the id of this GeoLocation.

        地理位置信息ID。

        :return: The id of this GeoLocation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GeoLocation.

        地理位置信息ID。

        :param id: The id of this GeoLocation.
        :type id: str
        """
        self._id = id

    @property
    def area(self):
        r"""Gets the area of this GeoLocation.

        所在大区。

        :return: The area of this GeoLocation.
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area):
        r"""Sets the area of this GeoLocation.

        所在大区。

        :param area: The area of this GeoLocation.
        :type area: str
        """
        self._area = area

    @property
    def city(self):
        r"""Gets the city of this GeoLocation.

        所在城市。

        :return: The city of this GeoLocation.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        r"""Sets the city of this GeoLocation.

        所在城市。

        :param city: The city of this GeoLocation.
        :type city: str
        """
        self._city = city

    @property
    def country(self):
        r"""Gets the country of this GeoLocation.

        所在的国家。

        :return: The country of this GeoLocation.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        r"""Sets the country of this GeoLocation.

        所在的国家。

        :param country: The country of this GeoLocation.
        :type country: str
        """
        self._country = country

    @property
    def i18n_area(self):
        r"""Gets the i18n_area of this GeoLocation.

        区域的国际化名称。

        :return: The i18n_area of this GeoLocation.
        :rtype: str
        """
        return self._i18n_area

    @i18n_area.setter
    def i18n_area(self, i18n_area):
        r"""Sets the i18n_area of this GeoLocation.

        区域的国际化名称。

        :param i18n_area: The i18n_area of this GeoLocation.
        :type i18n_area: str
        """
        self._i18n_area = i18n_area

    @property
    def i18n_city(self):
        r"""Gets the i18n_city of this GeoLocation.

        城市的国际化名称。

        :return: The i18n_city of this GeoLocation.
        :rtype: str
        """
        return self._i18n_city

    @i18n_city.setter
    def i18n_city(self, i18n_city):
        r"""Sets the i18n_city of this GeoLocation.

        城市的国际化名称。

        :param i18n_city: The i18n_city of this GeoLocation.
        :type i18n_city: str
        """
        self._i18n_city = i18n_city

    @property
    def i18n_country(self):
        r"""Gets the i18n_country of this GeoLocation.

        国家的国际化名称。

        :return: The i18n_country of this GeoLocation.
        :rtype: str
        """
        return self._i18n_country

    @i18n_country.setter
    def i18n_country(self, i18n_country):
        r"""Sets the i18n_country of this GeoLocation.

        国家的国际化名称。

        :param i18n_country: The i18n_country of this GeoLocation.
        :type i18n_country: str
        """
        self._i18n_country = i18n_country

    @property
    def i18n_province(self):
        r"""Gets the i18n_province of this GeoLocation.

        省份的国际化名称。

        :return: The i18n_province of this GeoLocation.
        :rtype: str
        """
        return self._i18n_province

    @i18n_province.setter
    def i18n_province(self, i18n_province):
        r"""Sets the i18n_province of this GeoLocation.

        省份的国际化名称。

        :param i18n_province: The i18n_province of this GeoLocation.
        :type i18n_province: str
        """
        self._i18n_province = i18n_province

    @property
    def province(self):
        r"""Gets the province of this GeoLocation.

        所在省份。

        :return: The province of this GeoLocation.
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        r"""Sets the province of this GeoLocation.

        所在省份。

        :param province: The province of this GeoLocation.
        :type province: str
        """
        self._province = province

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
        if not isinstance(other, GeoLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
