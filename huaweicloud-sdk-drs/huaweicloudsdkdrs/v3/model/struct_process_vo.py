# coding: utf-8

import pprint
import re

import six





class StructProcessVO:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'status': 'int',
        'src_count': 'int',
        'dst_count': 'int',
        'start_time': 'int',
        'end_time': 'int'
    }

    attribute_map = {
        'type': 'type',
        'status': 'status',
        'src_count': 'src_count',
        'dst_count': 'dst_count',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, type=None, status=None, src_count=None, dst_count=None, start_time=None, end_time=None):
        """StructProcessVO - a model defined in huaweicloud sdk"""
        
        

        self._type = None
        self._status = None
        self._src_count = None
        self._dst_count = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.type = type
        self.status = status
        self.src_count = src_count
        self.dst_count = dst_count
        self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def type(self):
        """Gets the type of this StructProcessVO.

        对象类型

        :return: The type of this StructProcessVO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StructProcessVO.

        对象类型

        :param type: The type of this StructProcessVO.
        :type: str
        """
        self._type = type

    @property
    def status(self):
        """Gets the status of this StructProcessVO.

        状态

        :return: The status of this StructProcessVO.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this StructProcessVO.

        状态

        :param status: The status of this StructProcessVO.
        :type: int
        """
        self._status = status

    @property
    def src_count(self):
        """Gets the src_count of this StructProcessVO.

        源对象数量

        :return: The src_count of this StructProcessVO.
        :rtype: int
        """
        return self._src_count

    @src_count.setter
    def src_count(self, src_count):
        """Sets the src_count of this StructProcessVO.

        源对象数量

        :param src_count: The src_count of this StructProcessVO.
        :type: int
        """
        self._src_count = src_count

    @property
    def dst_count(self):
        """Gets the dst_count of this StructProcessVO.

        目标对象数量

        :return: The dst_count of this StructProcessVO.
        :rtype: int
        """
        return self._dst_count

    @dst_count.setter
    def dst_count(self, dst_count):
        """Sets the dst_count of this StructProcessVO.

        目标对象数量

        :param dst_count: The dst_count of this StructProcessVO.
        :type: int
        """
        self._dst_count = dst_count

    @property
    def start_time(self):
        """Gets the start_time of this StructProcessVO.

        开始时间

        :return: The start_time of this StructProcessVO.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this StructProcessVO.

        开始时间

        :param start_time: The start_time of this StructProcessVO.
        :type: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this StructProcessVO.

        结束时间

        :return: The end_time of this StructProcessVO.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this StructProcessVO.

        结束时间

        :param end_time: The end_time of this StructProcessVO.
        :type: int
        """
        self._end_time = end_time

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
        if not isinstance(other, StructProcessVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other