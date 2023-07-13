# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVmsSendTasksRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_name': 'str',
        'task_id': 'str',
        'tpl_id': 'str',
        'tpl_name': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'send_begin_time': 'str',
        'send_end_time': 'str',
        'operator': 'str',
        'task_status': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'task_name': 'task_name',
        'task_id': 'task_id',
        'tpl_id': 'tpl_id',
        'tpl_name': 'tpl_name',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'send_begin_time': 'send_begin_time',
        'send_end_time': 'send_end_time',
        'operator': 'operator',
        'task_status': 'task_status',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, task_name=None, task_id=None, tpl_id=None, tpl_name=None, begin_time=None, end_time=None, send_begin_time=None, send_end_time=None, operator=None, task_status=None, offset=None, limit=None):
        """ListVmsSendTasksRequest

        The model defined in huaweicloud sdk

        :param task_name: 智能信息基础版任务名称。
        :type task_name: str
        :param task_id: 智能信息基础版任务ID。
        :type task_id: str
        :param tpl_id: 智能信息基础版模板ID。
        :type tpl_id: str
        :param tpl_name: 智能信息基础版模板名称。
        :type tpl_name: str
        :param begin_time: 智能信息基础版任务创建开始时间。 样例为：2019-10-12T07:20:50Z。
        :type begin_time: str
        :param end_time: 智能信息基础版任务创建结束时间。 样例为：2019-10-12T07:20:50Z。
        :type end_time: str
        :param send_begin_time: 智能信息基础版任务发送开始时间。 样例为：2019-10-12T07:20:50Z。
        :type send_begin_time: str
        :param send_end_time: 智能信息基础版任务发送结束时间。 样例为：2019-10-12T07:20:50Z。
        :type send_end_time: str
        :param operator: 操作员。
        :type operator: str
        :param task_status: 发送状态类型。 - submit_success：提交成功 - submit_failed：提交失败 - processing：发送中 - sending_failed：发送失败 - re_submit_success：重试提交成功 - sending_complete：发送完成 - re_submit_failed：重试提交成功 - re_processing：重试进行中 - re_sending_complete：重试发送完成 - scheduled：定时任务
        :type task_status: str
        :param offset: 偏移量，表示从此偏移量开始查询，offset大于等于0。
        :type offset: int
        :param limit: 每页显示的条目数量。
        :type limit: int
        """
        
        

        self._task_name = None
        self._task_id = None
        self._tpl_id = None
        self._tpl_name = None
        self._begin_time = None
        self._end_time = None
        self._send_begin_time = None
        self._send_end_time = None
        self._operator = None
        self._task_status = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if task_name is not None:
            self.task_name = task_name
        if task_id is not None:
            self.task_id = task_id
        if tpl_id is not None:
            self.tpl_id = tpl_id
        if tpl_name is not None:
            self.tpl_name = tpl_name
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if send_begin_time is not None:
            self.send_begin_time = send_begin_time
        if send_end_time is not None:
            self.send_end_time = send_end_time
        if operator is not None:
            self.operator = operator
        if task_status is not None:
            self.task_status = task_status
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def task_name(self):
        """Gets the task_name of this ListVmsSendTasksRequest.

        智能信息基础版任务名称。

        :return: The task_name of this ListVmsSendTasksRequest.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this ListVmsSendTasksRequest.

        智能信息基础版任务名称。

        :param task_name: The task_name of this ListVmsSendTasksRequest.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def task_id(self):
        """Gets the task_id of this ListVmsSendTasksRequest.

        智能信息基础版任务ID。

        :return: The task_id of this ListVmsSendTasksRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ListVmsSendTasksRequest.

        智能信息基础版任务ID。

        :param task_id: The task_id of this ListVmsSendTasksRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def tpl_id(self):
        """Gets the tpl_id of this ListVmsSendTasksRequest.

        智能信息基础版模板ID。

        :return: The tpl_id of this ListVmsSendTasksRequest.
        :rtype: str
        """
        return self._tpl_id

    @tpl_id.setter
    def tpl_id(self, tpl_id):
        """Sets the tpl_id of this ListVmsSendTasksRequest.

        智能信息基础版模板ID。

        :param tpl_id: The tpl_id of this ListVmsSendTasksRequest.
        :type tpl_id: str
        """
        self._tpl_id = tpl_id

    @property
    def tpl_name(self):
        """Gets the tpl_name of this ListVmsSendTasksRequest.

        智能信息基础版模板名称。

        :return: The tpl_name of this ListVmsSendTasksRequest.
        :rtype: str
        """
        return self._tpl_name

    @tpl_name.setter
    def tpl_name(self, tpl_name):
        """Sets the tpl_name of this ListVmsSendTasksRequest.

        智能信息基础版模板名称。

        :param tpl_name: The tpl_name of this ListVmsSendTasksRequest.
        :type tpl_name: str
        """
        self._tpl_name = tpl_name

    @property
    def begin_time(self):
        """Gets the begin_time of this ListVmsSendTasksRequest.

        智能信息基础版任务创建开始时间。 样例为：2019-10-12T07:20:50Z。

        :return: The begin_time of this ListVmsSendTasksRequest.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ListVmsSendTasksRequest.

        智能信息基础版任务创建开始时间。 样例为：2019-10-12T07:20:50Z。

        :param begin_time: The begin_time of this ListVmsSendTasksRequest.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this ListVmsSendTasksRequest.

        智能信息基础版任务创建结束时间。 样例为：2019-10-12T07:20:50Z。

        :return: The end_time of this ListVmsSendTasksRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListVmsSendTasksRequest.

        智能信息基础版任务创建结束时间。 样例为：2019-10-12T07:20:50Z。

        :param end_time: The end_time of this ListVmsSendTasksRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def send_begin_time(self):
        """Gets the send_begin_time of this ListVmsSendTasksRequest.

        智能信息基础版任务发送开始时间。 样例为：2019-10-12T07:20:50Z。

        :return: The send_begin_time of this ListVmsSendTasksRequest.
        :rtype: str
        """
        return self._send_begin_time

    @send_begin_time.setter
    def send_begin_time(self, send_begin_time):
        """Sets the send_begin_time of this ListVmsSendTasksRequest.

        智能信息基础版任务发送开始时间。 样例为：2019-10-12T07:20:50Z。

        :param send_begin_time: The send_begin_time of this ListVmsSendTasksRequest.
        :type send_begin_time: str
        """
        self._send_begin_time = send_begin_time

    @property
    def send_end_time(self):
        """Gets the send_end_time of this ListVmsSendTasksRequest.

        智能信息基础版任务发送结束时间。 样例为：2019-10-12T07:20:50Z。

        :return: The send_end_time of this ListVmsSendTasksRequest.
        :rtype: str
        """
        return self._send_end_time

    @send_end_time.setter
    def send_end_time(self, send_end_time):
        """Sets the send_end_time of this ListVmsSendTasksRequest.

        智能信息基础版任务发送结束时间。 样例为：2019-10-12T07:20:50Z。

        :param send_end_time: The send_end_time of this ListVmsSendTasksRequest.
        :type send_end_time: str
        """
        self._send_end_time = send_end_time

    @property
    def operator(self):
        """Gets the operator of this ListVmsSendTasksRequest.

        操作员。

        :return: The operator of this ListVmsSendTasksRequest.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this ListVmsSendTasksRequest.

        操作员。

        :param operator: The operator of this ListVmsSendTasksRequest.
        :type operator: str
        """
        self._operator = operator

    @property
    def task_status(self):
        """Gets the task_status of this ListVmsSendTasksRequest.

        发送状态类型。 - submit_success：提交成功 - submit_failed：提交失败 - processing：发送中 - sending_failed：发送失败 - re_submit_success：重试提交成功 - sending_complete：发送完成 - re_submit_failed：重试提交成功 - re_processing：重试进行中 - re_sending_complete：重试发送完成 - scheduled：定时任务

        :return: The task_status of this ListVmsSendTasksRequest.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """Sets the task_status of this ListVmsSendTasksRequest.

        发送状态类型。 - submit_success：提交成功 - submit_failed：提交失败 - processing：发送中 - sending_failed：发送失败 - re_submit_success：重试提交成功 - sending_complete：发送完成 - re_submit_failed：重试提交成功 - re_processing：重试进行中 - re_sending_complete：重试发送完成 - scheduled：定时任务

        :param task_status: The task_status of this ListVmsSendTasksRequest.
        :type task_status: str
        """
        self._task_status = task_status

    @property
    def offset(self):
        """Gets the offset of this ListVmsSendTasksRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0。

        :return: The offset of this ListVmsSendTasksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListVmsSendTasksRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0。

        :param offset: The offset of this ListVmsSendTasksRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListVmsSendTasksRequest.

        每页显示的条目数量。

        :return: The limit of this ListVmsSendTasksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListVmsSendTasksRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListVmsSendTasksRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListVmsSendTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
