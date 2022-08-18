# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TimeCondition:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'time_measure_id': 'int',
        'begin_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'time_measure_id': 'time_measure_id',
        'begin_time': 'begin_time',
        'end_time': 'end_time'
    }

    def __init__(self, time_measure_id=None, begin_time=None, end_time=None):
        """TimeCondition

        The model defined in huaweicloud sdk

        :param time_measure_id: 时间单位，1：天2：月
        :type time_measure_id: int
        :param begin_time: 查询开始时间，必须是日期格式。当time_measure_id值为1或为空时，格式为YYYY-MM-DD当time_measure_id值为2时，格式为YYYY-MM
        :type begin_time: str
        :param end_time: 查询结束时间：必须是日期格式。当time_measure_id值为1或为空时，格式为YYYY-MM-DD当time_measure_id值为2时，格式为YYYY-MM
        :type end_time: str
        """
        
        

        self._time_measure_id = None
        self._begin_time = None
        self._end_time = None
        self.discriminator = None

        self.time_measure_id = time_measure_id
        self.begin_time = begin_time
        self.end_time = end_time

    @property
    def time_measure_id(self):
        """Gets the time_measure_id of this TimeCondition.

        时间单位，1：天2：月

        :return: The time_measure_id of this TimeCondition.
        :rtype: int
        """
        return self._time_measure_id

    @time_measure_id.setter
    def time_measure_id(self, time_measure_id):
        """Sets the time_measure_id of this TimeCondition.

        时间单位，1：天2：月

        :param time_measure_id: The time_measure_id of this TimeCondition.
        :type time_measure_id: int
        """
        self._time_measure_id = time_measure_id

    @property
    def begin_time(self):
        """Gets the begin_time of this TimeCondition.

        查询开始时间，必须是日期格式。当time_measure_id值为1或为空时，格式为YYYY-MM-DD当time_measure_id值为2时，格式为YYYY-MM

        :return: The begin_time of this TimeCondition.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this TimeCondition.

        查询开始时间，必须是日期格式。当time_measure_id值为1或为空时，格式为YYYY-MM-DD当time_measure_id值为2时，格式为YYYY-MM

        :param begin_time: The begin_time of this TimeCondition.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this TimeCondition.

        查询结束时间：必须是日期格式。当time_measure_id值为1或为空时，格式为YYYY-MM-DD当time_measure_id值为2时，格式为YYYY-MM

        :return: The end_time of this TimeCondition.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this TimeCondition.

        查询结束时间：必须是日期格式。当time_measure_id值为1或为空时，格式为YYYY-MM-DD当time_measure_id值为2时，格式为YYYY-MM

        :param end_time: The end_time of this TimeCondition.
        :type end_time: str
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
        if not isinstance(other, TimeCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
