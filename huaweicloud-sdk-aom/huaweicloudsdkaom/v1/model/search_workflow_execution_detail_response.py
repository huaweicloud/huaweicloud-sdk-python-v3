# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchWorkflowExecutionDetailResponse(SdkResponse):

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
        'execution_id': 'str',
        'status': 'str',
        'begin_time': 'int',
        'end_time': 'int',
        'last_update_time': 'int',
        'execution_result_list': 'list[ExecutionResultList]',
        'approve_user_name_list': 'list[str]',
        'project_id': 'str',
        'workflow_edit_time': 'int',
        'last_record_id_with_snapshot': 'str'
    }

    attribute_map = {
        'workflow_id': 'workflow_id',
        'execution_id': 'execution_id',
        'status': 'status',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'last_update_time': 'last_update_time',
        'execution_result_list': 'execution_result_list',
        'approve_user_name_list': 'approve_user_name_list',
        'project_id': 'project_id',
        'workflow_edit_time': 'workflow_edit_time',
        'last_record_id_with_snapshot': 'last_record_id_with_snapshot'
    }

    def __init__(self, workflow_id=None, execution_id=None, status=None, begin_time=None, end_time=None, last_update_time=None, execution_result_list=None, approve_user_name_list=None, project_id=None, workflow_edit_time=None, last_record_id_with_snapshot=None):
        """SearchWorkflowExecutionDetailResponse

        The model defined in huaweicloud sdk

        :param workflow_id: 流程定义ID。
        :type workflow_id: str
        :param execution_id: 流程执行实例ID。
        :type execution_id: str
        :param status: 流程实例执行状态。
        :type status: str
        :param begin_time: 流程实例创建时间，格式：UTC时间戳
        :type begin_time: int
        :param end_time: 流程实例结束时间，格式：UTC时间戳
        :type end_time: int
        :param last_update_time: 流程实例上次更新时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间。
        :type last_update_time: int
        :param execution_result_list: 节点执行信息。
        :type execution_result_list: list[:class:`huaweicloudsdkaom.v1.ExecutionResultList`]
        :param approve_user_name_list: 审批用户列表
        :type approve_user_name_list: list[str]
        :param project_id: 租户从IAM申请到的projectid，一般为32位字符串。
        :type project_id: str
        :param workflow_edit_time: 执行workflow的更新时间
        :type workflow_edit_time: int
        :param last_record_id_with_snapshot: 执行快照
        :type last_record_id_with_snapshot: str
        """
        
        super(SearchWorkflowExecutionDetailResponse, self).__init__()

        self._workflow_id = None
        self._execution_id = None
        self._status = None
        self._begin_time = None
        self._end_time = None
        self._last_update_time = None
        self._execution_result_list = None
        self._approve_user_name_list = None
        self._project_id = None
        self._workflow_edit_time = None
        self._last_record_id_with_snapshot = None
        self.discriminator = None

        if workflow_id is not None:
            self.workflow_id = workflow_id
        if execution_id is not None:
            self.execution_id = execution_id
        if status is not None:
            self.status = status
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if execution_result_list is not None:
            self.execution_result_list = execution_result_list
        if approve_user_name_list is not None:
            self.approve_user_name_list = approve_user_name_list
        if project_id is not None:
            self.project_id = project_id
        if workflow_edit_time is not None:
            self.workflow_edit_time = workflow_edit_time
        if last_record_id_with_snapshot is not None:
            self.last_record_id_with_snapshot = last_record_id_with_snapshot

    @property
    def workflow_id(self):
        """Gets the workflow_id of this SearchWorkflowExecutionDetailResponse.

        流程定义ID。

        :return: The workflow_id of this SearchWorkflowExecutionDetailResponse.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        """Sets the workflow_id of this SearchWorkflowExecutionDetailResponse.

        流程定义ID。

        :param workflow_id: The workflow_id of this SearchWorkflowExecutionDetailResponse.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def execution_id(self):
        """Gets the execution_id of this SearchWorkflowExecutionDetailResponse.

        流程执行实例ID。

        :return: The execution_id of this SearchWorkflowExecutionDetailResponse.
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        """Sets the execution_id of this SearchWorkflowExecutionDetailResponse.

        流程执行实例ID。

        :param execution_id: The execution_id of this SearchWorkflowExecutionDetailResponse.
        :type execution_id: str
        """
        self._execution_id = execution_id

    @property
    def status(self):
        """Gets the status of this SearchWorkflowExecutionDetailResponse.

        流程实例执行状态。

        :return: The status of this SearchWorkflowExecutionDetailResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SearchWorkflowExecutionDetailResponse.

        流程实例执行状态。

        :param status: The status of this SearchWorkflowExecutionDetailResponse.
        :type status: str
        """
        self._status = status

    @property
    def begin_time(self):
        """Gets the begin_time of this SearchWorkflowExecutionDetailResponse.

        流程实例创建时间，格式：UTC时间戳

        :return: The begin_time of this SearchWorkflowExecutionDetailResponse.
        :rtype: int
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this SearchWorkflowExecutionDetailResponse.

        流程实例创建时间，格式：UTC时间戳

        :param begin_time: The begin_time of this SearchWorkflowExecutionDetailResponse.
        :type begin_time: int
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this SearchWorkflowExecutionDetailResponse.

        流程实例结束时间，格式：UTC时间戳

        :return: The end_time of this SearchWorkflowExecutionDetailResponse.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this SearchWorkflowExecutionDetailResponse.

        流程实例结束时间，格式：UTC时间戳

        :param end_time: The end_time of this SearchWorkflowExecutionDetailResponse.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def last_update_time(self):
        """Gets the last_update_time of this SearchWorkflowExecutionDetailResponse.

        流程实例上次更新时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间。

        :return: The last_update_time of this SearchWorkflowExecutionDetailResponse.
        :rtype: int
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """Sets the last_update_time of this SearchWorkflowExecutionDetailResponse.

        流程实例上次更新时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间。

        :param last_update_time: The last_update_time of this SearchWorkflowExecutionDetailResponse.
        :type last_update_time: int
        """
        self._last_update_time = last_update_time

    @property
    def execution_result_list(self):
        """Gets the execution_result_list of this SearchWorkflowExecutionDetailResponse.

        节点执行信息。

        :return: The execution_result_list of this SearchWorkflowExecutionDetailResponse.
        :rtype: list[:class:`huaweicloudsdkaom.v1.ExecutionResultList`]
        """
        return self._execution_result_list

    @execution_result_list.setter
    def execution_result_list(self, execution_result_list):
        """Sets the execution_result_list of this SearchWorkflowExecutionDetailResponse.

        节点执行信息。

        :param execution_result_list: The execution_result_list of this SearchWorkflowExecutionDetailResponse.
        :type execution_result_list: list[:class:`huaweicloudsdkaom.v1.ExecutionResultList`]
        """
        self._execution_result_list = execution_result_list

    @property
    def approve_user_name_list(self):
        """Gets the approve_user_name_list of this SearchWorkflowExecutionDetailResponse.

        审批用户列表

        :return: The approve_user_name_list of this SearchWorkflowExecutionDetailResponse.
        :rtype: list[str]
        """
        return self._approve_user_name_list

    @approve_user_name_list.setter
    def approve_user_name_list(self, approve_user_name_list):
        """Sets the approve_user_name_list of this SearchWorkflowExecutionDetailResponse.

        审批用户列表

        :param approve_user_name_list: The approve_user_name_list of this SearchWorkflowExecutionDetailResponse.
        :type approve_user_name_list: list[str]
        """
        self._approve_user_name_list = approve_user_name_list

    @property
    def project_id(self):
        """Gets the project_id of this SearchWorkflowExecutionDetailResponse.

        租户从IAM申请到的projectid，一般为32位字符串。

        :return: The project_id of this SearchWorkflowExecutionDetailResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this SearchWorkflowExecutionDetailResponse.

        租户从IAM申请到的projectid，一般为32位字符串。

        :param project_id: The project_id of this SearchWorkflowExecutionDetailResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workflow_edit_time(self):
        """Gets the workflow_edit_time of this SearchWorkflowExecutionDetailResponse.

        执行workflow的更新时间

        :return: The workflow_edit_time of this SearchWorkflowExecutionDetailResponse.
        :rtype: int
        """
        return self._workflow_edit_time

    @workflow_edit_time.setter
    def workflow_edit_time(self, workflow_edit_time):
        """Sets the workflow_edit_time of this SearchWorkflowExecutionDetailResponse.

        执行workflow的更新时间

        :param workflow_edit_time: The workflow_edit_time of this SearchWorkflowExecutionDetailResponse.
        :type workflow_edit_time: int
        """
        self._workflow_edit_time = workflow_edit_time

    @property
    def last_record_id_with_snapshot(self):
        """Gets the last_record_id_with_snapshot of this SearchWorkflowExecutionDetailResponse.

        执行快照

        :return: The last_record_id_with_snapshot of this SearchWorkflowExecutionDetailResponse.
        :rtype: str
        """
        return self._last_record_id_with_snapshot

    @last_record_id_with_snapshot.setter
    def last_record_id_with_snapshot(self, last_record_id_with_snapshot):
        """Sets the last_record_id_with_snapshot of this SearchWorkflowExecutionDetailResponse.

        执行快照

        :param last_record_id_with_snapshot: The last_record_id_with_snapshot of this SearchWorkflowExecutionDetailResponse.
        :type last_record_id_with_snapshot: str
        """
        self._last_record_id_with_snapshot = last_record_id_with_snapshot

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
        if not isinstance(other, SearchWorkflowExecutionDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
