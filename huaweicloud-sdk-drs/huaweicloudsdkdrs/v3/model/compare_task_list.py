# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompareTaskList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'compare_task_id': 'str',
        'compare_type': 'str',
        'compare_task_status': 'str',
        'create_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'compare_task_id': 'compare_task_id',
        'compare_type': 'compare_type',
        'compare_task_status': 'compare_task_status',
        'create_time': 'create_time',
        'end_time': 'end_time'
    }

    def __init__(self, compare_task_id=None, compare_type=None, compare_task_status=None, create_time=None, end_time=None):
        """CompareTaskList

        The model defined in huaweicloud sdk

        :param compare_task_id: 对比任务的id。
        :type compare_task_id: str
        :param compare_type: 对比任务的类型。
        :type compare_type: str
        :param compare_task_status: 对比任务的状态。 - RUNNING-运行中 - WAITING_FOR_RUNNING-等待启动中 - SUCCESSFUL-完成 - FAILED-失败 - CANCELLED-已取消 - TIMEOUT_INTERRUPT-超时中断 - FULL_DOING-全量校验中 - INCRE_DOING-增量校验中
        :type compare_task_status: str
        :param create_time: 对比开始时间。
        :type create_time: str
        :param end_time: 对比结束时间。
        :type end_time: str
        """
        
        

        self._compare_task_id = None
        self._compare_type = None
        self._compare_task_status = None
        self._create_time = None
        self._end_time = None
        self.discriminator = None

        self.compare_task_id = compare_task_id
        self.compare_type = compare_type
        self.compare_task_status = compare_task_status
        self.create_time = create_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def compare_task_id(self):
        """Gets the compare_task_id of this CompareTaskList.

        对比任务的id。

        :return: The compare_task_id of this CompareTaskList.
        :rtype: str
        """
        return self._compare_task_id

    @compare_task_id.setter
    def compare_task_id(self, compare_task_id):
        """Sets the compare_task_id of this CompareTaskList.

        对比任务的id。

        :param compare_task_id: The compare_task_id of this CompareTaskList.
        :type compare_task_id: str
        """
        self._compare_task_id = compare_task_id

    @property
    def compare_type(self):
        """Gets the compare_type of this CompareTaskList.

        对比任务的类型。

        :return: The compare_type of this CompareTaskList.
        :rtype: str
        """
        return self._compare_type

    @compare_type.setter
    def compare_type(self, compare_type):
        """Sets the compare_type of this CompareTaskList.

        对比任务的类型。

        :param compare_type: The compare_type of this CompareTaskList.
        :type compare_type: str
        """
        self._compare_type = compare_type

    @property
    def compare_task_status(self):
        """Gets the compare_task_status of this CompareTaskList.

        对比任务的状态。 - RUNNING-运行中 - WAITING_FOR_RUNNING-等待启动中 - SUCCESSFUL-完成 - FAILED-失败 - CANCELLED-已取消 - TIMEOUT_INTERRUPT-超时中断 - FULL_DOING-全量校验中 - INCRE_DOING-增量校验中

        :return: The compare_task_status of this CompareTaskList.
        :rtype: str
        """
        return self._compare_task_status

    @compare_task_status.setter
    def compare_task_status(self, compare_task_status):
        """Sets the compare_task_status of this CompareTaskList.

        对比任务的状态。 - RUNNING-运行中 - WAITING_FOR_RUNNING-等待启动中 - SUCCESSFUL-完成 - FAILED-失败 - CANCELLED-已取消 - TIMEOUT_INTERRUPT-超时中断 - FULL_DOING-全量校验中 - INCRE_DOING-增量校验中

        :param compare_task_status: The compare_task_status of this CompareTaskList.
        :type compare_task_status: str
        """
        self._compare_task_status = compare_task_status

    @property
    def create_time(self):
        """Gets the create_time of this CompareTaskList.

        对比开始时间。

        :return: The create_time of this CompareTaskList.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CompareTaskList.

        对比开始时间。

        :param create_time: The create_time of this CompareTaskList.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def end_time(self):
        """Gets the end_time of this CompareTaskList.

        对比结束时间。

        :return: The end_time of this CompareTaskList.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this CompareTaskList.

        对比结束时间。

        :param end_time: The end_time of this CompareTaskList.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, CompareTaskList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
