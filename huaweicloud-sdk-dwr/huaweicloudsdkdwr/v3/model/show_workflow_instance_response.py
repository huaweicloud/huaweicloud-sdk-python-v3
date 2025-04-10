# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWorkflowInstanceResponse(SdkResponse):

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
        'node_execution_details': 'list[NodeExecution]',
        'x_request_id': 'str',
        'connection': 'str',
        'content_length': 'str',
        'date': 'str'
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
        'node_execution_details': 'node_execution_details',
        'x_request_id': 'x-request-id',
        'connection': 'Connection',
        'content_length': 'Content-Length',
        'date': 'Date'
    }

    def __init__(self, workflow_id=None, workflow_urn=None, execution_id=None, status=None, headers=None, input=None, output=None, begin_time=None, end_time=None, last_update_time=None, created_by=None, node_execution_details=None, x_request_id=None, connection=None, content_length=None, date=None):
        r"""ShowWorkflowInstanceResponse

        The model defined in huaweicloud sdk

        :param workflow_id: 流程定义ID  最小长度：1  最大长度：64
        :type workflow_id: str
        :param workflow_urn: 函数工作流URN, 格式为： urn:fss:&lt;region_id&gt;:&lt;project_id&gt;:workflow:&lt;package&gt;:&lt;workflow_name&gt;:&lt;version&gt; 注意： package当前只支持default version当前只支持latest
        :type workflow_urn: str
        :param execution_id: 流程执行实例ID  最小长度：1  最大长度：64
        :type execution_id: str
        :param status: 流程实例执行状态  最小长度：1  最大长度：32  枚举值：  success  fail  running  timeout  cancel
        :type status: str
        :param headers: 函数执行时需要的Header。
        :type headers: object
        :param input: 函数执行时的入参
        :type input: object
        :param output: 函数执行结果
        :type output: object
        :param begin_time: 流程实例创建时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间  最小长度：0  最大长度：64
        :type begin_time: str
        :param end_time: 流程实例结束时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间  最小长度：0  最大长度：64
        :type end_time: str
        :param last_update_time: 流程实例上次更新时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间  最小长度：0  最大长度：64
        :type last_update_time: str
        :param created_by: 流程实例创建者  最小长度：1  最大长度：32
        :type created_by: str
        :param node_execution_details: 节点执行信息
        :type node_execution_details: list[:class:`huaweicloudsdkdwr.v3.NodeExecution`]
        :param x_request_id: 
        :type x_request_id: str
        :param connection: 
        :type connection: str
        :param content_length: 
        :type content_length: str
        :param date: 
        :type date: str
        """
        
        super(ShowWorkflowInstanceResponse, self).__init__()

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
        self._x_request_id = None
        self._connection = None
        self._content_length = None
        self._date = None
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
        if x_request_id is not None:
            self.x_request_id = x_request_id
        if connection is not None:
            self.connection = connection
        if content_length is not None:
            self.content_length = content_length
        if date is not None:
            self.date = date

    @property
    def workflow_id(self):
        r"""Gets the workflow_id of this ShowWorkflowInstanceResponse.

        流程定义ID  最小长度：1  最大长度：64

        :return: The workflow_id of this ShowWorkflowInstanceResponse.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        r"""Sets the workflow_id of this ShowWorkflowInstanceResponse.

        流程定义ID  最小长度：1  最大长度：64

        :param workflow_id: The workflow_id of this ShowWorkflowInstanceResponse.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def workflow_urn(self):
        r"""Gets the workflow_urn of this ShowWorkflowInstanceResponse.

        函数工作流URN, 格式为： urn:fss:<region_id>:<project_id>:workflow:<package>:<workflow_name>:<version> 注意： package当前只支持default version当前只支持latest

        :return: The workflow_urn of this ShowWorkflowInstanceResponse.
        :rtype: str
        """
        return self._workflow_urn

    @workflow_urn.setter
    def workflow_urn(self, workflow_urn):
        r"""Sets the workflow_urn of this ShowWorkflowInstanceResponse.

        函数工作流URN, 格式为： urn:fss:<region_id>:<project_id>:workflow:<package>:<workflow_name>:<version> 注意： package当前只支持default version当前只支持latest

        :param workflow_urn: The workflow_urn of this ShowWorkflowInstanceResponse.
        :type workflow_urn: str
        """
        self._workflow_urn = workflow_urn

    @property
    def execution_id(self):
        r"""Gets the execution_id of this ShowWorkflowInstanceResponse.

        流程执行实例ID  最小长度：1  最大长度：64

        :return: The execution_id of this ShowWorkflowInstanceResponse.
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        r"""Sets the execution_id of this ShowWorkflowInstanceResponse.

        流程执行实例ID  最小长度：1  最大长度：64

        :param execution_id: The execution_id of this ShowWorkflowInstanceResponse.
        :type execution_id: str
        """
        self._execution_id = execution_id

    @property
    def status(self):
        r"""Gets the status of this ShowWorkflowInstanceResponse.

        流程实例执行状态  最小长度：1  最大长度：32  枚举值：  success  fail  running  timeout  cancel

        :return: The status of this ShowWorkflowInstanceResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowWorkflowInstanceResponse.

        流程实例执行状态  最小长度：1  最大长度：32  枚举值：  success  fail  running  timeout  cancel

        :param status: The status of this ShowWorkflowInstanceResponse.
        :type status: str
        """
        self._status = status

    @property
    def headers(self):
        r"""Gets the headers of this ShowWorkflowInstanceResponse.

        函数执行时需要的Header。

        :return: The headers of this ShowWorkflowInstanceResponse.
        :rtype: object
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        r"""Sets the headers of this ShowWorkflowInstanceResponse.

        函数执行时需要的Header。

        :param headers: The headers of this ShowWorkflowInstanceResponse.
        :type headers: object
        """
        self._headers = headers

    @property
    def input(self):
        r"""Gets the input of this ShowWorkflowInstanceResponse.

        函数执行时的入参

        :return: The input of this ShowWorkflowInstanceResponse.
        :rtype: object
        """
        return self._input

    @input.setter
    def input(self, input):
        r"""Sets the input of this ShowWorkflowInstanceResponse.

        函数执行时的入参

        :param input: The input of this ShowWorkflowInstanceResponse.
        :type input: object
        """
        self._input = input

    @property
    def output(self):
        r"""Gets the output of this ShowWorkflowInstanceResponse.

        函数执行结果

        :return: The output of this ShowWorkflowInstanceResponse.
        :rtype: object
        """
        return self._output

    @output.setter
    def output(self, output):
        r"""Sets the output of this ShowWorkflowInstanceResponse.

        函数执行结果

        :param output: The output of this ShowWorkflowInstanceResponse.
        :type output: object
        """
        self._output = output

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ShowWorkflowInstanceResponse.

        流程实例创建时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间  最小长度：0  最大长度：64

        :return: The begin_time of this ShowWorkflowInstanceResponse.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ShowWorkflowInstanceResponse.

        流程实例创建时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间  最小长度：0  最大长度：64

        :param begin_time: The begin_time of this ShowWorkflowInstanceResponse.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowWorkflowInstanceResponse.

        流程实例结束时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间  最小长度：0  最大长度：64

        :return: The end_time of this ShowWorkflowInstanceResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowWorkflowInstanceResponse.

        流程实例结束时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间  最小长度：0  最大长度：64

        :param end_time: The end_time of this ShowWorkflowInstanceResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def last_update_time(self):
        r"""Gets the last_update_time of this ShowWorkflowInstanceResponse.

        流程实例上次更新时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间  最小长度：0  最大长度：64

        :return: The last_update_time of this ShowWorkflowInstanceResponse.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        r"""Sets the last_update_time of this ShowWorkflowInstanceResponse.

        流程实例上次更新时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间  最小长度：0  最大长度：64

        :param last_update_time: The last_update_time of this ShowWorkflowInstanceResponse.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def created_by(self):
        r"""Gets the created_by of this ShowWorkflowInstanceResponse.

        流程实例创建者  最小长度：1  最大长度：32

        :return: The created_by of this ShowWorkflowInstanceResponse.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this ShowWorkflowInstanceResponse.

        流程实例创建者  最小长度：1  最大长度：32

        :param created_by: The created_by of this ShowWorkflowInstanceResponse.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def node_execution_details(self):
        r"""Gets the node_execution_details of this ShowWorkflowInstanceResponse.

        节点执行信息

        :return: The node_execution_details of this ShowWorkflowInstanceResponse.
        :rtype: list[:class:`huaweicloudsdkdwr.v3.NodeExecution`]
        """
        return self._node_execution_details

    @node_execution_details.setter
    def node_execution_details(self, node_execution_details):
        r"""Sets the node_execution_details of this ShowWorkflowInstanceResponse.

        节点执行信息

        :param node_execution_details: The node_execution_details of this ShowWorkflowInstanceResponse.
        :type node_execution_details: list[:class:`huaweicloudsdkdwr.v3.NodeExecution`]
        """
        self._node_execution_details = node_execution_details

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowWorkflowInstanceResponse.

        :return: The x_request_id of this ShowWorkflowInstanceResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowWorkflowInstanceResponse.

        :param x_request_id: The x_request_id of this ShowWorkflowInstanceResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    @property
    def connection(self):
        r"""Gets the connection of this ShowWorkflowInstanceResponse.

        :return: The connection of this ShowWorkflowInstanceResponse.
        :rtype: str
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        r"""Sets the connection of this ShowWorkflowInstanceResponse.

        :param connection: The connection of this ShowWorkflowInstanceResponse.
        :type connection: str
        """
        self._connection = connection

    @property
    def content_length(self):
        r"""Gets the content_length of this ShowWorkflowInstanceResponse.

        :return: The content_length of this ShowWorkflowInstanceResponse.
        :rtype: str
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        r"""Sets the content_length of this ShowWorkflowInstanceResponse.

        :param content_length: The content_length of this ShowWorkflowInstanceResponse.
        :type content_length: str
        """
        self._content_length = content_length

    @property
    def date(self):
        r"""Gets the date of this ShowWorkflowInstanceResponse.

        :return: The date of this ShowWorkflowInstanceResponse.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        r"""Sets the date of this ShowWorkflowInstanceResponse.

        :param date: The date of this ShowWorkflowInstanceResponse.
        :type date: str
        """
        self._date = date

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
        if not isinstance(other, ShowWorkflowInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
