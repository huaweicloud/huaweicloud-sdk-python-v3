# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobRun:

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
        'category': 'str',
        'sequence': 'int',
        '_async': 'str',
        'name': 'str',
        'identifier': 'str',
        'depends_on': 'list[str]',
        'condition': 'str',
        'resource': 'str',
        'is_select': 'bool',
        'timeout': 'str',
        'last_dispatch_id': 'str',
        'status': 'str',
        'message': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'steps': 'list[StepRun]',
        'exec_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'category': 'category',
        'sequence': 'sequence',
        '_async': 'async',
        'name': 'name',
        'identifier': 'identifier',
        'depends_on': 'depends_on',
        'condition': 'condition',
        'resource': 'resource',
        'is_select': 'is_select',
        'timeout': 'timeout',
        'last_dispatch_id': 'last_dispatch_id',
        'status': 'status',
        'message': 'message',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'steps': 'steps',
        'exec_id': 'exec_id'
    }

    def __init__(self, id=None, category=None, sequence=None, _async=None, name=None, identifier=None, depends_on=None, condition=None, resource=None, is_select=None, timeout=None, last_dispatch_id=None, status=None, message=None, start_time=None, end_time=None, steps=None, exec_id=None):
        r"""JobRun

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 任务ID。 **取值范围**： 不涉及。 
        :type id: str
        :param category: **参数解释**： 任务类型。 **取值范围**： 不涉及。 
        :type category: str
        :param sequence: **参数解释**： 序列号。 **取值范围**： 不涉及。 
        :type sequence: int
        :param _async: **参数解释**： 是否异步。 **取值范围**： - true：异步。 - false：非异步。 
        :type _async: str
        :param name: **参数解释**： 任务名称。 **取值范围**： 不涉及。 
        :type name: str
        :param identifier: **参数解释**： 任务唯一标识。 **取值范围**： 不涉及。 
        :type identifier: str
        :param depends_on: **参数解释**： 依赖。 **取值范围**： 不涉及。 
        :type depends_on: list[str]
        :param condition: **参数解释**： 运行条件。 **取值范围**： 不涉及。 
        :type condition: str
        :param resource: **参数解释**： 执行资源。 **取值范围**： 不涉及。 
        :type resource: str
        :param is_select: **参数解释**： 是否选中。 **取值范围**： - true：选中。 - false：未选中。 
        :type is_select: bool
        :param timeout: **参数解释**： 任务超时设置。 **取值范围**： 不涉及。 
        :type timeout: str
        :param last_dispatch_id: **参数解释**： 任务上次下发ID。 **取值范围**： 不涉及。 
        :type last_dispatch_id: str
        :param status: **参数解释**： 状态。 **取值范围**： - INIT：初始化。 - QUEUED：排队。 - RUNNING：运行中。 - CANCELED：取消。 - COMPLETED：已完成。 - FAILED：失败。 - SKIPPED：跳过。 - IGNORED：忽略。 - PAUSED：暂停。 - SUSPEND：挂起。 - ASYNC_RUNNING：异步运行。 - ASYNC_FAILED：异步失败。 - UNSELECTED：未选择。 - REDISPATCH：重新调度。 
        :type status: str
        :param message: **参数解释**： 错误信息。 **取值范围**： 不涉及。 
        :type message: str
        :param start_time: **参数解释**： 任务开始时间。 **取值范围**： 不涉及。 
        :type start_time: int
        :param end_time: **参数解释**： 任务结束时间。 **取值范围**： 不涉及。 
        :type end_time: int
        :param steps: **参数解释**： 步骤。 **取值范围**： 不涉及。 
        :type steps: list[:class:`huaweicloudsdkcodeartspipeline.v2.StepRun`]
        :param exec_id: **参数解释**： 任务执行ID。 **取值范围**： 不涉及。 
        :type exec_id: str
        """
        
        

        self._id = None
        self._category = None
        self._sequence = None
        self.__async = None
        self._name = None
        self._identifier = None
        self._depends_on = None
        self._condition = None
        self._resource = None
        self._is_select = None
        self._timeout = None
        self._last_dispatch_id = None
        self._status = None
        self._message = None
        self._start_time = None
        self._end_time = None
        self._steps = None
        self._exec_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if category is not None:
            self.category = category
        if sequence is not None:
            self.sequence = sequence
        if _async is not None:
            self._async = _async
        if name is not None:
            self.name = name
        if identifier is not None:
            self.identifier = identifier
        if depends_on is not None:
            self.depends_on = depends_on
        if condition is not None:
            self.condition = condition
        if resource is not None:
            self.resource = resource
        if is_select is not None:
            self.is_select = is_select
        if timeout is not None:
            self.timeout = timeout
        if last_dispatch_id is not None:
            self.last_dispatch_id = last_dispatch_id
        if status is not None:
            self.status = status
        if message is not None:
            self.message = message
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if steps is not None:
            self.steps = steps
        if exec_id is not None:
            self.exec_id = exec_id

    @property
    def id(self):
        r"""Gets the id of this JobRun.

        **参数解释**： 任务ID。 **取值范围**： 不涉及。 

        :return: The id of this JobRun.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this JobRun.

        **参数解释**： 任务ID。 **取值范围**： 不涉及。 

        :param id: The id of this JobRun.
        :type id: str
        """
        self._id = id

    @property
    def category(self):
        r"""Gets the category of this JobRun.

        **参数解释**： 任务类型。 **取值范围**： 不涉及。 

        :return: The category of this JobRun.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this JobRun.

        **参数解释**： 任务类型。 **取值范围**： 不涉及。 

        :param category: The category of this JobRun.
        :type category: str
        """
        self._category = category

    @property
    def sequence(self):
        r"""Gets the sequence of this JobRun.

        **参数解释**： 序列号。 **取值范围**： 不涉及。 

        :return: The sequence of this JobRun.
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        r"""Sets the sequence of this JobRun.

        **参数解释**： 序列号。 **取值范围**： 不涉及。 

        :param sequence: The sequence of this JobRun.
        :type sequence: int
        """
        self._sequence = sequence

    @property
    def _async(self):
        r"""Gets the _async of this JobRun.

        **参数解释**： 是否异步。 **取值范围**： - true：异步。 - false：非异步。 

        :return: The _async of this JobRun.
        :rtype: str
        """
        return self.__async

    @_async.setter
    def _async(self, _async):
        r"""Sets the _async of this JobRun.

        **参数解释**： 是否异步。 **取值范围**： - true：异步。 - false：非异步。 

        :param _async: The _async of this JobRun.
        :type _async: str
        """
        self.__async = _async

    @property
    def name(self):
        r"""Gets the name of this JobRun.

        **参数解释**： 任务名称。 **取值范围**： 不涉及。 

        :return: The name of this JobRun.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this JobRun.

        **参数解释**： 任务名称。 **取值范围**： 不涉及。 

        :param name: The name of this JobRun.
        :type name: str
        """
        self._name = name

    @property
    def identifier(self):
        r"""Gets the identifier of this JobRun.

        **参数解释**： 任务唯一标识。 **取值范围**： 不涉及。 

        :return: The identifier of this JobRun.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        r"""Sets the identifier of this JobRun.

        **参数解释**： 任务唯一标识。 **取值范围**： 不涉及。 

        :param identifier: The identifier of this JobRun.
        :type identifier: str
        """
        self._identifier = identifier

    @property
    def depends_on(self):
        r"""Gets the depends_on of this JobRun.

        **参数解释**： 依赖。 **取值范围**： 不涉及。 

        :return: The depends_on of this JobRun.
        :rtype: list[str]
        """
        return self._depends_on

    @depends_on.setter
    def depends_on(self, depends_on):
        r"""Sets the depends_on of this JobRun.

        **参数解释**： 依赖。 **取值范围**： 不涉及。 

        :param depends_on: The depends_on of this JobRun.
        :type depends_on: list[str]
        """
        self._depends_on = depends_on

    @property
    def condition(self):
        r"""Gets the condition of this JobRun.

        **参数解释**： 运行条件。 **取值范围**： 不涉及。 

        :return: The condition of this JobRun.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        r"""Sets the condition of this JobRun.

        **参数解释**： 运行条件。 **取值范围**： 不涉及。 

        :param condition: The condition of this JobRun.
        :type condition: str
        """
        self._condition = condition

    @property
    def resource(self):
        r"""Gets the resource of this JobRun.

        **参数解释**： 执行资源。 **取值范围**： 不涉及。 

        :return: The resource of this JobRun.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        r"""Sets the resource of this JobRun.

        **参数解释**： 执行资源。 **取值范围**： 不涉及。 

        :param resource: The resource of this JobRun.
        :type resource: str
        """
        self._resource = resource

    @property
    def is_select(self):
        r"""Gets the is_select of this JobRun.

        **参数解释**： 是否选中。 **取值范围**： - true：选中。 - false：未选中。 

        :return: The is_select of this JobRun.
        :rtype: bool
        """
        return self._is_select

    @is_select.setter
    def is_select(self, is_select):
        r"""Sets the is_select of this JobRun.

        **参数解释**： 是否选中。 **取值范围**： - true：选中。 - false：未选中。 

        :param is_select: The is_select of this JobRun.
        :type is_select: bool
        """
        self._is_select = is_select

    @property
    def timeout(self):
        r"""Gets the timeout of this JobRun.

        **参数解释**： 任务超时设置。 **取值范围**： 不涉及。 

        :return: The timeout of this JobRun.
        :rtype: str
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        r"""Sets the timeout of this JobRun.

        **参数解释**： 任务超时设置。 **取值范围**： 不涉及。 

        :param timeout: The timeout of this JobRun.
        :type timeout: str
        """
        self._timeout = timeout

    @property
    def last_dispatch_id(self):
        r"""Gets the last_dispatch_id of this JobRun.

        **参数解释**： 任务上次下发ID。 **取值范围**： 不涉及。 

        :return: The last_dispatch_id of this JobRun.
        :rtype: str
        """
        return self._last_dispatch_id

    @last_dispatch_id.setter
    def last_dispatch_id(self, last_dispatch_id):
        r"""Sets the last_dispatch_id of this JobRun.

        **参数解释**： 任务上次下发ID。 **取值范围**： 不涉及。 

        :param last_dispatch_id: The last_dispatch_id of this JobRun.
        :type last_dispatch_id: str
        """
        self._last_dispatch_id = last_dispatch_id

    @property
    def status(self):
        r"""Gets the status of this JobRun.

        **参数解释**： 状态。 **取值范围**： - INIT：初始化。 - QUEUED：排队。 - RUNNING：运行中。 - CANCELED：取消。 - COMPLETED：已完成。 - FAILED：失败。 - SKIPPED：跳过。 - IGNORED：忽略。 - PAUSED：暂停。 - SUSPEND：挂起。 - ASYNC_RUNNING：异步运行。 - ASYNC_FAILED：异步失败。 - UNSELECTED：未选择。 - REDISPATCH：重新调度。 

        :return: The status of this JobRun.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this JobRun.

        **参数解释**： 状态。 **取值范围**： - INIT：初始化。 - QUEUED：排队。 - RUNNING：运行中。 - CANCELED：取消。 - COMPLETED：已完成。 - FAILED：失败。 - SKIPPED：跳过。 - IGNORED：忽略。 - PAUSED：暂停。 - SUSPEND：挂起。 - ASYNC_RUNNING：异步运行。 - ASYNC_FAILED：异步失败。 - UNSELECTED：未选择。 - REDISPATCH：重新调度。 

        :param status: The status of this JobRun.
        :type status: str
        """
        self._status = status

    @property
    def message(self):
        r"""Gets the message of this JobRun.

        **参数解释**： 错误信息。 **取值范围**： 不涉及。 

        :return: The message of this JobRun.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this JobRun.

        **参数解释**： 错误信息。 **取值范围**： 不涉及。 

        :param message: The message of this JobRun.
        :type message: str
        """
        self._message = message

    @property
    def start_time(self):
        r"""Gets the start_time of this JobRun.

        **参数解释**： 任务开始时间。 **取值范围**： 不涉及。 

        :return: The start_time of this JobRun.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this JobRun.

        **参数解释**： 任务开始时间。 **取值范围**： 不涉及。 

        :param start_time: The start_time of this JobRun.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this JobRun.

        **参数解释**： 任务结束时间。 **取值范围**： 不涉及。 

        :return: The end_time of this JobRun.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this JobRun.

        **参数解释**： 任务结束时间。 **取值范围**： 不涉及。 

        :param end_time: The end_time of this JobRun.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def steps(self):
        r"""Gets the steps of this JobRun.

        **参数解释**： 步骤。 **取值范围**： 不涉及。 

        :return: The steps of this JobRun.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.StepRun`]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        r"""Sets the steps of this JobRun.

        **参数解释**： 步骤。 **取值范围**： 不涉及。 

        :param steps: The steps of this JobRun.
        :type steps: list[:class:`huaweicloudsdkcodeartspipeline.v2.StepRun`]
        """
        self._steps = steps

    @property
    def exec_id(self):
        r"""Gets the exec_id of this JobRun.

        **参数解释**： 任务执行ID。 **取值范围**： 不涉及。 

        :return: The exec_id of this JobRun.
        :rtype: str
        """
        return self._exec_id

    @exec_id.setter
    def exec_id(self, exec_id):
        r"""Sets the exec_id of this JobRun.

        **参数解释**： 任务执行ID。 **取值范围**： 不涉及。 

        :param exec_id: The exec_id of this JobRun.
        :type exec_id: str
        """
        self._exec_id = exec_id

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
        if not isinstance(other, JobRun):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
