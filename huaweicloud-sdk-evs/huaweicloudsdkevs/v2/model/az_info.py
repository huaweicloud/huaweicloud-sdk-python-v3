# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AzInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'zone_name': 'str',
        'zone_state': 'ZoneState'
    }

    attribute_map = {
        'zone_name': 'zoneName',
        'zone_state': 'zoneState'
    }

    def __init__(self, zone_name=None, zone_state=None):
        r"""AzInfo

        The model defined in huaweicloud sdk

        :param zone_name: 可用分区的名字。
        :type zone_name: str
        :param zone_state: 
        :type zone_state: :class:`huaweicloudsdkevs.v2.ZoneState`
        """
        
        

        self._zone_name = None
        self._zone_state = None
        self.discriminator = None

        self.zone_name = zone_name
        self.zone_state = zone_state

    @property
    def zone_name(self):
        r"""Gets the zone_name of this AzInfo.

        可用分区的名字。

        :return: The zone_name of this AzInfo.
        :rtype: str
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, zone_name):
        r"""Sets the zone_name of this AzInfo.

        可用分区的名字。

        :param zone_name: The zone_name of this AzInfo.
        :type zone_name: str
        """
        self._zone_name = zone_name

    @property
    def zone_state(self):
        r"""Gets the zone_state of this AzInfo.

        :return: The zone_state of this AzInfo.
        :rtype: :class:`huaweicloudsdkevs.v2.ZoneState`
        """
        return self._zone_state

    @zone_state.setter
    def zone_state(self, zone_state):
        r"""Sets the zone_state of this AzInfo.

        :param zone_state: The zone_state of this AzInfo.
        :type zone_state: :class:`huaweicloudsdkevs.v2.ZoneState`
        """
        self._zone_state = zone_state

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
        if not isinstance(other, AzInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
