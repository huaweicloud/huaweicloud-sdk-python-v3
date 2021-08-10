# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateGeoipRuleRequestBody:


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
        'white': 'int'
    }

    attribute_map = {
        'geoip': 'geoip',
        'white': 'white'
    }

    def __init__(self, geoip=None, white=None):
        """UpdateGeoipRuleRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._geoip = None
        self._white = None
        self.discriminator = None

        self.geoip = geoip
        if white is not None:
            self.white = white

    @property
    def geoip(self):
        """Gets the geoip of this UpdateGeoipRuleRequestBody.

        地理位置

        :return: The geoip of this UpdateGeoipRuleRequestBody.
        :rtype: str
        """
        return self._geoip

    @geoip.setter
    def geoip(self, geoip):
        """Sets the geoip of this UpdateGeoipRuleRequestBody.

        地理位置

        :param geoip: The geoip of this UpdateGeoipRuleRequestBody.
        :type: str
        """
        self._geoip = geoip

    @property
    def white(self):
        """Gets the white of this UpdateGeoipRuleRequestBody.

        放行或者拦截(0拦截,1放行)

        :return: The white of this UpdateGeoipRuleRequestBody.
        :rtype: int
        """
        return self._white

    @white.setter
    def white(self, white):
        """Sets the white of this UpdateGeoipRuleRequestBody.

        放行或者拦截(0拦截,1放行)

        :param white: The white of this UpdateGeoipRuleRequestBody.
        :type: int
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
        if not isinstance(other, UpdateGeoipRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
