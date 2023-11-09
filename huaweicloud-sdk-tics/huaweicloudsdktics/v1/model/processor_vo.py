# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProcessorVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'end_time': 'int',
        'exec_duration_nano': 'int',
        'id': 'str',
        'last_step_task_ins_id': 'list[str]',
        'start_time': 'int',
        'task_in_record_cnt': 'int',
        'task_name': 'str',
        'task_out_record_cnt': 'int',
        'task_show_info': 'object',
        'task_status': 'str'
    }

    attribute_map = {
        'end_time': 'end_time',
        'exec_duration_nano': 'exec_duration_nano',
        'id': 'id',
        'last_step_task_ins_id': 'last_step_task_ins_id',
        'start_time': 'start_time',
        'task_in_record_cnt': 'task_in_record_cnt',
        'task_name': 'task_name',
        'task_out_record_cnt': 'task_out_record_cnt',
        'task_show_info': 'task_show_info',
        'task_status': 'task_status'
    }

    def __init__(self, end_time=None, exec_duration_nano=None, id=None, last_step_task_ins_id=None, start_time=None, task_in_record_cnt=None, task_name=None, task_out_record_cnt=None, task_show_info=None, task_status=None):
        """ProcessorVo

        The model defined in huaweicloud sdk

        :param end_time: 结束时间
        :type end_time: int
        :param exec_duration_nano: 执行时长
        :type exec_duration_nano: int
        :param id: 执行过程id
        :type id: str
        :param last_step_task_ins_id: 上游子任务id
        :type last_step_task_ins_id: list[str]
        :param start_time: 开始时间
        :type start_time: int
        :param task_in_record_cnt: 输入个数
        :type task_in_record_cnt: int
        :param task_name: 执行过程名称
        :type task_name: str
        :param task_out_record_cnt: 输出个数
        :type task_out_record_cnt: int
        :param task_show_info: processor对外展示信息，k,v
        :type task_show_info: object
        :param task_status: 执行状态，作业任务状态，NEW.新建,SUBMITING.提交中,ACCEPTED.已接收,DEPLOYING.部署中,RUNNING.运行中,SUCCEEDED.成功,FAILED.失败,TERMINATED.中止,TERMINATING.中止中,PENDING.等待中
        :type task_status: str
        """
        
        

        self._end_time = None
        self._exec_duration_nano = None
        self._id = None
        self._last_step_task_ins_id = None
        self._start_time = None
        self._task_in_record_cnt = None
        self._task_name = None
        self._task_out_record_cnt = None
        self._task_show_info = None
        self._task_status = None
        self.discriminator = None

        if end_time is not None:
            self.end_time = end_time
        if exec_duration_nano is not None:
            self.exec_duration_nano = exec_duration_nano
        self.id = id
        if last_step_task_ins_id is not None:
            self.last_step_task_ins_id = last_step_task_ins_id
        if start_time is not None:
            self.start_time = start_time
        if task_in_record_cnt is not None:
            self.task_in_record_cnt = task_in_record_cnt
        self.task_name = task_name
        if task_out_record_cnt is not None:
            self.task_out_record_cnt = task_out_record_cnt
        if task_show_info is not None:
            self.task_show_info = task_show_info
        if task_status is not None:
            self.task_status = task_status

    @property
    def end_time(self):
        """Gets the end_time of this ProcessorVo.

        结束时间

        :return: The end_time of this ProcessorVo.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ProcessorVo.

        结束时间

        :param end_time: The end_time of this ProcessorVo.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def exec_duration_nano(self):
        """Gets the exec_duration_nano of this ProcessorVo.

        执行时长

        :return: The exec_duration_nano of this ProcessorVo.
        :rtype: int
        """
        return self._exec_duration_nano

    @exec_duration_nano.setter
    def exec_duration_nano(self, exec_duration_nano):
        """Sets the exec_duration_nano of this ProcessorVo.

        执行时长

        :param exec_duration_nano: The exec_duration_nano of this ProcessorVo.
        :type exec_duration_nano: int
        """
        self._exec_duration_nano = exec_duration_nano

    @property
    def id(self):
        """Gets the id of this ProcessorVo.

        执行过程id

        :return: The id of this ProcessorVo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProcessorVo.

        执行过程id

        :param id: The id of this ProcessorVo.
        :type id: str
        """
        self._id = id

    @property
    def last_step_task_ins_id(self):
        """Gets the last_step_task_ins_id of this ProcessorVo.

        上游子任务id

        :return: The last_step_task_ins_id of this ProcessorVo.
        :rtype: list[str]
        """
        return self._last_step_task_ins_id

    @last_step_task_ins_id.setter
    def last_step_task_ins_id(self, last_step_task_ins_id):
        """Sets the last_step_task_ins_id of this ProcessorVo.

        上游子任务id

        :param last_step_task_ins_id: The last_step_task_ins_id of this ProcessorVo.
        :type last_step_task_ins_id: list[str]
        """
        self._last_step_task_ins_id = last_step_task_ins_id

    @property
    def start_time(self):
        """Gets the start_time of this ProcessorVo.

        开始时间

        :return: The start_time of this ProcessorVo.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ProcessorVo.

        开始时间

        :param start_time: The start_time of this ProcessorVo.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def task_in_record_cnt(self):
        """Gets the task_in_record_cnt of this ProcessorVo.

        输入个数

        :return: The task_in_record_cnt of this ProcessorVo.
        :rtype: int
        """
        return self._task_in_record_cnt

    @task_in_record_cnt.setter
    def task_in_record_cnt(self, task_in_record_cnt):
        """Sets the task_in_record_cnt of this ProcessorVo.

        输入个数

        :param task_in_record_cnt: The task_in_record_cnt of this ProcessorVo.
        :type task_in_record_cnt: int
        """
        self._task_in_record_cnt = task_in_record_cnt

    @property
    def task_name(self):
        """Gets the task_name of this ProcessorVo.

        执行过程名称

        :return: The task_name of this ProcessorVo.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this ProcessorVo.

        执行过程名称

        :param task_name: The task_name of this ProcessorVo.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def task_out_record_cnt(self):
        """Gets the task_out_record_cnt of this ProcessorVo.

        输出个数

        :return: The task_out_record_cnt of this ProcessorVo.
        :rtype: int
        """
        return self._task_out_record_cnt

    @task_out_record_cnt.setter
    def task_out_record_cnt(self, task_out_record_cnt):
        """Sets the task_out_record_cnt of this ProcessorVo.

        输出个数

        :param task_out_record_cnt: The task_out_record_cnt of this ProcessorVo.
        :type task_out_record_cnt: int
        """
        self._task_out_record_cnt = task_out_record_cnt

    @property
    def task_show_info(self):
        """Gets the task_show_info of this ProcessorVo.

        processor对外展示信息，k,v

        :return: The task_show_info of this ProcessorVo.
        :rtype: object
        """
        return self._task_show_info

    @task_show_info.setter
    def task_show_info(self, task_show_info):
        """Sets the task_show_info of this ProcessorVo.

        processor对外展示信息，k,v

        :param task_show_info: The task_show_info of this ProcessorVo.
        :type task_show_info: object
        """
        self._task_show_info = task_show_info

    @property
    def task_status(self):
        """Gets the task_status of this ProcessorVo.

        执行状态，作业任务状态，NEW.新建,SUBMITING.提交中,ACCEPTED.已接收,DEPLOYING.部署中,RUNNING.运行中,SUCCEEDED.成功,FAILED.失败,TERMINATED.中止,TERMINATING.中止中,PENDING.等待中

        :return: The task_status of this ProcessorVo.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """Sets the task_status of this ProcessorVo.

        执行状态，作业任务状态，NEW.新建,SUBMITING.提交中,ACCEPTED.已接收,DEPLOYING.部署中,RUNNING.运行中,SUCCEEDED.成功,FAILED.失败,TERMINATED.中止,TERMINATING.中止中,PENDING.等待中

        :param task_status: The task_status of this ProcessorVo.
        :type task_status: str
        """
        self._task_status = task_status

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
        if not isinstance(other, ProcessorVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
