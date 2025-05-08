# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExcutionStep:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'execution_step_id': 'str',
        'action': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'message': 'str',
        'name': 'str',
        'status': 'str',
        'inputs': 'list[ExcutionStepInputs]',
        'outputs': 'list[ExcutionStepInputs]',
        'properties': 'dict(str, str)'
    }

    attribute_map = {
        'execution_step_id': 'execution_step_id',
        'action': 'action',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'message': 'message',
        'name': 'name',
        'status': 'status',
        'inputs': 'inputs',
        'outputs': 'outputs',
        'properties': 'properties'
    }

    def __init__(self, execution_step_id=None, action=None, start_time=None, end_time=None, message=None, name=None, status=None, inputs=None, outputs=None, properties=None):
        r"""ExcutionStep

        The model defined in huaweicloud sdk

        :param execution_step_id: 工单步骤id
        :type execution_step_id: str
        :param action: 原子能力action
        :type action: str
        :param start_time: 工单步骤开始时间
        :type start_time: int
        :param end_time: 工单步骤结束时间
        :type end_time: int
        :param message: 工单步骤执行信息
        :type message: str
        :param name: 工单步骤名称
        :type name: str
        :param status: 工单步骤执行状态
        :type status: str
        :param inputs: 步骤输入参数
        :type inputs: list[:class:`huaweicloudsdkcoc.v1.ExcutionStepInputs`]
        :param outputs: 步骤输出参数
        :type outputs: list[:class:`huaweicloudsdkcoc.v1.ExcutionStepInputs`]
        :param properties: 工单步骤附加属性，map形式存储，如展示内网ip，则为{\&quot;fixed_ip\&quot;: \&quot;192.168.1.228\&quot;}
        :type properties: dict(str, str)
        """
        
        

        self._execution_step_id = None
        self._action = None
        self._start_time = None
        self._end_time = None
        self._message = None
        self._name = None
        self._status = None
        self._inputs = None
        self._outputs = None
        self._properties = None
        self.discriminator = None

        if execution_step_id is not None:
            self.execution_step_id = execution_step_id
        if action is not None:
            self.action = action
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if message is not None:
            self.message = message
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if inputs is not None:
            self.inputs = inputs
        if outputs is not None:
            self.outputs = outputs
        if properties is not None:
            self.properties = properties

    @property
    def execution_step_id(self):
        r"""Gets the execution_step_id of this ExcutionStep.

        工单步骤id

        :return: The execution_step_id of this ExcutionStep.
        :rtype: str
        """
        return self._execution_step_id

    @execution_step_id.setter
    def execution_step_id(self, execution_step_id):
        r"""Sets the execution_step_id of this ExcutionStep.

        工单步骤id

        :param execution_step_id: The execution_step_id of this ExcutionStep.
        :type execution_step_id: str
        """
        self._execution_step_id = execution_step_id

    @property
    def action(self):
        r"""Gets the action of this ExcutionStep.

        原子能力action

        :return: The action of this ExcutionStep.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ExcutionStep.

        原子能力action

        :param action: The action of this ExcutionStep.
        :type action: str
        """
        self._action = action

    @property
    def start_time(self):
        r"""Gets the start_time of this ExcutionStep.

        工单步骤开始时间

        :return: The start_time of this ExcutionStep.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ExcutionStep.

        工单步骤开始时间

        :param start_time: The start_time of this ExcutionStep.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ExcutionStep.

        工单步骤结束时间

        :return: The end_time of this ExcutionStep.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ExcutionStep.

        工单步骤结束时间

        :param end_time: The end_time of this ExcutionStep.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def message(self):
        r"""Gets the message of this ExcutionStep.

        工单步骤执行信息

        :return: The message of this ExcutionStep.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ExcutionStep.

        工单步骤执行信息

        :param message: The message of this ExcutionStep.
        :type message: str
        """
        self._message = message

    @property
    def name(self):
        r"""Gets the name of this ExcutionStep.

        工单步骤名称

        :return: The name of this ExcutionStep.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ExcutionStep.

        工单步骤名称

        :param name: The name of this ExcutionStep.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ExcutionStep.

        工单步骤执行状态

        :return: The status of this ExcutionStep.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ExcutionStep.

        工单步骤执行状态

        :param status: The status of this ExcutionStep.
        :type status: str
        """
        self._status = status

    @property
    def inputs(self):
        r"""Gets the inputs of this ExcutionStep.

        步骤输入参数

        :return: The inputs of this ExcutionStep.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.ExcutionStepInputs`]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        r"""Sets the inputs of this ExcutionStep.

        步骤输入参数

        :param inputs: The inputs of this ExcutionStep.
        :type inputs: list[:class:`huaweicloudsdkcoc.v1.ExcutionStepInputs`]
        """
        self._inputs = inputs

    @property
    def outputs(self):
        r"""Gets the outputs of this ExcutionStep.

        步骤输出参数

        :return: The outputs of this ExcutionStep.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.ExcutionStepInputs`]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        r"""Sets the outputs of this ExcutionStep.

        步骤输出参数

        :param outputs: The outputs of this ExcutionStep.
        :type outputs: list[:class:`huaweicloudsdkcoc.v1.ExcutionStepInputs`]
        """
        self._outputs = outputs

    @property
    def properties(self):
        r"""Gets the properties of this ExcutionStep.

        工单步骤附加属性，map形式存储，如展示内网ip，则为{\"fixed_ip\": \"192.168.1.228\"}

        :return: The properties of this ExcutionStep.
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this ExcutionStep.

        工单步骤附加属性，map形式存储，如展示内网ip，则为{\"fixed_ip\": \"192.168.1.228\"}

        :param properties: The properties of this ExcutionStep.
        :type properties: dict(str, str)
        """
        self._properties = properties

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
        if not isinstance(other, ExcutionStep):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
