# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPulsarMonitorStatsBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_timestamp': 'int',
        'end_timestamp': 'int'
    }

    attribute_map = {
        'start_timestamp': 'start_timestamp',
        'end_timestamp': 'end_timestamp'
    }

    def __init__(self, start_timestamp=None, end_timestamp=None):
        r"""ShowPulsarMonitorStatsBody

        The model defined in huaweicloud sdk

        :param start_timestamp: 毫秒时间戳
        :type start_timestamp: int
        :param end_timestamp: 毫秒时间戳
        :type end_timestamp: int
        """
        
        

        self._start_timestamp = None
        self._end_timestamp = None
        self.discriminator = None

        if start_timestamp is not None:
            self.start_timestamp = start_timestamp
        if end_timestamp is not None:
            self.end_timestamp = end_timestamp

    @property
    def start_timestamp(self):
        r"""Gets the start_timestamp of this ShowPulsarMonitorStatsBody.

        毫秒时间戳

        :return: The start_timestamp of this ShowPulsarMonitorStatsBody.
        :rtype: int
        """
        return self._start_timestamp

    @start_timestamp.setter
    def start_timestamp(self, start_timestamp):
        r"""Sets the start_timestamp of this ShowPulsarMonitorStatsBody.

        毫秒时间戳

        :param start_timestamp: The start_timestamp of this ShowPulsarMonitorStatsBody.
        :type start_timestamp: int
        """
        self._start_timestamp = start_timestamp

    @property
    def end_timestamp(self):
        r"""Gets the end_timestamp of this ShowPulsarMonitorStatsBody.

        毫秒时间戳

        :return: The end_timestamp of this ShowPulsarMonitorStatsBody.
        :rtype: int
        """
        return self._end_timestamp

    @end_timestamp.setter
    def end_timestamp(self, end_timestamp):
        r"""Sets the end_timestamp of this ShowPulsarMonitorStatsBody.

        毫秒时间戳

        :param end_timestamp: The end_timestamp of this ShowPulsarMonitorStatsBody.
        :type end_timestamp: int
        """
        self._end_timestamp = end_timestamp

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
        if not isinstance(other, ShowPulsarMonitorStatsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
