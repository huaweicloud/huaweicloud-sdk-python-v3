# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAiAssistantUsageFrequencyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'count': 'count',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, count=None, start_time=None, end_time=None):
        r"""ShowAiAssistantUsageFrequencyRequest

        The model defined in huaweicloud sdk

        :param count: 返回统计个数，默认为前10个用户的统计。
        :type count: int
        :param start_time: 开始时间：由日期加时间组成，UTC格式，例如“2021-05-11T11:45:42Z”。
        :type start_time: str
        :param end_time: 结束时间：由日期加时间组成，UTC格式，例如“2021-05-11T11:45:42Z”。
        :type end_time: str
        """
        
        

        self._count = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if count is not None:
            self.count = count
        self.start_time = start_time
        self.end_time = end_time

    @property
    def count(self):
        r"""Gets the count of this ShowAiAssistantUsageFrequencyRequest.

        返回统计个数，默认为前10个用户的统计。

        :return: The count of this ShowAiAssistantUsageFrequencyRequest.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ShowAiAssistantUsageFrequencyRequest.

        返回统计个数，默认为前10个用户的统计。

        :param count: The count of this ShowAiAssistantUsageFrequencyRequest.
        :type count: int
        """
        self._count = count

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowAiAssistantUsageFrequencyRequest.

        开始时间：由日期加时间组成，UTC格式，例如“2021-05-11T11:45:42Z”。

        :return: The start_time of this ShowAiAssistantUsageFrequencyRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowAiAssistantUsageFrequencyRequest.

        开始时间：由日期加时间组成，UTC格式，例如“2021-05-11T11:45:42Z”。

        :param start_time: The start_time of this ShowAiAssistantUsageFrequencyRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowAiAssistantUsageFrequencyRequest.

        结束时间：由日期加时间组成，UTC格式，例如“2021-05-11T11:45:42Z”。

        :return: The end_time of this ShowAiAssistantUsageFrequencyRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowAiAssistantUsageFrequencyRequest.

        结束时间：由日期加时间组成，UTC格式，例如“2021-05-11T11:45:42Z”。

        :param end_time: The end_time of this ShowAiAssistantUsageFrequencyRequest.
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
        if not isinstance(other, ShowAiAssistantUsageFrequencyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
