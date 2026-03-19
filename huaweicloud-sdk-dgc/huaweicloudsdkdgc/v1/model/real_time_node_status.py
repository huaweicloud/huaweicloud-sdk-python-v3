# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RealTimeNodeStatus:

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
        'status': 'str',
        'log_path': 'str',
        'node_type': 'str',
        'last_instance_status': 'str',
        'running_data': 'str',
        'extend_counter': 'str'
    }

    attribute_map = {
        'name': 'name',
        'status': 'status',
        'log_path': 'logPath',
        'node_type': 'nodeType',
        'last_instance_status': 'lastInstanceStatus',
        'running_data': 'runningData',
        'extend_counter': 'extendCounter'
    }

    def __init__(self, name=None, status=None, log_path=None, node_type=None, last_instance_status=None, running_data=None, extend_counter=None):
        r"""RealTimeNodeStatus

        The model defined in huaweicloud sdk

        :param name: 节点名称。
        :type name: str
        :param status: 节点状态： - STARTING：启动中 - NORMAL：正常 - EXCEPTION：异常 - STOPPING： 停止中 - STOPPED：停止 - PAUSE: 暂停 - ABNORMAL: 运行异常/失败 - DISABLE: 节点禁用 - OVERLOAD: 繁忙 - INIT: 初始化
        :type status: str
        :param log_path: 节点运行日志路径
        :type log_path: str
        :param node_type: 节点类型
        :type node_type: str
        :param last_instance_status: 上一次实例的执行状态。
        :type last_instance_status: str
        :param running_data: 节点运行时内部存放的部分数据。
        :type running_data: str
        :param extend_counter: 扩展计数器。
        :type extend_counter: str
        """
        
        

        self._name = None
        self._status = None
        self._log_path = None
        self._node_type = None
        self._last_instance_status = None
        self._running_data = None
        self._extend_counter = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if log_path is not None:
            self.log_path = log_path
        if node_type is not None:
            self.node_type = node_type
        if last_instance_status is not None:
            self.last_instance_status = last_instance_status
        if running_data is not None:
            self.running_data = running_data
        if extend_counter is not None:
            self.extend_counter = extend_counter

    @property
    def name(self):
        r"""Gets the name of this RealTimeNodeStatus.

        节点名称。

        :return: The name of this RealTimeNodeStatus.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RealTimeNodeStatus.

        节点名称。

        :param name: The name of this RealTimeNodeStatus.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this RealTimeNodeStatus.

        节点状态： - STARTING：启动中 - NORMAL：正常 - EXCEPTION：异常 - STOPPING： 停止中 - STOPPED：停止 - PAUSE: 暂停 - ABNORMAL: 运行异常/失败 - DISABLE: 节点禁用 - OVERLOAD: 繁忙 - INIT: 初始化

        :return: The status of this RealTimeNodeStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RealTimeNodeStatus.

        节点状态： - STARTING：启动中 - NORMAL：正常 - EXCEPTION：异常 - STOPPING： 停止中 - STOPPED：停止 - PAUSE: 暂停 - ABNORMAL: 运行异常/失败 - DISABLE: 节点禁用 - OVERLOAD: 繁忙 - INIT: 初始化

        :param status: The status of this RealTimeNodeStatus.
        :type status: str
        """
        self._status = status

    @property
    def log_path(self):
        r"""Gets the log_path of this RealTimeNodeStatus.

        节点运行日志路径

        :return: The log_path of this RealTimeNodeStatus.
        :rtype: str
        """
        return self._log_path

    @log_path.setter
    def log_path(self, log_path):
        r"""Sets the log_path of this RealTimeNodeStatus.

        节点运行日志路径

        :param log_path: The log_path of this RealTimeNodeStatus.
        :type log_path: str
        """
        self._log_path = log_path

    @property
    def node_type(self):
        r"""Gets the node_type of this RealTimeNodeStatus.

        节点类型

        :return: The node_type of this RealTimeNodeStatus.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        r"""Sets the node_type of this RealTimeNodeStatus.

        节点类型

        :param node_type: The node_type of this RealTimeNodeStatus.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def last_instance_status(self):
        r"""Gets the last_instance_status of this RealTimeNodeStatus.

        上一次实例的执行状态。

        :return: The last_instance_status of this RealTimeNodeStatus.
        :rtype: str
        """
        return self._last_instance_status

    @last_instance_status.setter
    def last_instance_status(self, last_instance_status):
        r"""Sets the last_instance_status of this RealTimeNodeStatus.

        上一次实例的执行状态。

        :param last_instance_status: The last_instance_status of this RealTimeNodeStatus.
        :type last_instance_status: str
        """
        self._last_instance_status = last_instance_status

    @property
    def running_data(self):
        r"""Gets the running_data of this RealTimeNodeStatus.

        节点运行时内部存放的部分数据。

        :return: The running_data of this RealTimeNodeStatus.
        :rtype: str
        """
        return self._running_data

    @running_data.setter
    def running_data(self, running_data):
        r"""Sets the running_data of this RealTimeNodeStatus.

        节点运行时内部存放的部分数据。

        :param running_data: The running_data of this RealTimeNodeStatus.
        :type running_data: str
        """
        self._running_data = running_data

    @property
    def extend_counter(self):
        r"""Gets the extend_counter of this RealTimeNodeStatus.

        扩展计数器。

        :return: The extend_counter of this RealTimeNodeStatus.
        :rtype: str
        """
        return self._extend_counter

    @extend_counter.setter
    def extend_counter(self, extend_counter):
        r"""Sets the extend_counter of this RealTimeNodeStatus.

        扩展计数器。

        :param extend_counter: The extend_counter of this RealTimeNodeStatus.
        :type extend_counter: str
        """
        self._extend_counter = extend_counter

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
        if not isinstance(other, RealTimeNodeStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
