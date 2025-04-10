# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PermissionApprovalOpenapiDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'approval_dispatch_error_msg': 'str',
        'approval_dispatch_status': 'str',
        'approval_type': 'str',
        'approve_reason': 'str',
        'current_node_id': 'str',
        'current_node_name': 'str',
        'current_node_type': 'str',
        'detail': 'PermissionApprovalDetailDTO',
        'end_time': 'int',
        'expire_time': 'int',
        'id': 'str',
        'instance_id': 'str',
        'permission_set_id': 'str',
        'project_id': 'str',
        'proposer_id': 'str',
        'proposer_name': 'str',
        'proposer_workspace_id': 'str',
        'reason': 'str',
        'start_time': 'int',
        'status': 'str',
        'workspace_id': 'str',
        'workspace_name': 'str'
    }

    attribute_map = {
        'approval_dispatch_error_msg': 'approval_dispatch_error_msg',
        'approval_dispatch_status': 'approval_dispatch_status',
        'approval_type': 'approval_type',
        'approve_reason': 'approve_reason',
        'current_node_id': 'current_node_id',
        'current_node_name': 'current_node_name',
        'current_node_type': 'current_node_type',
        'detail': 'detail',
        'end_time': 'end_time',
        'expire_time': 'expire_time',
        'id': 'id',
        'instance_id': 'instance_id',
        'permission_set_id': 'permission_set_id',
        'project_id': 'project_id',
        'proposer_id': 'proposer_id',
        'proposer_name': 'proposer_name',
        'proposer_workspace_id': 'proposer_workspace_id',
        'reason': 'reason',
        'start_time': 'start_time',
        'status': 'status',
        'workspace_id': 'workspace_id',
        'workspace_name': 'workspace_name'
    }

    def __init__(self, approval_dispatch_error_msg=None, approval_dispatch_status=None, approval_type=None, approve_reason=None, current_node_id=None, current_node_name=None, current_node_type=None, detail=None, end_time=None, expire_time=None, id=None, instance_id=None, permission_set_id=None, project_id=None, proposer_id=None, proposer_name=None, proposer_workspace_id=None, reason=None, start_time=None, status=None, workspace_id=None, workspace_name=None):
        r"""PermissionApprovalOpenapiDTO

        The model defined in huaweicloud sdk

        :param approval_dispatch_error_msg: 审批外发失败消息
        :type approval_dispatch_error_msg: str
        :param approval_dispatch_status: 审批外发状态，0表示成功，1表示失败，null表示非SMN节点
        :type approval_dispatch_status: str
        :param approval_type: 申请类型, DATA_PERMISSION
        :type approval_type: str
        :param approve_reason: 申请原因
        :type approve_reason: str
        :param current_node_id: 当前审批节点id
        :type current_node_id: str
        :param current_node_name: 当前审批节点审批人
        :type current_node_name: str
        :param current_node_type: 当前审批节点审批人类型
        :type current_node_type: str
        :param detail: 
        :type detail: :class:`huaweicloudsdkdataartsstudio.v1.PermissionApprovalDetailDTO`
        :param end_time: 工单结束时间
        :type end_time: int
        :param expire_time: 到期时间
        :type expire_time: int
        :param id: 工单id
        :type id: str
        :param instance_id: 实例id
        :type instance_id: str
        :param permission_set_id: 审批人所在权限集id
        :type permission_set_id: str
        :param project_id: 项目id
        :type project_id: str
        :param proposer_id: 申请人id
        :type proposer_id: str
        :param proposer_name: 申请人名称
        :type proposer_name: str
        :param proposer_workspace_id: 用户申请权限时所在工作空间id
        :type proposer_workspace_id: str
        :param reason: 拒绝理由
        :type reason: str
        :param start_time: 工单开始时间
        :type start_time: int
        :param status: 工单状态, WAITING_APPROVE,APPROVED,REJECT,REVOKE
        :type status: str
        :param workspace_id: 工作空间id
        :type workspace_id: str
        :param workspace_name: 工作空间名称
        :type workspace_name: str
        """
        
        

        self._approval_dispatch_error_msg = None
        self._approval_dispatch_status = None
        self._approval_type = None
        self._approve_reason = None
        self._current_node_id = None
        self._current_node_name = None
        self._current_node_type = None
        self._detail = None
        self._end_time = None
        self._expire_time = None
        self._id = None
        self._instance_id = None
        self._permission_set_id = None
        self._project_id = None
        self._proposer_id = None
        self._proposer_name = None
        self._proposer_workspace_id = None
        self._reason = None
        self._start_time = None
        self._status = None
        self._workspace_id = None
        self._workspace_name = None
        self.discriminator = None

        if approval_dispatch_error_msg is not None:
            self.approval_dispatch_error_msg = approval_dispatch_error_msg
        if approval_dispatch_status is not None:
            self.approval_dispatch_status = approval_dispatch_status
        if approval_type is not None:
            self.approval_type = approval_type
        if approve_reason is not None:
            self.approve_reason = approve_reason
        if current_node_id is not None:
            self.current_node_id = current_node_id
        if current_node_name is not None:
            self.current_node_name = current_node_name
        if current_node_type is not None:
            self.current_node_type = current_node_type
        if detail is not None:
            self.detail = detail
        if end_time is not None:
            self.end_time = end_time
        if expire_time is not None:
            self.expire_time = expire_time
        if id is not None:
            self.id = id
        if instance_id is not None:
            self.instance_id = instance_id
        if permission_set_id is not None:
            self.permission_set_id = permission_set_id
        if project_id is not None:
            self.project_id = project_id
        if proposer_id is not None:
            self.proposer_id = proposer_id
        if proposer_name is not None:
            self.proposer_name = proposer_name
        if proposer_workspace_id is not None:
            self.proposer_workspace_id = proposer_workspace_id
        if reason is not None:
            self.reason = reason
        if start_time is not None:
            self.start_time = start_time
        if status is not None:
            self.status = status
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if workspace_name is not None:
            self.workspace_name = workspace_name

    @property
    def approval_dispatch_error_msg(self):
        r"""Gets the approval_dispatch_error_msg of this PermissionApprovalOpenapiDTO.

        审批外发失败消息

        :return: The approval_dispatch_error_msg of this PermissionApprovalOpenapiDTO.
        :rtype: str
        """
        return self._approval_dispatch_error_msg

    @approval_dispatch_error_msg.setter
    def approval_dispatch_error_msg(self, approval_dispatch_error_msg):
        r"""Sets the approval_dispatch_error_msg of this PermissionApprovalOpenapiDTO.

        审批外发失败消息

        :param approval_dispatch_error_msg: The approval_dispatch_error_msg of this PermissionApprovalOpenapiDTO.
        :type approval_dispatch_error_msg: str
        """
        self._approval_dispatch_error_msg = approval_dispatch_error_msg

    @property
    def approval_dispatch_status(self):
        r"""Gets the approval_dispatch_status of this PermissionApprovalOpenapiDTO.

        审批外发状态，0表示成功，1表示失败，null表示非SMN节点

        :return: The approval_dispatch_status of this PermissionApprovalOpenapiDTO.
        :rtype: str
        """
        return self._approval_dispatch_status

    @approval_dispatch_status.setter
    def approval_dispatch_status(self, approval_dispatch_status):
        r"""Sets the approval_dispatch_status of this PermissionApprovalOpenapiDTO.

        审批外发状态，0表示成功，1表示失败，null表示非SMN节点

        :param approval_dispatch_status: The approval_dispatch_status of this PermissionApprovalOpenapiDTO.
        :type approval_dispatch_status: str
        """
        self._approval_dispatch_status = approval_dispatch_status

    @property
    def approval_type(self):
        r"""Gets the approval_type of this PermissionApprovalOpenapiDTO.

        申请类型, DATA_PERMISSION

        :return: The approval_type of this PermissionApprovalOpenapiDTO.
        :rtype: str
        """
        return self._approval_type

    @approval_type.setter
    def approval_type(self, approval_type):
        r"""Sets the approval_type of this PermissionApprovalOpenapiDTO.

        申请类型, DATA_PERMISSION

        :param approval_type: The approval_type of this PermissionApprovalOpenapiDTO.
        :type approval_type: str
        """
        self._approval_type = approval_type

    @property
    def approve_reason(self):
        r"""Gets the approve_reason of this PermissionApprovalOpenapiDTO.

        申请原因

        :return: The approve_reason of this PermissionApprovalOpenapiDTO.
        :rtype: str
        """
        return self._approve_reason

    @approve_reason.setter
    def approve_reason(self, approve_reason):
        r"""Sets the approve_reason of this PermissionApprovalOpenapiDTO.

        申请原因

        :param approve_reason: The approve_reason of this PermissionApprovalOpenapiDTO.
        :type approve_reason: str
        """
        self._approve_reason = approve_reason

    @property
    def current_node_id(self):
        r"""Gets the current_node_id of this PermissionApprovalOpenapiDTO.

        当前审批节点id

        :return: The current_node_id of this PermissionApprovalOpenapiDTO.
        :rtype: str
        """
        return self._current_node_id

    @current_node_id.setter
    def current_node_id(self, current_node_id):
        r"""Sets the current_node_id of this PermissionApprovalOpenapiDTO.

        当前审批节点id

        :param current_node_id: The current_node_id of this PermissionApprovalOpenapiDTO.
        :type current_node_id: str
        """
        self._current_node_id = current_node_id

    @property
    def current_node_name(self):
        r"""Gets the current_node_name of this PermissionApprovalOpenapiDTO.

        当前审批节点审批人

        :return: The current_node_name of this PermissionApprovalOpenapiDTO.
        :rtype: str
        """
        return self._current_node_name

    @current_node_name.setter
    def current_node_name(self, current_node_name):
        r"""Sets the current_node_name of this PermissionApprovalOpenapiDTO.

        当前审批节点审批人

        :param current_node_name: The current_node_name of this PermissionApprovalOpenapiDTO.
        :type current_node_name: str
        """
        self._current_node_name = current_node_name

    @property
    def current_node_type(self):
        r"""Gets the current_node_type of this PermissionApprovalOpenapiDTO.

        当前审批节点审批人类型

        :return: The current_node_type of this PermissionApprovalOpenapiDTO.
        :rtype: str
        """
        return self._current_node_type

    @current_node_type.setter
    def current_node_type(self, current_node_type):
        r"""Sets the current_node_type of this PermissionApprovalOpenapiDTO.

        当前审批节点审批人类型

        :param current_node_type: The current_node_type of this PermissionApprovalOpenapiDTO.
        :type current_node_type: str
        """
        self._current_node_type = current_node_type

    @property
    def detail(self):
        r"""Gets the detail of this PermissionApprovalOpenapiDTO.

        :return: The detail of this PermissionApprovalOpenapiDTO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.PermissionApprovalDetailDTO`
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        r"""Sets the detail of this PermissionApprovalOpenapiDTO.

        :param detail: The detail of this PermissionApprovalOpenapiDTO.
        :type detail: :class:`huaweicloudsdkdataartsstudio.v1.PermissionApprovalDetailDTO`
        """
        self._detail = detail

    @property
    def end_time(self):
        r"""Gets the end_time of this PermissionApprovalOpenapiDTO.

        工单结束时间

        :return: The end_time of this PermissionApprovalOpenapiDTO.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this PermissionApprovalOpenapiDTO.

        工单结束时间

        :param end_time: The end_time of this PermissionApprovalOpenapiDTO.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def expire_time(self):
        r"""Gets the expire_time of this PermissionApprovalOpenapiDTO.

        到期时间

        :return: The expire_time of this PermissionApprovalOpenapiDTO.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this PermissionApprovalOpenapiDTO.

        到期时间

        :param expire_time: The expire_time of this PermissionApprovalOpenapiDTO.
        :type expire_time: int
        """
        self._expire_time = expire_time

    @property
    def id(self):
        r"""Gets the id of this PermissionApprovalOpenapiDTO.

        工单id

        :return: The id of this PermissionApprovalOpenapiDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PermissionApprovalOpenapiDTO.

        工单id

        :param id: The id of this PermissionApprovalOpenapiDTO.
        :type id: str
        """
        self._id = id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this PermissionApprovalOpenapiDTO.

        实例id

        :return: The instance_id of this PermissionApprovalOpenapiDTO.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this PermissionApprovalOpenapiDTO.

        实例id

        :param instance_id: The instance_id of this PermissionApprovalOpenapiDTO.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def permission_set_id(self):
        r"""Gets the permission_set_id of this PermissionApprovalOpenapiDTO.

        审批人所在权限集id

        :return: The permission_set_id of this PermissionApprovalOpenapiDTO.
        :rtype: str
        """
        return self._permission_set_id

    @permission_set_id.setter
    def permission_set_id(self, permission_set_id):
        r"""Sets the permission_set_id of this PermissionApprovalOpenapiDTO.

        审批人所在权限集id

        :param permission_set_id: The permission_set_id of this PermissionApprovalOpenapiDTO.
        :type permission_set_id: str
        """
        self._permission_set_id = permission_set_id

    @property
    def project_id(self):
        r"""Gets the project_id of this PermissionApprovalOpenapiDTO.

        项目id

        :return: The project_id of this PermissionApprovalOpenapiDTO.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this PermissionApprovalOpenapiDTO.

        项目id

        :param project_id: The project_id of this PermissionApprovalOpenapiDTO.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def proposer_id(self):
        r"""Gets the proposer_id of this PermissionApprovalOpenapiDTO.

        申请人id

        :return: The proposer_id of this PermissionApprovalOpenapiDTO.
        :rtype: str
        """
        return self._proposer_id

    @proposer_id.setter
    def proposer_id(self, proposer_id):
        r"""Sets the proposer_id of this PermissionApprovalOpenapiDTO.

        申请人id

        :param proposer_id: The proposer_id of this PermissionApprovalOpenapiDTO.
        :type proposer_id: str
        """
        self._proposer_id = proposer_id

    @property
    def proposer_name(self):
        r"""Gets the proposer_name of this PermissionApprovalOpenapiDTO.

        申请人名称

        :return: The proposer_name of this PermissionApprovalOpenapiDTO.
        :rtype: str
        """
        return self._proposer_name

    @proposer_name.setter
    def proposer_name(self, proposer_name):
        r"""Sets the proposer_name of this PermissionApprovalOpenapiDTO.

        申请人名称

        :param proposer_name: The proposer_name of this PermissionApprovalOpenapiDTO.
        :type proposer_name: str
        """
        self._proposer_name = proposer_name

    @property
    def proposer_workspace_id(self):
        r"""Gets the proposer_workspace_id of this PermissionApprovalOpenapiDTO.

        用户申请权限时所在工作空间id

        :return: The proposer_workspace_id of this PermissionApprovalOpenapiDTO.
        :rtype: str
        """
        return self._proposer_workspace_id

    @proposer_workspace_id.setter
    def proposer_workspace_id(self, proposer_workspace_id):
        r"""Sets the proposer_workspace_id of this PermissionApprovalOpenapiDTO.

        用户申请权限时所在工作空间id

        :param proposer_workspace_id: The proposer_workspace_id of this PermissionApprovalOpenapiDTO.
        :type proposer_workspace_id: str
        """
        self._proposer_workspace_id = proposer_workspace_id

    @property
    def reason(self):
        r"""Gets the reason of this PermissionApprovalOpenapiDTO.

        拒绝理由

        :return: The reason of this PermissionApprovalOpenapiDTO.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this PermissionApprovalOpenapiDTO.

        拒绝理由

        :param reason: The reason of this PermissionApprovalOpenapiDTO.
        :type reason: str
        """
        self._reason = reason

    @property
    def start_time(self):
        r"""Gets the start_time of this PermissionApprovalOpenapiDTO.

        工单开始时间

        :return: The start_time of this PermissionApprovalOpenapiDTO.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this PermissionApprovalOpenapiDTO.

        工单开始时间

        :param start_time: The start_time of this PermissionApprovalOpenapiDTO.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def status(self):
        r"""Gets the status of this PermissionApprovalOpenapiDTO.

        工单状态, WAITING_APPROVE,APPROVED,REJECT,REVOKE

        :return: The status of this PermissionApprovalOpenapiDTO.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this PermissionApprovalOpenapiDTO.

        工单状态, WAITING_APPROVE,APPROVED,REJECT,REVOKE

        :param status: The status of this PermissionApprovalOpenapiDTO.
        :type status: str
        """
        self._status = status

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this PermissionApprovalOpenapiDTO.

        工作空间id

        :return: The workspace_id of this PermissionApprovalOpenapiDTO.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this PermissionApprovalOpenapiDTO.

        工作空间id

        :param workspace_id: The workspace_id of this PermissionApprovalOpenapiDTO.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def workspace_name(self):
        r"""Gets the workspace_name of this PermissionApprovalOpenapiDTO.

        工作空间名称

        :return: The workspace_name of this PermissionApprovalOpenapiDTO.
        :rtype: str
        """
        return self._workspace_name

    @workspace_name.setter
    def workspace_name(self, workspace_name):
        r"""Sets the workspace_name of this PermissionApprovalOpenapiDTO.

        工作空间名称

        :param workspace_name: The workspace_name of this PermissionApprovalOpenapiDTO.
        :type workspace_name: str
        """
        self._workspace_name = workspace_name

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
        if not isinstance(other, PermissionApprovalOpenapiDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
