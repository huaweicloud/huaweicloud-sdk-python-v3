# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Geo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'latitude': 'float',
        'longitude': 'float',
        'city_code': 'str',
        'country_code': 'str'
    }

    attribute_map = {
        'latitude': 'latitude',
        'longitude': 'longitude',
        'city_code': 'city_code',
        'country_code': 'country_code'
    }

    def __init__(self, latitude=None, longitude=None, city_code=None, country_code=None):
        """Geo

        The model defined in huaweicloud sdk

        :param latitude: 纬度。
        :type latitude: float
        :param longitude: 经度。
        :type longitude: float
        :param city_code: 城市编码。
        :type city_code: str
        :param country_code: 国家简码ISO 3166-1 alpha-2，例如：CN、US、DE、IT、SG。
        :type country_code: str
        """
        
        

        self._latitude = None
        self._longitude = None
        self._city_code = None
        self._country_code = None
        self.discriminator = None

        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude
        if city_code is not None:
            self.city_code = city_code
        if country_code is not None:
            self.country_code = country_code

    @property
    def latitude(self):
        """Gets the latitude of this Geo.

        纬度。

        :return: The latitude of this Geo.
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this Geo.

        纬度。

        :param latitude: The latitude of this Geo.
        :type latitude: float
        """
        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this Geo.

        经度。

        :return: The longitude of this Geo.
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this Geo.

        经度。

        :param longitude: The longitude of this Geo.
        :type longitude: float
        """
        self._longitude = longitude

    @property
    def city_code(self):
        """Gets the city_code of this Geo.

        城市编码。

        :return: The city_code of this Geo.
        :rtype: str
        """
        return self._city_code

    @city_code.setter
    def city_code(self, city_code):
        """Sets the city_code of this Geo.

        城市编码。

        :param city_code: The city_code of this Geo.
        :type city_code: str
        """
        self._city_code = city_code

    @property
    def country_code(self):
        """Gets the country_code of this Geo.

        国家简码ISO 3166-1 alpha-2，例如：CN、US、DE、IT、SG。

        :return: The country_code of this Geo.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this Geo.

        国家简码ISO 3166-1 alpha-2，例如：CN、US、DE、IT、SG。

        :param country_code: The country_code of this Geo.
        :type country_code: str
        """
        self._country_code = country_code

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
        if not isinstance(other, Geo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
