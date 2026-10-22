# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAiguardTemplateRuleRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_id': 'str',
        'name': 'str',
        'action': 'AiGuardRuleAction',
        'status': 'str',
        'supported_language_labels': 'list[str]',
        'not_supported_language_action': 'str',
        'custom_answers_id': 'str',
        'custom_answers_name': 'str'
    }

    attribute_map = {
        'template_id': 'template_id',
        'name': 'name',
        'action': 'action',
        'status': 'status',
        'supported_language_labels': 'supported_language_labels',
        'not_supported_language_action': 'not_supported_language_action',
        'custom_answers_id': 'custom_answers_id',
        'custom_answers_name': 'custom_answers_name'
    }

    def __init__(self, template_id=None, name=None, action=None, status=None, supported_language_labels=None, not_supported_language_action=None, custom_answers_id=None, custom_answers_name=None):
        r"""CreateAiguardTemplateRuleRequestBody

        The model defined in huaweicloud sdk

        :param template_id: 模板ID（8位字符串）
        :type template_id: str
        :param name: 规则名称，非必选，通过模板生成
        :type name: str
        :param action: 
        :type action: :class:`huaweicloudsdkwaf.v1.AiGuardRuleAction`
        :param status: 规则状态，非必选：enable(启用), disable(禁用)
        :type status: str
        :param supported_language_labels: 语言检测标签列表，只有使用语言模板添加时生效
        :type supported_language_labels: list[str]
        :param not_supported_language_action: 其他语言检测动作，只有使用语言模板添加时生效。pass: 放行, block: 拦截
        :type not_supported_language_action: str
        :param custom_answers_id: 自定义代答库ID（可选，当action.category&#x3D;block时有效）
        :type custom_answers_id: str
        :param custom_answers_name: 自定义代答库名称（可选，当action.category&#x3D;block时有效，与custom_answers_id对应）
        :type custom_answers_name: str
        """
        
        

        self._template_id = None
        self._name = None
        self._action = None
        self._status = None
        self._supported_language_labels = None
        self._not_supported_language_action = None
        self._custom_answers_id = None
        self._custom_answers_name = None
        self.discriminator = None

        self.template_id = template_id
        if name is not None:
            self.name = name
        if action is not None:
            self.action = action
        if status is not None:
            self.status = status
        if supported_language_labels is not None:
            self.supported_language_labels = supported_language_labels
        if not_supported_language_action is not None:
            self.not_supported_language_action = not_supported_language_action
        if custom_answers_id is not None:
            self.custom_answers_id = custom_answers_id
        if custom_answers_name is not None:
            self.custom_answers_name = custom_answers_name

    @property
    def template_id(self):
        r"""Gets the template_id of this CreateAiguardTemplateRuleRequestBody.

        模板ID（8位字符串）

        :return: The template_id of this CreateAiguardTemplateRuleRequestBody.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this CreateAiguardTemplateRuleRequestBody.

        模板ID（8位字符串）

        :param template_id: The template_id of this CreateAiguardTemplateRuleRequestBody.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def name(self):
        r"""Gets the name of this CreateAiguardTemplateRuleRequestBody.

        规则名称，非必选，通过模板生成

        :return: The name of this CreateAiguardTemplateRuleRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateAiguardTemplateRuleRequestBody.

        规则名称，非必选，通过模板生成

        :param name: The name of this CreateAiguardTemplateRuleRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def action(self):
        r"""Gets the action of this CreateAiguardTemplateRuleRequestBody.

        :return: The action of this CreateAiguardTemplateRuleRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.AiGuardRuleAction`
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this CreateAiguardTemplateRuleRequestBody.

        :param action: The action of this CreateAiguardTemplateRuleRequestBody.
        :type action: :class:`huaweicloudsdkwaf.v1.AiGuardRuleAction`
        """
        self._action = action

    @property
    def status(self):
        r"""Gets the status of this CreateAiguardTemplateRuleRequestBody.

        规则状态，非必选：enable(启用), disable(禁用)

        :return: The status of this CreateAiguardTemplateRuleRequestBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateAiguardTemplateRuleRequestBody.

        规则状态，非必选：enable(启用), disable(禁用)

        :param status: The status of this CreateAiguardTemplateRuleRequestBody.
        :type status: str
        """
        self._status = status

    @property
    def supported_language_labels(self):
        r"""Gets the supported_language_labels of this CreateAiguardTemplateRuleRequestBody.

        语言检测标签列表，只有使用语言模板添加时生效

        :return: The supported_language_labels of this CreateAiguardTemplateRuleRequestBody.
        :rtype: list[str]
        """
        return self._supported_language_labels

    @supported_language_labels.setter
    def supported_language_labels(self, supported_language_labels):
        r"""Sets the supported_language_labels of this CreateAiguardTemplateRuleRequestBody.

        语言检测标签列表，只有使用语言模板添加时生效

        :param supported_language_labels: The supported_language_labels of this CreateAiguardTemplateRuleRequestBody.
        :type supported_language_labels: list[str]
        """
        self._supported_language_labels = supported_language_labels

    @property
    def not_supported_language_action(self):
        r"""Gets the not_supported_language_action of this CreateAiguardTemplateRuleRequestBody.

        其他语言检测动作，只有使用语言模板添加时生效。pass: 放行, block: 拦截

        :return: The not_supported_language_action of this CreateAiguardTemplateRuleRequestBody.
        :rtype: str
        """
        return self._not_supported_language_action

    @not_supported_language_action.setter
    def not_supported_language_action(self, not_supported_language_action):
        r"""Sets the not_supported_language_action of this CreateAiguardTemplateRuleRequestBody.

        其他语言检测动作，只有使用语言模板添加时生效。pass: 放行, block: 拦截

        :param not_supported_language_action: The not_supported_language_action of this CreateAiguardTemplateRuleRequestBody.
        :type not_supported_language_action: str
        """
        self._not_supported_language_action = not_supported_language_action

    @property
    def custom_answers_id(self):
        r"""Gets the custom_answers_id of this CreateAiguardTemplateRuleRequestBody.

        自定义代答库ID（可选，当action.category=block时有效）

        :return: The custom_answers_id of this CreateAiguardTemplateRuleRequestBody.
        :rtype: str
        """
        return self._custom_answers_id

    @custom_answers_id.setter
    def custom_answers_id(self, custom_answers_id):
        r"""Sets the custom_answers_id of this CreateAiguardTemplateRuleRequestBody.

        自定义代答库ID（可选，当action.category=block时有效）

        :param custom_answers_id: The custom_answers_id of this CreateAiguardTemplateRuleRequestBody.
        :type custom_answers_id: str
        """
        self._custom_answers_id = custom_answers_id

    @property
    def custom_answers_name(self):
        r"""Gets the custom_answers_name of this CreateAiguardTemplateRuleRequestBody.

        自定义代答库名称（可选，当action.category=block时有效，与custom_answers_id对应）

        :return: The custom_answers_name of this CreateAiguardTemplateRuleRequestBody.
        :rtype: str
        """
        return self._custom_answers_name

    @custom_answers_name.setter
    def custom_answers_name(self, custom_answers_name):
        r"""Sets the custom_answers_name of this CreateAiguardTemplateRuleRequestBody.

        自定义代答库名称（可选，当action.category=block时有效，与custom_answers_id对应）

        :param custom_answers_name: The custom_answers_name of this CreateAiguardTemplateRuleRequestBody.
        :type custom_answers_name: str
        """
        self._custom_answers_name = custom_answers_name

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
        if not isinstance(other, CreateAiguardTemplateRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
