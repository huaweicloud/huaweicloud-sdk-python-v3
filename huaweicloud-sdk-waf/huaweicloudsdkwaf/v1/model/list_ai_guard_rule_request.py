# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAiGuardRuleRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'name': 'str',
        'status': 'str',
        'detect_opt': 'str',
        'detect_type': 'str',
        'with_template': 'bool'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'limit': 'limit',
        'offset': 'offset',
        'name': 'name',
        'status': 'status',
        'detect_opt': 'detect_opt',
        'detect_type': 'detect_type',
        'with_template': 'with_template'
    }

    def __init__(self, policy_id=None, limit=None, offset=None, name=None, status=None, detect_opt=None, detect_type=None, with_template=None):
        r"""ListAiGuardRuleRequest

        The model defined in huaweicloud sdk

        :param policy_id: **参数解释：** 策略ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type policy_id: str
        :param limit: **参数解释：** 最大数量 **约束限制：** 不涉及 **取值范围：** 1-1000 **默认取值：** 10
        :type limit: int
        :param offset: **参数解释：** 偏移量 **约束限制：** 不涉及 **取值范围：** 0-10000 **默认取值：** 0
        :type offset: int
        :param name: **参数解释：** 规则名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type name: str
        :param status: **参数解释：** 规则状态 **约束限制：** 不涉及 **取值范围：** enable, disable **默认取值：** 不涉及
        :type status: str
        :param detect_opt: **参数解释：** 检测选项类型 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type detect_opt: str
        :param detect_type: **参数解释：** 检测类型 **约束限制：** 不涉及 **取值范围：** text(文本检测), image(图片检测) **默认取值：** 不涉及
        :type detect_type: str
        :param with_template: **参数解释：** 是否查询模板规则 **约束限制：** 不涉及 **取值范围：** true, false **默认取值：** 不涉及
        :type with_template: bool
        """
        
        

        self._policy_id = None
        self._limit = None
        self._offset = None
        self._name = None
        self._status = None
        self._detect_opt = None
        self._detect_type = None
        self._with_template = None
        self.discriminator = None

        self.policy_id = policy_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if detect_opt is not None:
            self.detect_opt = detect_opt
        if detect_type is not None:
            self.detect_type = detect_type
        if with_template is not None:
            self.with_template = with_template

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ListAiGuardRuleRequest.

        **参数解释：** 策略ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The policy_id of this ListAiGuardRuleRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ListAiGuardRuleRequest.

        **参数解释：** 策略ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param policy_id: The policy_id of this ListAiGuardRuleRequest.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def limit(self):
        r"""Gets the limit of this ListAiGuardRuleRequest.

        **参数解释：** 最大数量 **约束限制：** 不涉及 **取值范围：** 1-1000 **默认取值：** 10

        :return: The limit of this ListAiGuardRuleRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAiGuardRuleRequest.

        **参数解释：** 最大数量 **约束限制：** 不涉及 **取值范围：** 1-1000 **默认取值：** 10

        :param limit: The limit of this ListAiGuardRuleRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListAiGuardRuleRequest.

        **参数解释：** 偏移量 **约束限制：** 不涉及 **取值范围：** 0-10000 **默认取值：** 0

        :return: The offset of this ListAiGuardRuleRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAiGuardRuleRequest.

        **参数解释：** 偏移量 **约束限制：** 不涉及 **取值范围：** 0-10000 **默认取值：** 0

        :param offset: The offset of this ListAiGuardRuleRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def name(self):
        r"""Gets the name of this ListAiGuardRuleRequest.

        **参数解释：** 规则名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The name of this ListAiGuardRuleRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListAiGuardRuleRequest.

        **参数解释：** 规则名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param name: The name of this ListAiGuardRuleRequest.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ListAiGuardRuleRequest.

        **参数解释：** 规则状态 **约束限制：** 不涉及 **取值范围：** enable, disable **默认取值：** 不涉及

        :return: The status of this ListAiGuardRuleRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListAiGuardRuleRequest.

        **参数解释：** 规则状态 **约束限制：** 不涉及 **取值范围：** enable, disable **默认取值：** 不涉及

        :param status: The status of this ListAiGuardRuleRequest.
        :type status: str
        """
        self._status = status

    @property
    def detect_opt(self):
        r"""Gets the detect_opt of this ListAiGuardRuleRequest.

        **参数解释：** 检测选项类型 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The detect_opt of this ListAiGuardRuleRequest.
        :rtype: str
        """
        return self._detect_opt

    @detect_opt.setter
    def detect_opt(self, detect_opt):
        r"""Sets the detect_opt of this ListAiGuardRuleRequest.

        **参数解释：** 检测选项类型 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param detect_opt: The detect_opt of this ListAiGuardRuleRequest.
        :type detect_opt: str
        """
        self._detect_opt = detect_opt

    @property
    def detect_type(self):
        r"""Gets the detect_type of this ListAiGuardRuleRequest.

        **参数解释：** 检测类型 **约束限制：** 不涉及 **取值范围：** text(文本检测), image(图片检测) **默认取值：** 不涉及

        :return: The detect_type of this ListAiGuardRuleRequest.
        :rtype: str
        """
        return self._detect_type

    @detect_type.setter
    def detect_type(self, detect_type):
        r"""Sets the detect_type of this ListAiGuardRuleRequest.

        **参数解释：** 检测类型 **约束限制：** 不涉及 **取值范围：** text(文本检测), image(图片检测) **默认取值：** 不涉及

        :param detect_type: The detect_type of this ListAiGuardRuleRequest.
        :type detect_type: str
        """
        self._detect_type = detect_type

    @property
    def with_template(self):
        r"""Gets the with_template of this ListAiGuardRuleRequest.

        **参数解释：** 是否查询模板规则 **约束限制：** 不涉及 **取值范围：** true, false **默认取值：** 不涉及

        :return: The with_template of this ListAiGuardRuleRequest.
        :rtype: bool
        """
        return self._with_template

    @with_template.setter
    def with_template(self, with_template):
        r"""Sets the with_template of this ListAiGuardRuleRequest.

        **参数解释：** 是否查询模板规则 **约束限制：** 不涉及 **取值范围：** true, false **默认取值：** 不涉及

        :param with_template: The with_template of this ListAiGuardRuleRequest.
        :type with_template: bool
        """
        self._with_template = with_template

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
        if not isinstance(other, ListAiGuardRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
