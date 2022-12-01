# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'streams': 'list[TaskStream]',
        'task_id': 'str',
        'start_time_info': 'StartTimeInfo',
        'source_usage_estimate': 'TaskSourceUsageEstimate'
    }

    attribute_map = {
        'streams': 'streams',
        'task_id': 'task_id',
        'start_time_info': 'start_time_info',
        'source_usage_estimate': 'source_usage_estimate'
    }

    def __init__(self, streams=None, task_id=None, start_time_info=None, source_usage_estimate=None):
        """TaskData

        The model defined in huaweicloud sdk

        :param streams: 作业流详情
        :type streams: list[:class:`huaweicloudsdkhilens.v3.TaskStream`]
        :param task_id: 作业id
        :type task_id: str
        :param start_time_info: 
        :type start_time_info: :class:`huaweicloudsdkhilens.v3.StartTimeInfo`
        :param source_usage_estimate: 
        :type source_usage_estimate: :class:`huaweicloudsdkhilens.v3.TaskSourceUsageEstimate`
        """
        
        

        self._streams = None
        self._task_id = None
        self._start_time_info = None
        self._source_usage_estimate = None
        self.discriminator = None

        self.streams = streams
        if task_id is not None:
            self.task_id = task_id
        if start_time_info is not None:
            self.start_time_info = start_time_info
        if source_usage_estimate is not None:
            self.source_usage_estimate = source_usage_estimate

    @property
    def streams(self):
        """Gets the streams of this TaskData.

        作业流详情

        :return: The streams of this TaskData.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.TaskStream`]
        """
        return self._streams

    @streams.setter
    def streams(self, streams):
        """Sets the streams of this TaskData.

        作业流详情

        :param streams: The streams of this TaskData.
        :type streams: list[:class:`huaweicloudsdkhilens.v3.TaskStream`]
        """
        self._streams = streams

    @property
    def task_id(self):
        """Gets the task_id of this TaskData.

        作业id

        :return: The task_id of this TaskData.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this TaskData.

        作业id

        :param task_id: The task_id of this TaskData.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def start_time_info(self):
        """Gets the start_time_info of this TaskData.

        :return: The start_time_info of this TaskData.
        :rtype: :class:`huaweicloudsdkhilens.v3.StartTimeInfo`
        """
        return self._start_time_info

    @start_time_info.setter
    def start_time_info(self, start_time_info):
        """Sets the start_time_info of this TaskData.

        :param start_time_info: The start_time_info of this TaskData.
        :type start_time_info: :class:`huaweicloudsdkhilens.v3.StartTimeInfo`
        """
        self._start_time_info = start_time_info

    @property
    def source_usage_estimate(self):
        """Gets the source_usage_estimate of this TaskData.

        :return: The source_usage_estimate of this TaskData.
        :rtype: :class:`huaweicloudsdkhilens.v3.TaskSourceUsageEstimate`
        """
        return self._source_usage_estimate

    @source_usage_estimate.setter
    def source_usage_estimate(self, source_usage_estimate):
        """Sets the source_usage_estimate of this TaskData.

        :param source_usage_estimate: The source_usage_estimate of this TaskData.
        :type source_usage_estimate: :class:`huaweicloudsdkhilens.v3.TaskSourceUsageEstimate`
        """
        self._source_usage_estimate = source_usage_estimate

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
        if not isinstance(other, TaskData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
