# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TimeResourceUsageInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time': 'str',
        'resources_usage': 'list[ResourceUsageInfo]'
    }

    attribute_map = {
        'time': 'time',
        'resources_usage': 'resources_usage'
    }

    def __init__(self, time=None, resources_usage=None):
        r"""TimeResourceUsageInfo

        The model defined in huaweicloud sdk

        :param time: 查询时间段开始时间,格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;
        :type time: str
        :param resources_usage: 资源用量列表
        :type resources_usage: list[:class:`huaweicloudsdkmetastudio.v1.ResourceUsageInfo`]
        """
        
        

        self._time = None
        self._resources_usage = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if resources_usage is not None:
            self.resources_usage = resources_usage

    @property
    def time(self):
        r"""Gets the time of this TimeResourceUsageInfo.

        查询时间段开始时间,格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"

        :return: The time of this TimeResourceUsageInfo.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this TimeResourceUsageInfo.

        查询时间段开始时间,格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"

        :param time: The time of this TimeResourceUsageInfo.
        :type time: str
        """
        self._time = time

    @property
    def resources_usage(self):
        r"""Gets the resources_usage of this TimeResourceUsageInfo.

        资源用量列表

        :return: The resources_usage of this TimeResourceUsageInfo.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.ResourceUsageInfo`]
        """
        return self._resources_usage

    @resources_usage.setter
    def resources_usage(self, resources_usage):
        r"""Sets the resources_usage of this TimeResourceUsageInfo.

        资源用量列表

        :param resources_usage: The resources_usage of this TimeResourceUsageInfo.
        :type resources_usage: list[:class:`huaweicloudsdkmetastudio.v1.ResourceUsageInfo`]
        """
        self._resources_usage = resources_usage

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
        if not isinstance(other, TimeResourceUsageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
