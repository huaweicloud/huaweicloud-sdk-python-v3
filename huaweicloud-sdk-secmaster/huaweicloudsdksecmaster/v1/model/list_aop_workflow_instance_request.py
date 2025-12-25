# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAopWorkflowInstanceRequest:

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
        'from_date': 'date',
        'to_date': 'date',
        'workflow_id': 'str',
        'id': 'str',
        'name': 'str',
        'dataobject_id': 'str',
        'dataclass_id': 'str',
        'playbook_id': 'str',
        'defence_id': 'str',
        'status': 'str',
        'trigger_type': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'offset': 'offset',
        'limit': 'limit',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'from_date': 'from_date',
        'to_date': 'to_date',
        'workflow_id': 'workflow_id',
        'id': 'id',
        'name': 'name',
        'dataobject_id': 'dataobject_id',
        'dataclass_id': 'dataclass_id',
        'playbook_id': 'playbook_id',
        'defence_id': 'defence_id',
        'status': 'status',
        'trigger_type': 'trigger_type'
    }

    def __init__(self, project_id=None, workspace_id=None, offset=None, limit=None, sort_key=None, sort_dir=None, from_date=None, to_date=None, workflow_id=None, id=None, name=None, dataobject_id=None, dataclass_id=None, playbook_id=None, defence_id=None, status=None, trigger_type=None):
        r"""ListAopWorkflowInstanceRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type project_id: str
        :param workspace_id: **参数解释**: 工作空间ID **取值范围**: 不涉及
        :type workspace_id: str
        :param offset: **参数解释：** 偏移量 **约束限制：** 0-10000 **取值范围：** 不涉及 **默认取值：** 0
        :type offset: int
        :param limit: **参数解释：** 数据量 **约束限制：** 1-100 **取值范围：** 不涉及 **默认取值：** 10
        :type limit: int
        :param sort_key: **参数解释：** 排序字段， - create_time：创建时间 - update_time：更新时间  **约束限制：** 不涉及 **取值范围：** - create_time - update_time  **默认取值：** create_time
        :type sort_key: str
        :param sort_dir: **参数解释：** 排序顺序 - ASC：升序 - DESC：降序  **约束限制：** 不涉及 **取值范围：** - ASC：升序 - DESC：降序  **默认取值：** DESC
        :type sort_dir: str
        :param from_date: **参数解释**: 开始时间 **约束限制**: 不涉及               **取值范围**: 不涉及 **默认值**:  不涉及
        :type from_date: date
        :param to_date: **参数解释**: 截止时间 **约束限制**: 不涉及               **取值范围**: 不涉及 **默认值**:  不涉及
        :type to_date: date
        :param workflow_id: **参数解释**: 流程的ID **约束限制**: 不涉及               **取值范围**: 不涉及 **默认值**:  不涉及
        :type workflow_id: str
        :param id: **参数解释**: 实例的ID **约束限制**: 不涉及               **取值范围**: 不涉及 **默认值**:  不涉及
        :type id: str
        :param name: **参数解释**: 实例的名字 **约束限制**: 不涉及               **取值范围**: 不涉及 **默认值**:  不涉及
        :type name: str
        :param dataobject_id: **参数解释**: 触发流程对象的id **约束限制**: 不涉及               **取值范围**: 不涉及 **默认值**:  不涉及
        :type dataobject_id: str
        :param dataclass_id: **参数解释**: 数据类的ID **约束限制**: 不涉及               **取值范围**: 不涉及 **默认值**:  不涉及
        :type dataclass_id: str
        :param playbook_id: **参数解释**: 剧本ID **约束限制**: 不涉及               **取值范围**: 不涉及 **默认值**:  不涉及
        :type playbook_id: str
        :param defence_id: **参数解释**: 防线ID **约束限制**: 不涉及               **取值范围**: 不涉及 **默认值**:  不涉及
        :type defence_id: str
        :param status: **参数解释**:          流程实例的状态 - RUNNING   运行中 - FAILED    运行失败 - FINISHED  运行结束 - RETRYING  重试中 - TERMINATING 终止中 - TERMINATED  已终止  **约束限制**: 不涉及               **取值范围**: - RUNNING    - FAILED     - FINISHED   - RETRYING   - TERMINATING  - TERMINATED  **默认值**:  不涉及
        :type status: str
        :param trigger_type: **参数解释**:          触发方式 - DEBUG   调试触发 - TIMER   定时触发 - EVENT   事件触发 - MANUAL  手动触发  **约束限制**: 不涉及               **取值范围**: - DEBUG - TIMER - EVENT - MANUAL  **默认值**:  不涉及
        :type trigger_type: str
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._offset = None
        self._limit = None
        self._sort_key = None
        self._sort_dir = None
        self._from_date = None
        self._to_date = None
        self._workflow_id = None
        self._id = None
        self._name = None
        self._dataobject_id = None
        self._dataclass_id = None
        self._playbook_id = None
        self._defence_id = None
        self._status = None
        self._trigger_type = None
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
        if from_date is not None:
            self.from_date = from_date
        if to_date is not None:
            self.to_date = to_date
        if workflow_id is not None:
            self.workflow_id = workflow_id
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if dataobject_id is not None:
            self.dataobject_id = dataobject_id
        if dataclass_id is not None:
            self.dataclass_id = dataclass_id
        if playbook_id is not None:
            self.playbook_id = playbook_id
        if defence_id is not None:
            self.defence_id = defence_id
        if status is not None:
            self.status = status
        if trigger_type is not None:
            self.trigger_type = trigger_type

    @property
    def project_id(self):
        r"""Gets the project_id of this ListAopWorkflowInstanceRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The project_id of this ListAopWorkflowInstanceRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListAopWorkflowInstanceRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param project_id: The project_id of this ListAopWorkflowInstanceRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListAopWorkflowInstanceRequest.

        **参数解释**: 工作空间ID **取值范围**: 不涉及

        :return: The workspace_id of this ListAopWorkflowInstanceRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListAopWorkflowInstanceRequest.

        **参数解释**: 工作空间ID **取值范围**: 不涉及

        :param workspace_id: The workspace_id of this ListAopWorkflowInstanceRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def offset(self):
        r"""Gets the offset of this ListAopWorkflowInstanceRequest.

        **参数解释：** 偏移量 **约束限制：** 0-10000 **取值范围：** 不涉及 **默认取值：** 0

        :return: The offset of this ListAopWorkflowInstanceRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAopWorkflowInstanceRequest.

        **参数解释：** 偏移量 **约束限制：** 0-10000 **取值范围：** 不涉及 **默认取值：** 0

        :param offset: The offset of this ListAopWorkflowInstanceRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListAopWorkflowInstanceRequest.

        **参数解释：** 数据量 **约束限制：** 1-100 **取值范围：** 不涉及 **默认取值：** 10

        :return: The limit of this ListAopWorkflowInstanceRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAopWorkflowInstanceRequest.

        **参数解释：** 数据量 **约束限制：** 1-100 **取值范围：** 不涉及 **默认取值：** 10

        :param limit: The limit of this ListAopWorkflowInstanceRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListAopWorkflowInstanceRequest.

        **参数解释：** 排序字段， - create_time：创建时间 - update_time：更新时间  **约束限制：** 不涉及 **取值范围：** - create_time - update_time  **默认取值：** create_time

        :return: The sort_key of this ListAopWorkflowInstanceRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListAopWorkflowInstanceRequest.

        **参数解释：** 排序字段， - create_time：创建时间 - update_time：更新时间  **约束限制：** 不涉及 **取值范围：** - create_time - update_time  **默认取值：** create_time

        :param sort_key: The sort_key of this ListAopWorkflowInstanceRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListAopWorkflowInstanceRequest.

        **参数解释：** 排序顺序 - ASC：升序 - DESC：降序  **约束限制：** 不涉及 **取值范围：** - ASC：升序 - DESC：降序  **默认取值：** DESC

        :return: The sort_dir of this ListAopWorkflowInstanceRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListAopWorkflowInstanceRequest.

        **参数解释：** 排序顺序 - ASC：升序 - DESC：降序  **约束限制：** 不涉及 **取值范围：** - ASC：升序 - DESC：降序  **默认取值：** DESC

        :param sort_dir: The sort_dir of this ListAopWorkflowInstanceRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def from_date(self):
        r"""Gets the from_date of this ListAopWorkflowInstanceRequest.

        **参数解释**: 开始时间 **约束限制**: 不涉及               **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The from_date of this ListAopWorkflowInstanceRequest.
        :rtype: date
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        r"""Sets the from_date of this ListAopWorkflowInstanceRequest.

        **参数解释**: 开始时间 **约束限制**: 不涉及               **取值范围**: 不涉及 **默认值**:  不涉及

        :param from_date: The from_date of this ListAopWorkflowInstanceRequest.
        :type from_date: date
        """
        self._from_date = from_date

    @property
    def to_date(self):
        r"""Gets the to_date of this ListAopWorkflowInstanceRequest.

        **参数解释**: 截止时间 **约束限制**: 不涉及               **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The to_date of this ListAopWorkflowInstanceRequest.
        :rtype: date
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        r"""Sets the to_date of this ListAopWorkflowInstanceRequest.

        **参数解释**: 截止时间 **约束限制**: 不涉及               **取值范围**: 不涉及 **默认值**:  不涉及

        :param to_date: The to_date of this ListAopWorkflowInstanceRequest.
        :type to_date: date
        """
        self._to_date = to_date

    @property
    def workflow_id(self):
        r"""Gets the workflow_id of this ListAopWorkflowInstanceRequest.

        **参数解释**: 流程的ID **约束限制**: 不涉及               **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The workflow_id of this ListAopWorkflowInstanceRequest.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        r"""Sets the workflow_id of this ListAopWorkflowInstanceRequest.

        **参数解释**: 流程的ID **约束限制**: 不涉及               **取值范围**: 不涉及 **默认值**:  不涉及

        :param workflow_id: The workflow_id of this ListAopWorkflowInstanceRequest.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def id(self):
        r"""Gets the id of this ListAopWorkflowInstanceRequest.

        **参数解释**: 实例的ID **约束限制**: 不涉及               **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The id of this ListAopWorkflowInstanceRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListAopWorkflowInstanceRequest.

        **参数解释**: 实例的ID **约束限制**: 不涉及               **取值范围**: 不涉及 **默认值**:  不涉及

        :param id: The id of this ListAopWorkflowInstanceRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListAopWorkflowInstanceRequest.

        **参数解释**: 实例的名字 **约束限制**: 不涉及               **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The name of this ListAopWorkflowInstanceRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListAopWorkflowInstanceRequest.

        **参数解释**: 实例的名字 **约束限制**: 不涉及               **取值范围**: 不涉及 **默认值**:  不涉及

        :param name: The name of this ListAopWorkflowInstanceRequest.
        :type name: str
        """
        self._name = name

    @property
    def dataobject_id(self):
        r"""Gets the dataobject_id of this ListAopWorkflowInstanceRequest.

        **参数解释**: 触发流程对象的id **约束限制**: 不涉及               **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The dataobject_id of this ListAopWorkflowInstanceRequest.
        :rtype: str
        """
        return self._dataobject_id

    @dataobject_id.setter
    def dataobject_id(self, dataobject_id):
        r"""Sets the dataobject_id of this ListAopWorkflowInstanceRequest.

        **参数解释**: 触发流程对象的id **约束限制**: 不涉及               **取值范围**: 不涉及 **默认值**:  不涉及

        :param dataobject_id: The dataobject_id of this ListAopWorkflowInstanceRequest.
        :type dataobject_id: str
        """
        self._dataobject_id = dataobject_id

    @property
    def dataclass_id(self):
        r"""Gets the dataclass_id of this ListAopWorkflowInstanceRequest.

        **参数解释**: 数据类的ID **约束限制**: 不涉及               **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The dataclass_id of this ListAopWorkflowInstanceRequest.
        :rtype: str
        """
        return self._dataclass_id

    @dataclass_id.setter
    def dataclass_id(self, dataclass_id):
        r"""Sets the dataclass_id of this ListAopWorkflowInstanceRequest.

        **参数解释**: 数据类的ID **约束限制**: 不涉及               **取值范围**: 不涉及 **默认值**:  不涉及

        :param dataclass_id: The dataclass_id of this ListAopWorkflowInstanceRequest.
        :type dataclass_id: str
        """
        self._dataclass_id = dataclass_id

    @property
    def playbook_id(self):
        r"""Gets the playbook_id of this ListAopWorkflowInstanceRequest.

        **参数解释**: 剧本ID **约束限制**: 不涉及               **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The playbook_id of this ListAopWorkflowInstanceRequest.
        :rtype: str
        """
        return self._playbook_id

    @playbook_id.setter
    def playbook_id(self, playbook_id):
        r"""Sets the playbook_id of this ListAopWorkflowInstanceRequest.

        **参数解释**: 剧本ID **约束限制**: 不涉及               **取值范围**: 不涉及 **默认值**:  不涉及

        :param playbook_id: The playbook_id of this ListAopWorkflowInstanceRequest.
        :type playbook_id: str
        """
        self._playbook_id = playbook_id

    @property
    def defence_id(self):
        r"""Gets the defence_id of this ListAopWorkflowInstanceRequest.

        **参数解释**: 防线ID **约束限制**: 不涉及               **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The defence_id of this ListAopWorkflowInstanceRequest.
        :rtype: str
        """
        return self._defence_id

    @defence_id.setter
    def defence_id(self, defence_id):
        r"""Sets the defence_id of this ListAopWorkflowInstanceRequest.

        **参数解释**: 防线ID **约束限制**: 不涉及               **取值范围**: 不涉及 **默认值**:  不涉及

        :param defence_id: The defence_id of this ListAopWorkflowInstanceRequest.
        :type defence_id: str
        """
        self._defence_id = defence_id

    @property
    def status(self):
        r"""Gets the status of this ListAopWorkflowInstanceRequest.

        **参数解释**:          流程实例的状态 - RUNNING   运行中 - FAILED    运行失败 - FINISHED  运行结束 - RETRYING  重试中 - TERMINATING 终止中 - TERMINATED  已终止  **约束限制**: 不涉及               **取值范围**: - RUNNING    - FAILED     - FINISHED   - RETRYING   - TERMINATING  - TERMINATED  **默认值**:  不涉及

        :return: The status of this ListAopWorkflowInstanceRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListAopWorkflowInstanceRequest.

        **参数解释**:          流程实例的状态 - RUNNING   运行中 - FAILED    运行失败 - FINISHED  运行结束 - RETRYING  重试中 - TERMINATING 终止中 - TERMINATED  已终止  **约束限制**: 不涉及               **取值范围**: - RUNNING    - FAILED     - FINISHED   - RETRYING   - TERMINATING  - TERMINATED  **默认值**:  不涉及

        :param status: The status of this ListAopWorkflowInstanceRequest.
        :type status: str
        """
        self._status = status

    @property
    def trigger_type(self):
        r"""Gets the trigger_type of this ListAopWorkflowInstanceRequest.

        **参数解释**:          触发方式 - DEBUG   调试触发 - TIMER   定时触发 - EVENT   事件触发 - MANUAL  手动触发  **约束限制**: 不涉及               **取值范围**: - DEBUG - TIMER - EVENT - MANUAL  **默认值**:  不涉及

        :return: The trigger_type of this ListAopWorkflowInstanceRequest.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        r"""Sets the trigger_type of this ListAopWorkflowInstanceRequest.

        **参数解释**:          触发方式 - DEBUG   调试触发 - TIMER   定时触发 - EVENT   事件触发 - MANUAL  手动触发  **约束限制**: 不涉及               **取值范围**: - DEBUG - TIMER - EVENT - MANUAL  **默认值**:  不涉及

        :param trigger_type: The trigger_type of this ListAopWorkflowInstanceRequest.
        :type trigger_type: str
        """
        self._trigger_type = trigger_type

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
        if not isinstance(other, ListAopWorkflowInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
