# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartSyncWorkflowExecutionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'execution_id': 'str',
        'status': 'str',
        'output': 'object',
        'errors': 'list[SyncExecutionNodeErrorDetail]',
        'begin_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'execution_id': 'execution_id',
        'status': 'status',
        'output': 'output',
        'errors': 'errors',
        'begin_time': 'begin_time',
        'end_time': 'end_time'
    }

    def __init__(self, execution_id=None, status=None, output=None, errors=None, begin_time=None, end_time=None):
        r"""StartSyncWorkflowExecutionResponse

        The model defined in huaweicloud sdk

        :param execution_id: 流程实例ID
        :type execution_id: str
        :param status: 流程执行最终状态
        :type status: str
        :param output: 函数流的执行结果，JSON格式，仅在status为success时有值
        :type output: object
        :param errors: 流程执行错误信息，仅在status为fail时有值
        :type errors: list[:class:`huaweicloudsdkfunctiongraph.v2.SyncExecutionNodeErrorDetail`]
        :param begin_time: 流程实例创建时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间
        :type begin_time: str
        :param end_time: 流程实例结束时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间
        :type end_time: str
        """
        
        super(StartSyncWorkflowExecutionResponse, self).__init__()

        self._execution_id = None
        self._status = None
        self._output = None
        self._errors = None
        self._begin_time = None
        self._end_time = None
        self.discriminator = None

        if execution_id is not None:
            self.execution_id = execution_id
        if status is not None:
            self.status = status
        if output is not None:
            self.output = output
        if errors is not None:
            self.errors = errors
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def execution_id(self):
        r"""Gets the execution_id of this StartSyncWorkflowExecutionResponse.

        流程实例ID

        :return: The execution_id of this StartSyncWorkflowExecutionResponse.
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        r"""Sets the execution_id of this StartSyncWorkflowExecutionResponse.

        流程实例ID

        :param execution_id: The execution_id of this StartSyncWorkflowExecutionResponse.
        :type execution_id: str
        """
        self._execution_id = execution_id

    @property
    def status(self):
        r"""Gets the status of this StartSyncWorkflowExecutionResponse.

        流程执行最终状态

        :return: The status of this StartSyncWorkflowExecutionResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this StartSyncWorkflowExecutionResponse.

        流程执行最终状态

        :param status: The status of this StartSyncWorkflowExecutionResponse.
        :type status: str
        """
        self._status = status

    @property
    def output(self):
        r"""Gets the output of this StartSyncWorkflowExecutionResponse.

        函数流的执行结果，JSON格式，仅在status为success时有值

        :return: The output of this StartSyncWorkflowExecutionResponse.
        :rtype: object
        """
        return self._output

    @output.setter
    def output(self, output):
        r"""Sets the output of this StartSyncWorkflowExecutionResponse.

        函数流的执行结果，JSON格式，仅在status为success时有值

        :param output: The output of this StartSyncWorkflowExecutionResponse.
        :type output: object
        """
        self._output = output

    @property
    def errors(self):
        r"""Gets the errors of this StartSyncWorkflowExecutionResponse.

        流程执行错误信息，仅在status为fail时有值

        :return: The errors of this StartSyncWorkflowExecutionResponse.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.SyncExecutionNodeErrorDetail`]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        r"""Sets the errors of this StartSyncWorkflowExecutionResponse.

        流程执行错误信息，仅在status为fail时有值

        :param errors: The errors of this StartSyncWorkflowExecutionResponse.
        :type errors: list[:class:`huaweicloudsdkfunctiongraph.v2.SyncExecutionNodeErrorDetail`]
        """
        self._errors = errors

    @property
    def begin_time(self):
        r"""Gets the begin_time of this StartSyncWorkflowExecutionResponse.

        流程实例创建时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间

        :return: The begin_time of this StartSyncWorkflowExecutionResponse.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this StartSyncWorkflowExecutionResponse.

        流程实例创建时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间

        :param begin_time: The begin_time of this StartSyncWorkflowExecutionResponse.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this StartSyncWorkflowExecutionResponse.

        流程实例结束时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间

        :return: The end_time of this StartSyncWorkflowExecutionResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this StartSyncWorkflowExecutionResponse.

        流程实例结束时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间

        :param end_time: The end_time of this StartSyncWorkflowExecutionResponse.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, StartSyncWorkflowExecutionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
