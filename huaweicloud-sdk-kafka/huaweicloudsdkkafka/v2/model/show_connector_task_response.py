# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowConnectorTaskResponse(SdkResponse):

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
        'topics': 'str',
        'source_type': 'str',
        'source_task': 'SmartConnectTaskRespSourceConfig',
        'sink_type': 'str',
        'sink_task': 'SmartConnectTaskRespSinkConfig',
        'id': 'str',
        'status': 'str',
        'create_time': 'int'
    }

    attribute_map = {
        'task_name': 'task_name',
        'topics': 'topics',
        'source_type': 'source_type',
        'source_task': 'source_task',
        'sink_type': 'sink_type',
        'sink_task': 'sink_task',
        'id': 'id',
        'status': 'status',
        'create_time': 'create_time'
    }

    def __init__(self, task_name=None, topics=None, source_type=None, source_task=None, sink_type=None, sink_task=None, id=None, status=None, create_time=None):
        """ShowConnectorTaskResponse

        The model defined in huaweicloud sdk

        :param task_name: SmartConnect任务名称。
        :type task_name: str
        :param topics: SmartConnect任务配置的Topic。
        :type topics: str
        :param source_type: SmartConnect任务的源端类型。
        :type source_type: str
        :param source_task: 
        :type source_task: :class:`huaweicloudsdkkafka.v2.SmartConnectTaskRespSourceConfig`
        :param sink_type: SmartConnect任务的目标端类型。
        :type sink_type: str
        :param sink_task: 
        :type sink_task: :class:`huaweicloudsdkkafka.v2.SmartConnectTaskRespSinkConfig`
        :param id: SmartConnect任务的id。
        :type id: str
        :param status: SmartConnect任务的状态。
        :type status: str
        :param create_time: SmartConnect任务的创建时间。
        :type create_time: int
        """
        
        super(ShowConnectorTaskResponse, self).__init__()

        self._task_name = None
        self._topics = None
        self._source_type = None
        self._source_task = None
        self._sink_type = None
        self._sink_task = None
        self._id = None
        self._status = None
        self._create_time = None
        self.discriminator = None

        if task_name is not None:
            self.task_name = task_name
        if topics is not None:
            self.topics = topics
        if source_type is not None:
            self.source_type = source_type
        if source_task is not None:
            self.source_task = source_task
        if sink_type is not None:
            self.sink_type = sink_type
        if sink_task is not None:
            self.sink_task = sink_task
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time

    @property
    def task_name(self):
        """Gets the task_name of this ShowConnectorTaskResponse.

        SmartConnect任务名称。

        :return: The task_name of this ShowConnectorTaskResponse.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this ShowConnectorTaskResponse.

        SmartConnect任务名称。

        :param task_name: The task_name of this ShowConnectorTaskResponse.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def topics(self):
        """Gets the topics of this ShowConnectorTaskResponse.

        SmartConnect任务配置的Topic。

        :return: The topics of this ShowConnectorTaskResponse.
        :rtype: str
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        """Sets the topics of this ShowConnectorTaskResponse.

        SmartConnect任务配置的Topic。

        :param topics: The topics of this ShowConnectorTaskResponse.
        :type topics: str
        """
        self._topics = topics

    @property
    def source_type(self):
        """Gets the source_type of this ShowConnectorTaskResponse.

        SmartConnect任务的源端类型。

        :return: The source_type of this ShowConnectorTaskResponse.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this ShowConnectorTaskResponse.

        SmartConnect任务的源端类型。

        :param source_type: The source_type of this ShowConnectorTaskResponse.
        :type source_type: str
        """
        self._source_type = source_type

    @property
    def source_task(self):
        """Gets the source_task of this ShowConnectorTaskResponse.

        :return: The source_task of this ShowConnectorTaskResponse.
        :rtype: :class:`huaweicloudsdkkafka.v2.SmartConnectTaskRespSourceConfig`
        """
        return self._source_task

    @source_task.setter
    def source_task(self, source_task):
        """Sets the source_task of this ShowConnectorTaskResponse.

        :param source_task: The source_task of this ShowConnectorTaskResponse.
        :type source_task: :class:`huaweicloudsdkkafka.v2.SmartConnectTaskRespSourceConfig`
        """
        self._source_task = source_task

    @property
    def sink_type(self):
        """Gets the sink_type of this ShowConnectorTaskResponse.

        SmartConnect任务的目标端类型。

        :return: The sink_type of this ShowConnectorTaskResponse.
        :rtype: str
        """
        return self._sink_type

    @sink_type.setter
    def sink_type(self, sink_type):
        """Sets the sink_type of this ShowConnectorTaskResponse.

        SmartConnect任务的目标端类型。

        :param sink_type: The sink_type of this ShowConnectorTaskResponse.
        :type sink_type: str
        """
        self._sink_type = sink_type

    @property
    def sink_task(self):
        """Gets the sink_task of this ShowConnectorTaskResponse.

        :return: The sink_task of this ShowConnectorTaskResponse.
        :rtype: :class:`huaweicloudsdkkafka.v2.SmartConnectTaskRespSinkConfig`
        """
        return self._sink_task

    @sink_task.setter
    def sink_task(self, sink_task):
        """Sets the sink_task of this ShowConnectorTaskResponse.

        :param sink_task: The sink_task of this ShowConnectorTaskResponse.
        :type sink_task: :class:`huaweicloudsdkkafka.v2.SmartConnectTaskRespSinkConfig`
        """
        self._sink_task = sink_task

    @property
    def id(self):
        """Gets the id of this ShowConnectorTaskResponse.

        SmartConnect任务的id。

        :return: The id of this ShowConnectorTaskResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowConnectorTaskResponse.

        SmartConnect任务的id。

        :param id: The id of this ShowConnectorTaskResponse.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this ShowConnectorTaskResponse.

        SmartConnect任务的状态。

        :return: The status of this ShowConnectorTaskResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowConnectorTaskResponse.

        SmartConnect任务的状态。

        :param status: The status of this ShowConnectorTaskResponse.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this ShowConnectorTaskResponse.

        SmartConnect任务的创建时间。

        :return: The create_time of this ShowConnectorTaskResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowConnectorTaskResponse.

        SmartConnect任务的创建时间。

        :param create_time: The create_time of this ShowConnectorTaskResponse.
        :type create_time: int
        """
        self._create_time = create_time

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
        if not isinstance(other, ShowConnectorTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
