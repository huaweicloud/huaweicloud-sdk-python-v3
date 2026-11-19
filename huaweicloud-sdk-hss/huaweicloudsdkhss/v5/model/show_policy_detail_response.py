# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPolicyDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'content': 'str',
        'description': 'str',
        'enabled': 'bool',
        'name': 'str',
        'support_os': 'str',
        'policy_id': 'str',
        'feature_name': 'str'
    }

    attribute_map = {
        'category': 'category',
        'content': 'content',
        'description': 'description',
        'enabled': 'enabled',
        'name': 'name',
        'support_os': 'support_os',
        'policy_id': 'policy_id',
        'feature_name': 'feature_name'
    }

    def __init__(self, category=None, content=None, description=None, enabled=None, name=None, support_os=None, policy_id=None, feature_name=None):
        r"""ShowPolicyDetailResponse

        The model defined in huaweicloud sdk

        :param category: **参数解释**： 功能类别 **取值范围**： 字符长度1-128位 
        :type category: str
        :param content: **参数解释**： 策略内容 **取值范围**： 字符长度0-4096位 
        :type content: str
        :param description: **参数解释**： 策略描述 **取值范围**： 字符长度0-1024位 
        :type description: str
        :param enabled: **参数解释**： 策略是否开启 **取值范围**： - true：开启 - false：关闭 
        :type enabled: bool
        :param name: **参数解释**： 策略名 **取值范围**： 字符长度1-256位 
        :type name: str
        :param support_os: **参数解释**： 策略支持的主机种类 **取值范围**: - Linux：Linux操作系统 - Windows：Windows操作系统 
        :type support_os: str
        :param policy_id: **参数解释**： 策略Id **取值范围**： 字符长度1-128位 
        :type policy_id: str
        :param feature_name: **参数解释**： 特性名 **取值范围**： 字符长度1-128位 
        :type feature_name: str
        """
        
        super().__init__()

        self._category = None
        self._content = None
        self._description = None
        self._enabled = None
        self._name = None
        self._support_os = None
        self._policy_id = None
        self._feature_name = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if content is not None:
            self.content = content
        if description is not None:
            self.description = description
        if enabled is not None:
            self.enabled = enabled
        if name is not None:
            self.name = name
        if support_os is not None:
            self.support_os = support_os
        if policy_id is not None:
            self.policy_id = policy_id
        if feature_name is not None:
            self.feature_name = feature_name

    @property
    def category(self):
        r"""Gets the category of this ShowPolicyDetailResponse.

        **参数解释**： 功能类别 **取值范围**： 字符长度1-128位 

        :return: The category of this ShowPolicyDetailResponse.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ShowPolicyDetailResponse.

        **参数解释**： 功能类别 **取值范围**： 字符长度1-128位 

        :param category: The category of this ShowPolicyDetailResponse.
        :type category: str
        """
        self._category = category

    @property
    def content(self):
        r"""Gets the content of this ShowPolicyDetailResponse.

        **参数解释**： 策略内容 **取值范围**： 字符长度0-4096位 

        :return: The content of this ShowPolicyDetailResponse.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this ShowPolicyDetailResponse.

        **参数解释**： 策略内容 **取值范围**： 字符长度0-4096位 

        :param content: The content of this ShowPolicyDetailResponse.
        :type content: str
        """
        self._content = content

    @property
    def description(self):
        r"""Gets the description of this ShowPolicyDetailResponse.

        **参数解释**： 策略描述 **取值范围**： 字符长度0-1024位 

        :return: The description of this ShowPolicyDetailResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowPolicyDetailResponse.

        **参数解释**： 策略描述 **取值范围**： 字符长度0-1024位 

        :param description: The description of this ShowPolicyDetailResponse.
        :type description: str
        """
        self._description = description

    @property
    def enabled(self):
        r"""Gets the enabled of this ShowPolicyDetailResponse.

        **参数解释**： 策略是否开启 **取值范围**： - true：开启 - false：关闭 

        :return: The enabled of this ShowPolicyDetailResponse.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this ShowPolicyDetailResponse.

        **参数解释**： 策略是否开启 **取值范围**： - true：开启 - false：关闭 

        :param enabled: The enabled of this ShowPolicyDetailResponse.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def name(self):
        r"""Gets the name of this ShowPolicyDetailResponse.

        **参数解释**： 策略名 **取值范围**： 字符长度1-256位 

        :return: The name of this ShowPolicyDetailResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowPolicyDetailResponse.

        **参数解释**： 策略名 **取值范围**： 字符长度1-256位 

        :param name: The name of this ShowPolicyDetailResponse.
        :type name: str
        """
        self._name = name

    @property
    def support_os(self):
        r"""Gets the support_os of this ShowPolicyDetailResponse.

        **参数解释**： 策略支持的主机种类 **取值范围**: - Linux：Linux操作系统 - Windows：Windows操作系统 

        :return: The support_os of this ShowPolicyDetailResponse.
        :rtype: str
        """
        return self._support_os

    @support_os.setter
    def support_os(self, support_os):
        r"""Sets the support_os of this ShowPolicyDetailResponse.

        **参数解释**： 策略支持的主机种类 **取值范围**: - Linux：Linux操作系统 - Windows：Windows操作系统 

        :param support_os: The support_os of this ShowPolicyDetailResponse.
        :type support_os: str
        """
        self._support_os = support_os

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ShowPolicyDetailResponse.

        **参数解释**： 策略Id **取值范围**： 字符长度1-128位 

        :return: The policy_id of this ShowPolicyDetailResponse.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ShowPolicyDetailResponse.

        **参数解释**： 策略Id **取值范围**： 字符长度1-128位 

        :param policy_id: The policy_id of this ShowPolicyDetailResponse.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def feature_name(self):
        r"""Gets the feature_name of this ShowPolicyDetailResponse.

        **参数解释**： 特性名 **取值范围**： 字符长度1-128位 

        :return: The feature_name of this ShowPolicyDetailResponse.
        :rtype: str
        """
        return self._feature_name

    @feature_name.setter
    def feature_name(self, feature_name):
        r"""Sets the feature_name of this ShowPolicyDetailResponse.

        **参数解释**： 特性名 **取值范围**： 字符长度1-128位 

        :param feature_name: The feature_name of this ShowPolicyDetailResponse.
        :type feature_name: str
        """
        self._feature_name = feature_name

    def to_dict(self):
        import warnings
        warnings.warn("ShowPolicyDetailResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowPolicyDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
