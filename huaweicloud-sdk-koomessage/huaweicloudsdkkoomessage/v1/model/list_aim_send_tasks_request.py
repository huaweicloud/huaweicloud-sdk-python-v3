# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAimSendTasksRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'task_name': 'str',
        'tpl_id': 'str',
        'tpl_name': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'task_status': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'task_id': 'task_id',
        'task_name': 'task_name',
        'tpl_id': 'tpl_id',
        'tpl_name': 'tpl_name',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'task_status': 'task_status',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, task_id=None, task_name=None, tpl_id=None, tpl_name=None, begin_time=None, end_time=None, task_status=None, offset=None, limit=None):
        r"""ListAimSendTasksRequest

        The model defined in huaweicloud sdk

        :param task_id: 智能信息发送任务ID。
        :type task_id: str
        :param task_name: 智能信息发送任务名称。
        :type task_name: str
        :param tpl_id: 智能信息模板ID。
        :type tpl_id: str
        :param tpl_name: 智能信息模板名称。
        :type tpl_name: str
        :param begin_time: 智能信息发送任务创建开始时间。样例：2019-10-12T07:20:50.522Z。  &gt; 需同时传入end_time才能生效，单独传begin_time不会作为过滤条件。缺省：查询最近7天（168小时）数据。 &gt; &gt; 仅支持查询最近1年内创建的智能信息发送任务。 
        :type begin_time: str
        :param end_time: 智能信息发送任务创建结束时间。样例：2019-10-12T07:20:50.522Z。  &gt; 需同时传入begin_time才能生效，单独传end_time不会作为过滤条件。缺省：查询最近7天（168小时）数据。 
        :type end_time: str
        :param task_status: 智能信息发送任务状态。  - Success：创建成功  - Fail：创建失败 
        :type task_status: str
        :param offset: 偏移量，表示从此偏移量开始查询，offset大于等于0。  &gt;为提高查询效率，offset+limit须小于等于10000，超出范围查询为空。 
        :type offset: int
        :param limit: 每页显示的条目数量。 
        :type limit: int
        """
        
        

        self._task_id = None
        self._task_name = None
        self._tpl_id = None
        self._tpl_name = None
        self._begin_time = None
        self._end_time = None
        self._task_status = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if tpl_id is not None:
            self.tpl_id = tpl_id
        if tpl_name is not None:
            self.tpl_name = tpl_name
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if task_status is not None:
            self.task_status = task_status
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def task_id(self):
        r"""Gets the task_id of this ListAimSendTasksRequest.

        智能信息发送任务ID。

        :return: The task_id of this ListAimSendTasksRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ListAimSendTasksRequest.

        智能信息发送任务ID。

        :param task_id: The task_id of this ListAimSendTasksRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        r"""Gets the task_name of this ListAimSendTasksRequest.

        智能信息发送任务名称。

        :return: The task_name of this ListAimSendTasksRequest.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this ListAimSendTasksRequest.

        智能信息发送任务名称。

        :param task_name: The task_name of this ListAimSendTasksRequest.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def tpl_id(self):
        r"""Gets the tpl_id of this ListAimSendTasksRequest.

        智能信息模板ID。

        :return: The tpl_id of this ListAimSendTasksRequest.
        :rtype: str
        """
        return self._tpl_id

    @tpl_id.setter
    def tpl_id(self, tpl_id):
        r"""Sets the tpl_id of this ListAimSendTasksRequest.

        智能信息模板ID。

        :param tpl_id: The tpl_id of this ListAimSendTasksRequest.
        :type tpl_id: str
        """
        self._tpl_id = tpl_id

    @property
    def tpl_name(self):
        r"""Gets the tpl_name of this ListAimSendTasksRequest.

        智能信息模板名称。

        :return: The tpl_name of this ListAimSendTasksRequest.
        :rtype: str
        """
        return self._tpl_name

    @tpl_name.setter
    def tpl_name(self, tpl_name):
        r"""Sets the tpl_name of this ListAimSendTasksRequest.

        智能信息模板名称。

        :param tpl_name: The tpl_name of this ListAimSendTasksRequest.
        :type tpl_name: str
        """
        self._tpl_name = tpl_name

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ListAimSendTasksRequest.

        智能信息发送任务创建开始时间。样例：2019-10-12T07:20:50.522Z。  > 需同时传入end_time才能生效，单独传begin_time不会作为过滤条件。缺省：查询最近7天（168小时）数据。 > > 仅支持查询最近1年内创建的智能信息发送任务。 

        :return: The begin_time of this ListAimSendTasksRequest.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ListAimSendTasksRequest.

        智能信息发送任务创建开始时间。样例：2019-10-12T07:20:50.522Z。  > 需同时传入end_time才能生效，单独传begin_time不会作为过滤条件。缺省：查询最近7天（168小时）数据。 > > 仅支持查询最近1年内创建的智能信息发送任务。 

        :param begin_time: The begin_time of this ListAimSendTasksRequest.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListAimSendTasksRequest.

        智能信息发送任务创建结束时间。样例：2019-10-12T07:20:50.522Z。  > 需同时传入begin_time才能生效，单独传end_time不会作为过滤条件。缺省：查询最近7天（168小时）数据。 

        :return: The end_time of this ListAimSendTasksRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListAimSendTasksRequest.

        智能信息发送任务创建结束时间。样例：2019-10-12T07:20:50.522Z。  > 需同时传入begin_time才能生效，单独传end_time不会作为过滤条件。缺省：查询最近7天（168小时）数据。 

        :param end_time: The end_time of this ListAimSendTasksRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def task_status(self):
        r"""Gets the task_status of this ListAimSendTasksRequest.

        智能信息发送任务状态。  - Success：创建成功  - Fail：创建失败 

        :return: The task_status of this ListAimSendTasksRequest.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        r"""Sets the task_status of this ListAimSendTasksRequest.

        智能信息发送任务状态。  - Success：创建成功  - Fail：创建失败 

        :param task_status: The task_status of this ListAimSendTasksRequest.
        :type task_status: str
        """
        self._task_status = task_status

    @property
    def offset(self):
        r"""Gets the offset of this ListAimSendTasksRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0。  >为提高查询效率，offset+limit须小于等于10000，超出范围查询为空。 

        :return: The offset of this ListAimSendTasksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAimSendTasksRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0。  >为提高查询效率，offset+limit须小于等于10000，超出范围查询为空。 

        :param offset: The offset of this ListAimSendTasksRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListAimSendTasksRequest.

        每页显示的条目数量。 

        :return: The limit of this ListAimSendTasksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAimSendTasksRequest.

        每页显示的条目数量。 

        :param limit: The limit of this ListAimSendTasksRequest.
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
        if not isinstance(other, ListAimSendTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
