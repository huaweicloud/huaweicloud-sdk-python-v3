# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PlanVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'title': 'str',
        'category': 'str',
        'description': 'str',
        'state': 'str',
        'status': 'str',
        'children': 'list[PlanVO]',
        'created_by': 'str',
        'modified_by': 'str',
        'plan_start_date': 'str',
        'plan_end_date': 'str',
        'created_date': 'int',
        'parent_id': 'str',
        'baseline': 'str',
        'workload': 'str',
        'owner': 'str'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'category': 'category',
        'description': 'description',
        'state': 'state',
        'status': 'status',
        'children': 'children',
        'created_by': 'created_by',
        'modified_by': 'modified_by',
        'plan_start_date': 'plan_start_date',
        'plan_end_date': 'plan_end_date',
        'created_date': 'created_date',
        'parent_id': 'parent_id',
        'baseline': 'baseline',
        'workload': 'workload',
        'owner': 'owner'
    }

    def __init__(self, id=None, title=None, category=None, description=None, state=None, status=None, children=None, created_by=None, modified_by=None, plan_start_date=None, plan_end_date=None, created_date=None, parent_id=None, baseline=None, workload=None, owner=None):
        r"""PlanVO

        The model defined in huaweicloud sdk

        :param id: **参数解释：** id（发布、迭代、里程碑的id） **取值范围：** 不涉及
        :type id: str
        :param title: **参数解释：** 标题 **取值范围：** 不涉及
        :type title: str
        :param category: **参数解释：** 分类，枚举类型 **取值范围：** - PI：发布 - Iteration：迭代 - PlanMilestone：里程碑
        :type category: str
        :param description: **参数解释：** 描述 **取值范围：** 不涉及
        :type description: str
        :param state: **参数解释：** 作废标识，枚举类型。 **取值范围：** - 正在工作：可正常操作的发布 - 作废：软删除后的发布，可在回收站恢复 - 删除：彻底删除后的发布，无法恢复
        :type state: str
        :param status: **参数解释：** 发布/迭代的状态，枚举类型。 **取值范围：** - planned：发布/计划未开始 - going：发布/计划进行中 - ended：发布/计划已结束
        :type status: str
        :param children: **参数解释：** 子项目迭代信息
        :type children: list[:class:`huaweicloudsdkprojectman.v4.PlanVO`]
        :param created_by: **参数解释：** 创建人Id **取值范围：** 不涉及
        :type created_by: str
        :param modified_by: **参数解释：** 最近更新人Id **取值范围：** 不涉及
        :type modified_by: str
        :param plan_start_date: **参数解释：** 计划开始时间，\&quot;yyyy-MM-dd\&quot;格式 **取值范围：** 不涉及
        :type plan_start_date: str
        :param plan_end_date: **参数解释：** 计划完成时间，\&quot;yyyy-MM-dd\&quot;格式 **取值范围：** 不涉及
        :type plan_end_date: str
        :param created_date: **参数解释：** 创建时间，unix时间戳，单位：毫秒 **取值范围：** 不涉及
        :type created_date: int
        :param parent_id: **参数解释：** 父工作项id **取值范围：** 不涉及
        :type parent_id: str
        :param baseline: **参数解释：** 基线状态，枚举类型 **取值范围：** - baselined：已基线 - unbaseline：未基线 - baseline-reviewing：基线评审中
        :type baseline: str
        :param workload: **参数解释：** 预估工作量 **取值范围：** 不涉及
        :type workload: str
        :param owner: **参数解释：** 责任人ID **取值范围：** 不涉及
        :type owner: str
        """
        
        

        self._id = None
        self._title = None
        self._category = None
        self._description = None
        self._state = None
        self._status = None
        self._children = None
        self._created_by = None
        self._modified_by = None
        self._plan_start_date = None
        self._plan_end_date = None
        self._created_date = None
        self._parent_id = None
        self._baseline = None
        self._workload = None
        self._owner = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if category is not None:
            self.category = category
        if description is not None:
            self.description = description
        if state is not None:
            self.state = state
        if status is not None:
            self.status = status
        if children is not None:
            self.children = children
        if created_by is not None:
            self.created_by = created_by
        if modified_by is not None:
            self.modified_by = modified_by
        if plan_start_date is not None:
            self.plan_start_date = plan_start_date
        if plan_end_date is not None:
            self.plan_end_date = plan_end_date
        if created_date is not None:
            self.created_date = created_date
        if parent_id is not None:
            self.parent_id = parent_id
        if baseline is not None:
            self.baseline = baseline
        if workload is not None:
            self.workload = workload
        if owner is not None:
            self.owner = owner

    @property
    def id(self):
        r"""Gets the id of this PlanVO.

        **参数解释：** id（发布、迭代、里程碑的id） **取值范围：** 不涉及

        :return: The id of this PlanVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PlanVO.

        **参数解释：** id（发布、迭代、里程碑的id） **取值范围：** 不涉及

        :param id: The id of this PlanVO.
        :type id: str
        """
        self._id = id

    @property
    def title(self):
        r"""Gets the title of this PlanVO.

        **参数解释：** 标题 **取值范围：** 不涉及

        :return: The title of this PlanVO.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this PlanVO.

        **参数解释：** 标题 **取值范围：** 不涉及

        :param title: The title of this PlanVO.
        :type title: str
        """
        self._title = title

    @property
    def category(self):
        r"""Gets the category of this PlanVO.

        **参数解释：** 分类，枚举类型 **取值范围：** - PI：发布 - Iteration：迭代 - PlanMilestone：里程碑

        :return: The category of this PlanVO.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this PlanVO.

        **参数解释：** 分类，枚举类型 **取值范围：** - PI：发布 - Iteration：迭代 - PlanMilestone：里程碑

        :param category: The category of this PlanVO.
        :type category: str
        """
        self._category = category

    @property
    def description(self):
        r"""Gets the description of this PlanVO.

        **参数解释：** 描述 **取值范围：** 不涉及

        :return: The description of this PlanVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PlanVO.

        **参数解释：** 描述 **取值范围：** 不涉及

        :param description: The description of this PlanVO.
        :type description: str
        """
        self._description = description

    @property
    def state(self):
        r"""Gets the state of this PlanVO.

        **参数解释：** 作废标识，枚举类型。 **取值范围：** - 正在工作：可正常操作的发布 - 作废：软删除后的发布，可在回收站恢复 - 删除：彻底删除后的发布，无法恢复

        :return: The state of this PlanVO.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this PlanVO.

        **参数解释：** 作废标识，枚举类型。 **取值范围：** - 正在工作：可正常操作的发布 - 作废：软删除后的发布，可在回收站恢复 - 删除：彻底删除后的发布，无法恢复

        :param state: The state of this PlanVO.
        :type state: str
        """
        self._state = state

    @property
    def status(self):
        r"""Gets the status of this PlanVO.

        **参数解释：** 发布/迭代的状态，枚举类型。 **取值范围：** - planned：发布/计划未开始 - going：发布/计划进行中 - ended：发布/计划已结束

        :return: The status of this PlanVO.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this PlanVO.

        **参数解释：** 发布/迭代的状态，枚举类型。 **取值范围：** - planned：发布/计划未开始 - going：发布/计划进行中 - ended：发布/计划已结束

        :param status: The status of this PlanVO.
        :type status: str
        """
        self._status = status

    @property
    def children(self):
        r"""Gets the children of this PlanVO.

        **参数解释：** 子项目迭代信息

        :return: The children of this PlanVO.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.PlanVO`]
        """
        return self._children

    @children.setter
    def children(self, children):
        r"""Sets the children of this PlanVO.

        **参数解释：** 子项目迭代信息

        :param children: The children of this PlanVO.
        :type children: list[:class:`huaweicloudsdkprojectman.v4.PlanVO`]
        """
        self._children = children

    @property
    def created_by(self):
        r"""Gets the created_by of this PlanVO.

        **参数解释：** 创建人Id **取值范围：** 不涉及

        :return: The created_by of this PlanVO.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this PlanVO.

        **参数解释：** 创建人Id **取值范围：** 不涉及

        :param created_by: The created_by of this PlanVO.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def modified_by(self):
        r"""Gets the modified_by of this PlanVO.

        **参数解释：** 最近更新人Id **取值范围：** 不涉及

        :return: The modified_by of this PlanVO.
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        r"""Sets the modified_by of this PlanVO.

        **参数解释：** 最近更新人Id **取值范围：** 不涉及

        :param modified_by: The modified_by of this PlanVO.
        :type modified_by: str
        """
        self._modified_by = modified_by

    @property
    def plan_start_date(self):
        r"""Gets the plan_start_date of this PlanVO.

        **参数解释：** 计划开始时间，\"yyyy-MM-dd\"格式 **取值范围：** 不涉及

        :return: The plan_start_date of this PlanVO.
        :rtype: str
        """
        return self._plan_start_date

    @plan_start_date.setter
    def plan_start_date(self, plan_start_date):
        r"""Sets the plan_start_date of this PlanVO.

        **参数解释：** 计划开始时间，\"yyyy-MM-dd\"格式 **取值范围：** 不涉及

        :param plan_start_date: The plan_start_date of this PlanVO.
        :type plan_start_date: str
        """
        self._plan_start_date = plan_start_date

    @property
    def plan_end_date(self):
        r"""Gets the plan_end_date of this PlanVO.

        **参数解释：** 计划完成时间，\"yyyy-MM-dd\"格式 **取值范围：** 不涉及

        :return: The plan_end_date of this PlanVO.
        :rtype: str
        """
        return self._plan_end_date

    @plan_end_date.setter
    def plan_end_date(self, plan_end_date):
        r"""Sets the plan_end_date of this PlanVO.

        **参数解释：** 计划完成时间，\"yyyy-MM-dd\"格式 **取值范围：** 不涉及

        :param plan_end_date: The plan_end_date of this PlanVO.
        :type plan_end_date: str
        """
        self._plan_end_date = plan_end_date

    @property
    def created_date(self):
        r"""Gets the created_date of this PlanVO.

        **参数解释：** 创建时间，unix时间戳，单位：毫秒 **取值范围：** 不涉及

        :return: The created_date of this PlanVO.
        :rtype: int
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        r"""Sets the created_date of this PlanVO.

        **参数解释：** 创建时间，unix时间戳，单位：毫秒 **取值范围：** 不涉及

        :param created_date: The created_date of this PlanVO.
        :type created_date: int
        """
        self._created_date = created_date

    @property
    def parent_id(self):
        r"""Gets the parent_id of this PlanVO.

        **参数解释：** 父工作项id **取值范围：** 不涉及

        :return: The parent_id of this PlanVO.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this PlanVO.

        **参数解释：** 父工作项id **取值范围：** 不涉及

        :param parent_id: The parent_id of this PlanVO.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def baseline(self):
        r"""Gets the baseline of this PlanVO.

        **参数解释：** 基线状态，枚举类型 **取值范围：** - baselined：已基线 - unbaseline：未基线 - baseline-reviewing：基线评审中

        :return: The baseline of this PlanVO.
        :rtype: str
        """
        return self._baseline

    @baseline.setter
    def baseline(self, baseline):
        r"""Sets the baseline of this PlanVO.

        **参数解释：** 基线状态，枚举类型 **取值范围：** - baselined：已基线 - unbaseline：未基线 - baseline-reviewing：基线评审中

        :param baseline: The baseline of this PlanVO.
        :type baseline: str
        """
        self._baseline = baseline

    @property
    def workload(self):
        r"""Gets the workload of this PlanVO.

        **参数解释：** 预估工作量 **取值范围：** 不涉及

        :return: The workload of this PlanVO.
        :rtype: str
        """
        return self._workload

    @workload.setter
    def workload(self, workload):
        r"""Sets the workload of this PlanVO.

        **参数解释：** 预估工作量 **取值范围：** 不涉及

        :param workload: The workload of this PlanVO.
        :type workload: str
        """
        self._workload = workload

    @property
    def owner(self):
        r"""Gets the owner of this PlanVO.

        **参数解释：** 责任人ID **取值范围：** 不涉及

        :return: The owner of this PlanVO.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this PlanVO.

        **参数解释：** 责任人ID **取值范围：** 不涉及

        :param owner: The owner of this PlanVO.
        :type owner: str
        """
        self._owner = owner

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
        if not isinstance(other, PlanVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
