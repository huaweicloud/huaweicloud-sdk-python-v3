# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OcaIpDataCenter:

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
        r"""OcaIpDataCenter

        The model defined in huaweicloud sdk

        :param latitude: 纬度
        :type latitude: float
        :param longitude: 经度
        :type longitude: float
        :param city_code: 城市编码
        :type city_code: str
        :param country_code: 国家编码
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
        self.city_code = city_code
        self.country_code = country_code

    @property
    def latitude(self):
        r"""Gets the latitude of this OcaIpDataCenter.

        纬度

        :return: The latitude of this OcaIpDataCenter.
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        r"""Sets the latitude of this OcaIpDataCenter.

        纬度

        :param latitude: The latitude of this OcaIpDataCenter.
        :type latitude: float
        """
        self._latitude = latitude

    @property
    def longitude(self):
        r"""Gets the longitude of this OcaIpDataCenter.

        经度

        :return: The longitude of this OcaIpDataCenter.
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        r"""Sets the longitude of this OcaIpDataCenter.

        经度

        :param longitude: The longitude of this OcaIpDataCenter.
        :type longitude: float
        """
        self._longitude = longitude

    @property
    def city_code(self):
        r"""Gets the city_code of this OcaIpDataCenter.

        城市编码

        :return: The city_code of this OcaIpDataCenter.
        :rtype: str
        """
        return self._city_code

    @city_code.setter
    def city_code(self, city_code):
        r"""Sets the city_code of this OcaIpDataCenter.

        城市编码

        :param city_code: The city_code of this OcaIpDataCenter.
        :type city_code: str
        """
        self._city_code = city_code

    @property
    def country_code(self):
        r"""Gets the country_code of this OcaIpDataCenter.

        国家编码

        :return: The country_code of this OcaIpDataCenter.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        r"""Sets the country_code of this OcaIpDataCenter.

        国家编码

        :param country_code: The country_code of this OcaIpDataCenter.
        :type country_code: str
        """
        self._country_code = country_code

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
        if not isinstance(other, OcaIpDataCenter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
