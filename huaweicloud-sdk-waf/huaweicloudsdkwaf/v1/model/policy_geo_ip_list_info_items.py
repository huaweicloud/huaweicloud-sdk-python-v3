# coding: utf-8

import pprint
import re

import six





class PolicyGeoIpListInfoItems:


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
        'geoip': 'str',
        'white': 'int',
        'timestamp': 'int'
    }

    attribute_map = {
        'id': 'id',
        'geoip': 'geoip',
        'white': 'white',
        'timestamp': 'timestamp'
    }

    def __init__(self, id=None, geoip=None, white=None, timestamp=None):
        """PolicyGeoIpListInfoItems - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._geoip = None
        self._white = None
        self._timestamp = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if geoip is not None:
            self.geoip = geoip
        if white is not None:
            self.white = white
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def id(self):
        """Gets the id of this PolicyGeoIpListInfoItems.

        规则id

        :return: The id of this PolicyGeoIpListInfoItems.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PolicyGeoIpListInfoItems.

        规则id

        :param id: The id of this PolicyGeoIpListInfoItems.
        :type: str
        """
        self._id = id

    @property
    def geoip(self):
        """Gets the geoip of this PolicyGeoIpListInfoItems.

        地理位置封禁区域

        :return: The geoip of this PolicyGeoIpListInfoItems.
        :rtype: str
        """
        return self._geoip

    @geoip.setter
    def geoip(self, geoip):
        """Sets the geoip of this PolicyGeoIpListInfoItems.

        地理位置封禁区域

        :param geoip: The geoip of this PolicyGeoIpListInfoItems.
        :type: str
        """
        self._geoip = geoip

    @property
    def white(self):
        """Gets the white of this PolicyGeoIpListInfoItems.

        放行或者拦截

        :return: The white of this PolicyGeoIpListInfoItems.
        :rtype: int
        """
        return self._white

    @white.setter
    def white(self, white):
        """Sets the white of this PolicyGeoIpListInfoItems.

        放行或者拦截

        :param white: The white of this PolicyGeoIpListInfoItems.
        :type: int
        """
        self._white = white

    @property
    def timestamp(self):
        """Gets the timestamp of this PolicyGeoIpListInfoItems.

        创建规则时间戳

        :return: The timestamp of this PolicyGeoIpListInfoItems.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this PolicyGeoIpListInfoItems.

        创建规则时间戳

        :param timestamp: The timestamp of this PolicyGeoIpListInfoItems.
        :type: int
        """
        self._timestamp = timestamp

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
        if not isinstance(other, PolicyGeoIpListInfoItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other