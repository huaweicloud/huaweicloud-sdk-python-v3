# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFactoryJobsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'limit': 'int',
        'offset': 'int',
        'job_type': 'str',
        'job_name': 'str',
        'job_id': 'str',
        'status': 'str',
        'need_alarms': 'bool',
        'tags': 'str',
        'match_all_tags': 'bool',
        'connection_name': 'str',
        'source_type': 'str',
        'source_name': 'str',
        'sink_type': 'str',
        'sink_name': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'limit': 'limit',
        'offset': 'offset',
        'job_type': 'job_type',
        'job_name': 'job_name',
        'job_id': 'job_id',
        'status': 'status',
        'need_alarms': 'need_alarms',
        'tags': 'tags',
        'match_all_tags': 'match_all_tags',
        'connection_name': 'connection_name',
        'source_type': 'source_type',
        'source_name': 'source_name',
        'sink_type': 'sink_type',
        'sink_name': 'sink_name'
    }

    def __init__(self, workspace=None, limit=None, offset=None, job_type=None, job_name=None, job_id=None, status=None, need_alarms=None, tags=None, match_all_tags=None, connection_name=None, source_type=None, source_name=None, sink_type=None, sink_name=None):
        r"""ListFactoryJobsRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace: str
        :param limit: 分页参数：每页限定数量
        :type limit: int
        :param offset: 分页参数：页数
        :type offset: int
        :param job_type: 作业类型:  - REAL_TIME: 实时处理  - BATCH: 批处理
        :type job_type: str
        :param job_name: 作业名称
        :type job_name: str
        :param job_id: 作业ID，支持多个ID逗号分隔查询，最多50个ID，总长度不超过1000字符。 每个ID必须为纯数字。
        :type job_id: str
        :param status: 作业状态，支持多个状态逗号分隔查询。 批处理作业状态：  - SCHEDULING: 调度中  - STOPPED: 停止  - PAUSED: 暂停 实时作业状态：  - STARTING: 启动中  - NORMAL: 正常  - EXCEPTION: 异常  - STOPPING: 停止中  - STOPPED: 停止  - PAUSE: 暂停  - ABNORMAL: 异常
        :type status: str
        :param need_alarms: 是否返回作业告警信息，默认为false。
        :type need_alarms: bool
        :param tags: 作业标签，多个标签逗号分隔。
        :type tags: str
        :param match_all_tags: 标签匹配模式：  - false: 任一标签匹配即返回（OR模式）  - true: 所有标签都匹配才返回（AND模式）
        :type match_all_tags: bool
        :param connection_name: 数据连接名称，按数据连接筛选作业。
        :type connection_name: str
        :param source_type: 源端数据连接类型，按源端数据类型筛选作业。
        :type source_type: str
        :param source_name: 源端数据连接名称，按源端数据名称筛选作业。
        :type source_name: str
        :param sink_type: 目的端数据连接类型，按目的端数据类型筛选作业。
        :type sink_type: str
        :param sink_name: 目的端数据连接名称，按目的端数据名称筛选作业。
        :type sink_name: str
        """
        
        

        self._workspace = None
        self._limit = None
        self._offset = None
        self._job_type = None
        self._job_name = None
        self._job_id = None
        self._status = None
        self._need_alarms = None
        self._tags = None
        self._match_all_tags = None
        self._connection_name = None
        self._source_type = None
        self._source_name = None
        self._sink_type = None
        self._sink_name = None
        self.discriminator = None

        self.workspace = workspace
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if job_type is not None:
            self.job_type = job_type
        if job_name is not None:
            self.job_name = job_name
        if job_id is not None:
            self.job_id = job_id
        if status is not None:
            self.status = status
        if need_alarms is not None:
            self.need_alarms = need_alarms
        if tags is not None:
            self.tags = tags
        if match_all_tags is not None:
            self.match_all_tags = match_all_tags
        if connection_name is not None:
            self.connection_name = connection_name
        if source_type is not None:
            self.source_type = source_type
        if source_name is not None:
            self.source_name = source_name
        if sink_type is not None:
            self.sink_type = sink_type
        if sink_name is not None:
            self.sink_name = sink_name

    @property
    def workspace(self):
        r"""Gets the workspace of this ListFactoryJobsRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this ListFactoryJobsRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ListFactoryJobsRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this ListFactoryJobsRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def limit(self):
        r"""Gets the limit of this ListFactoryJobsRequest.

        分页参数：每页限定数量

        :return: The limit of this ListFactoryJobsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListFactoryJobsRequest.

        分页参数：每页限定数量

        :param limit: The limit of this ListFactoryJobsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListFactoryJobsRequest.

        分页参数：页数

        :return: The offset of this ListFactoryJobsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListFactoryJobsRequest.

        分页参数：页数

        :param offset: The offset of this ListFactoryJobsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def job_type(self):
        r"""Gets the job_type of this ListFactoryJobsRequest.

        作业类型:  - REAL_TIME: 实时处理  - BATCH: 批处理

        :return: The job_type of this ListFactoryJobsRequest.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this ListFactoryJobsRequest.

        作业类型:  - REAL_TIME: 实时处理  - BATCH: 批处理

        :param job_type: The job_type of this ListFactoryJobsRequest.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def job_name(self):
        r"""Gets the job_name of this ListFactoryJobsRequest.

        作业名称

        :return: The job_name of this ListFactoryJobsRequest.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this ListFactoryJobsRequest.

        作业名称

        :param job_name: The job_name of this ListFactoryJobsRequest.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def job_id(self):
        r"""Gets the job_id of this ListFactoryJobsRequest.

        作业ID，支持多个ID逗号分隔查询，最多50个ID，总长度不超过1000字符。 每个ID必须为纯数字。

        :return: The job_id of this ListFactoryJobsRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ListFactoryJobsRequest.

        作业ID，支持多个ID逗号分隔查询，最多50个ID，总长度不超过1000字符。 每个ID必须为纯数字。

        :param job_id: The job_id of this ListFactoryJobsRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def status(self):
        r"""Gets the status of this ListFactoryJobsRequest.

        作业状态，支持多个状态逗号分隔查询。 批处理作业状态：  - SCHEDULING: 调度中  - STOPPED: 停止  - PAUSED: 暂停 实时作业状态：  - STARTING: 启动中  - NORMAL: 正常  - EXCEPTION: 异常  - STOPPING: 停止中  - STOPPED: 停止  - PAUSE: 暂停  - ABNORMAL: 异常

        :return: The status of this ListFactoryJobsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListFactoryJobsRequest.

        作业状态，支持多个状态逗号分隔查询。 批处理作业状态：  - SCHEDULING: 调度中  - STOPPED: 停止  - PAUSED: 暂停 实时作业状态：  - STARTING: 启动中  - NORMAL: 正常  - EXCEPTION: 异常  - STOPPING: 停止中  - STOPPED: 停止  - PAUSE: 暂停  - ABNORMAL: 异常

        :param status: The status of this ListFactoryJobsRequest.
        :type status: str
        """
        self._status = status

    @property
    def need_alarms(self):
        r"""Gets the need_alarms of this ListFactoryJobsRequest.

        是否返回作业告警信息，默认为false。

        :return: The need_alarms of this ListFactoryJobsRequest.
        :rtype: bool
        """
        return self._need_alarms

    @need_alarms.setter
    def need_alarms(self, need_alarms):
        r"""Sets the need_alarms of this ListFactoryJobsRequest.

        是否返回作业告警信息，默认为false。

        :param need_alarms: The need_alarms of this ListFactoryJobsRequest.
        :type need_alarms: bool
        """
        self._need_alarms = need_alarms

    @property
    def tags(self):
        r"""Gets the tags of this ListFactoryJobsRequest.

        作业标签，多个标签逗号分隔。

        :return: The tags of this ListFactoryJobsRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListFactoryJobsRequest.

        作业标签，多个标签逗号分隔。

        :param tags: The tags of this ListFactoryJobsRequest.
        :type tags: str
        """
        self._tags = tags

    @property
    def match_all_tags(self):
        r"""Gets the match_all_tags of this ListFactoryJobsRequest.

        标签匹配模式：  - false: 任一标签匹配即返回（OR模式）  - true: 所有标签都匹配才返回（AND模式）

        :return: The match_all_tags of this ListFactoryJobsRequest.
        :rtype: bool
        """
        return self._match_all_tags

    @match_all_tags.setter
    def match_all_tags(self, match_all_tags):
        r"""Sets the match_all_tags of this ListFactoryJobsRequest.

        标签匹配模式：  - false: 任一标签匹配即返回（OR模式）  - true: 所有标签都匹配才返回（AND模式）

        :param match_all_tags: The match_all_tags of this ListFactoryJobsRequest.
        :type match_all_tags: bool
        """
        self._match_all_tags = match_all_tags

    @property
    def connection_name(self):
        r"""Gets the connection_name of this ListFactoryJobsRequest.

        数据连接名称，按数据连接筛选作业。

        :return: The connection_name of this ListFactoryJobsRequest.
        :rtype: str
        """
        return self._connection_name

    @connection_name.setter
    def connection_name(self, connection_name):
        r"""Sets the connection_name of this ListFactoryJobsRequest.

        数据连接名称，按数据连接筛选作业。

        :param connection_name: The connection_name of this ListFactoryJobsRequest.
        :type connection_name: str
        """
        self._connection_name = connection_name

    @property
    def source_type(self):
        r"""Gets the source_type of this ListFactoryJobsRequest.

        源端数据连接类型，按源端数据类型筛选作业。

        :return: The source_type of this ListFactoryJobsRequest.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        r"""Sets the source_type of this ListFactoryJobsRequest.

        源端数据连接类型，按源端数据类型筛选作业。

        :param source_type: The source_type of this ListFactoryJobsRequest.
        :type source_type: str
        """
        self._source_type = source_type

    @property
    def source_name(self):
        r"""Gets the source_name of this ListFactoryJobsRequest.

        源端数据连接名称，按源端数据名称筛选作业。

        :return: The source_name of this ListFactoryJobsRequest.
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        r"""Sets the source_name of this ListFactoryJobsRequest.

        源端数据连接名称，按源端数据名称筛选作业。

        :param source_name: The source_name of this ListFactoryJobsRequest.
        :type source_name: str
        """
        self._source_name = source_name

    @property
    def sink_type(self):
        r"""Gets the sink_type of this ListFactoryJobsRequest.

        目的端数据连接类型，按目的端数据类型筛选作业。

        :return: The sink_type of this ListFactoryJobsRequest.
        :rtype: str
        """
        return self._sink_type

    @sink_type.setter
    def sink_type(self, sink_type):
        r"""Sets the sink_type of this ListFactoryJobsRequest.

        目的端数据连接类型，按目的端数据类型筛选作业。

        :param sink_type: The sink_type of this ListFactoryJobsRequest.
        :type sink_type: str
        """
        self._sink_type = sink_type

    @property
    def sink_name(self):
        r"""Gets the sink_name of this ListFactoryJobsRequest.

        目的端数据连接名称，按目的端数据名称筛选作业。

        :return: The sink_name of this ListFactoryJobsRequest.
        :rtype: str
        """
        return self._sink_name

    @sink_name.setter
    def sink_name(self, sink_name):
        r"""Sets the sink_name of this ListFactoryJobsRequest.

        目的端数据连接名称，按目的端数据名称筛选作业。

        :param sink_name: The sink_name of this ListFactoryJobsRequest.
        :type sink_name: str
        """
        self._sink_name = sink_name

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListFactoryJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
