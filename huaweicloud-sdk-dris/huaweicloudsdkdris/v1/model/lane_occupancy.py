# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LaneOccupancy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'lane_id': 'int',
        'space_occupancy': 'float',
        'time_occupancy': 'float'
    }

    attribute_map = {
        'lane_id': 'lane_id',
        'space_occupancy': 'space_occupancy',
        'time_occupancy': 'time_occupancy'
    }

    def __init__(self, lane_id=None, space_occupancy=None, time_occupancy=None):
        """LaneOccupancy

        The model defined in huaweicloud sdk

        :param lane_id: **参数说明**：车道编号。车道从左到右，从0开始编号
        :type lane_id: int
        :param space_occupancy: **参数说明**：车道的空间占有率。
        :type space_occupancy: float
        :param time_occupancy: **参数说明**：车道的时间占有率。
        :type time_occupancy: float
        """
        
        

        self._lane_id = None
        self._space_occupancy = None
        self._time_occupancy = None
        self.discriminator = None

        if lane_id is not None:
            self.lane_id = lane_id
        if space_occupancy is not None:
            self.space_occupancy = space_occupancy
        if time_occupancy is not None:
            self.time_occupancy = time_occupancy

    @property
    def lane_id(self):
        """Gets the lane_id of this LaneOccupancy.

        **参数说明**：车道编号。车道从左到右，从0开始编号

        :return: The lane_id of this LaneOccupancy.
        :rtype: int
        """
        return self._lane_id

    @lane_id.setter
    def lane_id(self, lane_id):
        """Sets the lane_id of this LaneOccupancy.

        **参数说明**：车道编号。车道从左到右，从0开始编号

        :param lane_id: The lane_id of this LaneOccupancy.
        :type lane_id: int
        """
        self._lane_id = lane_id

    @property
    def space_occupancy(self):
        """Gets the space_occupancy of this LaneOccupancy.

        **参数说明**：车道的空间占有率。

        :return: The space_occupancy of this LaneOccupancy.
        :rtype: float
        """
        return self._space_occupancy

    @space_occupancy.setter
    def space_occupancy(self, space_occupancy):
        """Sets the space_occupancy of this LaneOccupancy.

        **参数说明**：车道的空间占有率。

        :param space_occupancy: The space_occupancy of this LaneOccupancy.
        :type space_occupancy: float
        """
        self._space_occupancy = space_occupancy

    @property
    def time_occupancy(self):
        """Gets the time_occupancy of this LaneOccupancy.

        **参数说明**：车道的时间占有率。

        :return: The time_occupancy of this LaneOccupancy.
        :rtype: float
        """
        return self._time_occupancy

    @time_occupancy.setter
    def time_occupancy(self, time_occupancy):
        """Sets the time_occupancy of this LaneOccupancy.

        **参数说明**：车道的时间占有率。

        :param time_occupancy: The time_occupancy of this LaneOccupancy.
        :type time_occupancy: float
        """
        self._time_occupancy = time_occupancy

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
        if not isinstance(other, LaneOccupancy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
