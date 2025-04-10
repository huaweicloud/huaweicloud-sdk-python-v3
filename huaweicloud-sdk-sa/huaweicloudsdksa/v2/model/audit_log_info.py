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
        r"""AuditLogInfo

        The model defined in huaweicloud sdk

        :param instance_type: instance type.
        :type instance_type: str
        :param action_id: Action id.
        :type action_id: str
        :param action_name: action name.
        :type action_name: str
        :param instance_id: Instance id.
        :type instance_id: str
        :param parent_instance_id: parent instance id.
        :type parent_instance_id: str
        :param log_level: log level.
        :type log_level: str
        :param input: input.
        :type input: str
        :param output: output.
        :type output: str
        :param error_msg: error_msg.
        :type error_msg: str
        :param start_time: start_time.
        :type start_time: str
        :param end_time: end_time.
        :type end_time: str
        :param status: status.
        :type status: str
        :param trigger_type: trigger type.
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
        r"""Gets the instance_type of this AuditLogInfo.

        instance type.

        :return: The instance_type of this AuditLogInfo.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        r"""Sets the instance_type of this AuditLogInfo.

        instance type.

        :param instance_type: The instance_type of this AuditLogInfo.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def action_id(self):
        r"""Gets the action_id of this AuditLogInfo.

        Action id.

        :return: The action_id of this AuditLogInfo.
        :rtype: str
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        r"""Sets the action_id of this AuditLogInfo.

        Action id.

        :param action_id: The action_id of this AuditLogInfo.
        :type action_id: str
        """
        self._action_id = action_id

    @property
    def action_name(self):
        r"""Gets the action_name of this AuditLogInfo.

        action name.

        :return: The action_name of this AuditLogInfo.
        :rtype: str
        """
        return self._action_name

    @action_name.setter
    def action_name(self, action_name):
        r"""Sets the action_name of this AuditLogInfo.

        action name.

        :param action_name: The action_name of this AuditLogInfo.
        :type action_name: str
        """
        self._action_name = action_name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this AuditLogInfo.

        Instance id.

        :return: The instance_id of this AuditLogInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this AuditLogInfo.

        Instance id.

        :param instance_id: The instance_id of this AuditLogInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def parent_instance_id(self):
        r"""Gets the parent_instance_id of this AuditLogInfo.

        parent instance id.

        :return: The parent_instance_id of this AuditLogInfo.
        :rtype: str
        """
        return self._parent_instance_id

    @parent_instance_id.setter
    def parent_instance_id(self, parent_instance_id):
        r"""Sets the parent_instance_id of this AuditLogInfo.

        parent instance id.

        :param parent_instance_id: The parent_instance_id of this AuditLogInfo.
        :type parent_instance_id: str
        """
        self._parent_instance_id = parent_instance_id

    @property
    def log_level(self):
        r"""Gets the log_level of this AuditLogInfo.

        log level.

        :return: The log_level of this AuditLogInfo.
        :rtype: str
        """
        return self._log_level

    @log_level.setter
    def log_level(self, log_level):
        r"""Sets the log_level of this AuditLogInfo.

        log level.

        :param log_level: The log_level of this AuditLogInfo.
        :type log_level: str
        """
        self._log_level = log_level

    @property
    def input(self):
        r"""Gets the input of this AuditLogInfo.

        input.

        :return: The input of this AuditLogInfo.
        :rtype: str
        """
        return self._input

    @input.setter
    def input(self, input):
        r"""Sets the input of this AuditLogInfo.

        input.

        :param input: The input of this AuditLogInfo.
        :type input: str
        """
        self._input = input

    @property
    def output(self):
        r"""Gets the output of this AuditLogInfo.

        output.

        :return: The output of this AuditLogInfo.
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        r"""Sets the output of this AuditLogInfo.

        output.

        :param output: The output of this AuditLogInfo.
        :type output: str
        """
        self._output = output

    @property
    def error_msg(self):
        r"""Gets the error_msg of this AuditLogInfo.

        error_msg.

        :return: The error_msg of this AuditLogInfo.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this AuditLogInfo.

        error_msg.

        :param error_msg: The error_msg of this AuditLogInfo.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def start_time(self):
        r"""Gets the start_time of this AuditLogInfo.

        start_time.

        :return: The start_time of this AuditLogInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this AuditLogInfo.

        start_time.

        :param start_time: The start_time of this AuditLogInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this AuditLogInfo.

        end_time.

        :return: The end_time of this AuditLogInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this AuditLogInfo.

        end_time.

        :param end_time: The end_time of this AuditLogInfo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def status(self):
        r"""Gets the status of this AuditLogInfo.

        status.

        :return: The status of this AuditLogInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AuditLogInfo.

        status.

        :param status: The status of this AuditLogInfo.
        :type status: str
        """
        self._status = status

    @property
    def trigger_type(self):
        r"""Gets the trigger_type of this AuditLogInfo.

        trigger type.

        :return: The trigger_type of this AuditLogInfo.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        r"""Sets the trigger_type of this AuditLogInfo.

        trigger type.

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
