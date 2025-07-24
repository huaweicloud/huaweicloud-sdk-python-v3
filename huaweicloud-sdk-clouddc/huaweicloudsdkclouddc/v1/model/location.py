# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Location:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dc': 'str',
        'rack': 'str',
        'unit': 'str'
    }

    attribute_map = {
        'dc': 'dc',
        'rack': 'rack',
        'unit': 'unit'
    }

    def __init__(self, dc=None, rack=None, unit=None):
        r"""Location

        The model defined in huaweicloud sdk

        :param dc: 服务器所在的机房名称
        :type dc: str
        :param rack: 服务器所在的iRack名称
        :type rack: str
        :param unit: 服务器所在的U位
        :type unit: str
        """
        
        

        self._dc = None
        self._rack = None
        self._unit = None
        self.discriminator = None

        if dc is not None:
            self.dc = dc
        if rack is not None:
            self.rack = rack
        if unit is not None:
            self.unit = unit

    @property
    def dc(self):
        r"""Gets the dc of this Location.

        服务器所在的机房名称

        :return: The dc of this Location.
        :rtype: str
        """
        return self._dc

    @dc.setter
    def dc(self, dc):
        r"""Sets the dc of this Location.

        服务器所在的机房名称

        :param dc: The dc of this Location.
        :type dc: str
        """
        self._dc = dc

    @property
    def rack(self):
        r"""Gets the rack of this Location.

        服务器所在的iRack名称

        :return: The rack of this Location.
        :rtype: str
        """
        return self._rack

    @rack.setter
    def rack(self, rack):
        r"""Sets the rack of this Location.

        服务器所在的iRack名称

        :param rack: The rack of this Location.
        :type rack: str
        """
        self._rack = rack

    @property
    def unit(self):
        r"""Gets the unit of this Location.

        服务器所在的U位

        :return: The unit of this Location.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this Location.

        服务器所在的U位

        :param unit: The unit of this Location.
        :type unit: str
        """
        self._unit = unit

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
        if not isinstance(other, Location):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
