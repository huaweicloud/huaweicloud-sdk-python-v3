# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTasksRequest:

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
        'note': 'str',
        'name': 'str',
        'business_type': 'str',
        'creator_name': 'str',
        'query_type': 'str',
        'from_date': 'str',
        'to_date': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'offset': 'offset',
        'limit': 'limit',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'note': 'note',
        'name': 'name',
        'business_type': 'business_type',
        'creator_name': 'creator_name',
        'query_type': 'query_type',
        'from_date': 'from_date',
        'to_date': 'to_date'
    }

    def __init__(self, project_id=None, workspace_id=None, offset=None, limit=None, sort_key=None, sort_dir=None, note=None, name=None, business_type=None, creator_name=None, query_type=None, from_date=None, to_date=None):
        r"""ListTasksRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type project_id: str
        :param workspace_id: **参数解释**: 工作空间ID **取值范围**: 不涉及
        :type workspace_id: str
        :param offset: **参数解释**: 待办请求的偏移量 **约束限制**: 不涉及         **取值范围**: 0-9999 **默认值**:  0
        :type offset: int
        :param limit: **参数解释**: 待办分页大小 **约束限制**: 不涉及         **取值范围**: 1-100 **默认值**:  10
        :type limit: int
        :param sort_key: **参数解释**: 待办的排序字段 - create_time 按照创建时间排序 - update_time 按照更新时间排序  **约束限制**: 不涉及         **取值范围**: - create_time - update_time  **默认值**:  create_time
        :type sort_key: str
        :param sort_dir: **参数解释**: 待办的排序方式 - ASC 按照升序排序 - DESC 按照降序排序  **约束限制**: 不涉及         **取值范围**: - ASC - DESC  **默认值**:  DESC
        :type sort_dir: str
        :param note: **参数解释**: 待办的备注 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及
        :type note: str
        :param name: **参数解释**: 待办的任务名称 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及
        :type name: str
        :param business_type: **参数解释**: 待办的业务类型 - WORKFLOWPUBLISH 流程发布 - WORKFLOWNODEAPPROVE 流程节点审核 - PLAYBOOKPUBLISH 剧本发布 - PLAYBOOKNODEAPPROVE 剧本节点审核  **约束限制**: 不涉及         **取值范围**: - WORKFLOWPUBLISH - WORKFLOWNODEAPPROVE - PLAYBOOKPUBLISH - PLAYBOOKNODEAPPROVE  **默认值**:  不涉及
        :type business_type: str
        :param creator_name: **参数解释**: 待办的创建人 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及
        :type creator_name: str
        :param query_type: **参数解释**: 待办的分类 - my_todo 待处理的待办 - all_handled 已处理的待办   **约束限制**: 不涉及         **取值范围**: - my_todo - all_handled   **默认值**:  my_todo
        :type query_type: str
        :param from_date: **参数解释**: 起始时间，格式是 \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39;Z\&quot; **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及
        :type from_date: str
        :param to_date: **参数解释**: 的截止时间，格式是 \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39;Z\&quot; **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及
        :type to_date: str
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._offset = None
        self._limit = None
        self._sort_key = None
        self._sort_dir = None
        self._note = None
        self._name = None
        self._business_type = None
        self._creator_name = None
        self._query_type = None
        self._from_date = None
        self._to_date = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if note is not None:
            self.note = note
        if name is not None:
            self.name = name
        if business_type is not None:
            self.business_type = business_type
        if creator_name is not None:
            self.creator_name = creator_name
        if query_type is not None:
            self.query_type = query_type
        if from_date is not None:
            self.from_date = from_date
        if to_date is not None:
            self.to_date = to_date

    @property
    def project_id(self):
        r"""Gets the project_id of this ListTasksRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The project_id of this ListTasksRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListTasksRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param project_id: The project_id of this ListTasksRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListTasksRequest.

        **参数解释**: 工作空间ID **取值范围**: 不涉及

        :return: The workspace_id of this ListTasksRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListTasksRequest.

        **参数解释**: 工作空间ID **取值范围**: 不涉及

        :param workspace_id: The workspace_id of this ListTasksRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def offset(self):
        r"""Gets the offset of this ListTasksRequest.

        **参数解释**: 待办请求的偏移量 **约束限制**: 不涉及         **取值范围**: 0-9999 **默认值**:  0

        :return: The offset of this ListTasksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListTasksRequest.

        **参数解释**: 待办请求的偏移量 **约束限制**: 不涉及         **取值范围**: 0-9999 **默认值**:  0

        :param offset: The offset of this ListTasksRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListTasksRequest.

        **参数解释**: 待办分页大小 **约束限制**: 不涉及         **取值范围**: 1-100 **默认值**:  10

        :return: The limit of this ListTasksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTasksRequest.

        **参数解释**: 待办分页大小 **约束限制**: 不涉及         **取值范围**: 1-100 **默认值**:  10

        :param limit: The limit of this ListTasksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListTasksRequest.

        **参数解释**: 待办的排序字段 - create_time 按照创建时间排序 - update_time 按照更新时间排序  **约束限制**: 不涉及         **取值范围**: - create_time - update_time  **默认值**:  create_time

        :return: The sort_key of this ListTasksRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListTasksRequest.

        **参数解释**: 待办的排序字段 - create_time 按照创建时间排序 - update_time 按照更新时间排序  **约束限制**: 不涉及         **取值范围**: - create_time - update_time  **默认值**:  create_time

        :param sort_key: The sort_key of this ListTasksRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListTasksRequest.

        **参数解释**: 待办的排序方式 - ASC 按照升序排序 - DESC 按照降序排序  **约束限制**: 不涉及         **取值范围**: - ASC - DESC  **默认值**:  DESC

        :return: The sort_dir of this ListTasksRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListTasksRequest.

        **参数解释**: 待办的排序方式 - ASC 按照升序排序 - DESC 按照降序排序  **约束限制**: 不涉及         **取值范围**: - ASC - DESC  **默认值**:  DESC

        :param sort_dir: The sort_dir of this ListTasksRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def note(self):
        r"""Gets the note of this ListTasksRequest.

        **参数解释**: 待办的备注 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The note of this ListTasksRequest.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        r"""Sets the note of this ListTasksRequest.

        **参数解释**: 待办的备注 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :param note: The note of this ListTasksRequest.
        :type note: str
        """
        self._note = note

    @property
    def name(self):
        r"""Gets the name of this ListTasksRequest.

        **参数解释**: 待办的任务名称 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The name of this ListTasksRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListTasksRequest.

        **参数解释**: 待办的任务名称 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :param name: The name of this ListTasksRequest.
        :type name: str
        """
        self._name = name

    @property
    def business_type(self):
        r"""Gets the business_type of this ListTasksRequest.

        **参数解释**: 待办的业务类型 - WORKFLOWPUBLISH 流程发布 - WORKFLOWNODEAPPROVE 流程节点审核 - PLAYBOOKPUBLISH 剧本发布 - PLAYBOOKNODEAPPROVE 剧本节点审核  **约束限制**: 不涉及         **取值范围**: - WORKFLOWPUBLISH - WORKFLOWNODEAPPROVE - PLAYBOOKPUBLISH - PLAYBOOKNODEAPPROVE  **默认值**:  不涉及

        :return: The business_type of this ListTasksRequest.
        :rtype: str
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        r"""Sets the business_type of this ListTasksRequest.

        **参数解释**: 待办的业务类型 - WORKFLOWPUBLISH 流程发布 - WORKFLOWNODEAPPROVE 流程节点审核 - PLAYBOOKPUBLISH 剧本发布 - PLAYBOOKNODEAPPROVE 剧本节点审核  **约束限制**: 不涉及         **取值范围**: - WORKFLOWPUBLISH - WORKFLOWNODEAPPROVE - PLAYBOOKPUBLISH - PLAYBOOKNODEAPPROVE  **默认值**:  不涉及

        :param business_type: The business_type of this ListTasksRequest.
        :type business_type: str
        """
        self._business_type = business_type

    @property
    def creator_name(self):
        r"""Gets the creator_name of this ListTasksRequest.

        **参数解释**: 待办的创建人 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The creator_name of this ListTasksRequest.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this ListTasksRequest.

        **参数解释**: 待办的创建人 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :param creator_name: The creator_name of this ListTasksRequest.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def query_type(self):
        r"""Gets the query_type of this ListTasksRequest.

        **参数解释**: 待办的分类 - my_todo 待处理的待办 - all_handled 已处理的待办   **约束限制**: 不涉及         **取值范围**: - my_todo - all_handled   **默认值**:  my_todo

        :return: The query_type of this ListTasksRequest.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        r"""Sets the query_type of this ListTasksRequest.

        **参数解释**: 待办的分类 - my_todo 待处理的待办 - all_handled 已处理的待办   **约束限制**: 不涉及         **取值范围**: - my_todo - all_handled   **默认值**:  my_todo

        :param query_type: The query_type of this ListTasksRequest.
        :type query_type: str
        """
        self._query_type = query_type

    @property
    def from_date(self):
        r"""Gets the from_date of this ListTasksRequest.

        **参数解释**: 起始时间，格式是 \"yyyy-MM-dd'T'HH:mm:ss.SSS'Z'Z\" **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The from_date of this ListTasksRequest.
        :rtype: str
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        r"""Sets the from_date of this ListTasksRequest.

        **参数解释**: 起始时间，格式是 \"yyyy-MM-dd'T'HH:mm:ss.SSS'Z'Z\" **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :param from_date: The from_date of this ListTasksRequest.
        :type from_date: str
        """
        self._from_date = from_date

    @property
    def to_date(self):
        r"""Gets the to_date of this ListTasksRequest.

        **参数解释**: 的截止时间，格式是 \"yyyy-MM-dd'T'HH:mm:ss.SSS'Z'Z\" **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The to_date of this ListTasksRequest.
        :rtype: str
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        r"""Sets the to_date of this ListTasksRequest.

        **参数解释**: 的截止时间，格式是 \"yyyy-MM-dd'T'HH:mm:ss.SSS'Z'Z\" **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :param to_date: The to_date of this ListTasksRequest.
        :type to_date: str
        """
        self._to_date = to_date

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
        if not isinstance(other, ListTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
