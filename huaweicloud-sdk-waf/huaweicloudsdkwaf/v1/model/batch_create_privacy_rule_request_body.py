# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreatePrivacyRuleRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'category': 'str',
        'index': 'str',
        'description': 'str',
        'policy_ids': 'list[str]'
    }

    attribute_map = {
        'url': 'url',
        'category': 'category',
        'index': 'index',
        'description': 'description',
        'policy_ids': 'policy_ids'
    }

    def __init__(self, url=None, category=None, index=None, description=None, policy_ids=None):
        r"""BatchCreatePrivacyRuleRequestBody

        The model defined in huaweicloud sdk

        :param url: 隐私屏蔽规则防护的url，需要填写标准的url格式，例如/admin/xxx或者/admin/*,以\&quot;*\&quot;（星号）结尾代表路径前缀
        :type url: str
        :param category: **参数解释：** 屏蔽字段 **约束限制：** 不涉及 **取值范围：**  - params: 请求参数  - cookie: 根据Cookie区分的Web访问者  - header: 自定义HTTP首部  - form: 表单参数  **默认取值：** 不涉及
        :type category: str
        :param index: 屏蔽字段名，根据“屏蔽字段”设置字段名，被屏蔽的字段将不会出现在日志中。屏蔽字段名的长度不能超过2048字节，且只能由数字、字母、下划线和中划线组成。
        :type index: str
        :param description: 规则描述，可选参数，设置该规则的备注信息。
        :type description: str
        :param policy_ids: 添加规则的策略id列表。策略id从\&quot;查询防护策略列表\&quot;(ListPolicy)接口获取，多个策略之间用“,”隔开
        :type policy_ids: list[str]
        """
        
        

        self._url = None
        self._category = None
        self._index = None
        self._description = None
        self._policy_ids = None
        self.discriminator = None

        self.url = url
        self.category = category
        self.index = index
        if description is not None:
            self.description = description
        self.policy_ids = policy_ids

    @property
    def url(self):
        r"""Gets the url of this BatchCreatePrivacyRuleRequestBody.

        隐私屏蔽规则防护的url，需要填写标准的url格式，例如/admin/xxx或者/admin/*,以\"*\"（星号）结尾代表路径前缀

        :return: The url of this BatchCreatePrivacyRuleRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this BatchCreatePrivacyRuleRequestBody.

        隐私屏蔽规则防护的url，需要填写标准的url格式，例如/admin/xxx或者/admin/*,以\"*\"（星号）结尾代表路径前缀

        :param url: The url of this BatchCreatePrivacyRuleRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def category(self):
        r"""Gets the category of this BatchCreatePrivacyRuleRequestBody.

        **参数解释：** 屏蔽字段 **约束限制：** 不涉及 **取值范围：**  - params: 请求参数  - cookie: 根据Cookie区分的Web访问者  - header: 自定义HTTP首部  - form: 表单参数  **默认取值：** 不涉及

        :return: The category of this BatchCreatePrivacyRuleRequestBody.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this BatchCreatePrivacyRuleRequestBody.

        **参数解释：** 屏蔽字段 **约束限制：** 不涉及 **取值范围：**  - params: 请求参数  - cookie: 根据Cookie区分的Web访问者  - header: 自定义HTTP首部  - form: 表单参数  **默认取值：** 不涉及

        :param category: The category of this BatchCreatePrivacyRuleRequestBody.
        :type category: str
        """
        self._category = category

    @property
    def index(self):
        r"""Gets the index of this BatchCreatePrivacyRuleRequestBody.

        屏蔽字段名，根据“屏蔽字段”设置字段名，被屏蔽的字段将不会出现在日志中。屏蔽字段名的长度不能超过2048字节，且只能由数字、字母、下划线和中划线组成。

        :return: The index of this BatchCreatePrivacyRuleRequestBody.
        :rtype: str
        """
        return self._index

    @index.setter
    def index(self, index):
        r"""Sets the index of this BatchCreatePrivacyRuleRequestBody.

        屏蔽字段名，根据“屏蔽字段”设置字段名，被屏蔽的字段将不会出现在日志中。屏蔽字段名的长度不能超过2048字节，且只能由数字、字母、下划线和中划线组成。

        :param index: The index of this BatchCreatePrivacyRuleRequestBody.
        :type index: str
        """
        self._index = index

    @property
    def description(self):
        r"""Gets the description of this BatchCreatePrivacyRuleRequestBody.

        规则描述，可选参数，设置该规则的备注信息。

        :return: The description of this BatchCreatePrivacyRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this BatchCreatePrivacyRuleRequestBody.

        规则描述，可选参数，设置该规则的备注信息。

        :param description: The description of this BatchCreatePrivacyRuleRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def policy_ids(self):
        r"""Gets the policy_ids of this BatchCreatePrivacyRuleRequestBody.

        添加规则的策略id列表。策略id从\"查询防护策略列表\"(ListPolicy)接口获取，多个策略之间用“,”隔开

        :return: The policy_ids of this BatchCreatePrivacyRuleRequestBody.
        :rtype: list[str]
        """
        return self._policy_ids

    @policy_ids.setter
    def policy_ids(self, policy_ids):
        r"""Sets the policy_ids of this BatchCreatePrivacyRuleRequestBody.

        添加规则的策略id列表。策略id从\"查询防护策略列表\"(ListPolicy)接口获取，多个策略之间用“,”隔开

        :param policy_ids: The policy_ids of this BatchCreatePrivacyRuleRequestBody.
        :type policy_ids: list[str]
        """
        self._policy_ids = policy_ids

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
        if not isinstance(other, BatchCreatePrivacyRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
