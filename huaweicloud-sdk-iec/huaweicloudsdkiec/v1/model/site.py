# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Site:

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
        'name': 'str',
        'city': 'str',
        'i18n_city': 'str',
        'province': 'str',
        'i18n_province': 'str',
        'area': 'str',
        'i18n_area': 'str',
        'country': 'str',
        'i18n_country': 'str',
        'status': 'str',
        'pools': 'list[IpPool]',
        'city_short_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'city': 'city',
        'i18n_city': 'i18n_city',
        'province': 'province',
        'i18n_province': 'i18n_province',
        'area': 'area',
        'i18n_area': 'i18n_area',
        'country': 'country',
        'i18n_country': 'i18n_country',
        'status': 'status',
        'pools': 'pools',
        'city_short_name': 'city_short_name'
    }

    def __init__(self, id=None, name=None, city=None, i18n_city=None, province=None, i18n_province=None, area=None, i18n_area=None, country=None, i18n_country=None, status=None, pools=None, city_short_name=None):
        """Site

        The model defined in huaweicloud sdk

        :param id: 边缘站点ID。
        :type id: str
        :param name: 边缘站点名称。
        :type name: str
        :param city: 站点所在城市。
        :type city: str
        :param i18n_city: 城市的国际化名称。
        :type i18n_city: str
        :param province: 站点所在省份。
        :type province: str
        :param i18n_province: 省份的国际化名称。
        :type i18n_province: str
        :param area: 所在大区。
        :type area: str
        :param i18n_area: 大区的国际化名称。
        :type i18n_area: str
        :param country: 站点所在的国家。
        :type country: str
        :param i18n_country: 国家的国际化名称。
        :type i18n_country: str
        :param status: 站点当前的状态。  取值范围： - Normal(正常商用) - Obt(公测) - Gray(灰度) - Offline(下线) - Promotion(推荐，也是商用) - sellout(售罄)
        :type status: str
        :param pools: 站点IP线路列表。
        :type pools: list[:class:`huaweicloudsdkiec.v1.IpPool`]
        :param city_short_name: 城市名称缩写。
        :type city_short_name: str
        """
        
        

        self._id = None
        self._name = None
        self._city = None
        self._i18n_city = None
        self._province = None
        self._i18n_province = None
        self._area = None
        self._i18n_area = None
        self._country = None
        self._i18n_country = None
        self._status = None
        self._pools = None
        self._city_short_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if city is not None:
            self.city = city
        if i18n_city is not None:
            self.i18n_city = i18n_city
        if province is not None:
            self.province = province
        if i18n_province is not None:
            self.i18n_province = i18n_province
        if area is not None:
            self.area = area
        if i18n_area is not None:
            self.i18n_area = i18n_area
        if country is not None:
            self.country = country
        if i18n_country is not None:
            self.i18n_country = i18n_country
        if status is not None:
            self.status = status
        if pools is not None:
            self.pools = pools
        if city_short_name is not None:
            self.city_short_name = city_short_name

    @property
    def id(self):
        """Gets the id of this Site.

        边缘站点ID。

        :return: The id of this Site.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Site.

        边缘站点ID。

        :param id: The id of this Site.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Site.

        边缘站点名称。

        :return: The name of this Site.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Site.

        边缘站点名称。

        :param name: The name of this Site.
        :type name: str
        """
        self._name = name

    @property
    def city(self):
        """Gets the city of this Site.

        站点所在城市。

        :return: The city of this Site.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Site.

        站点所在城市。

        :param city: The city of this Site.
        :type city: str
        """
        self._city = city

    @property
    def i18n_city(self):
        """Gets the i18n_city of this Site.

        城市的国际化名称。

        :return: The i18n_city of this Site.
        :rtype: str
        """
        return self._i18n_city

    @i18n_city.setter
    def i18n_city(self, i18n_city):
        """Sets the i18n_city of this Site.

        城市的国际化名称。

        :param i18n_city: The i18n_city of this Site.
        :type i18n_city: str
        """
        self._i18n_city = i18n_city

    @property
    def province(self):
        """Gets the province of this Site.

        站点所在省份。

        :return: The province of this Site.
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        """Sets the province of this Site.

        站点所在省份。

        :param province: The province of this Site.
        :type province: str
        """
        self._province = province

    @property
    def i18n_province(self):
        """Gets the i18n_province of this Site.

        省份的国际化名称。

        :return: The i18n_province of this Site.
        :rtype: str
        """
        return self._i18n_province

    @i18n_province.setter
    def i18n_province(self, i18n_province):
        """Sets the i18n_province of this Site.

        省份的国际化名称。

        :param i18n_province: The i18n_province of this Site.
        :type i18n_province: str
        """
        self._i18n_province = i18n_province

    @property
    def area(self):
        """Gets the area of this Site.

        所在大区。

        :return: The area of this Site.
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this Site.

        所在大区。

        :param area: The area of this Site.
        :type area: str
        """
        self._area = area

    @property
    def i18n_area(self):
        """Gets the i18n_area of this Site.

        大区的国际化名称。

        :return: The i18n_area of this Site.
        :rtype: str
        """
        return self._i18n_area

    @i18n_area.setter
    def i18n_area(self, i18n_area):
        """Sets the i18n_area of this Site.

        大区的国际化名称。

        :param i18n_area: The i18n_area of this Site.
        :type i18n_area: str
        """
        self._i18n_area = i18n_area

    @property
    def country(self):
        """Gets the country of this Site.

        站点所在的国家。

        :return: The country of this Site.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Site.

        站点所在的国家。

        :param country: The country of this Site.
        :type country: str
        """
        self._country = country

    @property
    def i18n_country(self):
        """Gets the i18n_country of this Site.

        国家的国际化名称。

        :return: The i18n_country of this Site.
        :rtype: str
        """
        return self._i18n_country

    @i18n_country.setter
    def i18n_country(self, i18n_country):
        """Sets the i18n_country of this Site.

        国家的国际化名称。

        :param i18n_country: The i18n_country of this Site.
        :type i18n_country: str
        """
        self._i18n_country = i18n_country

    @property
    def status(self):
        """Gets the status of this Site.

        站点当前的状态。  取值范围： - Normal(正常商用) - Obt(公测) - Gray(灰度) - Offline(下线) - Promotion(推荐，也是商用) - sellout(售罄)

        :return: The status of this Site.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Site.

        站点当前的状态。  取值范围： - Normal(正常商用) - Obt(公测) - Gray(灰度) - Offline(下线) - Promotion(推荐，也是商用) - sellout(售罄)

        :param status: The status of this Site.
        :type status: str
        """
        self._status = status

    @property
    def pools(self):
        """Gets the pools of this Site.

        站点IP线路列表。

        :return: The pools of this Site.
        :rtype: list[:class:`huaweicloudsdkiec.v1.IpPool`]
        """
        return self._pools

    @pools.setter
    def pools(self, pools):
        """Sets the pools of this Site.

        站点IP线路列表。

        :param pools: The pools of this Site.
        :type pools: list[:class:`huaweicloudsdkiec.v1.IpPool`]
        """
        self._pools = pools

    @property
    def city_short_name(self):
        """Gets the city_short_name of this Site.

        城市名称缩写。

        :return: The city_short_name of this Site.
        :rtype: str
        """
        return self._city_short_name

    @city_short_name.setter
    def city_short_name(self, city_short_name):
        """Sets the city_short_name of this Site.

        城市名称缩写。

        :param city_short_name: The city_short_name of this Site.
        :type city_short_name: str
        """
        self._city_short_name = city_short_name

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
        if not isinstance(other, Site):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
