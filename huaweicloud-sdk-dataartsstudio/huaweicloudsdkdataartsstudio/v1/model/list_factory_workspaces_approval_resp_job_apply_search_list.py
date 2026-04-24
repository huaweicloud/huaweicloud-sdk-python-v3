# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFactoryWorkspacesApprovalRespJobApplySearchList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'actual_approver': 'str',
        'apply_id': 'str',
        'approval_msg': 'str',
        'approval_time': 'int',
        'approver_name': 'str',
        'change_type': 'str',
        'create_user': 'str',
        'object_id': 'str',
        'object_name': 'str',
        'object_type': 'str',
        'status': 'str',
        'submit_time': 'int'
    }

    attribute_map = {
        'actual_approver': 'actual_approver',
        'apply_id': 'apply_id',
        'approval_msg': 'approval_msg',
        'approval_time': 'approval_time',
        'approver_name': 'approver_name',
        'change_type': 'change_type',
        'create_user': 'create_user',
        'object_id': 'object_id',
        'object_name': 'object_name',
        'object_type': 'object_type',
        'status': 'status',
        'submit_time': 'submit_time'
    }

    def __init__(self, actual_approver=None, apply_id=None, approval_msg=None, approval_time=None, approver_name=None, change_type=None, create_user=None, object_id=None, object_name=None, object_type=None, status=None, submit_time=None):
        r"""ListFactoryWorkspacesApprovalRespJobApplySearchList

        The model defined in huaweicloud sdk

        :param actual_approver: 当前审批人。
        :type actual_approver: str
        :param apply_id: 审批单ID。
        :type apply_id: str
        :param approval_msg: 审核信息。
        :type approval_msg: str
        :param approval_time: 审批时间。
        :type approval_time: int
        :param approver_name: 审批人。
        :type approver_name: str
        :param change_type: 作业或脚本变更类型：修改或者删除。
        :type change_type: str
        :param create_user: 申请人。
        :type create_user: str
        :param object_id: 审批对象ID。
        :type object_id: str
        :param object_name: 作业或者脚本名称。
        :type object_name: str
        :param object_type: 审批对象类型：作业或者脚本。
        :type object_type: str
        :param status: 审批状态。
        :type status: str
        :param submit_time: 审批提交时间。
        :type submit_time: int
        """
        
        

        self._actual_approver = None
        self._apply_id = None
        self._approval_msg = None
        self._approval_time = None
        self._approver_name = None
        self._change_type = None
        self._create_user = None
        self._object_id = None
        self._object_name = None
        self._object_type = None
        self._status = None
        self._submit_time = None
        self.discriminator = None

        if actual_approver is not None:
            self.actual_approver = actual_approver
        if apply_id is not None:
            self.apply_id = apply_id
        if approval_msg is not None:
            self.approval_msg = approval_msg
        if approval_time is not None:
            self.approval_time = approval_time
        if approver_name is not None:
            self.approver_name = approver_name
        if change_type is not None:
            self.change_type = change_type
        if create_user is not None:
            self.create_user = create_user
        if object_id is not None:
            self.object_id = object_id
        if object_name is not None:
            self.object_name = object_name
        if object_type is not None:
            self.object_type = object_type
        if status is not None:
            self.status = status
        if submit_time is not None:
            self.submit_time = submit_time

    @property
    def actual_approver(self):
        r"""Gets the actual_approver of this ListFactoryWorkspacesApprovalRespJobApplySearchList.

        当前审批人。

        :return: The actual_approver of this ListFactoryWorkspacesApprovalRespJobApplySearchList.
        :rtype: str
        """
        return self._actual_approver

    @actual_approver.setter
    def actual_approver(self, actual_approver):
        r"""Sets the actual_approver of this ListFactoryWorkspacesApprovalRespJobApplySearchList.

        当前审批人。

        :param actual_approver: The actual_approver of this ListFactoryWorkspacesApprovalRespJobApplySearchList.
        :type actual_approver: str
        """
        self._actual_approver = actual_approver

    @property
    def apply_id(self):
        r"""Gets the apply_id of this ListFactoryWorkspacesApprovalRespJobApplySearchList.

        审批单ID。

        :return: The apply_id of this ListFactoryWorkspacesApprovalRespJobApplySearchList.
        :rtype: str
        """
        return self._apply_id

    @apply_id.setter
    def apply_id(self, apply_id):
        r"""Sets the apply_id of this ListFactoryWorkspacesApprovalRespJobApplySearchList.

        审批单ID。

        :param apply_id: The apply_id of this ListFactoryWorkspacesApprovalRespJobApplySearchList.
        :type apply_id: str
        """
        self._apply_id = apply_id

    @property
    def approval_msg(self):
        r"""Gets the approval_msg of this ListFactoryWorkspacesApprovalRespJobApplySearchList.

        审核信息。

        :return: The approval_msg of this ListFactoryWorkspacesApprovalRespJobApplySearchList.
        :rtype: str
        """
        return self._approval_msg

    @approval_msg.setter
    def approval_msg(self, approval_msg):
        r"""Sets the approval_msg of this ListFactoryWorkspacesApprovalRespJobApplySearchList.

        审核信息。

        :param approval_msg: The approval_msg of this ListFactoryWorkspacesApprovalRespJobApplySearchList.
        :type approval_msg: str
        """
        self._approval_msg = approval_msg

    @property
    def approval_time(self):
        r"""Gets the approval_time of this ListFactoryWorkspacesApprovalRespJobApplySearchList.

        审批时间。

        :return: The approval_time of this ListFactoryWorkspacesApprovalRespJobApplySearchList.
        :rtype: int
        """
        return self._approval_time

    @approval_time.setter
    def approval_time(self, approval_time):
        r"""Sets the approval_time of this ListFactoryWorkspacesApprovalRespJobApplySearchList.

        审批时间。

        :param approval_time: The approval_time of this ListFactoryWorkspacesApprovalRespJobApplySearchList.
        :type approval_time: int
        """
        self._approval_time = approval_time

    @property
    def approver_name(self):
        r"""Gets the approver_name of this ListFactoryWorkspacesApprovalRespJobApplySearchList.

        审批人。

        :return: The approver_name of this ListFactoryWorkspacesApprovalRespJobApplySearchList.
        :rtype: str
        """
        return self._approver_name

    @approver_name.setter
    def approver_name(self, approver_name):
        r"""Sets the approver_name of this ListFactoryWorkspacesApprovalRespJobApplySearchList.

        审批人。

        :param approver_name: The approver_name of this ListFactoryWorkspacesApprovalRespJobApplySearchList.
        :type approver_name: str
        """
        self._approver_name = approver_name

    @property
    def change_type(self):
        r"""Gets the change_type of this ListFactoryWorkspacesApprovalRespJobApplySearchList.

        作业或脚本变更类型：修改或者删除。

        :return: The change_type of this ListFactoryWorkspacesApprovalRespJobApplySearchList.
        :rtype: str
        """
        return self._change_type

    @change_type.setter
    def change_type(self, change_type):
        r"""Sets the change_type of this ListFactoryWorkspacesApprovalRespJobApplySearchList.

        作业或脚本变更类型：修改或者删除。

        :param change_type: The change_type of this ListFactoryWorkspacesApprovalRespJobApplySearchList.
        :type change_type: str
        """
        self._change_type = change_type

    @property
    def create_user(self):
        r"""Gets the create_user of this ListFactoryWorkspacesApprovalRespJobApplySearchList.

        申请人。

        :return: The create_user of this ListFactoryWorkspacesApprovalRespJobApplySearchList.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this ListFactoryWorkspacesApprovalRespJobApplySearchList.

        申请人。

        :param create_user: The create_user of this ListFactoryWorkspacesApprovalRespJobApplySearchList.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def object_id(self):
        r"""Gets the object_id of this ListFactoryWorkspacesApprovalRespJobApplySearchList.

        审批对象ID。

        :return: The object_id of this ListFactoryWorkspacesApprovalRespJobApplySearchList.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this ListFactoryWorkspacesApprovalRespJobApplySearchList.

        审批对象ID。

        :param object_id: The object_id of this ListFactoryWorkspacesApprovalRespJobApplySearchList.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def object_name(self):
        r"""Gets the object_name of this ListFactoryWorkspacesApprovalRespJobApplySearchList.

        作业或者脚本名称。

        :return: The object_name of this ListFactoryWorkspacesApprovalRespJobApplySearchList.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        r"""Sets the object_name of this ListFactoryWorkspacesApprovalRespJobApplySearchList.

        作业或者脚本名称。

        :param object_name: The object_name of this ListFactoryWorkspacesApprovalRespJobApplySearchList.
        :type object_name: str
        """
        self._object_name = object_name

    @property
    def object_type(self):
        r"""Gets the object_type of this ListFactoryWorkspacesApprovalRespJobApplySearchList.

        审批对象类型：作业或者脚本。

        :return: The object_type of this ListFactoryWorkspacesApprovalRespJobApplySearchList.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        r"""Sets the object_type of this ListFactoryWorkspacesApprovalRespJobApplySearchList.

        审批对象类型：作业或者脚本。

        :param object_type: The object_type of this ListFactoryWorkspacesApprovalRespJobApplySearchList.
        :type object_type: str
        """
        self._object_type = object_type

    @property
    def status(self):
        r"""Gets the status of this ListFactoryWorkspacesApprovalRespJobApplySearchList.

        审批状态。

        :return: The status of this ListFactoryWorkspacesApprovalRespJobApplySearchList.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListFactoryWorkspacesApprovalRespJobApplySearchList.

        审批状态。

        :param status: The status of this ListFactoryWorkspacesApprovalRespJobApplySearchList.
        :type status: str
        """
        self._status = status

    @property
    def submit_time(self):
        r"""Gets the submit_time of this ListFactoryWorkspacesApprovalRespJobApplySearchList.

        审批提交时间。

        :return: The submit_time of this ListFactoryWorkspacesApprovalRespJobApplySearchList.
        :rtype: int
        """
        return self._submit_time

    @submit_time.setter
    def submit_time(self, submit_time):
        r"""Sets the submit_time of this ListFactoryWorkspacesApprovalRespJobApplySearchList.

        审批提交时间。

        :param submit_time: The submit_time of this ListFactoryWorkspacesApprovalRespJobApplySearchList.
        :type submit_time: int
        """
        self._submit_time = submit_time

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
        if not isinstance(other, ListFactoryWorkspacesApprovalRespJobApplySearchList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
