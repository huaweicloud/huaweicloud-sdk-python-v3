# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CongestionLanesInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'laneid': 'int',
        'level': 'int',
        'length': 'int',
        'start_point': 'Position3D',
        'end_point': 'Position3D'
    }

    attribute_map = {
        'laneid': 'laneid',
        'level': 'level',
        'length': 'length',
        'start_point': 'start_point',
        'end_point': 'end_point'
    }

    def __init__(self, laneid=None, level=None, length=None, start_point=None, end_point=None):
        """CongestionLanesInfo

        The model defined in huaweicloud sdk

        :param laneid: **参数说明**：车道号。
        :type laneid: int
        :param level: **参数说明**：拥堵级别。  **取值范围**：  - 1：拥堵级别低，速度[25, 30) 单位：km/h  - 2：拥堵级别中，速度[15，25) 单位：km/h  - 3：拥堵级别高，速度[0, 15) 单位：km/h
        :type level: int
        :param length: **参数说明**：拥堵长度，单位为米（m）。
        :type length: int
        :param start_point: 
        :type start_point: :class:`huaweicloudsdkdris.v1.Position3D`
        :param end_point: 
        :type end_point: :class:`huaweicloudsdkdris.v1.Position3D`
        """
        
        

        self._laneid = None
        self._level = None
        self._length = None
        self._start_point = None
        self._end_point = None
        self.discriminator = None

        if laneid is not None:
            self.laneid = laneid
        if level is not None:
            self.level = level
        if length is not None:
            self.length = length
        if start_point is not None:
            self.start_point = start_point
        if end_point is not None:
            self.end_point = end_point

    @property
    def laneid(self):
        """Gets the laneid of this CongestionLanesInfo.

        **参数说明**：车道号。

        :return: The laneid of this CongestionLanesInfo.
        :rtype: int
        """
        return self._laneid

    @laneid.setter
    def laneid(self, laneid):
        """Sets the laneid of this CongestionLanesInfo.

        **参数说明**：车道号。

        :param laneid: The laneid of this CongestionLanesInfo.
        :type laneid: int
        """
        self._laneid = laneid

    @property
    def level(self):
        """Gets the level of this CongestionLanesInfo.

        **参数说明**：拥堵级别。  **取值范围**：  - 1：拥堵级别低，速度[25, 30) 单位：km/h  - 2：拥堵级别中，速度[15，25) 单位：km/h  - 3：拥堵级别高，速度[0, 15) 单位：km/h

        :return: The level of this CongestionLanesInfo.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this CongestionLanesInfo.

        **参数说明**：拥堵级别。  **取值范围**：  - 1：拥堵级别低，速度[25, 30) 单位：km/h  - 2：拥堵级别中，速度[15，25) 单位：km/h  - 3：拥堵级别高，速度[0, 15) 单位：km/h

        :param level: The level of this CongestionLanesInfo.
        :type level: int
        """
        self._level = level

    @property
    def length(self):
        """Gets the length of this CongestionLanesInfo.

        **参数说明**：拥堵长度，单位为米（m）。

        :return: The length of this CongestionLanesInfo.
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this CongestionLanesInfo.

        **参数说明**：拥堵长度，单位为米（m）。

        :param length: The length of this CongestionLanesInfo.
        :type length: int
        """
        self._length = length

    @property
    def start_point(self):
        """Gets the start_point of this CongestionLanesInfo.

        :return: The start_point of this CongestionLanesInfo.
        :rtype: :class:`huaweicloudsdkdris.v1.Position3D`
        """
        return self._start_point

    @start_point.setter
    def start_point(self, start_point):
        """Sets the start_point of this CongestionLanesInfo.

        :param start_point: The start_point of this CongestionLanesInfo.
        :type start_point: :class:`huaweicloudsdkdris.v1.Position3D`
        """
        self._start_point = start_point

    @property
    def end_point(self):
        """Gets the end_point of this CongestionLanesInfo.

        :return: The end_point of this CongestionLanesInfo.
        :rtype: :class:`huaweicloudsdkdris.v1.Position3D`
        """
        return self._end_point

    @end_point.setter
    def end_point(self, end_point):
        """Sets the end_point of this CongestionLanesInfo.

        :param end_point: The end_point of this CongestionLanesInfo.
        :type end_point: :class:`huaweicloudsdkdris.v1.Position3D`
        """
        self._end_point = end_point

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
        if not isinstance(other, CongestionLanesInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
