# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowIterationV4Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'begin_time': 'str',
        'charts': 'list[Chart]',
        'closed_total': 'int',
        'created_time': 'str',
        'end_time': 'str',
        'have_task': 'bool',
        'iteration_id': 'int',
        'name': 'str',
        'opened_total': 'int',
        'progress': 'str',
        'total': 'int',
        'updated_time': 'str',
        'status': 'str'
    }

    attribute_map = {
        'begin_time': 'begin_time',
        'charts': 'charts',
        'closed_total': 'closed_total',
        'created_time': 'created_time',
        'end_time': 'end_time',
        'have_task': 'have_task',
        'iteration_id': 'iteration_id',
        'name': 'name',
        'opened_total': 'opened_total',
        'progress': 'progress',
        'total': 'total',
        'updated_time': 'updated_time',
        'status': 'status'
    }

    def __init__(self, begin_time=None, charts=None, closed_total=None, created_time=None, end_time=None, have_task=None, iteration_id=None, name=None, opened_total=None, progress=None, total=None, updated_time=None, status=None):
        """ShowIterationV4Response

        The model defined in huaweicloud sdk

        :param begin_time: 迭代结束时间，年-月-日
        :type begin_time: str
        :param charts: 燃尽图
        :type charts: list[:class:`huaweicloudsdkprojectman.v4.Chart`]
        :param closed_total: 已关闭的工单数
        :type closed_total: int
        :param created_time: 迭代创建时间
        :type created_time: str
        :param end_time: 迭代开始时间，年-月-日
        :type end_time: str
        :param have_task: 是否有task
        :type have_task: bool
        :param iteration_id: 迭代id
        :type iteration_id: int
        :param name: 迭代标题
        :type name: str
        :param opened_total: 开启的工单数
        :type opened_total: int
        :param progress: 工作进展
        :type progress: str
        :param total: 工单总数
        :type total: int
        :param updated_time: 迭代更新时间
        :type updated_time: str
        :param status: 迭代的状态,0 未开始，1 进行中，2 结束
        :type status: str
        """
        
        super(ShowIterationV4Response, self).__init__()

        self._begin_time = None
        self._charts = None
        self._closed_total = None
        self._created_time = None
        self._end_time = None
        self._have_task = None
        self._iteration_id = None
        self._name = None
        self._opened_total = None
        self._progress = None
        self._total = None
        self._updated_time = None
        self._status = None
        self.discriminator = None

        if begin_time is not None:
            self.begin_time = begin_time
        if charts is not None:
            self.charts = charts
        if closed_total is not None:
            self.closed_total = closed_total
        if created_time is not None:
            self.created_time = created_time
        if end_time is not None:
            self.end_time = end_time
        if have_task is not None:
            self.have_task = have_task
        if iteration_id is not None:
            self.iteration_id = iteration_id
        if name is not None:
            self.name = name
        if opened_total is not None:
            self.opened_total = opened_total
        if progress is not None:
            self.progress = progress
        if total is not None:
            self.total = total
        if updated_time is not None:
            self.updated_time = updated_time
        if status is not None:
            self.status = status

    @property
    def begin_time(self):
        """Gets the begin_time of this ShowIterationV4Response.

        迭代结束时间，年-月-日

        :return: The begin_time of this ShowIterationV4Response.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ShowIterationV4Response.

        迭代结束时间，年-月-日

        :param begin_time: The begin_time of this ShowIterationV4Response.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def charts(self):
        """Gets the charts of this ShowIterationV4Response.

        燃尽图

        :return: The charts of this ShowIterationV4Response.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.Chart`]
        """
        return self._charts

    @charts.setter
    def charts(self, charts):
        """Sets the charts of this ShowIterationV4Response.

        燃尽图

        :param charts: The charts of this ShowIterationV4Response.
        :type charts: list[:class:`huaweicloudsdkprojectman.v4.Chart`]
        """
        self._charts = charts

    @property
    def closed_total(self):
        """Gets the closed_total of this ShowIterationV4Response.

        已关闭的工单数

        :return: The closed_total of this ShowIterationV4Response.
        :rtype: int
        """
        return self._closed_total

    @closed_total.setter
    def closed_total(self, closed_total):
        """Sets the closed_total of this ShowIterationV4Response.

        已关闭的工单数

        :param closed_total: The closed_total of this ShowIterationV4Response.
        :type closed_total: int
        """
        self._closed_total = closed_total

    @property
    def created_time(self):
        """Gets the created_time of this ShowIterationV4Response.

        迭代创建时间

        :return: The created_time of this ShowIterationV4Response.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this ShowIterationV4Response.

        迭代创建时间

        :param created_time: The created_time of this ShowIterationV4Response.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowIterationV4Response.

        迭代开始时间，年-月-日

        :return: The end_time of this ShowIterationV4Response.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowIterationV4Response.

        迭代开始时间，年-月-日

        :param end_time: The end_time of this ShowIterationV4Response.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def have_task(self):
        """Gets the have_task of this ShowIterationV4Response.

        是否有task

        :return: The have_task of this ShowIterationV4Response.
        :rtype: bool
        """
        return self._have_task

    @have_task.setter
    def have_task(self, have_task):
        """Sets the have_task of this ShowIterationV4Response.

        是否有task

        :param have_task: The have_task of this ShowIterationV4Response.
        :type have_task: bool
        """
        self._have_task = have_task

    @property
    def iteration_id(self):
        """Gets the iteration_id of this ShowIterationV4Response.

        迭代id

        :return: The iteration_id of this ShowIterationV4Response.
        :rtype: int
        """
        return self._iteration_id

    @iteration_id.setter
    def iteration_id(self, iteration_id):
        """Sets the iteration_id of this ShowIterationV4Response.

        迭代id

        :param iteration_id: The iteration_id of this ShowIterationV4Response.
        :type iteration_id: int
        """
        self._iteration_id = iteration_id

    @property
    def name(self):
        """Gets the name of this ShowIterationV4Response.

        迭代标题

        :return: The name of this ShowIterationV4Response.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowIterationV4Response.

        迭代标题

        :param name: The name of this ShowIterationV4Response.
        :type name: str
        """
        self._name = name

    @property
    def opened_total(self):
        """Gets the opened_total of this ShowIterationV4Response.

        开启的工单数

        :return: The opened_total of this ShowIterationV4Response.
        :rtype: int
        """
        return self._opened_total

    @opened_total.setter
    def opened_total(self, opened_total):
        """Sets the opened_total of this ShowIterationV4Response.

        开启的工单数

        :param opened_total: The opened_total of this ShowIterationV4Response.
        :type opened_total: int
        """
        self._opened_total = opened_total

    @property
    def progress(self):
        """Gets the progress of this ShowIterationV4Response.

        工作进展

        :return: The progress of this ShowIterationV4Response.
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this ShowIterationV4Response.

        工作进展

        :param progress: The progress of this ShowIterationV4Response.
        :type progress: str
        """
        self._progress = progress

    @property
    def total(self):
        """Gets the total of this ShowIterationV4Response.

        工单总数

        :return: The total of this ShowIterationV4Response.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ShowIterationV4Response.

        工单总数

        :param total: The total of this ShowIterationV4Response.
        :type total: int
        """
        self._total = total

    @property
    def updated_time(self):
        """Gets the updated_time of this ShowIterationV4Response.

        迭代更新时间

        :return: The updated_time of this ShowIterationV4Response.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this ShowIterationV4Response.

        迭代更新时间

        :param updated_time: The updated_time of this ShowIterationV4Response.
        :type updated_time: str
        """
        self._updated_time = updated_time

    @property
    def status(self):
        """Gets the status of this ShowIterationV4Response.

        迭代的状态,0 未开始，1 进行中，2 结束

        :return: The status of this ShowIterationV4Response.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowIterationV4Response.

        迭代的状态,0 未开始，1 进行中，2 结束

        :param status: The status of this ShowIterationV4Response.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ShowIterationV4Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
