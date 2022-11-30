# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkflowExecutionBrief:

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
        'begin_time': 'int',
        'end_time': 'int',
        'last_update_time': 'int',
        'created_by': 'str',
        'approve_user_name_list': 'list[str]',
        'execution_result_list': 'list[NodeExecutionDetail]',
        'project_id': 'str',
        'workflow_edit_time': 'int',
        'last_record_id_with_snapshot': 'str'
    }

    attribute_map = {
        'workflow_id': 'workflow_id',
        'workflow_urn': 'workflow_urn',
        'execution_id': 'execution_id',
        'status': 'status',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'last_update_time': 'last_update_time',
        'created_by': 'created_by',
        'approve_user_name_list': 'approve_user_name_list',
        'execution_result_list': 'execution_result_list',
        'project_id': 'project_id',
        'workflow_edit_time': 'workflow_edit_time',
        'last_record_id_with_snapshot': 'last_record_id_with_snapshot'
    }

    def __init__(self, workflow_id=None, workflow_urn=None, execution_id=None, status=None, begin_time=None, end_time=None, last_update_time=None, created_by=None, approve_user_name_list=None, execution_result_list=None, project_id=None, workflow_edit_time=None, last_record_id_with_snapshot=None):
        """WorkflowExecutionBrief

        The model defined in huaweicloud sdk

        :param workflow_id: 流程定义ID
        :type workflow_id: str
        :param workflow_urn: 工作流模板参数
        :type workflow_urn: str
        :param execution_id: 流程执行实例ID
        :type execution_id: str
        :param status: 流程实例执行状态
        :type status: str
        :param begin_time: 流程实例创建时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间
        :type begin_time: int
        :param end_time: 流程实例结束时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间
        :type end_time: int
        :param last_update_time: 流程实例上次更新时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间
        :type last_update_time: int
        :param created_by: 流程实例创建者
        :type created_by: str
        :param approve_user_name_list: 审批人列表
        :type approve_user_name_list: list[str]
        :param execution_result_list: 执行记录
        :type execution_result_list: list[:class:`huaweicloudsdkaom.v1.NodeExecutionDetail`]
        :param project_id: 租户从IAM申请到的projectid，一般为32位字符串。
        :type project_id: str
        :param workflow_edit_time: 执行工作流的修改时间
        :type workflow_edit_time: int
        :param last_record_id_with_snapshot: 执行快照
        :type last_record_id_with_snapshot: str
        """
        
        

        self._workflow_id = None
        self._workflow_urn = None
        self._execution_id = None
        self._status = None
        self._begin_time = None
        self._end_time = None
        self._last_update_time = None
        self._created_by = None
        self._approve_user_name_list = None
        self._execution_result_list = None
        self._project_id = None
        self._workflow_edit_time = None
        self._last_record_id_with_snapshot = None
        self.discriminator = None

        if workflow_id is not None:
            self.workflow_id = workflow_id
        if workflow_urn is not None:
            self.workflow_urn = workflow_urn
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
        if created_by is not None:
            self.created_by = created_by
        if approve_user_name_list is not None:
            self.approve_user_name_list = approve_user_name_list
        if execution_result_list is not None:
            self.execution_result_list = execution_result_list
        if project_id is not None:
            self.project_id = project_id
        if workflow_edit_time is not None:
            self.workflow_edit_time = workflow_edit_time
        if last_record_id_with_snapshot is not None:
            self.last_record_id_with_snapshot = last_record_id_with_snapshot

    @property
    def workflow_id(self):
        """Gets the workflow_id of this WorkflowExecutionBrief.

        流程定义ID

        :return: The workflow_id of this WorkflowExecutionBrief.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        """Sets the workflow_id of this WorkflowExecutionBrief.

        流程定义ID

        :param workflow_id: The workflow_id of this WorkflowExecutionBrief.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def workflow_urn(self):
        """Gets the workflow_urn of this WorkflowExecutionBrief.

        工作流模板参数

        :return: The workflow_urn of this WorkflowExecutionBrief.
        :rtype: str
        """
        return self._workflow_urn

    @workflow_urn.setter
    def workflow_urn(self, workflow_urn):
        """Sets the workflow_urn of this WorkflowExecutionBrief.

        工作流模板参数

        :param workflow_urn: The workflow_urn of this WorkflowExecutionBrief.
        :type workflow_urn: str
        """
        self._workflow_urn = workflow_urn

    @property
    def execution_id(self):
        """Gets the execution_id of this WorkflowExecutionBrief.

        流程执行实例ID

        :return: The execution_id of this WorkflowExecutionBrief.
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        """Sets the execution_id of this WorkflowExecutionBrief.

        流程执行实例ID

        :param execution_id: The execution_id of this WorkflowExecutionBrief.
        :type execution_id: str
        """
        self._execution_id = execution_id

    @property
    def status(self):
        """Gets the status of this WorkflowExecutionBrief.

        流程实例执行状态

        :return: The status of this WorkflowExecutionBrief.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WorkflowExecutionBrief.

        流程实例执行状态

        :param status: The status of this WorkflowExecutionBrief.
        :type status: str
        """
        self._status = status

    @property
    def begin_time(self):
        """Gets the begin_time of this WorkflowExecutionBrief.

        流程实例创建时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间

        :return: The begin_time of this WorkflowExecutionBrief.
        :rtype: int
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this WorkflowExecutionBrief.

        流程实例创建时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间

        :param begin_time: The begin_time of this WorkflowExecutionBrief.
        :type begin_time: int
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this WorkflowExecutionBrief.

        流程实例结束时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间

        :return: The end_time of this WorkflowExecutionBrief.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this WorkflowExecutionBrief.

        流程实例结束时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间

        :param end_time: The end_time of this WorkflowExecutionBrief.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def last_update_time(self):
        """Gets the last_update_time of this WorkflowExecutionBrief.

        流程实例上次更新时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间

        :return: The last_update_time of this WorkflowExecutionBrief.
        :rtype: int
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """Sets the last_update_time of this WorkflowExecutionBrief.

        流程实例上次更新时间，格式：yyyy-MM-ddTHH:mm:ssZ，UTC时间

        :param last_update_time: The last_update_time of this WorkflowExecutionBrief.
        :type last_update_time: int
        """
        self._last_update_time = last_update_time

    @property
    def created_by(self):
        """Gets the created_by of this WorkflowExecutionBrief.

        流程实例创建者

        :return: The created_by of this WorkflowExecutionBrief.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this WorkflowExecutionBrief.

        流程实例创建者

        :param created_by: The created_by of this WorkflowExecutionBrief.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def approve_user_name_list(self):
        """Gets the approve_user_name_list of this WorkflowExecutionBrief.

        审批人列表

        :return: The approve_user_name_list of this WorkflowExecutionBrief.
        :rtype: list[str]
        """
        return self._approve_user_name_list

    @approve_user_name_list.setter
    def approve_user_name_list(self, approve_user_name_list):
        """Sets the approve_user_name_list of this WorkflowExecutionBrief.

        审批人列表

        :param approve_user_name_list: The approve_user_name_list of this WorkflowExecutionBrief.
        :type approve_user_name_list: list[str]
        """
        self._approve_user_name_list = approve_user_name_list

    @property
    def execution_result_list(self):
        """Gets the execution_result_list of this WorkflowExecutionBrief.

        执行记录

        :return: The execution_result_list of this WorkflowExecutionBrief.
        :rtype: list[:class:`huaweicloudsdkaom.v1.NodeExecutionDetail`]
        """
        return self._execution_result_list

    @execution_result_list.setter
    def execution_result_list(self, execution_result_list):
        """Sets the execution_result_list of this WorkflowExecutionBrief.

        执行记录

        :param execution_result_list: The execution_result_list of this WorkflowExecutionBrief.
        :type execution_result_list: list[:class:`huaweicloudsdkaom.v1.NodeExecutionDetail`]
        """
        self._execution_result_list = execution_result_list

    @property
    def project_id(self):
        """Gets the project_id of this WorkflowExecutionBrief.

        租户从IAM申请到的projectid，一般为32位字符串。

        :return: The project_id of this WorkflowExecutionBrief.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this WorkflowExecutionBrief.

        租户从IAM申请到的projectid，一般为32位字符串。

        :param project_id: The project_id of this WorkflowExecutionBrief.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workflow_edit_time(self):
        """Gets the workflow_edit_time of this WorkflowExecutionBrief.

        执行工作流的修改时间

        :return: The workflow_edit_time of this WorkflowExecutionBrief.
        :rtype: int
        """
        return self._workflow_edit_time

    @workflow_edit_time.setter
    def workflow_edit_time(self, workflow_edit_time):
        """Sets the workflow_edit_time of this WorkflowExecutionBrief.

        执行工作流的修改时间

        :param workflow_edit_time: The workflow_edit_time of this WorkflowExecutionBrief.
        :type workflow_edit_time: int
        """
        self._workflow_edit_time = workflow_edit_time

    @property
    def last_record_id_with_snapshot(self):
        """Gets the last_record_id_with_snapshot of this WorkflowExecutionBrief.

        执行快照

        :return: The last_record_id_with_snapshot of this WorkflowExecutionBrief.
        :rtype: str
        """
        return self._last_record_id_with_snapshot

    @last_record_id_with_snapshot.setter
    def last_record_id_with_snapshot(self, last_record_id_with_snapshot):
        """Sets the last_record_id_with_snapshot of this WorkflowExecutionBrief.

        执行快照

        :param last_record_id_with_snapshot: The last_record_id_with_snapshot of this WorkflowExecutionBrief.
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
        if not isinstance(other, WorkflowExecutionBrief):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
