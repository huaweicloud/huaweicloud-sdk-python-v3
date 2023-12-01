# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TransferTask:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_name': 'str',
        'state': 'str',
        'destination_type': 'str',
        'create_time': 'int',
        'last_transfer_timestamp': 'int'
    }

    attribute_map = {
        'task_name': 'task_name',
        'state': 'state',
        'destination_type': 'destination_type',
        'create_time': 'create_time',
        'last_transfer_timestamp': 'last_transfer_timestamp'
    }

    def __init__(self, task_name=None, state=None, destination_type=None, create_time=None, last_transfer_timestamp=None):
        """TransferTask

        The model defined in huaweicloud sdk

        :param task_name: 转储任务名称。
        :type task_name: str
        :param state: 转储任务状态。  - ERROR：错误。 - STARTING：启动中。 - PAUSED：已停止。 - RUNNING：运行中。 - DELETE：已删除。 - ABNORMAL：异常。
        :type state: str
        :param destination_type: 转储任务类型。  - OBS：转储到OBS。 - MRS：转储到MRS。 - DLI：转储到DLI。 - CLOUDTABLE：转储到CloudTable。 - DWS：转储到DWS。
        :type destination_type: str
        :param create_time: 转储任务创建时间。
        :type create_time: int
        :param last_transfer_timestamp: 转储任务最近一次转储时间。
        :type last_transfer_timestamp: int
        """
        
        

        self._task_name = None
        self._state = None
        self._destination_type = None
        self._create_time = None
        self._last_transfer_timestamp = None
        self.discriminator = None

        if task_name is not None:
            self.task_name = task_name
        if state is not None:
            self.state = state
        if destination_type is not None:
            self.destination_type = destination_type
        if create_time is not None:
            self.create_time = create_time
        if last_transfer_timestamp is not None:
            self.last_transfer_timestamp = last_transfer_timestamp

    @property
    def task_name(self):
        """Gets the task_name of this TransferTask.

        转储任务名称。

        :return: The task_name of this TransferTask.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this TransferTask.

        转储任务名称。

        :param task_name: The task_name of this TransferTask.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def state(self):
        """Gets the state of this TransferTask.

        转储任务状态。  - ERROR：错误。 - STARTING：启动中。 - PAUSED：已停止。 - RUNNING：运行中。 - DELETE：已删除。 - ABNORMAL：异常。

        :return: The state of this TransferTask.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this TransferTask.

        转储任务状态。  - ERROR：错误。 - STARTING：启动中。 - PAUSED：已停止。 - RUNNING：运行中。 - DELETE：已删除。 - ABNORMAL：异常。

        :param state: The state of this TransferTask.
        :type state: str
        """
        self._state = state

    @property
    def destination_type(self):
        """Gets the destination_type of this TransferTask.

        转储任务类型。  - OBS：转储到OBS。 - MRS：转储到MRS。 - DLI：转储到DLI。 - CLOUDTABLE：转储到CloudTable。 - DWS：转储到DWS。

        :return: The destination_type of this TransferTask.
        :rtype: str
        """
        return self._destination_type

    @destination_type.setter
    def destination_type(self, destination_type):
        """Sets the destination_type of this TransferTask.

        转储任务类型。  - OBS：转储到OBS。 - MRS：转储到MRS。 - DLI：转储到DLI。 - CLOUDTABLE：转储到CloudTable。 - DWS：转储到DWS。

        :param destination_type: The destination_type of this TransferTask.
        :type destination_type: str
        """
        self._destination_type = destination_type

    @property
    def create_time(self):
        """Gets the create_time of this TransferTask.

        转储任务创建时间。

        :return: The create_time of this TransferTask.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this TransferTask.

        转储任务创建时间。

        :param create_time: The create_time of this TransferTask.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def last_transfer_timestamp(self):
        """Gets the last_transfer_timestamp of this TransferTask.

        转储任务最近一次转储时间。

        :return: The last_transfer_timestamp of this TransferTask.
        :rtype: int
        """
        return self._last_transfer_timestamp

    @last_transfer_timestamp.setter
    def last_transfer_timestamp(self, last_transfer_timestamp):
        """Sets the last_transfer_timestamp of this TransferTask.

        转储任务最近一次转储时间。

        :param last_transfer_timestamp: The last_transfer_timestamp of this TransferTask.
        :type last_transfer_timestamp: int
        """
        self._last_transfer_timestamp = last_transfer_timestamp

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
        if not isinstance(other, TransferTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
