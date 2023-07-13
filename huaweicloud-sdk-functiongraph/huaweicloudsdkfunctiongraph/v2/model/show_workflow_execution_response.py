# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWorkflowExecutionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workflow_id': 'str',
        'workflow_urn': 'str',
        'execution_id': 'str',
        'status': 'str',
        'headers': 'object',
        'input': 'object',
        'output': 'object',
        'begin_time': 'str',
        'end_time': 'str',
        'last_update_time': 'str',
        'created_by': 'str',
        'node_execution_details': 'list[NodeExecutionDetail]'
    }

    attribute_map = {
        'workflow_id': 'workflow_id',
        'workflow_urn': 'workflow_urn',
        'execution_id': 'execution_id',
        'status': 'status',
        'headers': 'headers',
        'input': 'input',
        'output': 'output',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'last_update_time': 'last_update_time',
        'created_by': 'created_by',
        'node_execution_details': 'node_execution_details'
    }

    def __init__(self, workflow_id=None, workflow_urn=None, execution_id=None, status=None, headers=None, input=None, output=None, begin_time=None, end_time=None, last_update_time=None, created_by=None, node_execution_details=None):
        """ShowWorkflowExecutionResponse

        The model defined in huaweicloud sdk

        :param workflow_id: 流程定义ID
        :type workflow_id: str
        :param workflow_urn: 函数工作流URN, 格式为： urn:fss:&lt;region_id&gt;:&lt;project_id&gt;:workflow:\\&lt;package\\&gt;:&lt;workflow_name&gt;:\\&lt;version\\&gt; 注意： package当前只支持default version当前只支持latest
        :type workflow_urn: str
        :param execution_id: 流程执行实例ID
        :type execution_id: str
        :param status: 流程实例执行状态
        :type status: str
        :param headers: 函数执行时需要的Header
        :type headers: object
        :param input: 函数执行时的入参
        :type input: object
        :param output: 函数执行结果
        :type output: object
        :param begin_time: 流程实例创建时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间
        :type begin_time: str
        :param end_time: 流程实例结束时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间
        :type end_time: str
        :param last_update_time: 流程实例上次更新时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间
        :type last_update_time: str
        :param created_by: 流程实例创建者
        :type created_by: str
        :param node_execution_details: 节点执行信息
        :type node_execution_details: list[:class:`huaweicloudsdkfunctiongraph.v2.NodeExecutionDetail`]
        """
        
        super(ShowWorkflowExecutionResponse, self).__init__()

        self._workflow_id = None
        self._workflow_urn = None
        self._execution_id = None
        self._status = None
        self._headers = None
        self._input = None
        self._output = None
        self._begin_time = None
        self._end_time = None
        self._last_update_time = None
        self._created_by = None
        self._node_execution_details = None
        self.discriminator = None

        if workflow_id is not None:
            self.workflow_id = workflow_id
        if workflow_urn is not None:
            self.workflow_urn = workflow_urn
        if execution_id is not None:
            self.execution_id = execution_id
        if status is not None:
            self.status = status
        if headers is not None:
            self.headers = headers
        if input is not None:
            self.input = input
        if output is not None:
            self.output = output
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if created_by is not None:
            self.created_by = created_by
        if node_execution_details is not None:
            self.node_execution_details = node_execution_details

    @property
    def workflow_id(self):
        """Gets the workflow_id of this ShowWorkflowExecutionResponse.

        流程定义ID

        :return: The workflow_id of this ShowWorkflowExecutionResponse.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        """Sets the workflow_id of this ShowWorkflowExecutionResponse.

        流程定义ID

        :param workflow_id: The workflow_id of this ShowWorkflowExecutionResponse.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def workflow_urn(self):
        """Gets the workflow_urn of this ShowWorkflowExecutionResponse.

        函数工作流URN, 格式为： urn:fss:<region_id>:<project_id>:workflow:\\<package\\>:<workflow_name>:\\<version\\> 注意： package当前只支持default version当前只支持latest

        :return: The workflow_urn of this ShowWorkflowExecutionResponse.
        :rtype: str
        """
        return self._workflow_urn

    @workflow_urn.setter
    def workflow_urn(self, workflow_urn):
        """Sets the workflow_urn of this ShowWorkflowExecutionResponse.

        函数工作流URN, 格式为： urn:fss:<region_id>:<project_id>:workflow:\\<package\\>:<workflow_name>:\\<version\\> 注意： package当前只支持default version当前只支持latest

        :param workflow_urn: The workflow_urn of this ShowWorkflowExecutionResponse.
        :type workflow_urn: str
        """
        self._workflow_urn = workflow_urn

    @property
    def execution_id(self):
        """Gets the execution_id of this ShowWorkflowExecutionResponse.

        流程执行实例ID

        :return: The execution_id of this ShowWorkflowExecutionResponse.
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        """Sets the execution_id of this ShowWorkflowExecutionResponse.

        流程执行实例ID

        :param execution_id: The execution_id of this ShowWorkflowExecutionResponse.
        :type execution_id: str
        """
        self._execution_id = execution_id

    @property
    def status(self):
        """Gets the status of this ShowWorkflowExecutionResponse.

        流程实例执行状态

        :return: The status of this ShowWorkflowExecutionResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowWorkflowExecutionResponse.

        流程实例执行状态

        :param status: The status of this ShowWorkflowExecutionResponse.
        :type status: str
        """
        self._status = status

    @property
    def headers(self):
        """Gets the headers of this ShowWorkflowExecutionResponse.

        函数执行时需要的Header

        :return: The headers of this ShowWorkflowExecutionResponse.
        :rtype: object
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this ShowWorkflowExecutionResponse.

        函数执行时需要的Header

        :param headers: The headers of this ShowWorkflowExecutionResponse.
        :type headers: object
        """
        self._headers = headers

    @property
    def input(self):
        """Gets the input of this ShowWorkflowExecutionResponse.

        函数执行时的入参

        :return: The input of this ShowWorkflowExecutionResponse.
        :rtype: object
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this ShowWorkflowExecutionResponse.

        函数执行时的入参

        :param input: The input of this ShowWorkflowExecutionResponse.
        :type input: object
        """
        self._input = input

    @property
    def output(self):
        """Gets the output of this ShowWorkflowExecutionResponse.

        函数执行结果

        :return: The output of this ShowWorkflowExecutionResponse.
        :rtype: object
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this ShowWorkflowExecutionResponse.

        函数执行结果

        :param output: The output of this ShowWorkflowExecutionResponse.
        :type output: object
        """
        self._output = output

    @property
    def begin_time(self):
        """Gets the begin_time of this ShowWorkflowExecutionResponse.

        流程实例创建时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间

        :return: The begin_time of this ShowWorkflowExecutionResponse.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ShowWorkflowExecutionResponse.

        流程实例创建时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间

        :param begin_time: The begin_time of this ShowWorkflowExecutionResponse.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowWorkflowExecutionResponse.

        流程实例结束时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间

        :return: The end_time of this ShowWorkflowExecutionResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowWorkflowExecutionResponse.

        流程实例结束时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间

        :param end_time: The end_time of this ShowWorkflowExecutionResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def last_update_time(self):
        """Gets the last_update_time of this ShowWorkflowExecutionResponse.

        流程实例上次更新时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间

        :return: The last_update_time of this ShowWorkflowExecutionResponse.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """Sets the last_update_time of this ShowWorkflowExecutionResponse.

        流程实例上次更新时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间

        :param last_update_time: The last_update_time of this ShowWorkflowExecutionResponse.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def created_by(self):
        """Gets the created_by of this ShowWorkflowExecutionResponse.

        流程实例创建者

        :return: The created_by of this ShowWorkflowExecutionResponse.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ShowWorkflowExecutionResponse.

        流程实例创建者

        :param created_by: The created_by of this ShowWorkflowExecutionResponse.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def node_execution_details(self):
        """Gets the node_execution_details of this ShowWorkflowExecutionResponse.

        节点执行信息

        :return: The node_execution_details of this ShowWorkflowExecutionResponse.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.NodeExecutionDetail`]
        """
        return self._node_execution_details

    @node_execution_details.setter
    def node_execution_details(self, node_execution_details):
        """Sets the node_execution_details of this ShowWorkflowExecutionResponse.

        节点执行信息

        :param node_execution_details: The node_execution_details of this ShowWorkflowExecutionResponse.
        :type node_execution_details: list[:class:`huaweicloudsdkfunctiongraph.v2.NodeExecutionDetail`]
        """
        self._node_execution_details = node_execution_details

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
        if not isinstance(other, ShowWorkflowExecutionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
