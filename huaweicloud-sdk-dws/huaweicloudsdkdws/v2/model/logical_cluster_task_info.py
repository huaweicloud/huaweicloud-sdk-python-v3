# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogicalClusterTaskInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'logical_cluster_name': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'result': 'str',
        'log': 'str'
    }

    attribute_map = {
        'type': 'type',
        'logical_cluster_name': 'logical_cluster_name',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'result': 'result',
        'log': 'log'
    }

    def __init__(self, type=None, logical_cluster_name=None, start_time=None, end_time=None, result=None, log=None):
        """LogicalClusterTaskInfo

        The model defined in huaweicloud sdk

        :param type: 任务类型
        :type type: str
        :param logical_cluster_name: 逻辑集群名称
        :type logical_cluster_name: str
        :param start_time: 任务开始时间
        :type start_time: str
        :param end_time: 任务结束时间
        :type end_time: str
        :param result: 任务执行结果
        :type result: str
        :param log: 任务执行日志
        :type log: str
        """
        
        

        self._type = None
        self._logical_cluster_name = None
        self._start_time = None
        self._end_time = None
        self._result = None
        self._log = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if logical_cluster_name is not None:
            self.logical_cluster_name = logical_cluster_name
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if result is not None:
            self.result = result
        if log is not None:
            self.log = log

    @property
    def type(self):
        """Gets the type of this LogicalClusterTaskInfo.

        任务类型

        :return: The type of this LogicalClusterTaskInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LogicalClusterTaskInfo.

        任务类型

        :param type: The type of this LogicalClusterTaskInfo.
        :type type: str
        """
        self._type = type

    @property
    def logical_cluster_name(self):
        """Gets the logical_cluster_name of this LogicalClusterTaskInfo.

        逻辑集群名称

        :return: The logical_cluster_name of this LogicalClusterTaskInfo.
        :rtype: str
        """
        return self._logical_cluster_name

    @logical_cluster_name.setter
    def logical_cluster_name(self, logical_cluster_name):
        """Sets the logical_cluster_name of this LogicalClusterTaskInfo.

        逻辑集群名称

        :param logical_cluster_name: The logical_cluster_name of this LogicalClusterTaskInfo.
        :type logical_cluster_name: str
        """
        self._logical_cluster_name = logical_cluster_name

    @property
    def start_time(self):
        """Gets the start_time of this LogicalClusterTaskInfo.

        任务开始时间

        :return: The start_time of this LogicalClusterTaskInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this LogicalClusterTaskInfo.

        任务开始时间

        :param start_time: The start_time of this LogicalClusterTaskInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this LogicalClusterTaskInfo.

        任务结束时间

        :return: The end_time of this LogicalClusterTaskInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this LogicalClusterTaskInfo.

        任务结束时间

        :param end_time: The end_time of this LogicalClusterTaskInfo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def result(self):
        """Gets the result of this LogicalClusterTaskInfo.

        任务执行结果

        :return: The result of this LogicalClusterTaskInfo.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this LogicalClusterTaskInfo.

        任务执行结果

        :param result: The result of this LogicalClusterTaskInfo.
        :type result: str
        """
        self._result = result

    @property
    def log(self):
        """Gets the log of this LogicalClusterTaskInfo.

        任务执行日志

        :return: The log of this LogicalClusterTaskInfo.
        :rtype: str
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this LogicalClusterTaskInfo.

        任务执行日志

        :param log: The log of this LogicalClusterTaskInfo.
        :type log: str
        """
        self._log = log

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
        if not isinstance(other, LogicalClusterTaskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
