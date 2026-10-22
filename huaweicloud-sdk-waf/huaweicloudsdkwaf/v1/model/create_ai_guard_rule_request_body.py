# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAiGuardRuleRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'detect_opts': 'list[DetectOpt]',
        'action': 'AiGuardRuleAction',
        'detect_labels': 'DetectLabels',
        'not_supported_language_action': 'str',
        'detect_target': 'str',
        'description': 'str',
        'custom_answers_id': 'str',
        'custom_answers_name': 'str',
        'abuse_config': 'AbuseConfig',
        'topic_config': 'TopicConfig'
    }

    attribute_map = {
        'name': 'name',
        'detect_opts': 'detect_opts',
        'action': 'action',
        'detect_labels': 'detect_labels',
        'not_supported_language_action': 'not_supported_language_action',
        'detect_target': 'detect_target',
        'description': 'description',
        'custom_answers_id': 'custom_answers_id',
        'custom_answers_name': 'custom_answers_name',
        'abuse_config': 'abuse_config',
        'topic_config': 'topic_config'
    }

    def __init__(self, name=None, detect_opts=None, action=None, detect_labels=None, not_supported_language_action=None, detect_target=None, description=None, custom_answers_id=None, custom_answers_name=None, abuse_config=None, topic_config=None):
        r"""CreateAiGuardRuleRequestBody

        The model defined in huaweicloud sdk

        :param name: 规则名称
        :type name: str
        :param detect_opts: 检测选项配置列表
        :type detect_opts: list[:class:`huaweicloudsdkwaf.v1.DetectOpt`]
        :param action: 
        :type action: :class:`huaweicloudsdkwaf.v1.AiGuardRuleAction`
        :param detect_labels: 
        :type detect_labels: :class:`huaweicloudsdkwaf.v1.DetectLabels`
        :param not_supported_language_action: 不支持语言的防护动作，支持pass和block
        :type not_supported_language_action: str
        :param detect_target: 检测目标，当detect_type&#x3D;image时生效，ocr代表图片中提取的文本，content代表图片语义
        :type detect_target: str
        :param description: 规则描述，最大长度1024
        :type description: str
        :param custom_answers_id: 自定义代答库ID（可选，当action.category&#x3D;block时有效）
        :type custom_answers_id: str
        :param custom_answers_name: 自定义代答库名称（可选，当action.category&#x3D;block时有效，与custom_answers_id对应）
        :type custom_answers_name: str
        :param abuse_config: 
        :type abuse_config: :class:`huaweicloudsdkwaf.v1.AbuseConfig`
        :param topic_config: 
        :type topic_config: :class:`huaweicloudsdkwaf.v1.TopicConfig`
        """
        
        

        self._name = None
        self._detect_opts = None
        self._action = None
        self._detect_labels = None
        self._not_supported_language_action = None
        self._detect_target = None
        self._description = None
        self._custom_answers_id = None
        self._custom_answers_name = None
        self._abuse_config = None
        self._topic_config = None
        self.discriminator = None

        self.name = name
        self.detect_opts = detect_opts
        self.action = action
        self.detect_labels = detect_labels
        if not_supported_language_action is not None:
            self.not_supported_language_action = not_supported_language_action
        if detect_target is not None:
            self.detect_target = detect_target
        if description is not None:
            self.description = description
        if custom_answers_id is not None:
            self.custom_answers_id = custom_answers_id
        if custom_answers_name is not None:
            self.custom_answers_name = custom_answers_name
        if abuse_config is not None:
            self.abuse_config = abuse_config
        if topic_config is not None:
            self.topic_config = topic_config

    @property
    def name(self):
        r"""Gets the name of this CreateAiGuardRuleRequestBody.

        规则名称

        :return: The name of this CreateAiGuardRuleRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateAiGuardRuleRequestBody.

        规则名称

        :param name: The name of this CreateAiGuardRuleRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def detect_opts(self):
        r"""Gets the detect_opts of this CreateAiGuardRuleRequestBody.

        检测选项配置列表

        :return: The detect_opts of this CreateAiGuardRuleRequestBody.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.DetectOpt`]
        """
        return self._detect_opts

    @detect_opts.setter
    def detect_opts(self, detect_opts):
        r"""Sets the detect_opts of this CreateAiGuardRuleRequestBody.

        检测选项配置列表

        :param detect_opts: The detect_opts of this CreateAiGuardRuleRequestBody.
        :type detect_opts: list[:class:`huaweicloudsdkwaf.v1.DetectOpt`]
        """
        self._detect_opts = detect_opts

    @property
    def action(self):
        r"""Gets the action of this CreateAiGuardRuleRequestBody.

        :return: The action of this CreateAiGuardRuleRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.AiGuardRuleAction`
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this CreateAiGuardRuleRequestBody.

        :param action: The action of this CreateAiGuardRuleRequestBody.
        :type action: :class:`huaweicloudsdkwaf.v1.AiGuardRuleAction`
        """
        self._action = action

    @property
    def detect_labels(self):
        r"""Gets the detect_labels of this CreateAiGuardRuleRequestBody.

        :return: The detect_labels of this CreateAiGuardRuleRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.DetectLabels`
        """
        return self._detect_labels

    @detect_labels.setter
    def detect_labels(self, detect_labels):
        r"""Sets the detect_labels of this CreateAiGuardRuleRequestBody.

        :param detect_labels: The detect_labels of this CreateAiGuardRuleRequestBody.
        :type detect_labels: :class:`huaweicloudsdkwaf.v1.DetectLabels`
        """
        self._detect_labels = detect_labels

    @property
    def not_supported_language_action(self):
        r"""Gets the not_supported_language_action of this CreateAiGuardRuleRequestBody.

        不支持语言的防护动作，支持pass和block

        :return: The not_supported_language_action of this CreateAiGuardRuleRequestBody.
        :rtype: str
        """
        return self._not_supported_language_action

    @not_supported_language_action.setter
    def not_supported_language_action(self, not_supported_language_action):
        r"""Sets the not_supported_language_action of this CreateAiGuardRuleRequestBody.

        不支持语言的防护动作，支持pass和block

        :param not_supported_language_action: The not_supported_language_action of this CreateAiGuardRuleRequestBody.
        :type not_supported_language_action: str
        """
        self._not_supported_language_action = not_supported_language_action

    @property
    def detect_target(self):
        r"""Gets the detect_target of this CreateAiGuardRuleRequestBody.

        检测目标，当detect_type=image时生效，ocr代表图片中提取的文本，content代表图片语义

        :return: The detect_target of this CreateAiGuardRuleRequestBody.
        :rtype: str
        """
        return self._detect_target

    @detect_target.setter
    def detect_target(self, detect_target):
        r"""Sets the detect_target of this CreateAiGuardRuleRequestBody.

        检测目标，当detect_type=image时生效，ocr代表图片中提取的文本，content代表图片语义

        :param detect_target: The detect_target of this CreateAiGuardRuleRequestBody.
        :type detect_target: str
        """
        self._detect_target = detect_target

    @property
    def description(self):
        r"""Gets the description of this CreateAiGuardRuleRequestBody.

        规则描述，最大长度1024

        :return: The description of this CreateAiGuardRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateAiGuardRuleRequestBody.

        规则描述，最大长度1024

        :param description: The description of this CreateAiGuardRuleRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def custom_answers_id(self):
        r"""Gets the custom_answers_id of this CreateAiGuardRuleRequestBody.

        自定义代答库ID（可选，当action.category=block时有效）

        :return: The custom_answers_id of this CreateAiGuardRuleRequestBody.
        :rtype: str
        """
        return self._custom_answers_id

    @custom_answers_id.setter
    def custom_answers_id(self, custom_answers_id):
        r"""Sets the custom_answers_id of this CreateAiGuardRuleRequestBody.

        自定义代答库ID（可选，当action.category=block时有效）

        :param custom_answers_id: The custom_answers_id of this CreateAiGuardRuleRequestBody.
        :type custom_answers_id: str
        """
        self._custom_answers_id = custom_answers_id

    @property
    def custom_answers_name(self):
        r"""Gets the custom_answers_name of this CreateAiGuardRuleRequestBody.

        自定义代答库名称（可选，当action.category=block时有效，与custom_answers_id对应）

        :return: The custom_answers_name of this CreateAiGuardRuleRequestBody.
        :rtype: str
        """
        return self._custom_answers_name

    @custom_answers_name.setter
    def custom_answers_name(self, custom_answers_name):
        r"""Sets the custom_answers_name of this CreateAiGuardRuleRequestBody.

        自定义代答库名称（可选，当action.category=block时有效，与custom_answers_id对应）

        :param custom_answers_name: The custom_answers_name of this CreateAiGuardRuleRequestBody.
        :type custom_answers_name: str
        """
        self._custom_answers_name = custom_answers_name

    @property
    def abuse_config(self):
        r"""Gets the abuse_config of this CreateAiGuardRuleRequestBody.

        :return: The abuse_config of this CreateAiGuardRuleRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.AbuseConfig`
        """
        return self._abuse_config

    @abuse_config.setter
    def abuse_config(self, abuse_config):
        r"""Sets the abuse_config of this CreateAiGuardRuleRequestBody.

        :param abuse_config: The abuse_config of this CreateAiGuardRuleRequestBody.
        :type abuse_config: :class:`huaweicloudsdkwaf.v1.AbuseConfig`
        """
        self._abuse_config = abuse_config

    @property
    def topic_config(self):
        r"""Gets the topic_config of this CreateAiGuardRuleRequestBody.

        :return: The topic_config of this CreateAiGuardRuleRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.TopicConfig`
        """
        return self._topic_config

    @topic_config.setter
    def topic_config(self, topic_config):
        r"""Sets the topic_config of this CreateAiGuardRuleRequestBody.

        :param topic_config: The topic_config of this CreateAiGuardRuleRequestBody.
        :type topic_config: :class:`huaweicloudsdkwaf.v1.TopicConfig`
        """
        self._topic_config = topic_config

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
        if not isinstance(other, CreateAiGuardRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
