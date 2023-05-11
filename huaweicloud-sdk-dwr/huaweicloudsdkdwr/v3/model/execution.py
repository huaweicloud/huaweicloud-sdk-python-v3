# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Execution:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'graph_urn': 'str',
        'execution_urn': 'str',
        'started_at': 'str',
        'execution_type': 'str',
        'stopped_at': 'str',
        'execution_state': 'str',
        'execution_name': 'str'
    }

    attribute_map = {
        'graph_urn': 'graph_urn',
        'execution_urn': 'execution_urn',
        'started_at': 'started_at',
        'execution_type': 'execution_type',
        'stopped_at': 'stopped_at',
        'execution_state': 'execution_state',
        'execution_name': 'execution_name'
    }

    def __init__(self, graph_urn=None, execution_urn=None, started_at=None, execution_type=None, stopped_at=None, execution_state=None, execution_name=None):
        """Execution

        The model defined in huaweicloud sdk

        :param graph_urn: 工作流URN
        :type graph_urn: str
        :param execution_urn: 工作流实例URN
        :type execution_urn: str
        :param started_at: 工作流实例启动时间
        :type started_at: str
        :param execution_type: 工作流执行方式。APICALL代表为通过API方式触发。
        :type execution_type: str
        :param stopped_at: 工作流停止时间。
        :type stopped_at: str
        :param execution_state: 工作流运行状态。success,fail,running,timeout,cancel
        :type execution_state: str
        :param execution_name: 工作流名称。
        :type execution_name: str
        """
        
        

        self._graph_urn = None
        self._execution_urn = None
        self._started_at = None
        self._execution_type = None
        self._stopped_at = None
        self._execution_state = None
        self._execution_name = None
        self.discriminator = None

        if graph_urn is not None:
            self.graph_urn = graph_urn
        if execution_urn is not None:
            self.execution_urn = execution_urn
        if started_at is not None:
            self.started_at = started_at
        if execution_type is not None:
            self.execution_type = execution_type
        if stopped_at is not None:
            self.stopped_at = stopped_at
        if execution_state is not None:
            self.execution_state = execution_state
        if execution_name is not None:
            self.execution_name = execution_name

    @property
    def graph_urn(self):
        """Gets the graph_urn of this Execution.

        工作流URN

        :return: The graph_urn of this Execution.
        :rtype: str
        """
        return self._graph_urn

    @graph_urn.setter
    def graph_urn(self, graph_urn):
        """Sets the graph_urn of this Execution.

        工作流URN

        :param graph_urn: The graph_urn of this Execution.
        :type graph_urn: str
        """
        self._graph_urn = graph_urn

    @property
    def execution_urn(self):
        """Gets the execution_urn of this Execution.

        工作流实例URN

        :return: The execution_urn of this Execution.
        :rtype: str
        """
        return self._execution_urn

    @execution_urn.setter
    def execution_urn(self, execution_urn):
        """Sets the execution_urn of this Execution.

        工作流实例URN

        :param execution_urn: The execution_urn of this Execution.
        :type execution_urn: str
        """
        self._execution_urn = execution_urn

    @property
    def started_at(self):
        """Gets the started_at of this Execution.

        工作流实例启动时间

        :return: The started_at of this Execution.
        :rtype: str
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this Execution.

        工作流实例启动时间

        :param started_at: The started_at of this Execution.
        :type started_at: str
        """
        self._started_at = started_at

    @property
    def execution_type(self):
        """Gets the execution_type of this Execution.

        工作流执行方式。APICALL代表为通过API方式触发。

        :return: The execution_type of this Execution.
        :rtype: str
        """
        return self._execution_type

    @execution_type.setter
    def execution_type(self, execution_type):
        """Sets the execution_type of this Execution.

        工作流执行方式。APICALL代表为通过API方式触发。

        :param execution_type: The execution_type of this Execution.
        :type execution_type: str
        """
        self._execution_type = execution_type

    @property
    def stopped_at(self):
        """Gets the stopped_at of this Execution.

        工作流停止时间。

        :return: The stopped_at of this Execution.
        :rtype: str
        """
        return self._stopped_at

    @stopped_at.setter
    def stopped_at(self, stopped_at):
        """Sets the stopped_at of this Execution.

        工作流停止时间。

        :param stopped_at: The stopped_at of this Execution.
        :type stopped_at: str
        """
        self._stopped_at = stopped_at

    @property
    def execution_state(self):
        """Gets the execution_state of this Execution.

        工作流运行状态。success,fail,running,timeout,cancel

        :return: The execution_state of this Execution.
        :rtype: str
        """
        return self._execution_state

    @execution_state.setter
    def execution_state(self, execution_state):
        """Sets the execution_state of this Execution.

        工作流运行状态。success,fail,running,timeout,cancel

        :param execution_state: The execution_state of this Execution.
        :type execution_state: str
        """
        self._execution_state = execution_state

    @property
    def execution_name(self):
        """Gets the execution_name of this Execution.

        工作流名称。

        :return: The execution_name of this Execution.
        :rtype: str
        """
        return self._execution_name

    @execution_name.setter
    def execution_name(self, execution_name):
        """Sets the execution_name of this Execution.

        工作流名称。

        :param execution_name: The execution_name of this Execution.
        :type execution_name: str
        """
        self._execution_name = execution_name

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
        if not isinstance(other, Execution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
