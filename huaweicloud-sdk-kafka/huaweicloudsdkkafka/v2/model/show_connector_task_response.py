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
        'topics_regex': 'str',
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
        'topics_regex': 'topics_regex',
        'source_type': 'source_type',
        'source_task': 'source_task',
        'sink_type': 'sink_type',
        'sink_task': 'sink_task',
        'id': 'id',
        'status': 'status',
        'create_time': 'create_time'
    }

    def __init__(self, task_name=None, topics=None, topics_regex=None, source_type=None, source_task=None, sink_type=None, sink_task=None, id=None, status=None, create_time=None):
        r"""ShowConnectorTaskResponse

        The model defined in huaweicloud sdk

        :param task_name: **参数解释**： Smart Connect任务名称。 **取值范围**： 不涉及。
        :type task_name: str
        :param topics: **参数解释**： Smart Connect任务配置的Topic。 **取值范围**： 不涉及。
        :type topics: str
        :param topics_regex: **参数解释**： Smart Connect任务配置的Topic正则表达式。 **取值范围**： 不涉及。
        :type topics_regex: str
        :param source_type: **参数解释**： Smart Connect任务的源端类型。 **取值范围**： - NONE：不配置。 - KAFKA_REPLICATOR_SOURCE：Kafka数据复制。
        :type source_type: str
        :param source_task: 
        :type source_task: :class:`huaweicloudsdkkafka.v2.SmartConnectTaskRespSourceConfig`
        :param sink_type: **参数解释**： Smart Connect任务的目标端类型。 **取值范围**： - NONE：不配置。 - OBS_SINK：转储。
        :type sink_type: str
        :param sink_task: 
        :type sink_task: :class:`huaweicloudsdkkafka.v2.SmartConnectTaskRespSinkConfig`
        :param id: **参数解释**： Smart Connect任务的id。 **取值范围**： 不涉及。
        :type id: str
        :param status: **参数解释**： Smart Connect任务的状态。 **取值范围**： 不涉及。
        :type status: str
        :param create_time: **参数解释**： Smart Connect任务的创建时间。 **取值范围**： 不涉及。
        :type create_time: int
        """
        
        super(ShowConnectorTaskResponse, self).__init__()

        self._task_name = None
        self._topics = None
        self._topics_regex = None
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
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time

    @property
    def task_name(self):
        r"""Gets the task_name of this ShowConnectorTaskResponse.

        **参数解释**： Smart Connect任务名称。 **取值范围**： 不涉及。

        :return: The task_name of this ShowConnectorTaskResponse.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this ShowConnectorTaskResponse.

        **参数解释**： Smart Connect任务名称。 **取值范围**： 不涉及。

        :param task_name: The task_name of this ShowConnectorTaskResponse.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def topics(self):
        r"""Gets the topics of this ShowConnectorTaskResponse.

        **参数解释**： Smart Connect任务配置的Topic。 **取值范围**： 不涉及。

        :return: The topics of this ShowConnectorTaskResponse.
        :rtype: str
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        r"""Sets the topics of this ShowConnectorTaskResponse.

        **参数解释**： Smart Connect任务配置的Topic。 **取值范围**： 不涉及。

        :param topics: The topics of this ShowConnectorTaskResponse.
        :type topics: str
        """
        self._topics = topics

    @property
    def topics_regex(self):
        r"""Gets the topics_regex of this ShowConnectorTaskResponse.

        **参数解释**： Smart Connect任务配置的Topic正则表达式。 **取值范围**： 不涉及。

        :return: The topics_regex of this ShowConnectorTaskResponse.
        :rtype: str
        """
        return self._topics_regex

    @topics_regex.setter
    def topics_regex(self, topics_regex):
        r"""Sets the topics_regex of this ShowConnectorTaskResponse.

        **参数解释**： Smart Connect任务配置的Topic正则表达式。 **取值范围**： 不涉及。

        :param topics_regex: The topics_regex of this ShowConnectorTaskResponse.
        :type topics_regex: str
        """
        self._topics_regex = topics_regex

    @property
    def source_type(self):
        r"""Gets the source_type of this ShowConnectorTaskResponse.

        **参数解释**： Smart Connect任务的源端类型。 **取值范围**： - NONE：不配置。 - KAFKA_REPLICATOR_SOURCE：Kafka数据复制。

        :return: The source_type of this ShowConnectorTaskResponse.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        r"""Sets the source_type of this ShowConnectorTaskResponse.

        **参数解释**： Smart Connect任务的源端类型。 **取值范围**： - NONE：不配置。 - KAFKA_REPLICATOR_SOURCE：Kafka数据复制。

        :param source_type: The source_type of this ShowConnectorTaskResponse.
        :type source_type: str
        """
        self._source_type = source_type

    @property
    def source_task(self):
        r"""Gets the source_task of this ShowConnectorTaskResponse.

        :return: The source_task of this ShowConnectorTaskResponse.
        :rtype: :class:`huaweicloudsdkkafka.v2.SmartConnectTaskRespSourceConfig`
        """
        return self._source_task

    @source_task.setter
    def source_task(self, source_task):
        r"""Sets the source_task of this ShowConnectorTaskResponse.

        :param source_task: The source_task of this ShowConnectorTaskResponse.
        :type source_task: :class:`huaweicloudsdkkafka.v2.SmartConnectTaskRespSourceConfig`
        """
        self._source_task = source_task

    @property
    def sink_type(self):
        r"""Gets the sink_type of this ShowConnectorTaskResponse.

        **参数解释**： Smart Connect任务的目标端类型。 **取值范围**： - NONE：不配置。 - OBS_SINK：转储。

        :return: The sink_type of this ShowConnectorTaskResponse.
        :rtype: str
        """
        return self._sink_type

    @sink_type.setter
    def sink_type(self, sink_type):
        r"""Sets the sink_type of this ShowConnectorTaskResponse.

        **参数解释**： Smart Connect任务的目标端类型。 **取值范围**： - NONE：不配置。 - OBS_SINK：转储。

        :param sink_type: The sink_type of this ShowConnectorTaskResponse.
        :type sink_type: str
        """
        self._sink_type = sink_type

    @property
    def sink_task(self):
        r"""Gets the sink_task of this ShowConnectorTaskResponse.

        :return: The sink_task of this ShowConnectorTaskResponse.
        :rtype: :class:`huaweicloudsdkkafka.v2.SmartConnectTaskRespSinkConfig`
        """
        return self._sink_task

    @sink_task.setter
    def sink_task(self, sink_task):
        r"""Sets the sink_task of this ShowConnectorTaskResponse.

        :param sink_task: The sink_task of this ShowConnectorTaskResponse.
        :type sink_task: :class:`huaweicloudsdkkafka.v2.SmartConnectTaskRespSinkConfig`
        """
        self._sink_task = sink_task

    @property
    def id(self):
        r"""Gets the id of this ShowConnectorTaskResponse.

        **参数解释**： Smart Connect任务的id。 **取值范围**： 不涉及。

        :return: The id of this ShowConnectorTaskResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowConnectorTaskResponse.

        **参数解释**： Smart Connect任务的id。 **取值范围**： 不涉及。

        :param id: The id of this ShowConnectorTaskResponse.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this ShowConnectorTaskResponse.

        **参数解释**： Smart Connect任务的状态。 **取值范围**： 不涉及。

        :return: The status of this ShowConnectorTaskResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowConnectorTaskResponse.

        **参数解释**： Smart Connect任务的状态。 **取值范围**： 不涉及。

        :param status: The status of this ShowConnectorTaskResponse.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowConnectorTaskResponse.

        **参数解释**： Smart Connect任务的创建时间。 **取值范围**： 不涉及。

        :return: The create_time of this ShowConnectorTaskResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowConnectorTaskResponse.

        **参数解释**： Smart Connect任务的创建时间。 **取值范围**： 不涉及。

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
