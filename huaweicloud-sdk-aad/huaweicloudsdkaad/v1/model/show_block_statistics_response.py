# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBlockStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_unblocking_times': 'int',
        'manual_unblocking_times': 'int',
        'automatic_unblocking_times': 'int',
        'current_blocked_ip_numbers': 'int'
    }

    attribute_map = {
        'total_unblocking_times': 'total_unblocking_times',
        'manual_unblocking_times': 'manual_unblocking_times',
        'automatic_unblocking_times': 'automatic_unblocking_times',
        'current_blocked_ip_numbers': 'current_blocked_ip_numbers'
    }

    def __init__(self, total_unblocking_times=None, manual_unblocking_times=None, automatic_unblocking_times=None, current_blocked_ip_numbers=None):
        """ShowBlockStatisticsResponse

        The model defined in huaweicloud sdk

        :param total_unblocking_times: 总解封次数
        :type total_unblocking_times: int
        :param manual_unblocking_times: 人工解封次数
        :type manual_unblocking_times: int
        :param automatic_unblocking_times: 自动解封次数
        :type automatic_unblocking_times: int
        :param current_blocked_ip_numbers: 当前封堵Ip数
        :type current_blocked_ip_numbers: int
        """
        
        super(ShowBlockStatisticsResponse, self).__init__()

        self._total_unblocking_times = None
        self._manual_unblocking_times = None
        self._automatic_unblocking_times = None
        self._current_blocked_ip_numbers = None
        self.discriminator = None

        if total_unblocking_times is not None:
            self.total_unblocking_times = total_unblocking_times
        if manual_unblocking_times is not None:
            self.manual_unblocking_times = manual_unblocking_times
        if automatic_unblocking_times is not None:
            self.automatic_unblocking_times = automatic_unblocking_times
        if current_blocked_ip_numbers is not None:
            self.current_blocked_ip_numbers = current_blocked_ip_numbers

    @property
    def total_unblocking_times(self):
        """Gets the total_unblocking_times of this ShowBlockStatisticsResponse.

        总解封次数

        :return: The total_unblocking_times of this ShowBlockStatisticsResponse.
        :rtype: int
        """
        return self._total_unblocking_times

    @total_unblocking_times.setter
    def total_unblocking_times(self, total_unblocking_times):
        """Sets the total_unblocking_times of this ShowBlockStatisticsResponse.

        总解封次数

        :param total_unblocking_times: The total_unblocking_times of this ShowBlockStatisticsResponse.
        :type total_unblocking_times: int
        """
        self._total_unblocking_times = total_unblocking_times

    @property
    def manual_unblocking_times(self):
        """Gets the manual_unblocking_times of this ShowBlockStatisticsResponse.

        人工解封次数

        :return: The manual_unblocking_times of this ShowBlockStatisticsResponse.
        :rtype: int
        """
        return self._manual_unblocking_times

    @manual_unblocking_times.setter
    def manual_unblocking_times(self, manual_unblocking_times):
        """Sets the manual_unblocking_times of this ShowBlockStatisticsResponse.

        人工解封次数

        :param manual_unblocking_times: The manual_unblocking_times of this ShowBlockStatisticsResponse.
        :type manual_unblocking_times: int
        """
        self._manual_unblocking_times = manual_unblocking_times

    @property
    def automatic_unblocking_times(self):
        """Gets the automatic_unblocking_times of this ShowBlockStatisticsResponse.

        自动解封次数

        :return: The automatic_unblocking_times of this ShowBlockStatisticsResponse.
        :rtype: int
        """
        return self._automatic_unblocking_times

    @automatic_unblocking_times.setter
    def automatic_unblocking_times(self, automatic_unblocking_times):
        """Sets the automatic_unblocking_times of this ShowBlockStatisticsResponse.

        自动解封次数

        :param automatic_unblocking_times: The automatic_unblocking_times of this ShowBlockStatisticsResponse.
        :type automatic_unblocking_times: int
        """
        self._automatic_unblocking_times = automatic_unblocking_times

    @property
    def current_blocked_ip_numbers(self):
        """Gets the current_blocked_ip_numbers of this ShowBlockStatisticsResponse.

        当前封堵Ip数

        :return: The current_blocked_ip_numbers of this ShowBlockStatisticsResponse.
        :rtype: int
        """
        return self._current_blocked_ip_numbers

    @current_blocked_ip_numbers.setter
    def current_blocked_ip_numbers(self, current_blocked_ip_numbers):
        """Sets the current_blocked_ip_numbers of this ShowBlockStatisticsResponse.

        当前封堵Ip数

        :param current_blocked_ip_numbers: The current_blocked_ip_numbers of this ShowBlockStatisticsResponse.
        :type current_blocked_ip_numbers: int
        """
        self._current_blocked_ip_numbers = current_blocked_ip_numbers

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
        if not isinstance(other, ShowBlockStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
