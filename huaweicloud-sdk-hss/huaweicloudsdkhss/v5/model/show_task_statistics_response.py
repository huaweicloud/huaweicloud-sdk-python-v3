# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_num': 'int',
        'running_num': 'int',
        'last_task_start_time': 'int'
    }

    attribute_map = {
        'total_num': 'total_num',
        'running_num': 'running_num',
        'last_task_start_time': 'last_task_start_time'
    }

    def __init__(self, total_num=None, running_num=None, last_task_start_time=None):
        r"""ShowTaskStatisticsResponse

        The model defined in huaweicloud sdk

        :param total_num: 累计执行的任务总数
        :type total_num: int
        :param running_num: 扫描中的任务数
        :type running_num: int
        :param last_task_start_time: 最近一次扫描任务的创建时间
        :type last_task_start_time: int
        """
        
        super(ShowTaskStatisticsResponse, self).__init__()

        self._total_num = None
        self._running_num = None
        self._last_task_start_time = None
        self.discriminator = None

        if total_num is not None:
            self.total_num = total_num
        if running_num is not None:
            self.running_num = running_num
        if last_task_start_time is not None:
            self.last_task_start_time = last_task_start_time

    @property
    def total_num(self):
        r"""Gets the total_num of this ShowTaskStatisticsResponse.

        累计执行的任务总数

        :return: The total_num of this ShowTaskStatisticsResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this ShowTaskStatisticsResponse.

        累计执行的任务总数

        :param total_num: The total_num of this ShowTaskStatisticsResponse.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def running_num(self):
        r"""Gets the running_num of this ShowTaskStatisticsResponse.

        扫描中的任务数

        :return: The running_num of this ShowTaskStatisticsResponse.
        :rtype: int
        """
        return self._running_num

    @running_num.setter
    def running_num(self, running_num):
        r"""Sets the running_num of this ShowTaskStatisticsResponse.

        扫描中的任务数

        :param running_num: The running_num of this ShowTaskStatisticsResponse.
        :type running_num: int
        """
        self._running_num = running_num

    @property
    def last_task_start_time(self):
        r"""Gets the last_task_start_time of this ShowTaskStatisticsResponse.

        最近一次扫描任务的创建时间

        :return: The last_task_start_time of this ShowTaskStatisticsResponse.
        :rtype: int
        """
        return self._last_task_start_time

    @last_task_start_time.setter
    def last_task_start_time(self, last_task_start_time):
        r"""Sets the last_task_start_time of this ShowTaskStatisticsResponse.

        最近一次扫描任务的创建时间

        :param last_task_start_time: The last_task_start_time of this ShowTaskStatisticsResponse.
        :type last_task_start_time: int
        """
        self._last_task_start_time = last_task_start_time

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
        if not isinstance(other, ShowTaskStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
