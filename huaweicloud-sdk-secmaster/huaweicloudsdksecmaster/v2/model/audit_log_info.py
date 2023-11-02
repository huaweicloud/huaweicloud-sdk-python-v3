# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuditLogInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_type': 'str',
        'action_id': 'str',
        'action_name': 'str',
        'instance_id': 'str',
        'parent_instance_id': 'str',
        'log_level': 'str',
        'input': 'str',
        'output': 'str',
        'error_msg': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'status': 'str',
        'trigger_type': 'str'
    }

    attribute_map = {
        'instance_type': 'instance_type',
        'action_id': 'action_id',
        'action_name': 'action_name',
        'instance_id': 'instance_id',
        'parent_instance_id': 'parent_instance_id',
        'log_level': 'log_level',
        'input': 'input',
        'output': 'output',
        'error_msg': 'error_msg',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'status': 'status',
        'trigger_type': 'trigger_type'
    }

    def __init__(self, instance_type=None, action_id=None, action_name=None, instance_id=None, parent_instance_id=None, log_level=None, input=None, output=None, error_msg=None, start_time=None, end_time=None, status=None, trigger_type=None):
        """AuditLogInfo

        The model defined in huaweicloud sdk

        :param instance_type: 实例类型（AOP_WORKFLOW--流程, SCRIPT--脚本, PLAYBOOK--剧本）
        :type instance_type: str
        :param action_id: 流程ID
        :type action_id: str
        :param action_name: 流程名称
        :type action_name: str
        :param instance_id: 实例ID
        :type instance_id: str
        :param parent_instance_id: 父节点实例ID
        :type parent_instance_id: str
        :param log_level: 日志级别
        :type log_level: str
        :param input: 输入
        :type input: str
        :param output: 输出
        :type output: str
        :param error_msg: 错误信息
        :type error_msg: str
        :param start_time: 开始时间
        :type start_time: str
        :param end_time: 结束时间
        :type end_time: str
        :param status: 状态。(RUNNING--运行中、FINISHED--成功、FAILED--失败、RETRYING--重试中、TERMINATING--终止中、TERMINATED--已终止)
        :type status: str
        :param trigger_type: 触发类型. TIMER--定时触发, EVENT--事件触发
        :type trigger_type: str
        """
        
        

        self._instance_type = None
        self._action_id = None
        self._action_name = None
        self._instance_id = None
        self._parent_instance_id = None
        self._log_level = None
        self._input = None
        self._output = None
        self._error_msg = None
        self._start_time = None
        self._end_time = None
        self._status = None
        self._trigger_type = None
        self.discriminator = None

        if instance_type is not None:
            self.instance_type = instance_type
        if action_id is not None:
            self.action_id = action_id
        if action_name is not None:
            self.action_name = action_name
        if instance_id is not None:
            self.instance_id = instance_id
        if parent_instance_id is not None:
            self.parent_instance_id = parent_instance_id
        if log_level is not None:
            self.log_level = log_level
        if input is not None:
            self.input = input
        if output is not None:
            self.output = output
        if error_msg is not None:
            self.error_msg = error_msg
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if status is not None:
            self.status = status
        if trigger_type is not None:
            self.trigger_type = trigger_type

    @property
    def instance_type(self):
        """Gets the instance_type of this AuditLogInfo.

        实例类型（AOP_WORKFLOW--流程, SCRIPT--脚本, PLAYBOOK--剧本）

        :return: The instance_type of this AuditLogInfo.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this AuditLogInfo.

        实例类型（AOP_WORKFLOW--流程, SCRIPT--脚本, PLAYBOOK--剧本）

        :param instance_type: The instance_type of this AuditLogInfo.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def action_id(self):
        """Gets the action_id of this AuditLogInfo.

        流程ID

        :return: The action_id of this AuditLogInfo.
        :rtype: str
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        """Sets the action_id of this AuditLogInfo.

        流程ID

        :param action_id: The action_id of this AuditLogInfo.
        :type action_id: str
        """
        self._action_id = action_id

    @property
    def action_name(self):
        """Gets the action_name of this AuditLogInfo.

        流程名称

        :return: The action_name of this AuditLogInfo.
        :rtype: str
        """
        return self._action_name

    @action_name.setter
    def action_name(self, action_name):
        """Sets the action_name of this AuditLogInfo.

        流程名称

        :param action_name: The action_name of this AuditLogInfo.
        :type action_name: str
        """
        self._action_name = action_name

    @property
    def instance_id(self):
        """Gets the instance_id of this AuditLogInfo.

        实例ID

        :return: The instance_id of this AuditLogInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this AuditLogInfo.

        实例ID

        :param instance_id: The instance_id of this AuditLogInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def parent_instance_id(self):
        """Gets the parent_instance_id of this AuditLogInfo.

        父节点实例ID

        :return: The parent_instance_id of this AuditLogInfo.
        :rtype: str
        """
        return self._parent_instance_id

    @parent_instance_id.setter
    def parent_instance_id(self, parent_instance_id):
        """Sets the parent_instance_id of this AuditLogInfo.

        父节点实例ID

        :param parent_instance_id: The parent_instance_id of this AuditLogInfo.
        :type parent_instance_id: str
        """
        self._parent_instance_id = parent_instance_id

    @property
    def log_level(self):
        """Gets the log_level of this AuditLogInfo.

        日志级别

        :return: The log_level of this AuditLogInfo.
        :rtype: str
        """
        return self._log_level

    @log_level.setter
    def log_level(self, log_level):
        """Sets the log_level of this AuditLogInfo.

        日志级别

        :param log_level: The log_level of this AuditLogInfo.
        :type log_level: str
        """
        self._log_level = log_level

    @property
    def input(self):
        """Gets the input of this AuditLogInfo.

        输入

        :return: The input of this AuditLogInfo.
        :rtype: str
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this AuditLogInfo.

        输入

        :param input: The input of this AuditLogInfo.
        :type input: str
        """
        self._input = input

    @property
    def output(self):
        """Gets the output of this AuditLogInfo.

        输出

        :return: The output of this AuditLogInfo.
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this AuditLogInfo.

        输出

        :param output: The output of this AuditLogInfo.
        :type output: str
        """
        self._output = output

    @property
    def error_msg(self):
        """Gets the error_msg of this AuditLogInfo.

        错误信息

        :return: The error_msg of this AuditLogInfo.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this AuditLogInfo.

        错误信息

        :param error_msg: The error_msg of this AuditLogInfo.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def start_time(self):
        """Gets the start_time of this AuditLogInfo.

        开始时间

        :return: The start_time of this AuditLogInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this AuditLogInfo.

        开始时间

        :param start_time: The start_time of this AuditLogInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this AuditLogInfo.

        结束时间

        :return: The end_time of this AuditLogInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this AuditLogInfo.

        结束时间

        :param end_time: The end_time of this AuditLogInfo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def status(self):
        """Gets the status of this AuditLogInfo.

        状态。(RUNNING--运行中、FINISHED--成功、FAILED--失败、RETRYING--重试中、TERMINATING--终止中、TERMINATED--已终止)

        :return: The status of this AuditLogInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AuditLogInfo.

        状态。(RUNNING--运行中、FINISHED--成功、FAILED--失败、RETRYING--重试中、TERMINATING--终止中、TERMINATED--已终止)

        :param status: The status of this AuditLogInfo.
        :type status: str
        """
        self._status = status

    @property
    def trigger_type(self):
        """Gets the trigger_type of this AuditLogInfo.

        触发类型. TIMER--定时触发, EVENT--事件触发

        :return: The trigger_type of this AuditLogInfo.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        """Sets the trigger_type of this AuditLogInfo.

        触发类型. TIMER--定时触发, EVENT--事件触发

        :param trigger_type: The trigger_type of this AuditLogInfo.
        :type trigger_type: str
        """
        self._trigger_type = trigger_type

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
        if not isinstance(other, AuditLogInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
