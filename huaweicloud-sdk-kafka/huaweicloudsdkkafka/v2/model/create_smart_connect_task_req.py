# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSmartConnectTaskReq:

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
        'start_later': 'bool',
        'topics': 'str',
        'topics_regex': 'str',
        'source_type': 'str',
        'source_task': 'SmartConnectTaskReqSourceConfig',
        'sink_type': 'str',
        'sink_task': 'SmartConnectTaskReqSinkConfig'
    }

    attribute_map = {
        'task_name': 'task_name',
        'start_later': 'start_later',
        'topics': 'topics',
        'topics_regex': 'topics_regex',
        'source_type': 'source_type',
        'source_task': 'source_task',
        'sink_type': 'sink_type',
        'sink_task': 'sink_task'
    }

    def __init__(self, task_name=None, start_later=None, topics=None, topics_regex=None, source_type=None, source_task=None, sink_type=None, sink_task=None):
        r"""CreateSmartConnectTaskReq

        The model defined in huaweicloud sdk

        :param task_name: SmartConnect任务名称。
        :type task_name: str
        :param start_later: 是否稍后再启动任务。如需要创建任务后立即启动，请填false；如希望稍后在任务列表中手动开启任务，请填true。
        :type start_later: bool
        :param topics: SmartConnect任务配置的Topic。
        :type topics: str
        :param topics_regex: SmartConnect任务配置的Topic正则表达式。
        :type topics_regex: str
        :param source_type: SmartConnect任务的源端类型。
        :type source_type: str
        :param source_task: 
        :type source_task: :class:`huaweicloudsdkkafka.v2.SmartConnectTaskReqSourceConfig`
        :param sink_type: SmartConnect任务的目标端类型。
        :type sink_type: str
        :param sink_task: 
        :type sink_task: :class:`huaweicloudsdkkafka.v2.SmartConnectTaskReqSinkConfig`
        """
        
        

        self._task_name = None
        self._start_later = None
        self._topics = None
        self._topics_regex = None
        self._source_type = None
        self._source_task = None
        self._sink_type = None
        self._sink_task = None
        self.discriminator = None

        if task_name is not None:
            self.task_name = task_name
        if start_later is not None:
            self.start_later = start_later
        if topics is not None:
            self.topics = topics
        if topics_regex is not None:
            self.topics_regex = topics_regex
        if source_type is not None:
            self.source_type = source_type
        if source_task is not None:
            self.source_task = source_task
        if sink_type is not None:
            self.sink_type = sink_type
        if sink_task is not None:
            self.sink_task = sink_task

    @property
    def task_name(self):
        r"""Gets the task_name of this CreateSmartConnectTaskReq.

        SmartConnect任务名称。

        :return: The task_name of this CreateSmartConnectTaskReq.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this CreateSmartConnectTaskReq.

        SmartConnect任务名称。

        :param task_name: The task_name of this CreateSmartConnectTaskReq.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def start_later(self):
        r"""Gets the start_later of this CreateSmartConnectTaskReq.

        是否稍后再启动任务。如需要创建任务后立即启动，请填false；如希望稍后在任务列表中手动开启任务，请填true。

        :return: The start_later of this CreateSmartConnectTaskReq.
        :rtype: bool
        """
        return self._start_later

    @start_later.setter
    def start_later(self, start_later):
        r"""Sets the start_later of this CreateSmartConnectTaskReq.

        是否稍后再启动任务。如需要创建任务后立即启动，请填false；如希望稍后在任务列表中手动开启任务，请填true。

        :param start_later: The start_later of this CreateSmartConnectTaskReq.
        :type start_later: bool
        """
        self._start_later = start_later

    @property
    def topics(self):
        r"""Gets the topics of this CreateSmartConnectTaskReq.

        SmartConnect任务配置的Topic。

        :return: The topics of this CreateSmartConnectTaskReq.
        :rtype: str
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        r"""Sets the topics of this CreateSmartConnectTaskReq.

        SmartConnect任务配置的Topic。

        :param topics: The topics of this CreateSmartConnectTaskReq.
        :type topics: str
        """
        self._topics = topics

    @property
    def topics_regex(self):
        r"""Gets the topics_regex of this CreateSmartConnectTaskReq.

        SmartConnect任务配置的Topic正则表达式。

        :return: The topics_regex of this CreateSmartConnectTaskReq.
        :rtype: str
        """
        return self._topics_regex

    @topics_regex.setter
    def topics_regex(self, topics_regex):
        r"""Sets the topics_regex of this CreateSmartConnectTaskReq.

        SmartConnect任务配置的Topic正则表达式。

        :param topics_regex: The topics_regex of this CreateSmartConnectTaskReq.
        :type topics_regex: str
        """
        self._topics_regex = topics_regex

    @property
    def source_type(self):
        r"""Gets the source_type of this CreateSmartConnectTaskReq.

        SmartConnect任务的源端类型。

        :return: The source_type of this CreateSmartConnectTaskReq.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        r"""Sets the source_type of this CreateSmartConnectTaskReq.

        SmartConnect任务的源端类型。

        :param source_type: The source_type of this CreateSmartConnectTaskReq.
        :type source_type: str
        """
        self._source_type = source_type

    @property
    def source_task(self):
        r"""Gets the source_task of this CreateSmartConnectTaskReq.

        :return: The source_task of this CreateSmartConnectTaskReq.
        :rtype: :class:`huaweicloudsdkkafka.v2.SmartConnectTaskReqSourceConfig`
        """
        return self._source_task

    @source_task.setter
    def source_task(self, source_task):
        r"""Sets the source_task of this CreateSmartConnectTaskReq.

        :param source_task: The source_task of this CreateSmartConnectTaskReq.
        :type source_task: :class:`huaweicloudsdkkafka.v2.SmartConnectTaskReqSourceConfig`
        """
        self._source_task = source_task

    @property
    def sink_type(self):
        r"""Gets the sink_type of this CreateSmartConnectTaskReq.

        SmartConnect任务的目标端类型。

        :return: The sink_type of this CreateSmartConnectTaskReq.
        :rtype: str
        """
        return self._sink_type

    @sink_type.setter
    def sink_type(self, sink_type):
        r"""Sets the sink_type of this CreateSmartConnectTaskReq.

        SmartConnect任务的目标端类型。

        :param sink_type: The sink_type of this CreateSmartConnectTaskReq.
        :type sink_type: str
        """
        self._sink_type = sink_type

    @property
    def sink_task(self):
        r"""Gets the sink_task of this CreateSmartConnectTaskReq.

        :return: The sink_task of this CreateSmartConnectTaskReq.
        :rtype: :class:`huaweicloudsdkkafka.v2.SmartConnectTaskReqSinkConfig`
        """
        return self._sink_task

    @sink_task.setter
    def sink_task(self, sink_task):
        r"""Sets the sink_task of this CreateSmartConnectTaskReq.

        :param sink_task: The sink_task of this CreateSmartConnectTaskReq.
        :type sink_task: :class:`huaweicloudsdkkafka.v2.SmartConnectTaskReqSinkConfig`
        """
        self._sink_task = sink_task

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
        if not isinstance(other, CreateSmartConnectTaskReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
