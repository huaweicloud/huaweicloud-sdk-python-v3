# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPlaybookAuditLogsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'workspace_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'sort_key': 'str',
        'sort_dir': 'str',
        'body': 'AuditLogInfo'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'offset': 'offset',
        'limit': 'limit',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'body': 'body'
    }

    def __init__(self, project_id=None, workspace_id=None, offset=None, limit=None, sort_key=None, sort_dir=None, body=None):
        r"""ListPlaybookAuditLogsRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID
        :type project_id: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param offset: 分页查询参数，用于指定查询结果的起始位置，从0开始，limit 和 offset相加需要小于10000
        :type offset: int
        :param limit: 分页查询参数，用于指定一次查询最多的结果数，从1开始，limit 和 offset相加需要小于10000
        :type limit: int
        :param sort_key: **参数解释：** 排序字段 - start_time    开始时间 - end_time 结束时间  **约束限制：** 不涉及 **取值范围：** - start_time - end_time  **默认取值：** 无
        :type sort_key: str
        :param sort_dir: 排序顺序
        :type sort_dir: str
        :param body: Body of the ListPlaybookAuditLogsRequest
        :type body: :class:`huaweicloudsdksecmaster.v1.AuditLogInfo`
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._offset = None
        self._limit = None
        self._sort_key = None
        self._sort_dir = None
        self._body = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        self.offset = offset
        self.limit = limit
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if body is not None:
            self.body = body

    @property
    def project_id(self):
        r"""Gets the project_id of this ListPlaybookAuditLogsRequest.

        项目ID

        :return: The project_id of this ListPlaybookAuditLogsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListPlaybookAuditLogsRequest.

        项目ID

        :param project_id: The project_id of this ListPlaybookAuditLogsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListPlaybookAuditLogsRequest.

        工作空间ID

        :return: The workspace_id of this ListPlaybookAuditLogsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListPlaybookAuditLogsRequest.

        工作空间ID

        :param workspace_id: The workspace_id of this ListPlaybookAuditLogsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def offset(self):
        r"""Gets the offset of this ListPlaybookAuditLogsRequest.

        分页查询参数，用于指定查询结果的起始位置，从0开始，limit 和 offset相加需要小于10000

        :return: The offset of this ListPlaybookAuditLogsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPlaybookAuditLogsRequest.

        分页查询参数，用于指定查询结果的起始位置，从0开始，limit 和 offset相加需要小于10000

        :param offset: The offset of this ListPlaybookAuditLogsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListPlaybookAuditLogsRequest.

        分页查询参数，用于指定一次查询最多的结果数，从1开始，limit 和 offset相加需要小于10000

        :return: The limit of this ListPlaybookAuditLogsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPlaybookAuditLogsRequest.

        分页查询参数，用于指定一次查询最多的结果数，从1开始，limit 和 offset相加需要小于10000

        :param limit: The limit of this ListPlaybookAuditLogsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListPlaybookAuditLogsRequest.

        **参数解释：** 排序字段 - start_time    开始时间 - end_time 结束时间  **约束限制：** 不涉及 **取值范围：** - start_time - end_time  **默认取值：** 无

        :return: The sort_key of this ListPlaybookAuditLogsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListPlaybookAuditLogsRequest.

        **参数解释：** 排序字段 - start_time    开始时间 - end_time 结束时间  **约束限制：** 不涉及 **取值范围：** - start_time - end_time  **默认取值：** 无

        :param sort_key: The sort_key of this ListPlaybookAuditLogsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListPlaybookAuditLogsRequest.

        排序顺序

        :return: The sort_dir of this ListPlaybookAuditLogsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListPlaybookAuditLogsRequest.

        排序顺序

        :param sort_dir: The sort_dir of this ListPlaybookAuditLogsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def body(self):
        r"""Gets the body of this ListPlaybookAuditLogsRequest.

        :return: The body of this ListPlaybookAuditLogsRequest.
        :rtype: :class:`huaweicloudsdksecmaster.v1.AuditLogInfo`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ListPlaybookAuditLogsRequest.

        :param body: The body of this ListPlaybookAuditLogsRequest.
        :type body: :class:`huaweicloudsdksecmaster.v1.AuditLogInfo`
        """
        self._body = body

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
        if not isinstance(other, ListPlaybookAuditLogsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
