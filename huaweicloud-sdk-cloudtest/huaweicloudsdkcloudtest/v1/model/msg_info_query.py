# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MsgInfoQuery:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alert_types': 'list[str]',
        'case_id': 'str',
        'case_name': 'str',
        'end_time': 'int',
        'page_num': 'int',
        'page_size': 'int',
        'send_alert_type': 'str',
        'start_time': 'int',
        'task_id': 'str',
        'task_name': 'str'
    }

    attribute_map = {
        'alert_types': 'alert_types',
        'case_id': 'case_id',
        'case_name': 'case_name',
        'end_time': 'end_time',
        'page_num': 'page_num',
        'page_size': 'page_size',
        'send_alert_type': 'send_alert_type',
        'start_time': 'start_time',
        'task_id': 'task_id',
        'task_name': 'task_name'
    }

    def __init__(self, alert_types=None, case_id=None, case_name=None, end_time=None, page_num=None, page_size=None, send_alert_type=None, start_time=None, task_id=None, task_name=None):
        r"""MsgInfoQuery

        The model defined in huaweicloud sdk

        :param alert_types: 告警类型
        :type alert_types: list[str]
        :param case_id: 用例id
        :type case_id: str
        :param case_name: 用例名
        :type case_name: str
        :param end_time: 结束时间
        :type end_time: int
        :param page_num: 页码
        :type page_num: int
        :param page_size: 分页大小
        :type page_size: int
        :param send_alert_type: 发送类型
        :type send_alert_type: str
        :param start_time: 开始时间
        :type start_time: int
        :param task_id: 任务id
        :type task_id: str
        :param task_name: 任务名
        :type task_name: str
        """
        
        

        self._alert_types = None
        self._case_id = None
        self._case_name = None
        self._end_time = None
        self._page_num = None
        self._page_size = None
        self._send_alert_type = None
        self._start_time = None
        self._task_id = None
        self._task_name = None
        self.discriminator = None

        if alert_types is not None:
            self.alert_types = alert_types
        if case_id is not None:
            self.case_id = case_id
        if case_name is not None:
            self.case_name = case_name
        if end_time is not None:
            self.end_time = end_time
        if page_num is not None:
            self.page_num = page_num
        if page_size is not None:
            self.page_size = page_size
        if send_alert_type is not None:
            self.send_alert_type = send_alert_type
        if start_time is not None:
            self.start_time = start_time
        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name

    @property
    def alert_types(self):
        r"""Gets the alert_types of this MsgInfoQuery.

        告警类型

        :return: The alert_types of this MsgInfoQuery.
        :rtype: list[str]
        """
        return self._alert_types

    @alert_types.setter
    def alert_types(self, alert_types):
        r"""Sets the alert_types of this MsgInfoQuery.

        告警类型

        :param alert_types: The alert_types of this MsgInfoQuery.
        :type alert_types: list[str]
        """
        self._alert_types = alert_types

    @property
    def case_id(self):
        r"""Gets the case_id of this MsgInfoQuery.

        用例id

        :return: The case_id of this MsgInfoQuery.
        :rtype: str
        """
        return self._case_id

    @case_id.setter
    def case_id(self, case_id):
        r"""Sets the case_id of this MsgInfoQuery.

        用例id

        :param case_id: The case_id of this MsgInfoQuery.
        :type case_id: str
        """
        self._case_id = case_id

    @property
    def case_name(self):
        r"""Gets the case_name of this MsgInfoQuery.

        用例名

        :return: The case_name of this MsgInfoQuery.
        :rtype: str
        """
        return self._case_name

    @case_name.setter
    def case_name(self, case_name):
        r"""Sets the case_name of this MsgInfoQuery.

        用例名

        :param case_name: The case_name of this MsgInfoQuery.
        :type case_name: str
        """
        self._case_name = case_name

    @property
    def end_time(self):
        r"""Gets the end_time of this MsgInfoQuery.

        结束时间

        :return: The end_time of this MsgInfoQuery.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this MsgInfoQuery.

        结束时间

        :param end_time: The end_time of this MsgInfoQuery.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def page_num(self):
        r"""Gets the page_num of this MsgInfoQuery.

        页码

        :return: The page_num of this MsgInfoQuery.
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        r"""Sets the page_num of this MsgInfoQuery.

        页码

        :param page_num: The page_num of this MsgInfoQuery.
        :type page_num: int
        """
        self._page_num = page_num

    @property
    def page_size(self):
        r"""Gets the page_size of this MsgInfoQuery.

        分页大小

        :return: The page_size of this MsgInfoQuery.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this MsgInfoQuery.

        分页大小

        :param page_size: The page_size of this MsgInfoQuery.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def send_alert_type(self):
        r"""Gets the send_alert_type of this MsgInfoQuery.

        发送类型

        :return: The send_alert_type of this MsgInfoQuery.
        :rtype: str
        """
        return self._send_alert_type

    @send_alert_type.setter
    def send_alert_type(self, send_alert_type):
        r"""Sets the send_alert_type of this MsgInfoQuery.

        发送类型

        :param send_alert_type: The send_alert_type of this MsgInfoQuery.
        :type send_alert_type: str
        """
        self._send_alert_type = send_alert_type

    @property
    def start_time(self):
        r"""Gets the start_time of this MsgInfoQuery.

        开始时间

        :return: The start_time of this MsgInfoQuery.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this MsgInfoQuery.

        开始时间

        :param start_time: The start_time of this MsgInfoQuery.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def task_id(self):
        r"""Gets the task_id of this MsgInfoQuery.

        任务id

        :return: The task_id of this MsgInfoQuery.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this MsgInfoQuery.

        任务id

        :param task_id: The task_id of this MsgInfoQuery.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        r"""Gets the task_name of this MsgInfoQuery.

        任务名

        :return: The task_name of this MsgInfoQuery.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this MsgInfoQuery.

        任务名

        :param task_name: The task_name of this MsgInfoQuery.
        :type task_name: str
        """
        self._task_name = task_name

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
        if not isinstance(other, MsgInfoQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
