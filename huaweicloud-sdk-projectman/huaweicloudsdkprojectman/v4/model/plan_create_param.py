# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PlanCreateParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'title': 'str',
        'category': 'str',
        'description': 'str',
        'plan_start_date': 'str',
        'plan_end_date': 'str',
        'parent_id': 'str',
        'workload': 'str',
        'owner': 'str'
    }

    attribute_map = {
        'title': 'title',
        'category': 'category',
        'description': 'description',
        'plan_start_date': 'plan_start_date',
        'plan_end_date': 'plan_end_date',
        'parent_id': 'parent_id',
        'workload': 'workload',
        'owner': 'owner'
    }

    def __init__(self, title=None, category=None, description=None, plan_start_date=None, plan_end_date=None, parent_id=None, workload=None, owner=None):
        r"""PlanCreateParam

        The model defined in huaweicloud sdk

        :param title: **参数解释**： 计划标题。 **约束限制**： 不涉及。 **取值范围**： 1~256个字符。 **默认取值**： 不涉及。
        :type title: str
        :param category: **参数解释**： 计划分类，枚举类型。 **约束限制**： 不涉及。 **取值范围**： - PI：发布 - Iteration：迭代 - PlanMilestone：里程碑 **默认取值**： 不涉及。
        :type category: str
        :param description: **参数解释**： 计划描述信息。 **约束限制**： 不涉及。 **取值范围**： 0~1000个字符。 **默认取值**： 不涉及。
        :type description: str
        :param plan_start_date: **参数解释**： 计划开始时间，格式为yyyy-MM-dd，如2024-01-01。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type plan_start_date: str
        :param plan_end_date: **参数解释**： 计划完成时间，格式为yyyy-MM-dd，如2024-01-01。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type plan_end_date: str
        :param parent_id: **参数解释**： 父计划ID，当category为Iteration时必填，用于指定所属的发布计划。 **约束限制**： category为Iteration时必填。 **取值范围**： 长度为18~19个字符的数字字符串。 **默认取值**： 不涉及。
        :type parent_id: str
        :param workload: **参数解释**： 预估工作量，用于标识计划所需的人力投入，单位人/天。 **约束限制**： 不涉及。 **取值范围**： 0~11个字符。 **默认取值**： 不涉及。
        :type workload: str
        :param owner: **参数解释**： 责任人ID，标识计划的负责人。 **约束限制**： 不涉及。 **取值范围**： 长度为32个字符。 **默认取值**： 不涉及。
        :type owner: str
        """
        
        

        self._title = None
        self._category = None
        self._description = None
        self._plan_start_date = None
        self._plan_end_date = None
        self._parent_id = None
        self._workload = None
        self._owner = None
        self.discriminator = None

        self.title = title
        self.category = category
        if description is not None:
            self.description = description
        self.plan_start_date = plan_start_date
        self.plan_end_date = plan_end_date
        if parent_id is not None:
            self.parent_id = parent_id
        if workload is not None:
            self.workload = workload
        if owner is not None:
            self.owner = owner

    @property
    def title(self):
        r"""Gets the title of this PlanCreateParam.

        **参数解释**： 计划标题。 **约束限制**： 不涉及。 **取值范围**： 1~256个字符。 **默认取值**： 不涉及。

        :return: The title of this PlanCreateParam.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this PlanCreateParam.

        **参数解释**： 计划标题。 **约束限制**： 不涉及。 **取值范围**： 1~256个字符。 **默认取值**： 不涉及。

        :param title: The title of this PlanCreateParam.
        :type title: str
        """
        self._title = title

    @property
    def category(self):
        r"""Gets the category of this PlanCreateParam.

        **参数解释**： 计划分类，枚举类型。 **约束限制**： 不涉及。 **取值范围**： - PI：发布 - Iteration：迭代 - PlanMilestone：里程碑 **默认取值**： 不涉及。

        :return: The category of this PlanCreateParam.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this PlanCreateParam.

        **参数解释**： 计划分类，枚举类型。 **约束限制**： 不涉及。 **取值范围**： - PI：发布 - Iteration：迭代 - PlanMilestone：里程碑 **默认取值**： 不涉及。

        :param category: The category of this PlanCreateParam.
        :type category: str
        """
        self._category = category

    @property
    def description(self):
        r"""Gets the description of this PlanCreateParam.

        **参数解释**： 计划描述信息。 **约束限制**： 不涉及。 **取值范围**： 0~1000个字符。 **默认取值**： 不涉及。

        :return: The description of this PlanCreateParam.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PlanCreateParam.

        **参数解释**： 计划描述信息。 **约束限制**： 不涉及。 **取值范围**： 0~1000个字符。 **默认取值**： 不涉及。

        :param description: The description of this PlanCreateParam.
        :type description: str
        """
        self._description = description

    @property
    def plan_start_date(self):
        r"""Gets the plan_start_date of this PlanCreateParam.

        **参数解释**： 计划开始时间，格式为yyyy-MM-dd，如2024-01-01。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The plan_start_date of this PlanCreateParam.
        :rtype: str
        """
        return self._plan_start_date

    @plan_start_date.setter
    def plan_start_date(self, plan_start_date):
        r"""Sets the plan_start_date of this PlanCreateParam.

        **参数解释**： 计划开始时间，格式为yyyy-MM-dd，如2024-01-01。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param plan_start_date: The plan_start_date of this PlanCreateParam.
        :type plan_start_date: str
        """
        self._plan_start_date = plan_start_date

    @property
    def plan_end_date(self):
        r"""Gets the plan_end_date of this PlanCreateParam.

        **参数解释**： 计划完成时间，格式为yyyy-MM-dd，如2024-01-01。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The plan_end_date of this PlanCreateParam.
        :rtype: str
        """
        return self._plan_end_date

    @plan_end_date.setter
    def plan_end_date(self, plan_end_date):
        r"""Sets the plan_end_date of this PlanCreateParam.

        **参数解释**： 计划完成时间，格式为yyyy-MM-dd，如2024-01-01。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param plan_end_date: The plan_end_date of this PlanCreateParam.
        :type plan_end_date: str
        """
        self._plan_end_date = plan_end_date

    @property
    def parent_id(self):
        r"""Gets the parent_id of this PlanCreateParam.

        **参数解释**： 父计划ID，当category为Iteration时必填，用于指定所属的发布计划。 **约束限制**： category为Iteration时必填。 **取值范围**： 长度为18~19个字符的数字字符串。 **默认取值**： 不涉及。

        :return: The parent_id of this PlanCreateParam.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this PlanCreateParam.

        **参数解释**： 父计划ID，当category为Iteration时必填，用于指定所属的发布计划。 **约束限制**： category为Iteration时必填。 **取值范围**： 长度为18~19个字符的数字字符串。 **默认取值**： 不涉及。

        :param parent_id: The parent_id of this PlanCreateParam.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def workload(self):
        r"""Gets the workload of this PlanCreateParam.

        **参数解释**： 预估工作量，用于标识计划所需的人力投入，单位人/天。 **约束限制**： 不涉及。 **取值范围**： 0~11个字符。 **默认取值**： 不涉及。

        :return: The workload of this PlanCreateParam.
        :rtype: str
        """
        return self._workload

    @workload.setter
    def workload(self, workload):
        r"""Sets the workload of this PlanCreateParam.

        **参数解释**： 预估工作量，用于标识计划所需的人力投入，单位人/天。 **约束限制**： 不涉及。 **取值范围**： 0~11个字符。 **默认取值**： 不涉及。

        :param workload: The workload of this PlanCreateParam.
        :type workload: str
        """
        self._workload = workload

    @property
    def owner(self):
        r"""Gets the owner of this PlanCreateParam.

        **参数解释**： 责任人ID，标识计划的负责人。 **约束限制**： 不涉及。 **取值范围**： 长度为32个字符。 **默认取值**： 不涉及。

        :return: The owner of this PlanCreateParam.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this PlanCreateParam.

        **参数解释**： 责任人ID，标识计划的负责人。 **约束限制**： 不涉及。 **取值范围**： 长度为32个字符。 **默认取值**： 不涉及。

        :param owner: The owner of this PlanCreateParam.
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
        if not isinstance(other, PlanCreateParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
