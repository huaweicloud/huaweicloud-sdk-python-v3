# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StepRun:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'task': 'str',
        'business_type': 'str',
        'inputs': 'list[StepRunInputs]',
        'sequence': 'int',
        'official_task_version': 'str',
        'identifier': 'str',
        'multi_step_editable': 'int',
        'id': 'str',
        'endpoint_ids': 'str',
        'last_dispatch_id': 'str',
        'status': 'str',
        'message': 'str',
        'start_time': 'int',
        'end_time': 'int'
    }

    attribute_map = {
        'name': 'name',
        'task': 'task',
        'business_type': 'business_type',
        'inputs': 'inputs',
        'sequence': 'sequence',
        'official_task_version': 'official_task_version',
        'identifier': 'identifier',
        'multi_step_editable': 'multi_step_editable',
        'id': 'id',
        'endpoint_ids': 'endpoint_ids',
        'last_dispatch_id': 'last_dispatch_id',
        'status': 'status',
        'message': 'message',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, name=None, task=None, business_type=None, inputs=None, sequence=None, official_task_version=None, identifier=None, multi_step_editable=None, id=None, endpoint_ids=None, last_dispatch_id=None, status=None, message=None, start_time=None, end_time=None):
        """StepRun

        The model defined in huaweicloud sdk

        :param name: 步骤名称
        :type name: str
        :param task: 步骤插件
        :type task: str
        :param business_type: 插件业务类型
        :type business_type: str
        :param inputs: 输入参数
        :type inputs: list[:class:`huaweicloudsdkcloudpipeline.v2.StepRunInputs`]
        :param sequence: 序列号
        :type sequence: int
        :param official_task_version: 官方插件版本号
        :type official_task_version: str
        :param identifier: 唯一标识符
        :type identifier: str
        :param multi_step_editable: 是否可编辑
        :type multi_step_editable: int
        :param id: 步骤ID
        :type id: str
        :param endpoint_ids: 扩展点
        :type endpoint_ids: str
        :param last_dispatch_id: 上次下发任务ID
        :type last_dispatch_id: str
        :param status: 状态
        :type status: str
        :param message: 错误消息
        :type message: str
        :param start_time: 开始时间
        :type start_time: int
        :param end_time: 结束时间
        :type end_time: int
        """
        
        

        self._name = None
        self._task = None
        self._business_type = None
        self._inputs = None
        self._sequence = None
        self._official_task_version = None
        self._identifier = None
        self._multi_step_editable = None
        self._id = None
        self._endpoint_ids = None
        self._last_dispatch_id = None
        self._status = None
        self._message = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if task is not None:
            self.task = task
        if business_type is not None:
            self.business_type = business_type
        if inputs is not None:
            self.inputs = inputs
        if sequence is not None:
            self.sequence = sequence
        if official_task_version is not None:
            self.official_task_version = official_task_version
        if identifier is not None:
            self.identifier = identifier
        if multi_step_editable is not None:
            self.multi_step_editable = multi_step_editable
        if id is not None:
            self.id = id
        if endpoint_ids is not None:
            self.endpoint_ids = endpoint_ids
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

    @property
    def name(self):
        """Gets the name of this StepRun.

        步骤名称

        :return: The name of this StepRun.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StepRun.

        步骤名称

        :param name: The name of this StepRun.
        :type name: str
        """
        self._name = name

    @property
    def task(self):
        """Gets the task of this StepRun.

        步骤插件

        :return: The task of this StepRun.
        :rtype: str
        """
        return self._task

    @task.setter
    def task(self, task):
        """Sets the task of this StepRun.

        步骤插件

        :param task: The task of this StepRun.
        :type task: str
        """
        self._task = task

    @property
    def business_type(self):
        """Gets the business_type of this StepRun.

        插件业务类型

        :return: The business_type of this StepRun.
        :rtype: str
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        """Sets the business_type of this StepRun.

        插件业务类型

        :param business_type: The business_type of this StepRun.
        :type business_type: str
        """
        self._business_type = business_type

    @property
    def inputs(self):
        """Gets the inputs of this StepRun.

        输入参数

        :return: The inputs of this StepRun.
        :rtype: list[:class:`huaweicloudsdkcloudpipeline.v2.StepRunInputs`]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this StepRun.

        输入参数

        :param inputs: The inputs of this StepRun.
        :type inputs: list[:class:`huaweicloudsdkcloudpipeline.v2.StepRunInputs`]
        """
        self._inputs = inputs

    @property
    def sequence(self):
        """Gets the sequence of this StepRun.

        序列号

        :return: The sequence of this StepRun.
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this StepRun.

        序列号

        :param sequence: The sequence of this StepRun.
        :type sequence: int
        """
        self._sequence = sequence

    @property
    def official_task_version(self):
        """Gets the official_task_version of this StepRun.

        官方插件版本号

        :return: The official_task_version of this StepRun.
        :rtype: str
        """
        return self._official_task_version

    @official_task_version.setter
    def official_task_version(self, official_task_version):
        """Sets the official_task_version of this StepRun.

        官方插件版本号

        :param official_task_version: The official_task_version of this StepRun.
        :type official_task_version: str
        """
        self._official_task_version = official_task_version

    @property
    def identifier(self):
        """Gets the identifier of this StepRun.

        唯一标识符

        :return: The identifier of this StepRun.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this StepRun.

        唯一标识符

        :param identifier: The identifier of this StepRun.
        :type identifier: str
        """
        self._identifier = identifier

    @property
    def multi_step_editable(self):
        """Gets the multi_step_editable of this StepRun.

        是否可编辑

        :return: The multi_step_editable of this StepRun.
        :rtype: int
        """
        return self._multi_step_editable

    @multi_step_editable.setter
    def multi_step_editable(self, multi_step_editable):
        """Sets the multi_step_editable of this StepRun.

        是否可编辑

        :param multi_step_editable: The multi_step_editable of this StepRun.
        :type multi_step_editable: int
        """
        self._multi_step_editable = multi_step_editable

    @property
    def id(self):
        """Gets the id of this StepRun.

        步骤ID

        :return: The id of this StepRun.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StepRun.

        步骤ID

        :param id: The id of this StepRun.
        :type id: str
        """
        self._id = id

    @property
    def endpoint_ids(self):
        """Gets the endpoint_ids of this StepRun.

        扩展点

        :return: The endpoint_ids of this StepRun.
        :rtype: str
        """
        return self._endpoint_ids

    @endpoint_ids.setter
    def endpoint_ids(self, endpoint_ids):
        """Sets the endpoint_ids of this StepRun.

        扩展点

        :param endpoint_ids: The endpoint_ids of this StepRun.
        :type endpoint_ids: str
        """
        self._endpoint_ids = endpoint_ids

    @property
    def last_dispatch_id(self):
        """Gets the last_dispatch_id of this StepRun.

        上次下发任务ID

        :return: The last_dispatch_id of this StepRun.
        :rtype: str
        """
        return self._last_dispatch_id

    @last_dispatch_id.setter
    def last_dispatch_id(self, last_dispatch_id):
        """Sets the last_dispatch_id of this StepRun.

        上次下发任务ID

        :param last_dispatch_id: The last_dispatch_id of this StepRun.
        :type last_dispatch_id: str
        """
        self._last_dispatch_id = last_dispatch_id

    @property
    def status(self):
        """Gets the status of this StepRun.

        状态

        :return: The status of this StepRun.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this StepRun.

        状态

        :param status: The status of this StepRun.
        :type status: str
        """
        self._status = status

    @property
    def message(self):
        """Gets the message of this StepRun.

        错误消息

        :return: The message of this StepRun.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this StepRun.

        错误消息

        :param message: The message of this StepRun.
        :type message: str
        """
        self._message = message

    @property
    def start_time(self):
        """Gets the start_time of this StepRun.

        开始时间

        :return: The start_time of this StepRun.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this StepRun.

        开始时间

        :param start_time: The start_time of this StepRun.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this StepRun.

        结束时间

        :return: The end_time of this StepRun.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this StepRun.

        结束时间

        :param end_time: The end_time of this StepRun.
        :type end_time: int
        """
        self._end_time = end_time

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
        if not isinstance(other, StepRun):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
