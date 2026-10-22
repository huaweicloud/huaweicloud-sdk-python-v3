# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAiGuardRuleResponse(SdkResponse):

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
        'name': 'str',
        'detect_type': 'str',
        'detect_target': 'str',
        'policy_id': 'str',
        'status': 'str',
        'detect_opts': 'list[DetectOpt]',
        'action': 'AiGuardRuleAction',
        'detect_labels': 'DetectLabels',
        'create_time': 'int',
        'update_time': 'int',
        'detect_labels_info': 'DetectLabelsInfo',
        'not_supported_language_action': 'str',
        'source': 'str',
        'source_id': 'str',
        'description': 'str',
        'custom_answers_id': 'str',
        'custom_answers_name': 'str',
        'abuse_config': 'AbuseConfig',
        'topic_config': 'TopicConfig'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'detect_type': 'detect_type',
        'detect_target': 'detect_target',
        'policy_id': 'policy_id',
        'status': 'status',
        'detect_opts': 'detect_opts',
        'action': 'action',
        'detect_labels': 'detect_labels',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'detect_labels_info': 'detect_labels_info',
        'not_supported_language_action': 'not_supported_language_action',
        'source': 'source',
        'source_id': 'source_id',
        'description': 'description',
        'custom_answers_id': 'custom_answers_id',
        'custom_answers_name': 'custom_answers_name',
        'abuse_config': 'abuse_config',
        'topic_config': 'topic_config'
    }

    def __init__(self, id=None, name=None, detect_type=None, detect_target=None, policy_id=None, status=None, detect_opts=None, action=None, detect_labels=None, create_time=None, update_time=None, detect_labels_info=None, not_supported_language_action=None, source=None, source_id=None, description=None, custom_answers_id=None, custom_answers_name=None, abuse_config=None, topic_config=None):
        r"""UpdateAiGuardRuleResponse

        The model defined in huaweicloud sdk

        :param id: 规则ID
        :type id: str
        :param name: 规则名称
        :type name: str
        :param detect_type: 检测类别。text: 文本检测, image: 图片检测，为null时代表文字
        :type detect_type: str
        :param detect_target: 检测目标，detect_type&#x3D;image时有效。ocr代表图片中提取的文本，content代表图片语义
        :type detect_target: str
        :param policy_id: 策略ID
        :type policy_id: str
        :param status: 规则状态，可选：enable(启用), disable(禁用)
        :type status: str
        :param detect_opts: 检测选项配置列表
        :type detect_opts: list[:class:`huaweicloudsdkwaf.v1.DetectOpt`]
        :param action: 
        :type action: :class:`huaweicloudsdkwaf.v1.AiGuardRuleAction`
        :param detect_labels: 
        :type detect_labels: :class:`huaweicloudsdkwaf.v1.DetectLabels`
        :param create_time: 创建时间
        :type create_time: int
        :param update_time: 更新时间
        :type update_time: int
        :param detect_labels_info: 
        :type detect_labels_info: :class:`huaweicloudsdkwaf.v1.DetectLabelsInfo`
        :param not_supported_language_action: 不支持语言的检测防护动作。pass: 放行, block: 拦截
        :type not_supported_language_action: str
        :param source: 规则来源，system代表系统，custom代表用户创建
        :type source: str
        :param source_id: 当source&#x3D;system时，source_id为默认模板规则的Id
        :type source_id: str
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
        
        super().__init__()

        self._id = None
        self._name = None
        self._detect_type = None
        self._detect_target = None
        self._policy_id = None
        self._status = None
        self._detect_opts = None
        self._action = None
        self._detect_labels = None
        self._create_time = None
        self._update_time = None
        self._detect_labels_info = None
        self._not_supported_language_action = None
        self._source = None
        self._source_id = None
        self._description = None
        self._custom_answers_id = None
        self._custom_answers_name = None
        self._abuse_config = None
        self._topic_config = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if detect_type is not None:
            self.detect_type = detect_type
        if detect_target is not None:
            self.detect_target = detect_target
        if policy_id is not None:
            self.policy_id = policy_id
        if status is not None:
            self.status = status
        if detect_opts is not None:
            self.detect_opts = detect_opts
        if action is not None:
            self.action = action
        if detect_labels is not None:
            self.detect_labels = detect_labels
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if detect_labels_info is not None:
            self.detect_labels_info = detect_labels_info
        if not_supported_language_action is not None:
            self.not_supported_language_action = not_supported_language_action
        if source is not None:
            self.source = source
        if source_id is not None:
            self.source_id = source_id
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
    def id(self):
        r"""Gets the id of this UpdateAiGuardRuleResponse.

        规则ID

        :return: The id of this UpdateAiGuardRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateAiGuardRuleResponse.

        规则ID

        :param id: The id of this UpdateAiGuardRuleResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this UpdateAiGuardRuleResponse.

        规则名称

        :return: The name of this UpdateAiGuardRuleResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateAiGuardRuleResponse.

        规则名称

        :param name: The name of this UpdateAiGuardRuleResponse.
        :type name: str
        """
        self._name = name

    @property
    def detect_type(self):
        r"""Gets the detect_type of this UpdateAiGuardRuleResponse.

        检测类别。text: 文本检测, image: 图片检测，为null时代表文字

        :return: The detect_type of this UpdateAiGuardRuleResponse.
        :rtype: str
        """
        return self._detect_type

    @detect_type.setter
    def detect_type(self, detect_type):
        r"""Sets the detect_type of this UpdateAiGuardRuleResponse.

        检测类别。text: 文本检测, image: 图片检测，为null时代表文字

        :param detect_type: The detect_type of this UpdateAiGuardRuleResponse.
        :type detect_type: str
        """
        self._detect_type = detect_type

    @property
    def detect_target(self):
        r"""Gets the detect_target of this UpdateAiGuardRuleResponse.

        检测目标，detect_type=image时有效。ocr代表图片中提取的文本，content代表图片语义

        :return: The detect_target of this UpdateAiGuardRuleResponse.
        :rtype: str
        """
        return self._detect_target

    @detect_target.setter
    def detect_target(self, detect_target):
        r"""Sets the detect_target of this UpdateAiGuardRuleResponse.

        检测目标，detect_type=image时有效。ocr代表图片中提取的文本，content代表图片语义

        :param detect_target: The detect_target of this UpdateAiGuardRuleResponse.
        :type detect_target: str
        """
        self._detect_target = detect_target

    @property
    def policy_id(self):
        r"""Gets the policy_id of this UpdateAiGuardRuleResponse.

        策略ID

        :return: The policy_id of this UpdateAiGuardRuleResponse.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this UpdateAiGuardRuleResponse.

        策略ID

        :param policy_id: The policy_id of this UpdateAiGuardRuleResponse.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def status(self):
        r"""Gets the status of this UpdateAiGuardRuleResponse.

        规则状态，可选：enable(启用), disable(禁用)

        :return: The status of this UpdateAiGuardRuleResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateAiGuardRuleResponse.

        规则状态，可选：enable(启用), disable(禁用)

        :param status: The status of this UpdateAiGuardRuleResponse.
        :type status: str
        """
        self._status = status

    @property
    def detect_opts(self):
        r"""Gets the detect_opts of this UpdateAiGuardRuleResponse.

        检测选项配置列表

        :return: The detect_opts of this UpdateAiGuardRuleResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.DetectOpt`]
        """
        return self._detect_opts

    @detect_opts.setter
    def detect_opts(self, detect_opts):
        r"""Sets the detect_opts of this UpdateAiGuardRuleResponse.

        检测选项配置列表

        :param detect_opts: The detect_opts of this UpdateAiGuardRuleResponse.
        :type detect_opts: list[:class:`huaweicloudsdkwaf.v1.DetectOpt`]
        """
        self._detect_opts = detect_opts

    @property
    def action(self):
        r"""Gets the action of this UpdateAiGuardRuleResponse.

        :return: The action of this UpdateAiGuardRuleResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.AiGuardRuleAction`
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this UpdateAiGuardRuleResponse.

        :param action: The action of this UpdateAiGuardRuleResponse.
        :type action: :class:`huaweicloudsdkwaf.v1.AiGuardRuleAction`
        """
        self._action = action

    @property
    def detect_labels(self):
        r"""Gets the detect_labels of this UpdateAiGuardRuleResponse.

        :return: The detect_labels of this UpdateAiGuardRuleResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.DetectLabels`
        """
        return self._detect_labels

    @detect_labels.setter
    def detect_labels(self, detect_labels):
        r"""Sets the detect_labels of this UpdateAiGuardRuleResponse.

        :param detect_labels: The detect_labels of this UpdateAiGuardRuleResponse.
        :type detect_labels: :class:`huaweicloudsdkwaf.v1.DetectLabels`
        """
        self._detect_labels = detect_labels

    @property
    def create_time(self):
        r"""Gets the create_time of this UpdateAiGuardRuleResponse.

        创建时间

        :return: The create_time of this UpdateAiGuardRuleResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this UpdateAiGuardRuleResponse.

        创建时间

        :param create_time: The create_time of this UpdateAiGuardRuleResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this UpdateAiGuardRuleResponse.

        更新时间

        :return: The update_time of this UpdateAiGuardRuleResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this UpdateAiGuardRuleResponse.

        更新时间

        :param update_time: The update_time of this UpdateAiGuardRuleResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def detect_labels_info(self):
        r"""Gets the detect_labels_info of this UpdateAiGuardRuleResponse.

        :return: The detect_labels_info of this UpdateAiGuardRuleResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.DetectLabelsInfo`
        """
        return self._detect_labels_info

    @detect_labels_info.setter
    def detect_labels_info(self, detect_labels_info):
        r"""Sets the detect_labels_info of this UpdateAiGuardRuleResponse.

        :param detect_labels_info: The detect_labels_info of this UpdateAiGuardRuleResponse.
        :type detect_labels_info: :class:`huaweicloudsdkwaf.v1.DetectLabelsInfo`
        """
        self._detect_labels_info = detect_labels_info

    @property
    def not_supported_language_action(self):
        r"""Gets the not_supported_language_action of this UpdateAiGuardRuleResponse.

        不支持语言的检测防护动作。pass: 放行, block: 拦截

        :return: The not_supported_language_action of this UpdateAiGuardRuleResponse.
        :rtype: str
        """
        return self._not_supported_language_action

    @not_supported_language_action.setter
    def not_supported_language_action(self, not_supported_language_action):
        r"""Sets the not_supported_language_action of this UpdateAiGuardRuleResponse.

        不支持语言的检测防护动作。pass: 放行, block: 拦截

        :param not_supported_language_action: The not_supported_language_action of this UpdateAiGuardRuleResponse.
        :type not_supported_language_action: str
        """
        self._not_supported_language_action = not_supported_language_action

    @property
    def source(self):
        r"""Gets the source of this UpdateAiGuardRuleResponse.

        规则来源，system代表系统，custom代表用户创建

        :return: The source of this UpdateAiGuardRuleResponse.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this UpdateAiGuardRuleResponse.

        规则来源，system代表系统，custom代表用户创建

        :param source: The source of this UpdateAiGuardRuleResponse.
        :type source: str
        """
        self._source = source

    @property
    def source_id(self):
        r"""Gets the source_id of this UpdateAiGuardRuleResponse.

        当source=system时，source_id为默认模板规则的Id

        :return: The source_id of this UpdateAiGuardRuleResponse.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        r"""Sets the source_id of this UpdateAiGuardRuleResponse.

        当source=system时，source_id为默认模板规则的Id

        :param source_id: The source_id of this UpdateAiGuardRuleResponse.
        :type source_id: str
        """
        self._source_id = source_id

    @property
    def description(self):
        r"""Gets the description of this UpdateAiGuardRuleResponse.

        规则描述，最大长度1024

        :return: The description of this UpdateAiGuardRuleResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateAiGuardRuleResponse.

        规则描述，最大长度1024

        :param description: The description of this UpdateAiGuardRuleResponse.
        :type description: str
        """
        self._description = description

    @property
    def custom_answers_id(self):
        r"""Gets the custom_answers_id of this UpdateAiGuardRuleResponse.

        自定义代答库ID（可选，当action.category=block时有效）

        :return: The custom_answers_id of this UpdateAiGuardRuleResponse.
        :rtype: str
        """
        return self._custom_answers_id

    @custom_answers_id.setter
    def custom_answers_id(self, custom_answers_id):
        r"""Sets the custom_answers_id of this UpdateAiGuardRuleResponse.

        自定义代答库ID（可选，当action.category=block时有效）

        :param custom_answers_id: The custom_answers_id of this UpdateAiGuardRuleResponse.
        :type custom_answers_id: str
        """
        self._custom_answers_id = custom_answers_id

    @property
    def custom_answers_name(self):
        r"""Gets the custom_answers_name of this UpdateAiGuardRuleResponse.

        自定义代答库名称（可选，当action.category=block时有效，与custom_answers_id对应）

        :return: The custom_answers_name of this UpdateAiGuardRuleResponse.
        :rtype: str
        """
        return self._custom_answers_name

    @custom_answers_name.setter
    def custom_answers_name(self, custom_answers_name):
        r"""Sets the custom_answers_name of this UpdateAiGuardRuleResponse.

        自定义代答库名称（可选，当action.category=block时有效，与custom_answers_id对应）

        :param custom_answers_name: The custom_answers_name of this UpdateAiGuardRuleResponse.
        :type custom_answers_name: str
        """
        self._custom_answers_name = custom_answers_name

    @property
    def abuse_config(self):
        r"""Gets the abuse_config of this UpdateAiGuardRuleResponse.

        :return: The abuse_config of this UpdateAiGuardRuleResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.AbuseConfig`
        """
        return self._abuse_config

    @abuse_config.setter
    def abuse_config(self, abuse_config):
        r"""Sets the abuse_config of this UpdateAiGuardRuleResponse.

        :param abuse_config: The abuse_config of this UpdateAiGuardRuleResponse.
        :type abuse_config: :class:`huaweicloudsdkwaf.v1.AbuseConfig`
        """
        self._abuse_config = abuse_config

    @property
    def topic_config(self):
        r"""Gets the topic_config of this UpdateAiGuardRuleResponse.

        :return: The topic_config of this UpdateAiGuardRuleResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.TopicConfig`
        """
        return self._topic_config

    @topic_config.setter
    def topic_config(self, topic_config):
        r"""Sets the topic_config of this UpdateAiGuardRuleResponse.

        :param topic_config: The topic_config of this UpdateAiGuardRuleResponse.
        :type topic_config: :class:`huaweicloudsdkwaf.v1.TopicConfig`
        """
        self._topic_config = topic_config

    def to_dict(self):
        import warnings
        warnings.warn("UpdateAiGuardRuleResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, UpdateAiGuardRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
