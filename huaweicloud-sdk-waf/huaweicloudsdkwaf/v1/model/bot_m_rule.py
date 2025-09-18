# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BotMRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'name': 'str',
        'description': 'str',
        'features': 'list[str]',
        'category': 'int',
        'sub_category': 'int',
        'defense_action': 'int',
        'created_time': 'int',
        'modified_time': 'int',
        'status': 'bool',
        'interaction_confidence': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'features': 'features',
        'category': 'category',
        'sub_category': 'sub_category',
        'defense_action': 'defense_action',
        'created_time': 'created_time',
        'modified_time': 'modified_time',
        'status': 'status',
        'interaction_confidence': 'interaction_confidence'
    }

    def __init__(self, id=None, name=None, description=None, features=None, category=None, sub_category=None, defense_action=None, created_time=None, modified_time=None, status=None, interaction_confidence=None):
        r"""BotMRule

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 规则ID，唯一标识当前BotM规则。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type id: int
        :param name: **参数解释：** 规则名称，用于标识当前BotM规则的名称。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type name: str
        :param description: **参数解释：** 规则描述，对当前BotM规则的功能说明。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type description: str
        :param features: **参数解释：** 规则列表，当前BotM规则包含的具体检测特征。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type features: list[str]
        :param category: **参数解释：** 规则所属类别，标识规则的一级分类（如0表示基础检测类）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type category: int
        :param sub_category: **参数解释：** 规则所属子类别，标识规则的二级分类（如0表示已知Bot子类）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type sub_category: int
        :param defense_action: **参数解释：** 规则对应的防护动作，标识触发规则后执行的动作（如0表示放行）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type defense_action: int
        :param created_time: **参数解释：** 规则创建的时间，时间戳（毫秒级）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type created_time: int
        :param modified_time: **参数解释：** 规则更新的时间，时间戳（毫秒级）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type modified_time: int
        :param status: **参数解释：** 规则目前是否被启用（true表示启用，false表示禁用）。 **约束限制：** 不涉及 **取值范围：** 仅支持true、false两个布尔值 **默认取值：** true
        :type status: bool
        :param interaction_confidence: **参数解释：** 交互置信度，标识主动交互检测的置信度阈值。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type interaction_confidence: int
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._features = None
        self._category = None
        self._sub_category = None
        self._defense_action = None
        self._created_time = None
        self._modified_time = None
        self._status = None
        self._interaction_confidence = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if features is not None:
            self.features = features
        if category is not None:
            self.category = category
        if sub_category is not None:
            self.sub_category = sub_category
        if defense_action is not None:
            self.defense_action = defense_action
        if created_time is not None:
            self.created_time = created_time
        if modified_time is not None:
            self.modified_time = modified_time
        if status is not None:
            self.status = status
        if interaction_confidence is not None:
            self.interaction_confidence = interaction_confidence

    @property
    def id(self):
        r"""Gets the id of this BotMRule.

        **参数解释：** 规则ID，唯一标识当前BotM规则。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The id of this BotMRule.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BotMRule.

        **参数解释：** 规则ID，唯一标识当前BotM规则。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param id: The id of this BotMRule.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this BotMRule.

        **参数解释：** 规则名称，用于标识当前BotM规则的名称。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The name of this BotMRule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BotMRule.

        **参数解释：** 规则名称，用于标识当前BotM规则的名称。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param name: The name of this BotMRule.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this BotMRule.

        **参数解释：** 规则描述，对当前BotM规则的功能说明。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The description of this BotMRule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this BotMRule.

        **参数解释：** 规则描述，对当前BotM规则的功能说明。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param description: The description of this BotMRule.
        :type description: str
        """
        self._description = description

    @property
    def features(self):
        r"""Gets the features of this BotMRule.

        **参数解释：** 规则列表，当前BotM规则包含的具体检测特征。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The features of this BotMRule.
        :rtype: list[str]
        """
        return self._features

    @features.setter
    def features(self, features):
        r"""Sets the features of this BotMRule.

        **参数解释：** 规则列表，当前BotM规则包含的具体检测特征。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param features: The features of this BotMRule.
        :type features: list[str]
        """
        self._features = features

    @property
    def category(self):
        r"""Gets the category of this BotMRule.

        **参数解释：** 规则所属类别，标识规则的一级分类（如0表示基础检测类）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The category of this BotMRule.
        :rtype: int
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this BotMRule.

        **参数解释：** 规则所属类别，标识规则的一级分类（如0表示基础检测类）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param category: The category of this BotMRule.
        :type category: int
        """
        self._category = category

    @property
    def sub_category(self):
        r"""Gets the sub_category of this BotMRule.

        **参数解释：** 规则所属子类别，标识规则的二级分类（如0表示已知Bot子类）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The sub_category of this BotMRule.
        :rtype: int
        """
        return self._sub_category

    @sub_category.setter
    def sub_category(self, sub_category):
        r"""Sets the sub_category of this BotMRule.

        **参数解释：** 规则所属子类别，标识规则的二级分类（如0表示已知Bot子类）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param sub_category: The sub_category of this BotMRule.
        :type sub_category: int
        """
        self._sub_category = sub_category

    @property
    def defense_action(self):
        r"""Gets the defense_action of this BotMRule.

        **参数解释：** 规则对应的防护动作，标识触发规则后执行的动作（如0表示放行）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The defense_action of this BotMRule.
        :rtype: int
        """
        return self._defense_action

    @defense_action.setter
    def defense_action(self, defense_action):
        r"""Sets the defense_action of this BotMRule.

        **参数解释：** 规则对应的防护动作，标识触发规则后执行的动作（如0表示放行）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param defense_action: The defense_action of this BotMRule.
        :type defense_action: int
        """
        self._defense_action = defense_action

    @property
    def created_time(self):
        r"""Gets the created_time of this BotMRule.

        **参数解释：** 规则创建的时间，时间戳（毫秒级）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The created_time of this BotMRule.
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this BotMRule.

        **参数解释：** 规则创建的时间，时间戳（毫秒级）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param created_time: The created_time of this BotMRule.
        :type created_time: int
        """
        self._created_time = created_time

    @property
    def modified_time(self):
        r"""Gets the modified_time of this BotMRule.

        **参数解释：** 规则更新的时间，时间戳（毫秒级）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The modified_time of this BotMRule.
        :rtype: int
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        r"""Sets the modified_time of this BotMRule.

        **参数解释：** 规则更新的时间，时间戳（毫秒级）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param modified_time: The modified_time of this BotMRule.
        :type modified_time: int
        """
        self._modified_time = modified_time

    @property
    def status(self):
        r"""Gets the status of this BotMRule.

        **参数解释：** 规则目前是否被启用（true表示启用，false表示禁用）。 **约束限制：** 不涉及 **取值范围：** 仅支持true、false两个布尔值 **默认取值：** true

        :return: The status of this BotMRule.
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BotMRule.

        **参数解释：** 规则目前是否被启用（true表示启用，false表示禁用）。 **约束限制：** 不涉及 **取值范围：** 仅支持true、false两个布尔值 **默认取值：** true

        :param status: The status of this BotMRule.
        :type status: bool
        """
        self._status = status

    @property
    def interaction_confidence(self):
        r"""Gets the interaction_confidence of this BotMRule.

        **参数解释：** 交互置信度，标识主动交互检测的置信度阈值。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The interaction_confidence of this BotMRule.
        :rtype: int
        """
        return self._interaction_confidence

    @interaction_confidence.setter
    def interaction_confidence(self, interaction_confidence):
        r"""Sets the interaction_confidence of this BotMRule.

        **参数解释：** 交互置信度，标识主动交互检测的置信度阈值。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param interaction_confidence: The interaction_confidence of this BotMRule.
        :type interaction_confidence: int
        """
        self._interaction_confidence = interaction_confidence

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BotMRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
