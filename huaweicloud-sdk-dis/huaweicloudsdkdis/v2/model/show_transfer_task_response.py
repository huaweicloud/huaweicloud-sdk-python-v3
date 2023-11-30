# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTransferTaskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stream_name': 'str',
        'task_name': 'str',
        'state': 'str',
        'destination_type': 'str',
        'create_time': 'int',
        'last_transfer_timestamp': 'int',
        'partitions': 'list[PartitionResult]',
        'obs_destination_description': 'OBSDestinationDescriptorRequest',
        'dws_destination_descripton': 'DWSDestinationDescriptorRequest',
        'mrs_destination_description': 'MRSDestinationDescriptorRequest',
        'dli_destination_description': 'DliDestinationDescriptorRequest',
        'cloudtable_destination_descripton': 'CloudtableDestinationDescriptorRequest'
    }

    attribute_map = {
        'stream_name': 'stream_name',
        'task_name': 'task_name',
        'state': 'state',
        'destination_type': 'destination_type',
        'create_time': 'create_time',
        'last_transfer_timestamp': 'last_transfer_timestamp',
        'partitions': 'partitions',
        'obs_destination_description': 'obs_destination_description',
        'dws_destination_descripton': 'dws_destination_descripton',
        'mrs_destination_description': 'mrs_destination_description',
        'dli_destination_description': 'dli_destination_description',
        'cloudtable_destination_descripton': 'cloudtable_destination_descripton'
    }

    def __init__(self, stream_name=None, task_name=None, state=None, destination_type=None, create_time=None, last_transfer_timestamp=None, partitions=None, obs_destination_description=None, dws_destination_descripton=None, mrs_destination_description=None, dli_destination_description=None, cloudtable_destination_descripton=None):
        """ShowTransferTaskResponse

        The model defined in huaweicloud sdk

        :param stream_name: 该转储任务所属通道名称。
        :type stream_name: str
        :param task_name: 转储任务名称。
        :type task_name: str
        :param state: 转储任务状态。  - ERROR：错误。 - STARTING：启动中。 - PAUSED：已停止。 - RUNNING：运行中。 - DELETE：已删除。 - ABNORMAL：异常。
        :type state: str
        :param destination_type: 转储任务类型。  - OBS：转储到OBS。 - MRS：转储到MRS。 - DLI：转储到DLI。 - CLOUDTABLE：转储到CloudTable。 - DWS：转储到DWS。
        :type destination_type: str
        :param create_time: 转储任务创建时间。
        :type create_time: int
        :param last_transfer_timestamp: 转储任务最近一次转储时间。
        :type last_transfer_timestamp: int
        :param partitions: 分区转储详情列表。
        :type partitions: list[:class:`huaweicloudsdkdis.v2.PartitionResult`]
        :param obs_destination_description: 
        :type obs_destination_description: :class:`huaweicloudsdkdis.v2.OBSDestinationDescriptorRequest`
        :param dws_destination_descripton: 
        :type dws_destination_descripton: :class:`huaweicloudsdkdis.v2.DWSDestinationDescriptorRequest`
        :param mrs_destination_description: 
        :type mrs_destination_description: :class:`huaweicloudsdkdis.v2.MRSDestinationDescriptorRequest`
        :param dli_destination_description: 
        :type dli_destination_description: :class:`huaweicloudsdkdis.v2.DliDestinationDescriptorRequest`
        :param cloudtable_destination_descripton: 
        :type cloudtable_destination_descripton: :class:`huaweicloudsdkdis.v2.CloudtableDestinationDescriptorRequest`
        """
        
        super(ShowTransferTaskResponse, self).__init__()

        self._stream_name = None
        self._task_name = None
        self._state = None
        self._destination_type = None
        self._create_time = None
        self._last_transfer_timestamp = None
        self._partitions = None
        self._obs_destination_description = None
        self._dws_destination_descripton = None
        self._mrs_destination_description = None
        self._dli_destination_description = None
        self._cloudtable_destination_descripton = None
        self.discriminator = None

        if stream_name is not None:
            self.stream_name = stream_name
        if task_name is not None:
            self.task_name = task_name
        if state is not None:
            self.state = state
        if destination_type is not None:
            self.destination_type = destination_type
        if create_time is not None:
            self.create_time = create_time
        if last_transfer_timestamp is not None:
            self.last_transfer_timestamp = last_transfer_timestamp
        if partitions is not None:
            self.partitions = partitions
        if obs_destination_description is not None:
            self.obs_destination_description = obs_destination_description
        if dws_destination_descripton is not None:
            self.dws_destination_descripton = dws_destination_descripton
        if mrs_destination_description is not None:
            self.mrs_destination_description = mrs_destination_description
        if dli_destination_description is not None:
            self.dli_destination_description = dli_destination_description
        if cloudtable_destination_descripton is not None:
            self.cloudtable_destination_descripton = cloudtable_destination_descripton

    @property
    def stream_name(self):
        """Gets the stream_name of this ShowTransferTaskResponse.

        该转储任务所属通道名称。

        :return: The stream_name of this ShowTransferTaskResponse.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """Sets the stream_name of this ShowTransferTaskResponse.

        该转储任务所属通道名称。

        :param stream_name: The stream_name of this ShowTransferTaskResponse.
        :type stream_name: str
        """
        self._stream_name = stream_name

    @property
    def task_name(self):
        """Gets the task_name of this ShowTransferTaskResponse.

        转储任务名称。

        :return: The task_name of this ShowTransferTaskResponse.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this ShowTransferTaskResponse.

        转储任务名称。

        :param task_name: The task_name of this ShowTransferTaskResponse.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def state(self):
        """Gets the state of this ShowTransferTaskResponse.

        转储任务状态。  - ERROR：错误。 - STARTING：启动中。 - PAUSED：已停止。 - RUNNING：运行中。 - DELETE：已删除。 - ABNORMAL：异常。

        :return: The state of this ShowTransferTaskResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ShowTransferTaskResponse.

        转储任务状态。  - ERROR：错误。 - STARTING：启动中。 - PAUSED：已停止。 - RUNNING：运行中。 - DELETE：已删除。 - ABNORMAL：异常。

        :param state: The state of this ShowTransferTaskResponse.
        :type state: str
        """
        self._state = state

    @property
    def destination_type(self):
        """Gets the destination_type of this ShowTransferTaskResponse.

        转储任务类型。  - OBS：转储到OBS。 - MRS：转储到MRS。 - DLI：转储到DLI。 - CLOUDTABLE：转储到CloudTable。 - DWS：转储到DWS。

        :return: The destination_type of this ShowTransferTaskResponse.
        :rtype: str
        """
        return self._destination_type

    @destination_type.setter
    def destination_type(self, destination_type):
        """Sets the destination_type of this ShowTransferTaskResponse.

        转储任务类型。  - OBS：转储到OBS。 - MRS：转储到MRS。 - DLI：转储到DLI。 - CLOUDTABLE：转储到CloudTable。 - DWS：转储到DWS。

        :param destination_type: The destination_type of this ShowTransferTaskResponse.
        :type destination_type: str
        """
        self._destination_type = destination_type

    @property
    def create_time(self):
        """Gets the create_time of this ShowTransferTaskResponse.

        转储任务创建时间。

        :return: The create_time of this ShowTransferTaskResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowTransferTaskResponse.

        转储任务创建时间。

        :param create_time: The create_time of this ShowTransferTaskResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def last_transfer_timestamp(self):
        """Gets the last_transfer_timestamp of this ShowTransferTaskResponse.

        转储任务最近一次转储时间。

        :return: The last_transfer_timestamp of this ShowTransferTaskResponse.
        :rtype: int
        """
        return self._last_transfer_timestamp

    @last_transfer_timestamp.setter
    def last_transfer_timestamp(self, last_transfer_timestamp):
        """Sets the last_transfer_timestamp of this ShowTransferTaskResponse.

        转储任务最近一次转储时间。

        :param last_transfer_timestamp: The last_transfer_timestamp of this ShowTransferTaskResponse.
        :type last_transfer_timestamp: int
        """
        self._last_transfer_timestamp = last_transfer_timestamp

    @property
    def partitions(self):
        """Gets the partitions of this ShowTransferTaskResponse.

        分区转储详情列表。

        :return: The partitions of this ShowTransferTaskResponse.
        :rtype: list[:class:`huaweicloudsdkdis.v2.PartitionResult`]
        """
        return self._partitions

    @partitions.setter
    def partitions(self, partitions):
        """Sets the partitions of this ShowTransferTaskResponse.

        分区转储详情列表。

        :param partitions: The partitions of this ShowTransferTaskResponse.
        :type partitions: list[:class:`huaweicloudsdkdis.v2.PartitionResult`]
        """
        self._partitions = partitions

    @property
    def obs_destination_description(self):
        """Gets the obs_destination_description of this ShowTransferTaskResponse.

        :return: The obs_destination_description of this ShowTransferTaskResponse.
        :rtype: :class:`huaweicloudsdkdis.v2.OBSDestinationDescriptorRequest`
        """
        return self._obs_destination_description

    @obs_destination_description.setter
    def obs_destination_description(self, obs_destination_description):
        """Sets the obs_destination_description of this ShowTransferTaskResponse.

        :param obs_destination_description: The obs_destination_description of this ShowTransferTaskResponse.
        :type obs_destination_description: :class:`huaweicloudsdkdis.v2.OBSDestinationDescriptorRequest`
        """
        self._obs_destination_description = obs_destination_description

    @property
    def dws_destination_descripton(self):
        """Gets the dws_destination_descripton of this ShowTransferTaskResponse.

        :return: The dws_destination_descripton of this ShowTransferTaskResponse.
        :rtype: :class:`huaweicloudsdkdis.v2.DWSDestinationDescriptorRequest`
        """
        return self._dws_destination_descripton

    @dws_destination_descripton.setter
    def dws_destination_descripton(self, dws_destination_descripton):
        """Sets the dws_destination_descripton of this ShowTransferTaskResponse.

        :param dws_destination_descripton: The dws_destination_descripton of this ShowTransferTaskResponse.
        :type dws_destination_descripton: :class:`huaweicloudsdkdis.v2.DWSDestinationDescriptorRequest`
        """
        self._dws_destination_descripton = dws_destination_descripton

    @property
    def mrs_destination_description(self):
        """Gets the mrs_destination_description of this ShowTransferTaskResponse.

        :return: The mrs_destination_description of this ShowTransferTaskResponse.
        :rtype: :class:`huaweicloudsdkdis.v2.MRSDestinationDescriptorRequest`
        """
        return self._mrs_destination_description

    @mrs_destination_description.setter
    def mrs_destination_description(self, mrs_destination_description):
        """Sets the mrs_destination_description of this ShowTransferTaskResponse.

        :param mrs_destination_description: The mrs_destination_description of this ShowTransferTaskResponse.
        :type mrs_destination_description: :class:`huaweicloudsdkdis.v2.MRSDestinationDescriptorRequest`
        """
        self._mrs_destination_description = mrs_destination_description

    @property
    def dli_destination_description(self):
        """Gets the dli_destination_description of this ShowTransferTaskResponse.

        :return: The dli_destination_description of this ShowTransferTaskResponse.
        :rtype: :class:`huaweicloudsdkdis.v2.DliDestinationDescriptorRequest`
        """
        return self._dli_destination_description

    @dli_destination_description.setter
    def dli_destination_description(self, dli_destination_description):
        """Sets the dli_destination_description of this ShowTransferTaskResponse.

        :param dli_destination_description: The dli_destination_description of this ShowTransferTaskResponse.
        :type dli_destination_description: :class:`huaweicloudsdkdis.v2.DliDestinationDescriptorRequest`
        """
        self._dli_destination_description = dli_destination_description

    @property
    def cloudtable_destination_descripton(self):
        """Gets the cloudtable_destination_descripton of this ShowTransferTaskResponse.

        :return: The cloudtable_destination_descripton of this ShowTransferTaskResponse.
        :rtype: :class:`huaweicloudsdkdis.v2.CloudtableDestinationDescriptorRequest`
        """
        return self._cloudtable_destination_descripton

    @cloudtable_destination_descripton.setter
    def cloudtable_destination_descripton(self, cloudtable_destination_descripton):
        """Sets the cloudtable_destination_descripton of this ShowTransferTaskResponse.

        :param cloudtable_destination_descripton: The cloudtable_destination_descripton of this ShowTransferTaskResponse.
        :type cloudtable_destination_descripton: :class:`huaweicloudsdkdis.v2.CloudtableDestinationDescriptorRequest`
        """
        self._cloudtable_destination_descripton = cloudtable_destination_descripton

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
        if not isinstance(other, ShowTransferTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
