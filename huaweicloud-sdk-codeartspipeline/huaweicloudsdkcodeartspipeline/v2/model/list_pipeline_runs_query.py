# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPipelineRunsQuery:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'list[str]',
        'start_time': 'str',
        'end_time': 'str',
        'update_time': 'str',
        'trigger_type': 'list[str]',
        'executor_ids': 'list[str]',
        'offset': 'int',
        'limit': 'int',
        'sort_key': 'str',
        'sort_dir': 'str',
        'show_job_details': 'bool',
        'stage_id': 'str',
        'job_id': 'str'
    }

    attribute_map = {
        'status': 'status',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'update_time': 'update_time',
        'trigger_type': 'trigger_type',
        'executor_ids': 'executor_ids',
        'offset': 'offset',
        'limit': 'limit',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'show_job_details': 'show_job_details',
        'stage_id': 'stage_id',
        'job_id': 'job_id'
    }

    def __init__(self, status=None, start_time=None, end_time=None, update_time=None, trigger_type=None, executor_ids=None, offset=None, limit=None, sort_key=None, sort_dir=None, show_job_details=None, stage_id=None, job_id=None):
        r"""ListPipelineRunsQuery

        The model defined in huaweicloud sdk

        :param status: **参数解释**： 流水线状态列表。 **约束限制**： 不涉及。 **取值范围**： - COMPLETED：已完成。 - RUNNING：运行中。 - FAILED：失败。 - CANCELED：取消。 - PAUSED：暂停。 - SUSPEND：挂起。 - IGNORED：忽略。 **默认取值**： 不涉及。 
        :type status: list[str]
        :param start_time: **参数解释**： 流水线开始时间。 **约束限制**： 不涉及。 **取值范围**： 时间戳或者yyyy-MM-dd HH:mm:ss格式均可。 **默认取值**： 不涉及。 
        :type start_time: str
        :param end_time: **参数解释**： 流水线结束时间。 **约束限制**： 不涉及。 **取值范围**： 时间戳或者yyyy-MM-dd HH:mm:ss格式均可。 **默认取值**： 不涉及。 
        :type end_time: str
        :param update_time: **参数解释**： 流水线状态更新时间。 **约束限制**： 不涉及。 **取值范围**： 时间戳或者yyyy-MM-dd HH:mm:ss格式均可。 **默认取值**： 不涉及。 
        :type update_time: str
        :param trigger_type: **参数解释**： 触发类型列表。 **约束限制**： 不涉及。 **取值范围**： - Manual：手动触发。 - Scheduler：定时触发。 - RollBack：回退触发。 - CreateTag：Tag事件触发。 - Note：评论触发。 - Issue：Issue触发。 - MR：MR触发。 - CR：CR触发。 - Generic：流水线触发器触发。 - Push：Push事件触发。 - SubPipeline：子流水线触发。 **默认取值**： 不涉及。 
        :type trigger_type: list[str]
        :param executor_ids: **参数解释**： 执行人ID列表。 **约束限制**： 不涉及。 **取值范围**： 32位字符，仅由数字和字母组成。 **默认取值**： 不涉及。 
        :type executor_ids: list[str]
        :param offset: **参数解释**： 起始偏移。 **约束限制**： 不涉及。 **取值范围**： 大于等于零。 **默认取值**： 不涉及。 
        :type offset: int
        :param limit: **参数解释**： 查询数量。 **约束限制**： 不涉及。 **取值范围**： 大于等于零。 **默认取值**： 不涉及。 
        :type limit: int
        :param sort_key: **参数解释**： 排序字段名称。 **约束限制**： 不涉及。 **取值范围**： \&quot;start_time\&quot; - 流水线开始时间。 \&quot;update_time\&quot; - 流水线更新时间。 **默认取值**： 不涉及。 
        :type sort_key: str
        :param sort_dir: **参数解释**： 排序规则。 **约束限制**： 不涉及。 **取值范围**： - asc：按排序字段升序。 - desc：按排序字段降序。 **默认取值**： 不涉及。 
        :type sort_dir: str
        :param show_job_details: **参数解释**： 是否返回Job状态详情。 **约束限制**： 不涉及。 **取值范围**： - true：返回Job状态列表。 - false：不返回。 **默认取值**： false。 
        :type show_job_details: bool
        :param stage_id: **参数解释**： 阶段ID，用于指定返回Job状态详情的阶段。 **约束限制**： 不涉及。 **取值范围**： 32位字符，仅由数字和字母组成。 **默认取值**： 不涉及，为空时默认取流水线最后一个阶段。 
        :type stage_id: str
        :param job_id: **参数解释**： Job ID，仅在show_job_details为true时生效，用于过滤包含指定Job的执行记录。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type job_id: str
        """
        
        

        self._status = None
        self._start_time = None
        self._end_time = None
        self._update_time = None
        self._trigger_type = None
        self._executor_ids = None
        self._offset = None
        self._limit = None
        self._sort_key = None
        self._sort_dir = None
        self._show_job_details = None
        self._stage_id = None
        self._job_id = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if update_time is not None:
            self.update_time = update_time
        if trigger_type is not None:
            self.trigger_type = trigger_type
        if executor_ids is not None:
            self.executor_ids = executor_ids
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if show_job_details is not None:
            self.show_job_details = show_job_details
        if stage_id is not None:
            self.stage_id = stage_id
        if job_id is not None:
            self.job_id = job_id

    @property
    def status(self):
        r"""Gets the status of this ListPipelineRunsQuery.

        **参数解释**： 流水线状态列表。 **约束限制**： 不涉及。 **取值范围**： - COMPLETED：已完成。 - RUNNING：运行中。 - FAILED：失败。 - CANCELED：取消。 - PAUSED：暂停。 - SUSPEND：挂起。 - IGNORED：忽略。 **默认取值**： 不涉及。 

        :return: The status of this ListPipelineRunsQuery.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListPipelineRunsQuery.

        **参数解释**： 流水线状态列表。 **约束限制**： 不涉及。 **取值范围**： - COMPLETED：已完成。 - RUNNING：运行中。 - FAILED：失败。 - CANCELED：取消。 - PAUSED：暂停。 - SUSPEND：挂起。 - IGNORED：忽略。 **默认取值**： 不涉及。 

        :param status: The status of this ListPipelineRunsQuery.
        :type status: list[str]
        """
        self._status = status

    @property
    def start_time(self):
        r"""Gets the start_time of this ListPipelineRunsQuery.

        **参数解释**： 流水线开始时间。 **约束限制**： 不涉及。 **取值范围**： 时间戳或者yyyy-MM-dd HH:mm:ss格式均可。 **默认取值**： 不涉及。 

        :return: The start_time of this ListPipelineRunsQuery.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListPipelineRunsQuery.

        **参数解释**： 流水线开始时间。 **约束限制**： 不涉及。 **取值范围**： 时间戳或者yyyy-MM-dd HH:mm:ss格式均可。 **默认取值**： 不涉及。 

        :param start_time: The start_time of this ListPipelineRunsQuery.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListPipelineRunsQuery.

        **参数解释**： 流水线结束时间。 **约束限制**： 不涉及。 **取值范围**： 时间戳或者yyyy-MM-dd HH:mm:ss格式均可。 **默认取值**： 不涉及。 

        :return: The end_time of this ListPipelineRunsQuery.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListPipelineRunsQuery.

        **参数解释**： 流水线结束时间。 **约束限制**： 不涉及。 **取值范围**： 时间戳或者yyyy-MM-dd HH:mm:ss格式均可。 **默认取值**： 不涉及。 

        :param end_time: The end_time of this ListPipelineRunsQuery.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ListPipelineRunsQuery.

        **参数解释**： 流水线状态更新时间。 **约束限制**： 不涉及。 **取值范围**： 时间戳或者yyyy-MM-dd HH:mm:ss格式均可。 **默认取值**： 不涉及。 

        :return: The update_time of this ListPipelineRunsQuery.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ListPipelineRunsQuery.

        **参数解释**： 流水线状态更新时间。 **约束限制**： 不涉及。 **取值范围**： 时间戳或者yyyy-MM-dd HH:mm:ss格式均可。 **默认取值**： 不涉及。 

        :param update_time: The update_time of this ListPipelineRunsQuery.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def trigger_type(self):
        r"""Gets the trigger_type of this ListPipelineRunsQuery.

        **参数解释**： 触发类型列表。 **约束限制**： 不涉及。 **取值范围**： - Manual：手动触发。 - Scheduler：定时触发。 - RollBack：回退触发。 - CreateTag：Tag事件触发。 - Note：评论触发。 - Issue：Issue触发。 - MR：MR触发。 - CR：CR触发。 - Generic：流水线触发器触发。 - Push：Push事件触发。 - SubPipeline：子流水线触发。 **默认取值**： 不涉及。 

        :return: The trigger_type of this ListPipelineRunsQuery.
        :rtype: list[str]
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        r"""Sets the trigger_type of this ListPipelineRunsQuery.

        **参数解释**： 触发类型列表。 **约束限制**： 不涉及。 **取值范围**： - Manual：手动触发。 - Scheduler：定时触发。 - RollBack：回退触发。 - CreateTag：Tag事件触发。 - Note：评论触发。 - Issue：Issue触发。 - MR：MR触发。 - CR：CR触发。 - Generic：流水线触发器触发。 - Push：Push事件触发。 - SubPipeline：子流水线触发。 **默认取值**： 不涉及。 

        :param trigger_type: The trigger_type of this ListPipelineRunsQuery.
        :type trigger_type: list[str]
        """
        self._trigger_type = trigger_type

    @property
    def executor_ids(self):
        r"""Gets the executor_ids of this ListPipelineRunsQuery.

        **参数解释**： 执行人ID列表。 **约束限制**： 不涉及。 **取值范围**： 32位字符，仅由数字和字母组成。 **默认取值**： 不涉及。 

        :return: The executor_ids of this ListPipelineRunsQuery.
        :rtype: list[str]
        """
        return self._executor_ids

    @executor_ids.setter
    def executor_ids(self, executor_ids):
        r"""Sets the executor_ids of this ListPipelineRunsQuery.

        **参数解释**： 执行人ID列表。 **约束限制**： 不涉及。 **取值范围**： 32位字符，仅由数字和字母组成。 **默认取值**： 不涉及。 

        :param executor_ids: The executor_ids of this ListPipelineRunsQuery.
        :type executor_ids: list[str]
        """
        self._executor_ids = executor_ids

    @property
    def offset(self):
        r"""Gets the offset of this ListPipelineRunsQuery.

        **参数解释**： 起始偏移。 **约束限制**： 不涉及。 **取值范围**： 大于等于零。 **默认取值**： 不涉及。 

        :return: The offset of this ListPipelineRunsQuery.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPipelineRunsQuery.

        **参数解释**： 起始偏移。 **约束限制**： 不涉及。 **取值范围**： 大于等于零。 **默认取值**： 不涉及。 

        :param offset: The offset of this ListPipelineRunsQuery.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListPipelineRunsQuery.

        **参数解释**： 查询数量。 **约束限制**： 不涉及。 **取值范围**： 大于等于零。 **默认取值**： 不涉及。 

        :return: The limit of this ListPipelineRunsQuery.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPipelineRunsQuery.

        **参数解释**： 查询数量。 **约束限制**： 不涉及。 **取值范围**： 大于等于零。 **默认取值**： 不涉及。 

        :param limit: The limit of this ListPipelineRunsQuery.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListPipelineRunsQuery.

        **参数解释**： 排序字段名称。 **约束限制**： 不涉及。 **取值范围**： \"start_time\" - 流水线开始时间。 \"update_time\" - 流水线更新时间。 **默认取值**： 不涉及。 

        :return: The sort_key of this ListPipelineRunsQuery.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListPipelineRunsQuery.

        **参数解释**： 排序字段名称。 **约束限制**： 不涉及。 **取值范围**： \"start_time\" - 流水线开始时间。 \"update_time\" - 流水线更新时间。 **默认取值**： 不涉及。 

        :param sort_key: The sort_key of this ListPipelineRunsQuery.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListPipelineRunsQuery.

        **参数解释**： 排序规则。 **约束限制**： 不涉及。 **取值范围**： - asc：按排序字段升序。 - desc：按排序字段降序。 **默认取值**： 不涉及。 

        :return: The sort_dir of this ListPipelineRunsQuery.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListPipelineRunsQuery.

        **参数解释**： 排序规则。 **约束限制**： 不涉及。 **取值范围**： - asc：按排序字段升序。 - desc：按排序字段降序。 **默认取值**： 不涉及。 

        :param sort_dir: The sort_dir of this ListPipelineRunsQuery.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def show_job_details(self):
        r"""Gets the show_job_details of this ListPipelineRunsQuery.

        **参数解释**： 是否返回Job状态详情。 **约束限制**： 不涉及。 **取值范围**： - true：返回Job状态列表。 - false：不返回。 **默认取值**： false。 

        :return: The show_job_details of this ListPipelineRunsQuery.
        :rtype: bool
        """
        return self._show_job_details

    @show_job_details.setter
    def show_job_details(self, show_job_details):
        r"""Sets the show_job_details of this ListPipelineRunsQuery.

        **参数解释**： 是否返回Job状态详情。 **约束限制**： 不涉及。 **取值范围**： - true：返回Job状态列表。 - false：不返回。 **默认取值**： false。 

        :param show_job_details: The show_job_details of this ListPipelineRunsQuery.
        :type show_job_details: bool
        """
        self._show_job_details = show_job_details

    @property
    def stage_id(self):
        r"""Gets the stage_id of this ListPipelineRunsQuery.

        **参数解释**： 阶段ID，用于指定返回Job状态详情的阶段。 **约束限制**： 不涉及。 **取值范围**： 32位字符，仅由数字和字母组成。 **默认取值**： 不涉及，为空时默认取流水线最后一个阶段。 

        :return: The stage_id of this ListPipelineRunsQuery.
        :rtype: str
        """
        return self._stage_id

    @stage_id.setter
    def stage_id(self, stage_id):
        r"""Sets the stage_id of this ListPipelineRunsQuery.

        **参数解释**： 阶段ID，用于指定返回Job状态详情的阶段。 **约束限制**： 不涉及。 **取值范围**： 32位字符，仅由数字和字母组成。 **默认取值**： 不涉及，为空时默认取流水线最后一个阶段。 

        :param stage_id: The stage_id of this ListPipelineRunsQuery.
        :type stage_id: str
        """
        self._stage_id = stage_id

    @property
    def job_id(self):
        r"""Gets the job_id of this ListPipelineRunsQuery.

        **参数解释**： Job ID，仅在show_job_details为true时生效，用于过滤包含指定Job的执行记录。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The job_id of this ListPipelineRunsQuery.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ListPipelineRunsQuery.

        **参数解释**： Job ID，仅在show_job_details为true时生效，用于过滤包含指定Job的执行记录。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param job_id: The job_id of this ListPipelineRunsQuery.
        :type job_id: str
        """
        self._job_id = job_id

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
        if not isinstance(other, ListPipelineRunsQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
