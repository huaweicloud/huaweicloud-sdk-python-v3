# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BuildStageRecord:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'status': 'str',
        'status_code': 'int',
        'log_status': 'str',
        'create_time': 'str',
        'schedule_time': 'str',
        'queued_time': 'str',
        'start_time': 'str',
        'finish_time': 'str',
        'duration': 'int',
        'build_duration': 'int',
        'pending_duration': 'int',
        'build_record_id': 'str',
        'execution_id': 'str',
        'execution_stage_name': 'str',
        'display_name': 'str',
        'node_id': 'int',
        'sequence': 'int'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'status_code': 'status_code',
        'log_status': 'log_status',
        'create_time': 'create_time',
        'schedule_time': 'schedule_time',
        'queued_time': 'queued_time',
        'start_time': 'start_time',
        'finish_time': 'finish_time',
        'duration': 'duration',
        'build_duration': 'build_duration',
        'pending_duration': 'pending_duration',
        'build_record_id': 'build_record_id',
        'execution_id': 'execution_id',
        'execution_stage_name': 'execution_stage_name',
        'display_name': 'display_name',
        'node_id': 'node_id',
        'sequence': 'sequence'
    }

    def __init__(self, id=None, status=None, status_code=None, log_status=None, create_time=None, schedule_time=None, queued_time=None, start_time=None, finish_time=None, duration=None, build_duration=None, pending_duration=None, build_record_id=None, execution_id=None, execution_stage_name=None, display_name=None, node_id=None, sequence=None):
        r"""BuildStageRecord

        The model defined in huaweicloud sdk

        :param id: 步骤编号
        :type id: str
        :param status: 步骤状态
        :type status: str
        :param status_code: 状态码
        :type status_code: int
        :param log_status: 日志状态
        :type log_status: str
        :param create_time: 创建时间
        :type create_time: str
        :param schedule_time: 构建下发时间
        :type schedule_time: str
        :param queued_time: 构建排队耗时
        :type queued_time: str
        :param start_time: 开始时间
        :type start_time: str
        :param finish_time: 结束时间
        :type finish_time: str
        :param duration: 构建时长
        :type duration: int
        :param build_duration: 子任务构建耗时
        :type build_duration: int
        :param pending_duration: 等待时间
        :type pending_duration: int
        :param build_record_id: 构建记录ID
        :type build_record_id: str
        :param execution_id: 八爪鱼任务ID
        :type execution_id: str
        :param execution_stage_name: 步骤名称
        :type execution_stage_name: str
        :param display_name: 步骤名称
        :type display_name: str
        :param node_id: 节点ID
        :type node_id: int
        :param sequence: 序号
        :type sequence: int
        """
        
        

        self._id = None
        self._status = None
        self._status_code = None
        self._log_status = None
        self._create_time = None
        self._schedule_time = None
        self._queued_time = None
        self._start_time = None
        self._finish_time = None
        self._duration = None
        self._build_duration = None
        self._pending_duration = None
        self._build_record_id = None
        self._execution_id = None
        self._execution_stage_name = None
        self._display_name = None
        self._node_id = None
        self._sequence = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if status_code is not None:
            self.status_code = status_code
        if log_status is not None:
            self.log_status = log_status
        if create_time is not None:
            self.create_time = create_time
        if schedule_time is not None:
            self.schedule_time = schedule_time
        if queued_time is not None:
            self.queued_time = queued_time
        if start_time is not None:
            self.start_time = start_time
        if finish_time is not None:
            self.finish_time = finish_time
        if duration is not None:
            self.duration = duration
        if build_duration is not None:
            self.build_duration = build_duration
        if pending_duration is not None:
            self.pending_duration = pending_duration
        if build_record_id is not None:
            self.build_record_id = build_record_id
        if execution_id is not None:
            self.execution_id = execution_id
        if execution_stage_name is not None:
            self.execution_stage_name = execution_stage_name
        if display_name is not None:
            self.display_name = display_name
        if node_id is not None:
            self.node_id = node_id
        if sequence is not None:
            self.sequence = sequence

    @property
    def id(self):
        r"""Gets the id of this BuildStageRecord.

        步骤编号

        :return: The id of this BuildStageRecord.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BuildStageRecord.

        步骤编号

        :param id: The id of this BuildStageRecord.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this BuildStageRecord.

        步骤状态

        :return: The status of this BuildStageRecord.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BuildStageRecord.

        步骤状态

        :param status: The status of this BuildStageRecord.
        :type status: str
        """
        self._status = status

    @property
    def status_code(self):
        r"""Gets the status_code of this BuildStageRecord.

        状态码

        :return: The status_code of this BuildStageRecord.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        r"""Sets the status_code of this BuildStageRecord.

        状态码

        :param status_code: The status_code of this BuildStageRecord.
        :type status_code: int
        """
        self._status_code = status_code

    @property
    def log_status(self):
        r"""Gets the log_status of this BuildStageRecord.

        日志状态

        :return: The log_status of this BuildStageRecord.
        :rtype: str
        """
        return self._log_status

    @log_status.setter
    def log_status(self, log_status):
        r"""Sets the log_status of this BuildStageRecord.

        日志状态

        :param log_status: The log_status of this BuildStageRecord.
        :type log_status: str
        """
        self._log_status = log_status

    @property
    def create_time(self):
        r"""Gets the create_time of this BuildStageRecord.

        创建时间

        :return: The create_time of this BuildStageRecord.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this BuildStageRecord.

        创建时间

        :param create_time: The create_time of this BuildStageRecord.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def schedule_time(self):
        r"""Gets the schedule_time of this BuildStageRecord.

        构建下发时间

        :return: The schedule_time of this BuildStageRecord.
        :rtype: str
        """
        return self._schedule_time

    @schedule_time.setter
    def schedule_time(self, schedule_time):
        r"""Sets the schedule_time of this BuildStageRecord.

        构建下发时间

        :param schedule_time: The schedule_time of this BuildStageRecord.
        :type schedule_time: str
        """
        self._schedule_time = schedule_time

    @property
    def queued_time(self):
        r"""Gets the queued_time of this BuildStageRecord.

        构建排队耗时

        :return: The queued_time of this BuildStageRecord.
        :rtype: str
        """
        return self._queued_time

    @queued_time.setter
    def queued_time(self, queued_time):
        r"""Sets the queued_time of this BuildStageRecord.

        构建排队耗时

        :param queued_time: The queued_time of this BuildStageRecord.
        :type queued_time: str
        """
        self._queued_time = queued_time

    @property
    def start_time(self):
        r"""Gets the start_time of this BuildStageRecord.

        开始时间

        :return: The start_time of this BuildStageRecord.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this BuildStageRecord.

        开始时间

        :param start_time: The start_time of this BuildStageRecord.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def finish_time(self):
        r"""Gets the finish_time of this BuildStageRecord.

        结束时间

        :return: The finish_time of this BuildStageRecord.
        :rtype: str
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        r"""Sets the finish_time of this BuildStageRecord.

        结束时间

        :param finish_time: The finish_time of this BuildStageRecord.
        :type finish_time: str
        """
        self._finish_time = finish_time

    @property
    def duration(self):
        r"""Gets the duration of this BuildStageRecord.

        构建时长

        :return: The duration of this BuildStageRecord.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this BuildStageRecord.

        构建时长

        :param duration: The duration of this BuildStageRecord.
        :type duration: int
        """
        self._duration = duration

    @property
    def build_duration(self):
        r"""Gets the build_duration of this BuildStageRecord.

        子任务构建耗时

        :return: The build_duration of this BuildStageRecord.
        :rtype: int
        """
        return self._build_duration

    @build_duration.setter
    def build_duration(self, build_duration):
        r"""Sets the build_duration of this BuildStageRecord.

        子任务构建耗时

        :param build_duration: The build_duration of this BuildStageRecord.
        :type build_duration: int
        """
        self._build_duration = build_duration

    @property
    def pending_duration(self):
        r"""Gets the pending_duration of this BuildStageRecord.

        等待时间

        :return: The pending_duration of this BuildStageRecord.
        :rtype: int
        """
        return self._pending_duration

    @pending_duration.setter
    def pending_duration(self, pending_duration):
        r"""Sets the pending_duration of this BuildStageRecord.

        等待时间

        :param pending_duration: The pending_duration of this BuildStageRecord.
        :type pending_duration: int
        """
        self._pending_duration = pending_duration

    @property
    def build_record_id(self):
        r"""Gets the build_record_id of this BuildStageRecord.

        构建记录ID

        :return: The build_record_id of this BuildStageRecord.
        :rtype: str
        """
        return self._build_record_id

    @build_record_id.setter
    def build_record_id(self, build_record_id):
        r"""Sets the build_record_id of this BuildStageRecord.

        构建记录ID

        :param build_record_id: The build_record_id of this BuildStageRecord.
        :type build_record_id: str
        """
        self._build_record_id = build_record_id

    @property
    def execution_id(self):
        r"""Gets the execution_id of this BuildStageRecord.

        八爪鱼任务ID

        :return: The execution_id of this BuildStageRecord.
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        r"""Sets the execution_id of this BuildStageRecord.

        八爪鱼任务ID

        :param execution_id: The execution_id of this BuildStageRecord.
        :type execution_id: str
        """
        self._execution_id = execution_id

    @property
    def execution_stage_name(self):
        r"""Gets the execution_stage_name of this BuildStageRecord.

        步骤名称

        :return: The execution_stage_name of this BuildStageRecord.
        :rtype: str
        """
        return self._execution_stage_name

    @execution_stage_name.setter
    def execution_stage_name(self, execution_stage_name):
        r"""Sets the execution_stage_name of this BuildStageRecord.

        步骤名称

        :param execution_stage_name: The execution_stage_name of this BuildStageRecord.
        :type execution_stage_name: str
        """
        self._execution_stage_name = execution_stage_name

    @property
    def display_name(self):
        r"""Gets the display_name of this BuildStageRecord.

        步骤名称

        :return: The display_name of this BuildStageRecord.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this BuildStageRecord.

        步骤名称

        :param display_name: The display_name of this BuildStageRecord.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def node_id(self):
        r"""Gets the node_id of this BuildStageRecord.

        节点ID

        :return: The node_id of this BuildStageRecord.
        :rtype: int
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this BuildStageRecord.

        节点ID

        :param node_id: The node_id of this BuildStageRecord.
        :type node_id: int
        """
        self._node_id = node_id

    @property
    def sequence(self):
        r"""Gets the sequence of this BuildStageRecord.

        序号

        :return: The sequence of this BuildStageRecord.
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        r"""Sets the sequence of this BuildStageRecord.

        序号

        :param sequence: The sequence of this BuildStageRecord.
        :type sequence: int
        """
        self._sequence = sequence

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
        if not isinstance(other, BuildStageRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
