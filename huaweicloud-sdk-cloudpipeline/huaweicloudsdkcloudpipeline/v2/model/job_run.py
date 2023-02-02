# coding: utf-8

import re
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
        'steps': 'list[StepRun]'
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
        'steps': 'steps'
    }

    def __init__(self, id=None, category=None, sequence=None, _async=None, name=None, identifier=None, depends_on=None, condition=None, resource=None, is_select=None, timeout=None, last_dispatch_id=None, status=None, message=None, start_time=None, end_time=None, steps=None):
        """JobRun

        The model defined in huaweicloud sdk

        :param id: 任务ID
        :type id: str
        :param category: 任务类型
        :type category: str
        :param sequence: 序列号
        :type sequence: int
        :param _async: 是否异步
        :type _async: str
        :param name: 任务名称
        :type name: str
        :param identifier: 任务唯一标识
        :type identifier: str
        :param depends_on: 依赖
        :type depends_on: list[str]
        :param condition: 运行条件
        :type condition: str
        :param resource: 执行资源
        :type resource: str
        :param is_select: 是否选中
        :type is_select: bool
        :param timeout: 任务超时设置
        :type timeout: str
        :param last_dispatch_id: 任务上次下发ID
        :type last_dispatch_id: str
        :param status: 状态
        :type status: str
        :param message: 错误信息
        :type message: str
        :param start_time: 开始时间
        :type start_time: int
        :param end_time: 结束时间
        :type end_time: int
        :param steps: 步骤
        :type steps: list[:class:`huaweicloudsdkcloudpipeline.v2.StepRun`]
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

    @property
    def id(self):
        """Gets the id of this JobRun.

        任务ID

        :return: The id of this JobRun.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JobRun.

        任务ID

        :param id: The id of this JobRun.
        :type id: str
        """
        self._id = id

    @property
    def category(self):
        """Gets the category of this JobRun.

        任务类型

        :return: The category of this JobRun.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this JobRun.

        任务类型

        :param category: The category of this JobRun.
        :type category: str
        """
        self._category = category

    @property
    def sequence(self):
        """Gets the sequence of this JobRun.

        序列号

        :return: The sequence of this JobRun.
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this JobRun.

        序列号

        :param sequence: The sequence of this JobRun.
        :type sequence: int
        """
        self._sequence = sequence

    @property
    def _async(self):
        """Gets the _async of this JobRun.

        是否异步

        :return: The _async of this JobRun.
        :rtype: str
        """
        return self.__async

    @_async.setter
    def _async(self, _async):
        """Sets the _async of this JobRun.

        是否异步

        :param _async: The _async of this JobRun.
        :type _async: str
        """
        self.__async = _async

    @property
    def name(self):
        """Gets the name of this JobRun.

        任务名称

        :return: The name of this JobRun.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobRun.

        任务名称

        :param name: The name of this JobRun.
        :type name: str
        """
        self._name = name

    @property
    def identifier(self):
        """Gets the identifier of this JobRun.

        任务唯一标识

        :return: The identifier of this JobRun.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this JobRun.

        任务唯一标识

        :param identifier: The identifier of this JobRun.
        :type identifier: str
        """
        self._identifier = identifier

    @property
    def depends_on(self):
        """Gets the depends_on of this JobRun.

        依赖

        :return: The depends_on of this JobRun.
        :rtype: list[str]
        """
        return self._depends_on

    @depends_on.setter
    def depends_on(self, depends_on):
        """Sets the depends_on of this JobRun.

        依赖

        :param depends_on: The depends_on of this JobRun.
        :type depends_on: list[str]
        """
        self._depends_on = depends_on

    @property
    def condition(self):
        """Gets the condition of this JobRun.

        运行条件

        :return: The condition of this JobRun.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this JobRun.

        运行条件

        :param condition: The condition of this JobRun.
        :type condition: str
        """
        self._condition = condition

    @property
    def resource(self):
        """Gets the resource of this JobRun.

        执行资源

        :return: The resource of this JobRun.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this JobRun.

        执行资源

        :param resource: The resource of this JobRun.
        :type resource: str
        """
        self._resource = resource

    @property
    def is_select(self):
        """Gets the is_select of this JobRun.

        是否选中

        :return: The is_select of this JobRun.
        :rtype: bool
        """
        return self._is_select

    @is_select.setter
    def is_select(self, is_select):
        """Sets the is_select of this JobRun.

        是否选中

        :param is_select: The is_select of this JobRun.
        :type is_select: bool
        """
        self._is_select = is_select

    @property
    def timeout(self):
        """Gets the timeout of this JobRun.

        任务超时设置

        :return: The timeout of this JobRun.
        :rtype: str
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this JobRun.

        任务超时设置

        :param timeout: The timeout of this JobRun.
        :type timeout: str
        """
        self._timeout = timeout

    @property
    def last_dispatch_id(self):
        """Gets the last_dispatch_id of this JobRun.

        任务上次下发ID

        :return: The last_dispatch_id of this JobRun.
        :rtype: str
        """
        return self._last_dispatch_id

    @last_dispatch_id.setter
    def last_dispatch_id(self, last_dispatch_id):
        """Sets the last_dispatch_id of this JobRun.

        任务上次下发ID

        :param last_dispatch_id: The last_dispatch_id of this JobRun.
        :type last_dispatch_id: str
        """
        self._last_dispatch_id = last_dispatch_id

    @property
    def status(self):
        """Gets the status of this JobRun.

        状态

        :return: The status of this JobRun.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this JobRun.

        状态

        :param status: The status of this JobRun.
        :type status: str
        """
        self._status = status

    @property
    def message(self):
        """Gets the message of this JobRun.

        错误信息

        :return: The message of this JobRun.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this JobRun.

        错误信息

        :param message: The message of this JobRun.
        :type message: str
        """
        self._message = message

    @property
    def start_time(self):
        """Gets the start_time of this JobRun.

        开始时间

        :return: The start_time of this JobRun.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this JobRun.

        开始时间

        :param start_time: The start_time of this JobRun.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this JobRun.

        结束时间

        :return: The end_time of this JobRun.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this JobRun.

        结束时间

        :param end_time: The end_time of this JobRun.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def steps(self):
        """Gets the steps of this JobRun.

        步骤

        :return: The steps of this JobRun.
        :rtype: list[:class:`huaweicloudsdkcloudpipeline.v2.StepRun`]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this JobRun.

        步骤

        :param steps: The steps of this JobRun.
        :type steps: list[:class:`huaweicloudsdkcloudpipeline.v2.StepRun`]
        """
        self._steps = steps

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
