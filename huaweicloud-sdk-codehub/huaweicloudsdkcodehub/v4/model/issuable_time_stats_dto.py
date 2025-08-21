# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IssuableTimeStatsDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time_estimate': 'int',
        'total_time_spent': 'int',
        'human_time_estimate': 'str',
        'human_total_time_spent': 'str'
    }

    attribute_map = {
        'time_estimate': 'time_estimate',
        'total_time_spent': 'total_time_spent',
        'human_time_estimate': 'human_time_estimate',
        'human_total_time_spent': 'human_total_time_spent'
    }

    def __init__(self, time_estimate=None, total_time_spent=None, human_time_estimate=None, human_total_time_spent=None):
        r"""IssuableTimeStatsDto

        The model defined in huaweicloud sdk

        :param time_estimate: 合并请求时间估计
        :type time_estimate: int
        :param total_time_spent: 合并请求总时长
        :type total_time_spent: int
        :param human_time_estimate: 合并请求人类时间估计
        :type human_time_estimate: str
        :param human_total_time_spent: 合并请求人类总时长
        :type human_total_time_spent: str
        """
        
        

        self._time_estimate = None
        self._total_time_spent = None
        self._human_time_estimate = None
        self._human_total_time_spent = None
        self.discriminator = None

        if time_estimate is not None:
            self.time_estimate = time_estimate
        if total_time_spent is not None:
            self.total_time_spent = total_time_spent
        if human_time_estimate is not None:
            self.human_time_estimate = human_time_estimate
        if human_total_time_spent is not None:
            self.human_total_time_spent = human_total_time_spent

    @property
    def time_estimate(self):
        r"""Gets the time_estimate of this IssuableTimeStatsDto.

        合并请求时间估计

        :return: The time_estimate of this IssuableTimeStatsDto.
        :rtype: int
        """
        return self._time_estimate

    @time_estimate.setter
    def time_estimate(self, time_estimate):
        r"""Sets the time_estimate of this IssuableTimeStatsDto.

        合并请求时间估计

        :param time_estimate: The time_estimate of this IssuableTimeStatsDto.
        :type time_estimate: int
        """
        self._time_estimate = time_estimate

    @property
    def total_time_spent(self):
        r"""Gets the total_time_spent of this IssuableTimeStatsDto.

        合并请求总时长

        :return: The total_time_spent of this IssuableTimeStatsDto.
        :rtype: int
        """
        return self._total_time_spent

    @total_time_spent.setter
    def total_time_spent(self, total_time_spent):
        r"""Sets the total_time_spent of this IssuableTimeStatsDto.

        合并请求总时长

        :param total_time_spent: The total_time_spent of this IssuableTimeStatsDto.
        :type total_time_spent: int
        """
        self._total_time_spent = total_time_spent

    @property
    def human_time_estimate(self):
        r"""Gets the human_time_estimate of this IssuableTimeStatsDto.

        合并请求人类时间估计

        :return: The human_time_estimate of this IssuableTimeStatsDto.
        :rtype: str
        """
        return self._human_time_estimate

    @human_time_estimate.setter
    def human_time_estimate(self, human_time_estimate):
        r"""Sets the human_time_estimate of this IssuableTimeStatsDto.

        合并请求人类时间估计

        :param human_time_estimate: The human_time_estimate of this IssuableTimeStatsDto.
        :type human_time_estimate: str
        """
        self._human_time_estimate = human_time_estimate

    @property
    def human_total_time_spent(self):
        r"""Gets the human_total_time_spent of this IssuableTimeStatsDto.

        合并请求人类总时长

        :return: The human_total_time_spent of this IssuableTimeStatsDto.
        :rtype: str
        """
        return self._human_total_time_spent

    @human_total_time_spent.setter
    def human_total_time_spent(self, human_total_time_spent):
        r"""Sets the human_total_time_spent of this IssuableTimeStatsDto.

        合并请求人类总时长

        :param human_total_time_spent: The human_total_time_spent of this IssuableTimeStatsDto.
        :type human_total_time_spent: str
        """
        self._human_total_time_spent = human_total_time_spent

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
        if not isinstance(other, IssuableTimeStatsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
