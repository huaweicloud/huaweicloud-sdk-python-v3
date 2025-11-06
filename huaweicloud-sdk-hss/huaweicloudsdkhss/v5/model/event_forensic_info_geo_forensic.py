# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventForensicInfoGeoForensic:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'src_country': 'str',
        'src_city': 'str',
        'src_latitude': 'int',
        'src_longitude': 'int',
        'dest_country': 'str',
        'dest_city': 'str',
        'dest_latitude': 'int',
        'dest_longitude': 'int'
    }

    attribute_map = {
        'src_country': 'src_country',
        'src_city': 'src_city',
        'src_latitude': 'src_latitude',
        'src_longitude': 'src_longitude',
        'dest_country': 'dest_country',
        'dest_city': 'dest_city',
        'dest_latitude': 'dest_latitude',
        'dest_longitude': 'dest_longitude'
    }

    def __init__(self, src_country=None, src_city=None, src_latitude=None, src_longitude=None, dest_country=None, dest_city=None, dest_latitude=None, dest_longitude=None):
        r"""EventForensicInfoGeoForensic

        The model defined in huaweicloud sdk

        :param src_country: **参数解释**： 源国家 **取值范围**： 不涉及
        :type src_country: str
        :param src_city: **参数解释**： 源城市 **取值范围**： 不涉及
        :type src_city: str
        :param src_latitude: **参数解释**： 源纬度 **取值范围**： 不涉及
        :type src_latitude: int
        :param src_longitude: **参数解释**： 源经度 **取值范围**： 不涉及
        :type src_longitude: int
        :param dest_country: **参数解释**： 目的国家 **取值范围**： 不涉及
        :type dest_country: str
        :param dest_city: **参数解释**： 目的城市 **取值范围**： 不涉及
        :type dest_city: str
        :param dest_latitude: **参数解释**： 目的纬度 **取值范围**： 不涉及
        :type dest_latitude: int
        :param dest_longitude: **参数解释**： 目的经度 **取值范围**： 不涉及
        :type dest_longitude: int
        """
        
        

        self._src_country = None
        self._src_city = None
        self._src_latitude = None
        self._src_longitude = None
        self._dest_country = None
        self._dest_city = None
        self._dest_latitude = None
        self._dest_longitude = None
        self.discriminator = None

        if src_country is not None:
            self.src_country = src_country
        if src_city is not None:
            self.src_city = src_city
        if src_latitude is not None:
            self.src_latitude = src_latitude
        if src_longitude is not None:
            self.src_longitude = src_longitude
        if dest_country is not None:
            self.dest_country = dest_country
        if dest_city is not None:
            self.dest_city = dest_city
        if dest_latitude is not None:
            self.dest_latitude = dest_latitude
        if dest_longitude is not None:
            self.dest_longitude = dest_longitude

    @property
    def src_country(self):
        r"""Gets the src_country of this EventForensicInfoGeoForensic.

        **参数解释**： 源国家 **取值范围**： 不涉及

        :return: The src_country of this EventForensicInfoGeoForensic.
        :rtype: str
        """
        return self._src_country

    @src_country.setter
    def src_country(self, src_country):
        r"""Sets the src_country of this EventForensicInfoGeoForensic.

        **参数解释**： 源国家 **取值范围**： 不涉及

        :param src_country: The src_country of this EventForensicInfoGeoForensic.
        :type src_country: str
        """
        self._src_country = src_country

    @property
    def src_city(self):
        r"""Gets the src_city of this EventForensicInfoGeoForensic.

        **参数解释**： 源城市 **取值范围**： 不涉及

        :return: The src_city of this EventForensicInfoGeoForensic.
        :rtype: str
        """
        return self._src_city

    @src_city.setter
    def src_city(self, src_city):
        r"""Sets the src_city of this EventForensicInfoGeoForensic.

        **参数解释**： 源城市 **取值范围**： 不涉及

        :param src_city: The src_city of this EventForensicInfoGeoForensic.
        :type src_city: str
        """
        self._src_city = src_city

    @property
    def src_latitude(self):
        r"""Gets the src_latitude of this EventForensicInfoGeoForensic.

        **参数解释**： 源纬度 **取值范围**： 不涉及

        :return: The src_latitude of this EventForensicInfoGeoForensic.
        :rtype: int
        """
        return self._src_latitude

    @src_latitude.setter
    def src_latitude(self, src_latitude):
        r"""Sets the src_latitude of this EventForensicInfoGeoForensic.

        **参数解释**： 源纬度 **取值范围**： 不涉及

        :param src_latitude: The src_latitude of this EventForensicInfoGeoForensic.
        :type src_latitude: int
        """
        self._src_latitude = src_latitude

    @property
    def src_longitude(self):
        r"""Gets the src_longitude of this EventForensicInfoGeoForensic.

        **参数解释**： 源经度 **取值范围**： 不涉及

        :return: The src_longitude of this EventForensicInfoGeoForensic.
        :rtype: int
        """
        return self._src_longitude

    @src_longitude.setter
    def src_longitude(self, src_longitude):
        r"""Sets the src_longitude of this EventForensicInfoGeoForensic.

        **参数解释**： 源经度 **取值范围**： 不涉及

        :param src_longitude: The src_longitude of this EventForensicInfoGeoForensic.
        :type src_longitude: int
        """
        self._src_longitude = src_longitude

    @property
    def dest_country(self):
        r"""Gets the dest_country of this EventForensicInfoGeoForensic.

        **参数解释**： 目的国家 **取值范围**： 不涉及

        :return: The dest_country of this EventForensicInfoGeoForensic.
        :rtype: str
        """
        return self._dest_country

    @dest_country.setter
    def dest_country(self, dest_country):
        r"""Sets the dest_country of this EventForensicInfoGeoForensic.

        **参数解释**： 目的国家 **取值范围**： 不涉及

        :param dest_country: The dest_country of this EventForensicInfoGeoForensic.
        :type dest_country: str
        """
        self._dest_country = dest_country

    @property
    def dest_city(self):
        r"""Gets the dest_city of this EventForensicInfoGeoForensic.

        **参数解释**： 目的城市 **取值范围**： 不涉及

        :return: The dest_city of this EventForensicInfoGeoForensic.
        :rtype: str
        """
        return self._dest_city

    @dest_city.setter
    def dest_city(self, dest_city):
        r"""Sets the dest_city of this EventForensicInfoGeoForensic.

        **参数解释**： 目的城市 **取值范围**： 不涉及

        :param dest_city: The dest_city of this EventForensicInfoGeoForensic.
        :type dest_city: str
        """
        self._dest_city = dest_city

    @property
    def dest_latitude(self):
        r"""Gets the dest_latitude of this EventForensicInfoGeoForensic.

        **参数解释**： 目的纬度 **取值范围**： 不涉及

        :return: The dest_latitude of this EventForensicInfoGeoForensic.
        :rtype: int
        """
        return self._dest_latitude

    @dest_latitude.setter
    def dest_latitude(self, dest_latitude):
        r"""Sets the dest_latitude of this EventForensicInfoGeoForensic.

        **参数解释**： 目的纬度 **取值范围**： 不涉及

        :param dest_latitude: The dest_latitude of this EventForensicInfoGeoForensic.
        :type dest_latitude: int
        """
        self._dest_latitude = dest_latitude

    @property
    def dest_longitude(self):
        r"""Gets the dest_longitude of this EventForensicInfoGeoForensic.

        **参数解释**： 目的经度 **取值范围**： 不涉及

        :return: The dest_longitude of this EventForensicInfoGeoForensic.
        :rtype: int
        """
        return self._dest_longitude

    @dest_longitude.setter
    def dest_longitude(self, dest_longitude):
        r"""Sets the dest_longitude of this EventForensicInfoGeoForensic.

        **参数解释**： 目的经度 **取值范围**： 不涉及

        :param dest_longitude: The dest_longitude of this EventForensicInfoGeoForensic.
        :type dest_longitude: int
        """
        self._dest_longitude = dest_longitude

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
        if not isinstance(other, EventForensicInfoGeoForensic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
