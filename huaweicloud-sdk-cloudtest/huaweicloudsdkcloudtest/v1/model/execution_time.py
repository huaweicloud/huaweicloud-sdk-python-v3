# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecutionTime:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'begin_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'begin_time': 'beginTime',
        'end_time': 'endTime'
    }

    def __init__(self, begin_time=None, end_time=None):
        r"""ExecutionTime

        The model defined in huaweicloud sdk

        :param begin_time: 开始时间 00:00
        :type begin_time: str
        :param end_time: 结束时间 23:59
        :type end_time: str
        """
        
        

        self._begin_time = None
        self._end_time = None
        self.discriminator = None

        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ExecutionTime.

        开始时间 00:00

        :return: The begin_time of this ExecutionTime.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ExecutionTime.

        开始时间 00:00

        :param begin_time: The begin_time of this ExecutionTime.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ExecutionTime.

        结束时间 23:59

        :return: The end_time of this ExecutionTime.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ExecutionTime.

        结束时间 23:59

        :param end_time: The end_time of this ExecutionTime.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, ExecutionTime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
