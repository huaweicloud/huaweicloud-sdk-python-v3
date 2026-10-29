# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProcessInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'exe_time': 'str',
        'execute_time': 'str',
        'message': 'str',
        'process': 'str',
        'status': 'str'
    }

    attribute_map = {
        'exe_time': 'exeTime',
        'execute_time': 'executeTime',
        'message': 'message',
        'process': 'process',
        'status': 'status'
    }

    def __init__(self, exe_time=None, execute_time=None, message=None, process=None, status=None):
        r"""ProcessInfo

        The model defined in huaweicloud sdk

        :param exe_time: **参数解释：** 执行时间，单位为秒。 **取值范围：** 不涉及。
        :type exe_time: str
        :param execute_time: **参数解释：** 执行时间，格式为%dm%ds，例如\&quot;6m6s\&quot;。 **取值范围：** 不涉及。
        :type execute_time: str
        :param message: **参数解释：** 执行过程。 **取值范围：** 不涉及。
        :type message: str
        :param process: **参数解释：** 任务执行的进度百分比。 **取值范围：** 不涉及。
        :type process: str
        :param status: **参数解释:** 任务执行状态。 **取值范围:** - quering：初始状态。 - running：执行中。 - success：检查成功。 - failed：检查失败。 - aborted：任务中止。
        :type status: str
        """
        
        

        self._exe_time = None
        self._execute_time = None
        self._message = None
        self._process = None
        self._status = None
        self.discriminator = None

        if exe_time is not None:
            self.exe_time = exe_time
        if execute_time is not None:
            self.execute_time = execute_time
        if message is not None:
            self.message = message
        if process is not None:
            self.process = process
        if status is not None:
            self.status = status

    @property
    def exe_time(self):
        r"""Gets the exe_time of this ProcessInfo.

        **参数解释：** 执行时间，单位为秒。 **取值范围：** 不涉及。

        :return: The exe_time of this ProcessInfo.
        :rtype: str
        """
        return self._exe_time

    @exe_time.setter
    def exe_time(self, exe_time):
        r"""Sets the exe_time of this ProcessInfo.

        **参数解释：** 执行时间，单位为秒。 **取值范围：** 不涉及。

        :param exe_time: The exe_time of this ProcessInfo.
        :type exe_time: str
        """
        self._exe_time = exe_time

    @property
    def execute_time(self):
        r"""Gets the execute_time of this ProcessInfo.

        **参数解释：** 执行时间，格式为%dm%ds，例如\"6m6s\"。 **取值范围：** 不涉及。

        :return: The execute_time of this ProcessInfo.
        :rtype: str
        """
        return self._execute_time

    @execute_time.setter
    def execute_time(self, execute_time):
        r"""Sets the execute_time of this ProcessInfo.

        **参数解释：** 执行时间，格式为%dm%ds，例如\"6m6s\"。 **取值范围：** 不涉及。

        :param execute_time: The execute_time of this ProcessInfo.
        :type execute_time: str
        """
        self._execute_time = execute_time

    @property
    def message(self):
        r"""Gets the message of this ProcessInfo.

        **参数解释：** 执行过程。 **取值范围：** 不涉及。

        :return: The message of this ProcessInfo.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ProcessInfo.

        **参数解释：** 执行过程。 **取值范围：** 不涉及。

        :param message: The message of this ProcessInfo.
        :type message: str
        """
        self._message = message

    @property
    def process(self):
        r"""Gets the process of this ProcessInfo.

        **参数解释：** 任务执行的进度百分比。 **取值范围：** 不涉及。

        :return: The process of this ProcessInfo.
        :rtype: str
        """
        return self._process

    @process.setter
    def process(self, process):
        r"""Sets the process of this ProcessInfo.

        **参数解释：** 任务执行的进度百分比。 **取值范围：** 不涉及。

        :param process: The process of this ProcessInfo.
        :type process: str
        """
        self._process = process

    @property
    def status(self):
        r"""Gets the status of this ProcessInfo.

        **参数解释:** 任务执行状态。 **取值范围:** - quering：初始状态。 - running：执行中。 - success：检查成功。 - failed：检查失败。 - aborted：任务中止。

        :return: The status of this ProcessInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ProcessInfo.

        **参数解释:** 任务执行状态。 **取值范围:** - quering：初始状态。 - running：执行中。 - success：检查成功。 - failed：检查失败。 - aborted：任务中止。

        :param status: The status of this ProcessInfo.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ProcessInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
