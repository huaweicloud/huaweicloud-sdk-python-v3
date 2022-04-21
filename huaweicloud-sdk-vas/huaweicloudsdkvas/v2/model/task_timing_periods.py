# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskTimingPeriods:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'begin_at': 'str',
        'end_at': 'str'
    }

    attribute_map = {
        'begin_at': 'begin_at',
        'end_at': 'end_at'
    }

    def __init__(self, begin_at=None, end_at=None):
        """TaskTimingPeriods

        The model defined in huaweicloud sdk

        :param begin_at: 单个时间段执行的起始时间，和end_at需成对出现。计划任务类型为once时，格式为yyyy-MM-ddThh:mm:ss，其余计划任务类型时，格式为hh:mm:ss。
        :type begin_at: str
        :param end_at: 单个时间段执行的结束时间，和begin_at需成对出现。计划任务类型为once时，格式为yyyy-MM-ddThh:mm:ss，其余计划任务类型时，格式为hh:mm:ss。
        :type end_at: str
        """
        
        

        self._begin_at = None
        self._end_at = None
        self.discriminator = None

        if begin_at is not None:
            self.begin_at = begin_at
        if end_at is not None:
            self.end_at = end_at

    @property
    def begin_at(self):
        """Gets the begin_at of this TaskTimingPeriods.

        单个时间段执行的起始时间，和end_at需成对出现。计划任务类型为once时，格式为yyyy-MM-ddThh:mm:ss，其余计划任务类型时，格式为hh:mm:ss。

        :return: The begin_at of this TaskTimingPeriods.
        :rtype: str
        """
        return self._begin_at

    @begin_at.setter
    def begin_at(self, begin_at):
        """Sets the begin_at of this TaskTimingPeriods.

        单个时间段执行的起始时间，和end_at需成对出现。计划任务类型为once时，格式为yyyy-MM-ddThh:mm:ss，其余计划任务类型时，格式为hh:mm:ss。

        :param begin_at: The begin_at of this TaskTimingPeriods.
        :type begin_at: str
        """
        self._begin_at = begin_at

    @property
    def end_at(self):
        """Gets the end_at of this TaskTimingPeriods.

        单个时间段执行的结束时间，和begin_at需成对出现。计划任务类型为once时，格式为yyyy-MM-ddThh:mm:ss，其余计划任务类型时，格式为hh:mm:ss。

        :return: The end_at of this TaskTimingPeriods.
        :rtype: str
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        """Sets the end_at of this TaskTimingPeriods.

        单个时间段执行的结束时间，和begin_at需成对出现。计划任务类型为once时，格式为yyyy-MM-ddThh:mm:ss，其余计划任务类型时，格式为hh:mm:ss。

        :param end_at: The end_at of this TaskTimingPeriods.
        :type end_at: str
        """
        self._end_at = end_at

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
        if not isinstance(other, TaskTimingPeriods):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
