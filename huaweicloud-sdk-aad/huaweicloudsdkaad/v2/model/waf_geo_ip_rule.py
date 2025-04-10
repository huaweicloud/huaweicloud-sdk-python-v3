# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WafGeoIpRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'geoip': 'str',
        'id': 'str',
        'name': 'str',
        'overseas_type': 'int',
        'timestamp': 'int',
        'white': 'int'
    }

    attribute_map = {
        'geoip': 'geoip',
        'id': 'id',
        'name': 'name',
        'overseas_type': 'overseas_type',
        'timestamp': 'timestamp',
        'white': 'white'
    }

    def __init__(self, geoip=None, id=None, name=None, overseas_type=None, timestamp=None, white=None):
        r"""WafGeoIpRule

        The model defined in huaweicloud sdk

        :param geoip: 地理位置
        :type geoip: str
        :param id: id
        :type id: str
        :param name: 规则名称
        :type name: str
        :param overseas_type: 防护区域，0-大陆，1-海外
        :type overseas_type: int
        :param timestamp: 添加时间
        :type timestamp: int
        :param white: 防护动作 0-阻断，1-放行，2-仅记录
        :type white: int
        """
        
        

        self._geoip = None
        self._id = None
        self._name = None
        self._overseas_type = None
        self._timestamp = None
        self._white = None
        self.discriminator = None

        if geoip is not None:
            self.geoip = geoip
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if overseas_type is not None:
            self.overseas_type = overseas_type
        if timestamp is not None:
            self.timestamp = timestamp
        if white is not None:
            self.white = white

    @property
    def geoip(self):
        r"""Gets the geoip of this WafGeoIpRule.

        地理位置

        :return: The geoip of this WafGeoIpRule.
        :rtype: str
        """
        return self._geoip

    @geoip.setter
    def geoip(self, geoip):
        r"""Sets the geoip of this WafGeoIpRule.

        地理位置

        :param geoip: The geoip of this WafGeoIpRule.
        :type geoip: str
        """
        self._geoip = geoip

    @property
    def id(self):
        r"""Gets the id of this WafGeoIpRule.

        id

        :return: The id of this WafGeoIpRule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this WafGeoIpRule.

        id

        :param id: The id of this WafGeoIpRule.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this WafGeoIpRule.

        规则名称

        :return: The name of this WafGeoIpRule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this WafGeoIpRule.

        规则名称

        :param name: The name of this WafGeoIpRule.
        :type name: str
        """
        self._name = name

    @property
    def overseas_type(self):
        r"""Gets the overseas_type of this WafGeoIpRule.

        防护区域，0-大陆，1-海外

        :return: The overseas_type of this WafGeoIpRule.
        :rtype: int
        """
        return self._overseas_type

    @overseas_type.setter
    def overseas_type(self, overseas_type):
        r"""Sets the overseas_type of this WafGeoIpRule.

        防护区域，0-大陆，1-海外

        :param overseas_type: The overseas_type of this WafGeoIpRule.
        :type overseas_type: int
        """
        self._overseas_type = overseas_type

    @property
    def timestamp(self):
        r"""Gets the timestamp of this WafGeoIpRule.

        添加时间

        :return: The timestamp of this WafGeoIpRule.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this WafGeoIpRule.

        添加时间

        :param timestamp: The timestamp of this WafGeoIpRule.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def white(self):
        r"""Gets the white of this WafGeoIpRule.

        防护动作 0-阻断，1-放行，2-仅记录

        :return: The white of this WafGeoIpRule.
        :rtype: int
        """
        return self._white

    @white.setter
    def white(self, white):
        r"""Sets the white of this WafGeoIpRule.

        防护动作 0-阻断，1-放行，2-仅记录

        :param white: The white of this WafGeoIpRule.
        :type white: int
        """
        self._white = white

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
        if not isinstance(other, WafGeoIpRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
