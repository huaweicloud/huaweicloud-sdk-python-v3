# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsEvaluatorsResponseBodyEvaluators:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'evaluator_id': 'str',
        'name': 'str',
        'description': 'str',
        'evaluator_type': 'int',
        'box_type': 'str',
        'builtin': 'bool',
        'latest_version': 'str',
        'draft_submitted': 'bool',
        'tags': 'list[OpsTmsTag]'
    }

    attribute_map = {
        'evaluator_id': 'evaluator_id',
        'name': 'name',
        'description': 'description',
        'evaluator_type': 'evaluator_type',
        'box_type': 'box_type',
        'builtin': 'builtin',
        'latest_version': 'latest_version',
        'draft_submitted': 'draft_submitted',
        'tags': 'tags'
    }

    def __init__(self, evaluator_id=None, name=None, description=None, evaluator_type=None, box_type=None, builtin=None, latest_version=None, draft_submitted=None, tags=None):
        r"""ListOpsEvaluatorsResponseBodyEvaluators

        The model defined in huaweicloud sdk

        :param evaluator_id: **参数解释** 评估器的唯一标识符。 **取值范围** 系统生成的ID字符串。 
        :type evaluator_id: str
        :param name: **参数解释** 评估器的名称，用于界面展示和检索。 **取值范围** 任意字符串。 
        :type name: str
        :param description: **参数解释** 评估器的功能描述或业务用途说明。 **取值范围** 任意字符串。 
        :type description: str
        :param evaluator_type: **参数解释** 评估器的类型编码，用于区分不同的逻辑实现（如自定义评估器或系统评估器）。 **取值范围** 整型编码。 
        :type evaluator_type: int
        :param box_type: **参数解释** 评估器的可见性或黑白盒属性。 **取值范围** White (白盒), Black (黑盒)。 
        :type box_type: str
        :param builtin: **参数解释** 标识该评估器是否为系统预置。 **取值范围** true (是), false (否)。 
        :type builtin: bool
        :param latest_version: **参数解释** 评估器的最新发布的版本号。 **取值范围** 如 0.0.2 格式的版本字符串。 
        :type latest_version: str
        :param draft_submitted: **参数解释** 标识当前的草稿内容是否已经提交。 **取值范围** true (已提交), false (未提交)。 
        :type draft_submitted: bool
        :param tags: **参数解释** 评估器绑定的TMS标签列表。数组元素引用OpsTmsTag对象。 **约束限制** 不涉及。 **取值范围** 不涉及。 
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTag`]
        """
        
        

        self._evaluator_id = None
        self._name = None
        self._description = None
        self._evaluator_type = None
        self._box_type = None
        self._builtin = None
        self._latest_version = None
        self._draft_submitted = None
        self._tags = None
        self.discriminator = None

        if evaluator_id is not None:
            self.evaluator_id = evaluator_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if evaluator_type is not None:
            self.evaluator_type = evaluator_type
        if box_type is not None:
            self.box_type = box_type
        if builtin is not None:
            self.builtin = builtin
        if latest_version is not None:
            self.latest_version = latest_version
        if draft_submitted is not None:
            self.draft_submitted = draft_submitted
        if tags is not None:
            self.tags = tags

    @property
    def evaluator_id(self):
        r"""Gets the evaluator_id of this ListOpsEvaluatorsResponseBodyEvaluators.

        **参数解释** 评估器的唯一标识符。 **取值范围** 系统生成的ID字符串。 

        :return: The evaluator_id of this ListOpsEvaluatorsResponseBodyEvaluators.
        :rtype: str
        """
        return self._evaluator_id

    @evaluator_id.setter
    def evaluator_id(self, evaluator_id):
        r"""Sets the evaluator_id of this ListOpsEvaluatorsResponseBodyEvaluators.

        **参数解释** 评估器的唯一标识符。 **取值范围** 系统生成的ID字符串。 

        :param evaluator_id: The evaluator_id of this ListOpsEvaluatorsResponseBodyEvaluators.
        :type evaluator_id: str
        """
        self._evaluator_id = evaluator_id

    @property
    def name(self):
        r"""Gets the name of this ListOpsEvaluatorsResponseBodyEvaluators.

        **参数解释** 评估器的名称，用于界面展示和检索。 **取值范围** 任意字符串。 

        :return: The name of this ListOpsEvaluatorsResponseBodyEvaluators.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListOpsEvaluatorsResponseBodyEvaluators.

        **参数解释** 评估器的名称，用于界面展示和检索。 **取值范围** 任意字符串。 

        :param name: The name of this ListOpsEvaluatorsResponseBodyEvaluators.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ListOpsEvaluatorsResponseBodyEvaluators.

        **参数解释** 评估器的功能描述或业务用途说明。 **取值范围** 任意字符串。 

        :return: The description of this ListOpsEvaluatorsResponseBodyEvaluators.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListOpsEvaluatorsResponseBodyEvaluators.

        **参数解释** 评估器的功能描述或业务用途说明。 **取值范围** 任意字符串。 

        :param description: The description of this ListOpsEvaluatorsResponseBodyEvaluators.
        :type description: str
        """
        self._description = description

    @property
    def evaluator_type(self):
        r"""Gets the evaluator_type of this ListOpsEvaluatorsResponseBodyEvaluators.

        **参数解释** 评估器的类型编码，用于区分不同的逻辑实现（如自定义评估器或系统评估器）。 **取值范围** 整型编码。 

        :return: The evaluator_type of this ListOpsEvaluatorsResponseBodyEvaluators.
        :rtype: int
        """
        return self._evaluator_type

    @evaluator_type.setter
    def evaluator_type(self, evaluator_type):
        r"""Sets the evaluator_type of this ListOpsEvaluatorsResponseBodyEvaluators.

        **参数解释** 评估器的类型编码，用于区分不同的逻辑实现（如自定义评估器或系统评估器）。 **取值范围** 整型编码。 

        :param evaluator_type: The evaluator_type of this ListOpsEvaluatorsResponseBodyEvaluators.
        :type evaluator_type: int
        """
        self._evaluator_type = evaluator_type

    @property
    def box_type(self):
        r"""Gets the box_type of this ListOpsEvaluatorsResponseBodyEvaluators.

        **参数解释** 评估器的可见性或黑白盒属性。 **取值范围** White (白盒), Black (黑盒)。 

        :return: The box_type of this ListOpsEvaluatorsResponseBodyEvaluators.
        :rtype: str
        """
        return self._box_type

    @box_type.setter
    def box_type(self, box_type):
        r"""Sets the box_type of this ListOpsEvaluatorsResponseBodyEvaluators.

        **参数解释** 评估器的可见性或黑白盒属性。 **取值范围** White (白盒), Black (黑盒)。 

        :param box_type: The box_type of this ListOpsEvaluatorsResponseBodyEvaluators.
        :type box_type: str
        """
        self._box_type = box_type

    @property
    def builtin(self):
        r"""Gets the builtin of this ListOpsEvaluatorsResponseBodyEvaluators.

        **参数解释** 标识该评估器是否为系统预置。 **取值范围** true (是), false (否)。 

        :return: The builtin of this ListOpsEvaluatorsResponseBodyEvaluators.
        :rtype: bool
        """
        return self._builtin

    @builtin.setter
    def builtin(self, builtin):
        r"""Sets the builtin of this ListOpsEvaluatorsResponseBodyEvaluators.

        **参数解释** 标识该评估器是否为系统预置。 **取值范围** true (是), false (否)。 

        :param builtin: The builtin of this ListOpsEvaluatorsResponseBodyEvaluators.
        :type builtin: bool
        """
        self._builtin = builtin

    @property
    def latest_version(self):
        r"""Gets the latest_version of this ListOpsEvaluatorsResponseBodyEvaluators.

        **参数解释** 评估器的最新发布的版本号。 **取值范围** 如 0.0.2 格式的版本字符串。 

        :return: The latest_version of this ListOpsEvaluatorsResponseBodyEvaluators.
        :rtype: str
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        r"""Sets the latest_version of this ListOpsEvaluatorsResponseBodyEvaluators.

        **参数解释** 评估器的最新发布的版本号。 **取值范围** 如 0.0.2 格式的版本字符串。 

        :param latest_version: The latest_version of this ListOpsEvaluatorsResponseBodyEvaluators.
        :type latest_version: str
        """
        self._latest_version = latest_version

    @property
    def draft_submitted(self):
        r"""Gets the draft_submitted of this ListOpsEvaluatorsResponseBodyEvaluators.

        **参数解释** 标识当前的草稿内容是否已经提交。 **取值范围** true (已提交), false (未提交)。 

        :return: The draft_submitted of this ListOpsEvaluatorsResponseBodyEvaluators.
        :rtype: bool
        """
        return self._draft_submitted

    @draft_submitted.setter
    def draft_submitted(self, draft_submitted):
        r"""Sets the draft_submitted of this ListOpsEvaluatorsResponseBodyEvaluators.

        **参数解释** 标识当前的草稿内容是否已经提交。 **取值范围** true (已提交), false (未提交)。 

        :param draft_submitted: The draft_submitted of this ListOpsEvaluatorsResponseBodyEvaluators.
        :type draft_submitted: bool
        """
        self._draft_submitted = draft_submitted

    @property
    def tags(self):
        r"""Gets the tags of this ListOpsEvaluatorsResponseBodyEvaluators.

        **参数解释** 评估器绑定的TMS标签列表。数组元素引用OpsTmsTag对象。 **约束限制** 不涉及。 **取值范围** 不涉及。 

        :return: The tags of this ListOpsEvaluatorsResponseBodyEvaluators.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListOpsEvaluatorsResponseBodyEvaluators.

        **参数解释** 评估器绑定的TMS标签列表。数组元素引用OpsTmsTag对象。 **约束限制** 不涉及。 **取值范围** 不涉及。 

        :param tags: The tags of this ListOpsEvaluatorsResponseBodyEvaluators.
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
        if not isinstance(other, ListOpsEvaluatorsResponseBodyEvaluators):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
