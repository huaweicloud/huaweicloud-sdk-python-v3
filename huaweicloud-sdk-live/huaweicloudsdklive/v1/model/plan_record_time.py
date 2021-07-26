# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PlanRecordTime:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'start_time': 'date',
        'end_time': 'date'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, start_time=None, end_time=None):
        """PlanRecordTime - a model defined in huaweicloud sdk"""
        
        

        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def start_time(self):
        """Gets the start_time of this PlanRecordTime.

        录制开始时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间。

        :return: The start_time of this PlanRecordTime.
        :rtype: date
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this PlanRecordTime.

        录制开始时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间。

        :param start_time: The start_time of this PlanRecordTime.
        :type: date
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this PlanRecordTime.

        录制结束时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间。如果填写，填写的时间必须晚于当前时间。如果不填写，则在计划录制触发后不停止。

        :return: The end_time of this PlanRecordTime.
        :rtype: date
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this PlanRecordTime.

        录制结束时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间。如果填写，填写的时间必须晚于当前时间。如果不填写，则在计划录制触发后不停止。

        :param end_time: The end_time of this PlanRecordTime.
        :type: date
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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PlanRecordTime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
