# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSinkTaskDetailResponse(SdkResponse):

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
        'destination_type': 'str',
        'create_time': 'int',
        'status': 'str',
        'topics': 'str',
        'obs_destination_descriptor': 'ShowSinkTaskDetailRespObsDestinationDescriptor',
        'topics_info': 'list[ShowSinkTaskDetailRespTopicsInfo]'
    }

    attribute_map = {
        'task_name': 'task_name',
        'destination_type': 'destination_type',
        'create_time': 'create_time',
        'status': 'status',
        'topics': 'topics',
        'obs_destination_descriptor': 'obs_destination_descriptor',
        'topics_info': 'topics_info'
    }

    def __init__(self, task_name=None, destination_type=None, create_time=None, status=None, topics=None, obs_destination_descriptor=None, topics_info=None):
        """ShowSinkTaskDetailResponse

        The model defined in huaweicloud sdk

        :param task_name: 转储任务名称。
        :type task_name: str
        :param destination_type: 转储任务类型。
        :type destination_type: str
        :param create_time: 转储任务创建时间戳。
        :type create_time: int
        :param status: 转储任务状态。
        :type status: str
        :param topics: 返回任务转存的topics列表或者正则表达式。
        :type topics: str
        :param obs_destination_descriptor: 
        :type obs_destination_descriptor: :class:`huaweicloudsdkkafka.v2.ShowSinkTaskDetailRespObsDestinationDescriptor`
        :param topics_info: topic信息。
        :type topics_info: list[:class:`huaweicloudsdkkafka.v2.ShowSinkTaskDetailRespTopicsInfo`]
        """
        
        super(ShowSinkTaskDetailResponse, self).__init__()

        self._task_name = None
        self._destination_type = None
        self._create_time = None
        self._status = None
        self._topics = None
        self._obs_destination_descriptor = None
        self._topics_info = None
        self.discriminator = None

        if task_name is not None:
            self.task_name = task_name
        if destination_type is not None:
            self.destination_type = destination_type
        if create_time is not None:
            self.create_time = create_time
        if status is not None:
            self.status = status
        if topics is not None:
            self.topics = topics
        if obs_destination_descriptor is not None:
            self.obs_destination_descriptor = obs_destination_descriptor
        if topics_info is not None:
            self.topics_info = topics_info

    @property
    def task_name(self):
        """Gets the task_name of this ShowSinkTaskDetailResponse.

        转储任务名称。

        :return: The task_name of this ShowSinkTaskDetailResponse.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this ShowSinkTaskDetailResponse.

        转储任务名称。

        :param task_name: The task_name of this ShowSinkTaskDetailResponse.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def destination_type(self):
        """Gets the destination_type of this ShowSinkTaskDetailResponse.

        转储任务类型。

        :return: The destination_type of this ShowSinkTaskDetailResponse.
        :rtype: str
        """
        return self._destination_type

    @destination_type.setter
    def destination_type(self, destination_type):
        """Sets the destination_type of this ShowSinkTaskDetailResponse.

        转储任务类型。

        :param destination_type: The destination_type of this ShowSinkTaskDetailResponse.
        :type destination_type: str
        """
        self._destination_type = destination_type

    @property
    def create_time(self):
        """Gets the create_time of this ShowSinkTaskDetailResponse.

        转储任务创建时间戳。

        :return: The create_time of this ShowSinkTaskDetailResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowSinkTaskDetailResponse.

        转储任务创建时间戳。

        :param create_time: The create_time of this ShowSinkTaskDetailResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def status(self):
        """Gets the status of this ShowSinkTaskDetailResponse.

        转储任务状态。

        :return: The status of this ShowSinkTaskDetailResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowSinkTaskDetailResponse.

        转储任务状态。

        :param status: The status of this ShowSinkTaskDetailResponse.
        :type status: str
        """
        self._status = status

    @property
    def topics(self):
        """Gets the topics of this ShowSinkTaskDetailResponse.

        返回任务转存的topics列表或者正则表达式。

        :return: The topics of this ShowSinkTaskDetailResponse.
        :rtype: str
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        """Sets the topics of this ShowSinkTaskDetailResponse.

        返回任务转存的topics列表或者正则表达式。

        :param topics: The topics of this ShowSinkTaskDetailResponse.
        :type topics: str
        """
        self._topics = topics

    @property
    def obs_destination_descriptor(self):
        """Gets the obs_destination_descriptor of this ShowSinkTaskDetailResponse.

        :return: The obs_destination_descriptor of this ShowSinkTaskDetailResponse.
        :rtype: :class:`huaweicloudsdkkafka.v2.ShowSinkTaskDetailRespObsDestinationDescriptor`
        """
        return self._obs_destination_descriptor

    @obs_destination_descriptor.setter
    def obs_destination_descriptor(self, obs_destination_descriptor):
        """Sets the obs_destination_descriptor of this ShowSinkTaskDetailResponse.

        :param obs_destination_descriptor: The obs_destination_descriptor of this ShowSinkTaskDetailResponse.
        :type obs_destination_descriptor: :class:`huaweicloudsdkkafka.v2.ShowSinkTaskDetailRespObsDestinationDescriptor`
        """
        self._obs_destination_descriptor = obs_destination_descriptor

    @property
    def topics_info(self):
        """Gets the topics_info of this ShowSinkTaskDetailResponse.

        topic信息。

        :return: The topics_info of this ShowSinkTaskDetailResponse.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.ShowSinkTaskDetailRespTopicsInfo`]
        """
        return self._topics_info

    @topics_info.setter
    def topics_info(self, topics_info):
        """Sets the topics_info of this ShowSinkTaskDetailResponse.

        topic信息。

        :param topics_info: The topics_info of this ShowSinkTaskDetailResponse.
        :type topics_info: list[:class:`huaweicloudsdkkafka.v2.ShowSinkTaskDetailRespTopicsInfo`]
        """
        self._topics_info = topics_info

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
        if not isinstance(other, ShowSinkTaskDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
