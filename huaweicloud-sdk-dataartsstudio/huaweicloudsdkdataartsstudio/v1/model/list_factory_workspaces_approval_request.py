# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFactoryWorkspacesApprovalRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'x_project_id': 'str',
        'begin_time': 'int',
        'end_time': 'int',
        'status': 'str',
        'type': 'str',
        'apply_id': 'str',
        'approver_name': 'str',
        'create_user': 'str',
        'object_name': 'str',
        'object_type': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'workspace': 'workspace',
        'x_project_id': 'X-Project-Id',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'status': 'status',
        'type': 'type',
        'apply_id': 'apply_id',
        'approver_name': 'approver_name',
        'create_user': 'create_user',
        'object_name': 'object_name',
        'object_type': 'object_type',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, workspace=None, x_project_id=None, begin_time=None, end_time=None, status=None, type=None, apply_id=None, approver_name=None, create_user=None, object_name=None, object_type=None, offset=None, limit=None):
        r"""ListFactoryWorkspacesApprovalRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace: str
        :param x_project_id: 项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。
        :type x_project_id: str
        :param begin_time: 申请开始时间，13位时间戳。
        :type begin_time: int
        :param end_time: 申请结束时间，13位时间戳。当开始时间和结束时间都不传时，默认查询前7天到当天的数据。
        :type end_time: int
        :param status: 审批状态：  - DEVELOPING: 待审批  - APPROVED: 已通过  - REJECT: 已驳回  默认查询全部的状态
        :type status: str
        :param type: 审批类型:  - DEVELOPING: 查询待审批信息  - FINISHED: 查询已审批信息  - APPLY: 查询我的申请页面  默认值：APPLY
        :type type: str
        :param apply_id: 申请单号。
        :type apply_id: str
        :param approver_name: 审批人。
        :type approver_name: str
        :param create_user: 申请人，该参数只支持在待审批和已审批页面使用。
        :type create_user: str
        :param object_name: 对象名。
        :type object_name: str
        :param object_type: 审批对象： - JOB: 作业 - SCRIPT: 脚本  默认审批全部对象。
        :type object_type: str
        :param offset: 分页的起始页，取值范围大于等于0。样例: offset&#x3D;0 默认值: 0。
        :type offset: int
        :param limit: 分页返回结果，指定每页最大记录数，范围[1,100]。样例: limit&#x3D;10 默认值: 10。
        :type limit: int
        """
        
        

        self._workspace = None
        self._x_project_id = None
        self._begin_time = None
        self._end_time = None
        self._status = None
        self._type = None
        self._apply_id = None
        self._approver_name = None
        self._create_user = None
        self._object_name = None
        self._object_type = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.workspace = workspace
        if x_project_id is not None:
            self.x_project_id = x_project_id
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if apply_id is not None:
            self.apply_id = apply_id
        if approver_name is not None:
            self.approver_name = approver_name
        if create_user is not None:
            self.create_user = create_user
        if object_name is not None:
            self.object_name = object_name
        if object_type is not None:
            self.object_type = object_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def workspace(self):
        r"""Gets the workspace of this ListFactoryWorkspacesApprovalRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this ListFactoryWorkspacesApprovalRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ListFactoryWorkspacesApprovalRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this ListFactoryWorkspacesApprovalRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def x_project_id(self):
        r"""Gets the x_project_id of this ListFactoryWorkspacesApprovalRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :return: The x_project_id of this ListFactoryWorkspacesApprovalRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        r"""Sets the x_project_id of this ListFactoryWorkspacesApprovalRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :param x_project_id: The x_project_id of this ListFactoryWorkspacesApprovalRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ListFactoryWorkspacesApprovalRequest.

        申请开始时间，13位时间戳。

        :return: The begin_time of this ListFactoryWorkspacesApprovalRequest.
        :rtype: int
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ListFactoryWorkspacesApprovalRequest.

        申请开始时间，13位时间戳。

        :param begin_time: The begin_time of this ListFactoryWorkspacesApprovalRequest.
        :type begin_time: int
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListFactoryWorkspacesApprovalRequest.

        申请结束时间，13位时间戳。当开始时间和结束时间都不传时，默认查询前7天到当天的数据。

        :return: The end_time of this ListFactoryWorkspacesApprovalRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListFactoryWorkspacesApprovalRequest.

        申请结束时间，13位时间戳。当开始时间和结束时间都不传时，默认查询前7天到当天的数据。

        :param end_time: The end_time of this ListFactoryWorkspacesApprovalRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def status(self):
        r"""Gets the status of this ListFactoryWorkspacesApprovalRequest.

        审批状态：  - DEVELOPING: 待审批  - APPROVED: 已通过  - REJECT: 已驳回  默认查询全部的状态

        :return: The status of this ListFactoryWorkspacesApprovalRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListFactoryWorkspacesApprovalRequest.

        审批状态：  - DEVELOPING: 待审批  - APPROVED: 已通过  - REJECT: 已驳回  默认查询全部的状态

        :param status: The status of this ListFactoryWorkspacesApprovalRequest.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        r"""Gets the type of this ListFactoryWorkspacesApprovalRequest.

        审批类型:  - DEVELOPING: 查询待审批信息  - FINISHED: 查询已审批信息  - APPLY: 查询我的申请页面  默认值：APPLY

        :return: The type of this ListFactoryWorkspacesApprovalRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListFactoryWorkspacesApprovalRequest.

        审批类型:  - DEVELOPING: 查询待审批信息  - FINISHED: 查询已审批信息  - APPLY: 查询我的申请页面  默认值：APPLY

        :param type: The type of this ListFactoryWorkspacesApprovalRequest.
        :type type: str
        """
        self._type = type

    @property
    def apply_id(self):
        r"""Gets the apply_id of this ListFactoryWorkspacesApprovalRequest.

        申请单号。

        :return: The apply_id of this ListFactoryWorkspacesApprovalRequest.
        :rtype: str
        """
        return self._apply_id

    @apply_id.setter
    def apply_id(self, apply_id):
        r"""Sets the apply_id of this ListFactoryWorkspacesApprovalRequest.

        申请单号。

        :param apply_id: The apply_id of this ListFactoryWorkspacesApprovalRequest.
        :type apply_id: str
        """
        self._apply_id = apply_id

    @property
    def approver_name(self):
        r"""Gets the approver_name of this ListFactoryWorkspacesApprovalRequest.

        审批人。

        :return: The approver_name of this ListFactoryWorkspacesApprovalRequest.
        :rtype: str
        """
        return self._approver_name

    @approver_name.setter
    def approver_name(self, approver_name):
        r"""Sets the approver_name of this ListFactoryWorkspacesApprovalRequest.

        审批人。

        :param approver_name: The approver_name of this ListFactoryWorkspacesApprovalRequest.
        :type approver_name: str
        """
        self._approver_name = approver_name

    @property
    def create_user(self):
        r"""Gets the create_user of this ListFactoryWorkspacesApprovalRequest.

        申请人，该参数只支持在待审批和已审批页面使用。

        :return: The create_user of this ListFactoryWorkspacesApprovalRequest.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this ListFactoryWorkspacesApprovalRequest.

        申请人，该参数只支持在待审批和已审批页面使用。

        :param create_user: The create_user of this ListFactoryWorkspacesApprovalRequest.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def object_name(self):
        r"""Gets the object_name of this ListFactoryWorkspacesApprovalRequest.

        对象名。

        :return: The object_name of this ListFactoryWorkspacesApprovalRequest.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        r"""Sets the object_name of this ListFactoryWorkspacesApprovalRequest.

        对象名。

        :param object_name: The object_name of this ListFactoryWorkspacesApprovalRequest.
        :type object_name: str
        """
        self._object_name = object_name

    @property
    def object_type(self):
        r"""Gets the object_type of this ListFactoryWorkspacesApprovalRequest.

        审批对象： - JOB: 作业 - SCRIPT: 脚本  默认审批全部对象。

        :return: The object_type of this ListFactoryWorkspacesApprovalRequest.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        r"""Sets the object_type of this ListFactoryWorkspacesApprovalRequest.

        审批对象： - JOB: 作业 - SCRIPT: 脚本  默认审批全部对象。

        :param object_type: The object_type of this ListFactoryWorkspacesApprovalRequest.
        :type object_type: str
        """
        self._object_type = object_type

    @property
    def offset(self):
        r"""Gets the offset of this ListFactoryWorkspacesApprovalRequest.

        分页的起始页，取值范围大于等于0。样例: offset=0 默认值: 0。

        :return: The offset of this ListFactoryWorkspacesApprovalRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListFactoryWorkspacesApprovalRequest.

        分页的起始页，取值范围大于等于0。样例: offset=0 默认值: 0。

        :param offset: The offset of this ListFactoryWorkspacesApprovalRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListFactoryWorkspacesApprovalRequest.

        分页返回结果，指定每页最大记录数，范围[1,100]。样例: limit=10 默认值: 10。

        :return: The limit of this ListFactoryWorkspacesApprovalRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListFactoryWorkspacesApprovalRequest.

        分页返回结果，指定每页最大记录数，范围[1,100]。样例: limit=10 默认值: 10。

        :param limit: The limit of this ListFactoryWorkspacesApprovalRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListFactoryWorkspacesApprovalRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
