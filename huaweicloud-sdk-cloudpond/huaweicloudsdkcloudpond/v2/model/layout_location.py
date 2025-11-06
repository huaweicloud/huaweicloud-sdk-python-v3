# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LayoutLocation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rack_id': 'str',
        'start_index': 'int',
        'unit': 'int'
    }

    attribute_map = {
        'rack_id': 'rack_id',
        'start_index': 'start_index',
        'unit': 'unit'
    }

    def __init__(self, rack_id=None, start_index=None, unit=None):
        r"""LayoutLocation

        The model defined in huaweicloud sdk

        :param rack_id: 机柜ID
        :type rack_id: str
        :param start_index: 起始U位
        :type start_index: int
        :param unit: U位数
        :type unit: int
        """
        
        

        self._rack_id = None
        self._start_index = None
        self._unit = None
        self.discriminator = None

        if rack_id is not None:
            self.rack_id = rack_id
        if start_index is not None:
            self.start_index = start_index
        if unit is not None:
            self.unit = unit

    @property
    def rack_id(self):
        r"""Gets the rack_id of this LayoutLocation.

        机柜ID

        :return: The rack_id of this LayoutLocation.
        :rtype: str
        """
        return self._rack_id

    @rack_id.setter
    def rack_id(self, rack_id):
        r"""Sets the rack_id of this LayoutLocation.

        机柜ID

        :param rack_id: The rack_id of this LayoutLocation.
        :type rack_id: str
        """
        self._rack_id = rack_id

    @property
    def start_index(self):
        r"""Gets the start_index of this LayoutLocation.

        起始U位

        :return: The start_index of this LayoutLocation.
        :rtype: int
        """
        return self._start_index

    @start_index.setter
    def start_index(self, start_index):
        r"""Sets the start_index of this LayoutLocation.

        起始U位

        :param start_index: The start_index of this LayoutLocation.
        :type start_index: int
        """
        self._start_index = start_index

    @property
    def unit(self):
        r"""Gets the unit of this LayoutLocation.

        U位数

        :return: The unit of this LayoutLocation.
        :rtype: int
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this LayoutLocation.

        U位数

        :param unit: The unit of this LayoutLocation.
        :type unit: int
        """
        self._unit = unit

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
        if not isinstance(other, LayoutLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
