# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Segment:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'start_time': 'int',
        'end_time': 'int',
        'result': 'TranscriberResult'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'result': 'result'
    }

    def __init__(self, start_time=None, end_time=None, result=None):
        """Segment

        The model defined in huaweicloud sdk

        :param start_time: 一句的起始时间戳，单位ms。
        :type start_time: int
        :param end_time: 一句的结束时间戳，单位ms。
        :type end_time: int
        :param result: 
        :type result: :class:`huaweicloudsdksis.v1.TranscriberResult`
        """
        
        

        self._start_time = None
        self._end_time = None
        self._result = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        self.result = result

    @property
    def start_time(self):
        """Gets the start_time of this Segment.

        一句的起始时间戳，单位ms。

        :return: The start_time of this Segment.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this Segment.

        一句的起始时间戳，单位ms。

        :param start_time: The start_time of this Segment.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this Segment.

        一句的结束时间戳，单位ms。

        :return: The end_time of this Segment.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this Segment.

        一句的结束时间戳，单位ms。

        :param end_time: The end_time of this Segment.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def result(self):
        """Gets the result of this Segment.


        :return: The result of this Segment.
        :rtype: :class:`huaweicloudsdksis.v1.TranscriberResult`
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this Segment.


        :param result: The result of this Segment.
        :type result: :class:`huaweicloudsdksis.v1.TranscriberResult`
        """
        self._result = result

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
        if not isinstance(other, Segment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
