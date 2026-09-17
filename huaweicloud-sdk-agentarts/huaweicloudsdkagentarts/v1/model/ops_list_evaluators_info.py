# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsListEvaluatorsInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'base_info': 'OpsEvaluatorBaseInfo',
        'evaluator_id': 'str',
        'account_id': 'str',
        'name': 'str',
        'description': 'str',
        'evaluator_type': 'int',
        'turn_type': 'str',
        'latest_version': 'str',
        'current_version': 'EvaluationOpsCurrentVersion',
        'current_version_id': 'str',
        'reference_count': 'int',
        'tags': 'list[OpsTmsTag]'
    }

    attribute_map = {
        'base_info': 'base_info',
        'evaluator_id': 'evaluator_id',
        'account_id': 'account_id',
        'name': 'name',
        'description': 'description',
        'evaluator_type': 'evaluator_type',
        'turn_type': 'turn_type',
        'latest_version': 'latest_version',
        'current_version': 'current_version',
        'current_version_id': 'current_version_id',
        'reference_count': 'reference_count',
        'tags': 'tags'
    }

    def __init__(self, base_info=None, evaluator_id=None, account_id=None, name=None, description=None, evaluator_type=None, turn_type=None, latest_version=None, current_version=None, current_version_id=None, reference_count=None, tags=None):
        r"""OpsListEvaluatorsInfo

        The model defined in huaweicloud sdk

        :param base_info: 
        :type base_info: :class:`huaweicloudsdkagentarts.v1.OpsEvaluatorBaseInfo`
        :param evaluator_id: **参数解释：** 评估器的唯一标识符。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 
        :type evaluator_id: str
        :param account_id: **参数解释：** 评估器所属的租户账号ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 
        :type account_id: str
        :param name: **参数解释：** 评估器的名称，用于界面展示和检索。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 
        :type name: str
        :param description: **参数解释：** 评估器的功能描述或业务用途说明。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 
        :type description: str
        :param evaluator_type: **参数解释：** 评估器的类型编码，用于区分不同的逻辑实现（如自定义评估器或系统评估器）。 **约束限制：** 不涉及。 **取值范围：** - 1：模型评估器 - 2：代码评估器 - 3：自适应评估器（自适应评估模式，可根据上下文与历史结果动态调整评判规则） 
        :type evaluator_type: int
        :param turn_type: **参数解释：** 评估器的对话轮次类型。 **约束限制：** 不涉及。 **取值范围：** - single：单轮 - multi：多轮 
        :type turn_type: str
        :param latest_version: **参数解释：** 评估器的最新发布的版本号。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 
        :type latest_version: str
        :param current_version: 
        :type current_version: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsCurrentVersion`
        :param current_version_id: **参数解释：** 评估器当前生效版本的唯一标识符。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 
        :type current_version_id: str
        :param reference_count: **参数解释：** 该评估器被评估任务引用的次数。 **约束限制：** 不涉及。 **取值范围：** 非负整数。 
        :type reference_count: int
        :param tags: **参数解释：** 评估器绑定的TMS标签列表。数组元素引用OpsTmsTag对象。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTag`]
        """
        
        

        self._base_info = None
        self._evaluator_id = None
        self._account_id = None
        self._name = None
        self._description = None
        self._evaluator_type = None
        self._turn_type = None
        self._latest_version = None
        self._current_version = None
        self._current_version_id = None
        self._reference_count = None
        self._tags = None
        self.discriminator = None

        if base_info is not None:
            self.base_info = base_info
        if evaluator_id is not None:
            self.evaluator_id = evaluator_id
        if account_id is not None:
            self.account_id = account_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if evaluator_type is not None:
            self.evaluator_type = evaluator_type
        if turn_type is not None:
            self.turn_type = turn_type
        if latest_version is not None:
            self.latest_version = latest_version
        if current_version is not None:
            self.current_version = current_version
        if current_version_id is not None:
            self.current_version_id = current_version_id
        if reference_count is not None:
            self.reference_count = reference_count
        if tags is not None:
            self.tags = tags

    @property
    def base_info(self):
        r"""Gets the base_info of this OpsListEvaluatorsInfo.

        :return: The base_info of this OpsListEvaluatorsInfo.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsEvaluatorBaseInfo`
        """
        return self._base_info

    @base_info.setter
    def base_info(self, base_info):
        r"""Sets the base_info of this OpsListEvaluatorsInfo.

        :param base_info: The base_info of this OpsListEvaluatorsInfo.
        :type base_info: :class:`huaweicloudsdkagentarts.v1.OpsEvaluatorBaseInfo`
        """
        self._base_info = base_info

    @property
    def evaluator_id(self):
        r"""Gets the evaluator_id of this OpsListEvaluatorsInfo.

        **参数解释：** 评估器的唯一标识符。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 

        :return: The evaluator_id of this OpsListEvaluatorsInfo.
        :rtype: str
        """
        return self._evaluator_id

    @evaluator_id.setter
    def evaluator_id(self, evaluator_id):
        r"""Sets the evaluator_id of this OpsListEvaluatorsInfo.

        **参数解释：** 评估器的唯一标识符。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 

        :param evaluator_id: The evaluator_id of this OpsListEvaluatorsInfo.
        :type evaluator_id: str
        """
        self._evaluator_id = evaluator_id

    @property
    def account_id(self):
        r"""Gets the account_id of this OpsListEvaluatorsInfo.

        **参数解释：** 评估器所属的租户账号ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 

        :return: The account_id of this OpsListEvaluatorsInfo.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        r"""Sets the account_id of this OpsListEvaluatorsInfo.

        **参数解释：** 评估器所属的租户账号ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 

        :param account_id: The account_id of this OpsListEvaluatorsInfo.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def name(self):
        r"""Gets the name of this OpsListEvaluatorsInfo.

        **参数解释：** 评估器的名称，用于界面展示和检索。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 

        :return: The name of this OpsListEvaluatorsInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this OpsListEvaluatorsInfo.

        **参数解释：** 评估器的名称，用于界面展示和检索。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 

        :param name: The name of this OpsListEvaluatorsInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this OpsListEvaluatorsInfo.

        **参数解释：** 评估器的功能描述或业务用途说明。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 

        :return: The description of this OpsListEvaluatorsInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this OpsListEvaluatorsInfo.

        **参数解释：** 评估器的功能描述或业务用途说明。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 

        :param description: The description of this OpsListEvaluatorsInfo.
        :type description: str
        """
        self._description = description

    @property
    def evaluator_type(self):
        r"""Gets the evaluator_type of this OpsListEvaluatorsInfo.

        **参数解释：** 评估器的类型编码，用于区分不同的逻辑实现（如自定义评估器或系统评估器）。 **约束限制：** 不涉及。 **取值范围：** - 1：模型评估器 - 2：代码评估器 - 3：自适应评估器（自适应评估模式，可根据上下文与历史结果动态调整评判规则） 

        :return: The evaluator_type of this OpsListEvaluatorsInfo.
        :rtype: int
        """
        return self._evaluator_type

    @evaluator_type.setter
    def evaluator_type(self, evaluator_type):
        r"""Sets the evaluator_type of this OpsListEvaluatorsInfo.

        **参数解释：** 评估器的类型编码，用于区分不同的逻辑实现（如自定义评估器或系统评估器）。 **约束限制：** 不涉及。 **取值范围：** - 1：模型评估器 - 2：代码评估器 - 3：自适应评估器（自适应评估模式，可根据上下文与历史结果动态调整评判规则） 

        :param evaluator_type: The evaluator_type of this OpsListEvaluatorsInfo.
        :type evaluator_type: int
        """
        self._evaluator_type = evaluator_type

    @property
    def turn_type(self):
        r"""Gets the turn_type of this OpsListEvaluatorsInfo.

        **参数解释：** 评估器的对话轮次类型。 **约束限制：** 不涉及。 **取值范围：** - single：单轮 - multi：多轮 

        :return: The turn_type of this OpsListEvaluatorsInfo.
        :rtype: str
        """
        return self._turn_type

    @turn_type.setter
    def turn_type(self, turn_type):
        r"""Sets the turn_type of this OpsListEvaluatorsInfo.

        **参数解释：** 评估器的对话轮次类型。 **约束限制：** 不涉及。 **取值范围：** - single：单轮 - multi：多轮 

        :param turn_type: The turn_type of this OpsListEvaluatorsInfo.
        :type turn_type: str
        """
        self._turn_type = turn_type

    @property
    def latest_version(self):
        r"""Gets the latest_version of this OpsListEvaluatorsInfo.

        **参数解释：** 评估器的最新发布的版本号。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 

        :return: The latest_version of this OpsListEvaluatorsInfo.
        :rtype: str
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        r"""Sets the latest_version of this OpsListEvaluatorsInfo.

        **参数解释：** 评估器的最新发布的版本号。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 

        :param latest_version: The latest_version of this OpsListEvaluatorsInfo.
        :type latest_version: str
        """
        self._latest_version = latest_version

    @property
    def current_version(self):
        r"""Gets the current_version of this OpsListEvaluatorsInfo.

        :return: The current_version of this OpsListEvaluatorsInfo.
        :rtype: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsCurrentVersion`
        """
        return self._current_version

    @current_version.setter
    def current_version(self, current_version):
        r"""Sets the current_version of this OpsListEvaluatorsInfo.

        :param current_version: The current_version of this OpsListEvaluatorsInfo.
        :type current_version: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsCurrentVersion`
        """
        self._current_version = current_version

    @property
    def current_version_id(self):
        r"""Gets the current_version_id of this OpsListEvaluatorsInfo.

        **参数解释：** 评估器当前生效版本的唯一标识符。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 

        :return: The current_version_id of this OpsListEvaluatorsInfo.
        :rtype: str
        """
        return self._current_version_id

    @current_version_id.setter
    def current_version_id(self, current_version_id):
        r"""Sets the current_version_id of this OpsListEvaluatorsInfo.

        **参数解释：** 评估器当前生效版本的唯一标识符。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 

        :param current_version_id: The current_version_id of this OpsListEvaluatorsInfo.
        :type current_version_id: str
        """
        self._current_version_id = current_version_id

    @property
    def reference_count(self):
        r"""Gets the reference_count of this OpsListEvaluatorsInfo.

        **参数解释：** 该评估器被评估任务引用的次数。 **约束限制：** 不涉及。 **取值范围：** 非负整数。 

        :return: The reference_count of this OpsListEvaluatorsInfo.
        :rtype: int
        """
        return self._reference_count

    @reference_count.setter
    def reference_count(self, reference_count):
        r"""Sets the reference_count of this OpsListEvaluatorsInfo.

        **参数解释：** 该评估器被评估任务引用的次数。 **约束限制：** 不涉及。 **取值范围：** 非负整数。 

        :param reference_count: The reference_count of this OpsListEvaluatorsInfo.
        :type reference_count: int
        """
        self._reference_count = reference_count

    @property
    def tags(self):
        r"""Gets the tags of this OpsListEvaluatorsInfo.

        **参数解释：** 评估器绑定的TMS标签列表。数组元素引用OpsTmsTag对象。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 

        :return: The tags of this OpsListEvaluatorsInfo.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this OpsListEvaluatorsInfo.

        **参数解释：** 评估器绑定的TMS标签列表。数组元素引用OpsTmsTag对象。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 

        :param tags: The tags of this OpsListEvaluatorsInfo.
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTag`]
        """
        self._tags = tags

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
        if not isinstance(other, OpsListEvaluatorsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
