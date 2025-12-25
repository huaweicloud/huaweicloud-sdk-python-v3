# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkflowsRequest:

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
        'order': 'str',
        'sortby': 'str',
        'enabled': 'bool',
        'name': 'str',
        'description': 'str',
        'dataclass_id': 'str',
        'dataclass_name': 'str',
        'aop_type': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'offset': 'offset',
        'limit': 'limit',
        'order': 'order',
        'sortby': 'sortby',
        'enabled': 'enabled',
        'name': 'name',
        'description': 'description',
        'dataclass_id': 'dataclass_id',
        'dataclass_name': 'dataclass_name',
        'aop_type': 'aop_type'
    }

    def __init__(self, project_id=None, workspace_id=None, offset=None, limit=None, order=None, sortby=None, enabled=None, name=None, description=None, dataclass_id=None, dataclass_name=None, aop_type=None):
        r"""ListWorkflowsRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type project_id: str
        :param workspace_id: **参数解释**: 工作空间ID **取值范围**: 不涉及
        :type workspace_id: str
        :param offset: **参数解释：** 偏移量 **约束限制：** 0-10000 **取值范围：** 不涉及 **默认取值：** 0
        :type offset: int
        :param limit: **参数解释：** 数据量 **约束限制：** 1-100 **取值范围：** 不涉及 **默认取值：** 10
        :type limit: int
        :param order: **参数解释：** 排序顺序 - ASC：升序 - DESC：降序  **约束限制：** 不涉及 **取值范围：** - ASC：升序 - DESC：降序  **默认取值：** DESC
        :type order: str
        :param sortby: **参数解释：** 排序字段， - create_time：创建时间 - update_time：更新时间  **约束限制：** 不涉及 **取值范围：** - create_time - update_time  **默认取值：** create_time
        :type sortby: str
        :param enabled: **参数解释**: 是否已启用 **约束限制**: 不涉及         **取值范围**: - true  已启用 - false 未启用  **默认值**:  不涉及
        :type enabled: bool
        :param name: **参数解释**: 流程名称 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及
        :type name: str
        :param description: **参数解释**: 流程描述 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及
        :type description: str
        :param dataclass_id: **参数解释**: 数据类的ID **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及
        :type dataclass_id: str
        :param dataclass_name: **参数解释**: 数据类名称 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及
        :type dataclass_name: str
        :param aop_type: **参数解释**: 流程的类型 - NORMAL 通用 - SURVEY 调查 - HEMOSTASIS 止血 - EASE 缓解  **约束限制**: 不涉及         **取值范围**: - NORMAL - SURVEY - HEMOSTASIS - EASE  **默认值**:  不涉及
        :type aop_type: str
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._offset = None
        self._limit = None
        self._order = None
        self._sortby = None
        self._enabled = None
        self._name = None
        self._description = None
        self._dataclass_id = None
        self._dataclass_name = None
        self._aop_type = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if order is not None:
            self.order = order
        if sortby is not None:
            self.sortby = sortby
        if enabled is not None:
            self.enabled = enabled
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if dataclass_id is not None:
            self.dataclass_id = dataclass_id
        if dataclass_name is not None:
            self.dataclass_name = dataclass_name
        if aop_type is not None:
            self.aop_type = aop_type

    @property
    def project_id(self):
        r"""Gets the project_id of this ListWorkflowsRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The project_id of this ListWorkflowsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListWorkflowsRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param project_id: The project_id of this ListWorkflowsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListWorkflowsRequest.

        **参数解释**: 工作空间ID **取值范围**: 不涉及

        :return: The workspace_id of this ListWorkflowsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListWorkflowsRequest.

        **参数解释**: 工作空间ID **取值范围**: 不涉及

        :param workspace_id: The workspace_id of this ListWorkflowsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def offset(self):
        r"""Gets the offset of this ListWorkflowsRequest.

        **参数解释：** 偏移量 **约束限制：** 0-10000 **取值范围：** 不涉及 **默认取值：** 0

        :return: The offset of this ListWorkflowsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListWorkflowsRequest.

        **参数解释：** 偏移量 **约束限制：** 0-10000 **取值范围：** 不涉及 **默认取值：** 0

        :param offset: The offset of this ListWorkflowsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListWorkflowsRequest.

        **参数解释：** 数据量 **约束限制：** 1-100 **取值范围：** 不涉及 **默认取值：** 10

        :return: The limit of this ListWorkflowsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListWorkflowsRequest.

        **参数解释：** 数据量 **约束限制：** 1-100 **取值范围：** 不涉及 **默认取值：** 10

        :param limit: The limit of this ListWorkflowsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def order(self):
        r"""Gets the order of this ListWorkflowsRequest.

        **参数解释：** 排序顺序 - ASC：升序 - DESC：降序  **约束限制：** 不涉及 **取值范围：** - ASC：升序 - DESC：降序  **默认取值：** DESC

        :return: The order of this ListWorkflowsRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ListWorkflowsRequest.

        **参数解释：** 排序顺序 - ASC：升序 - DESC：降序  **约束限制：** 不涉及 **取值范围：** - ASC：升序 - DESC：降序  **默认取值：** DESC

        :param order: The order of this ListWorkflowsRequest.
        :type order: str
        """
        self._order = order

    @property
    def sortby(self):
        r"""Gets the sortby of this ListWorkflowsRequest.

        **参数解释：** 排序字段， - create_time：创建时间 - update_time：更新时间  **约束限制：** 不涉及 **取值范围：** - create_time - update_time  **默认取值：** create_time

        :return: The sortby of this ListWorkflowsRequest.
        :rtype: str
        """
        return self._sortby

    @sortby.setter
    def sortby(self, sortby):
        r"""Sets the sortby of this ListWorkflowsRequest.

        **参数解释：** 排序字段， - create_time：创建时间 - update_time：更新时间  **约束限制：** 不涉及 **取值范围：** - create_time - update_time  **默认取值：** create_time

        :param sortby: The sortby of this ListWorkflowsRequest.
        :type sortby: str
        """
        self._sortby = sortby

    @property
    def enabled(self):
        r"""Gets the enabled of this ListWorkflowsRequest.

        **参数解释**: 是否已启用 **约束限制**: 不涉及         **取值范围**: - true  已启用 - false 未启用  **默认值**:  不涉及

        :return: The enabled of this ListWorkflowsRequest.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this ListWorkflowsRequest.

        **参数解释**: 是否已启用 **约束限制**: 不涉及         **取值范围**: - true  已启用 - false 未启用  **默认值**:  不涉及

        :param enabled: The enabled of this ListWorkflowsRequest.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def name(self):
        r"""Gets the name of this ListWorkflowsRequest.

        **参数解释**: 流程名称 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The name of this ListWorkflowsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListWorkflowsRequest.

        **参数解释**: 流程名称 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :param name: The name of this ListWorkflowsRequest.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ListWorkflowsRequest.

        **参数解释**: 流程描述 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The description of this ListWorkflowsRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListWorkflowsRequest.

        **参数解释**: 流程描述 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :param description: The description of this ListWorkflowsRequest.
        :type description: str
        """
        self._description = description

    @property
    def dataclass_id(self):
        r"""Gets the dataclass_id of this ListWorkflowsRequest.

        **参数解释**: 数据类的ID **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The dataclass_id of this ListWorkflowsRequest.
        :rtype: str
        """
        return self._dataclass_id

    @dataclass_id.setter
    def dataclass_id(self, dataclass_id):
        r"""Sets the dataclass_id of this ListWorkflowsRequest.

        **参数解释**: 数据类的ID **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :param dataclass_id: The dataclass_id of this ListWorkflowsRequest.
        :type dataclass_id: str
        """
        self._dataclass_id = dataclass_id

    @property
    def dataclass_name(self):
        r"""Gets the dataclass_name of this ListWorkflowsRequest.

        **参数解释**: 数据类名称 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :return: The dataclass_name of this ListWorkflowsRequest.
        :rtype: str
        """
        return self._dataclass_name

    @dataclass_name.setter
    def dataclass_name(self, dataclass_name):
        r"""Sets the dataclass_name of this ListWorkflowsRequest.

        **参数解释**: 数据类名称 **约束限制**: 不涉及         **取值范围**: 不涉及 **默认值**:  不涉及

        :param dataclass_name: The dataclass_name of this ListWorkflowsRequest.
        :type dataclass_name: str
        """
        self._dataclass_name = dataclass_name

    @property
    def aop_type(self):
        r"""Gets the aop_type of this ListWorkflowsRequest.

        **参数解释**: 流程的类型 - NORMAL 通用 - SURVEY 调查 - HEMOSTASIS 止血 - EASE 缓解  **约束限制**: 不涉及         **取值范围**: - NORMAL - SURVEY - HEMOSTASIS - EASE  **默认值**:  不涉及

        :return: The aop_type of this ListWorkflowsRequest.
        :rtype: str
        """
        return self._aop_type

    @aop_type.setter
    def aop_type(self, aop_type):
        r"""Sets the aop_type of this ListWorkflowsRequest.

        **参数解释**: 流程的类型 - NORMAL 通用 - SURVEY 调查 - HEMOSTASIS 止血 - EASE 缓解  **约束限制**: 不涉及         **取值范围**: - NORMAL - SURVEY - HEMOSTASIS - EASE  **默认值**:  不涉及

        :param aop_type: The aop_type of this ListWorkflowsRequest.
        :type aop_type: str
        """
        self._aop_type = aop_type

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
        if not isinstance(other, ListWorkflowsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
