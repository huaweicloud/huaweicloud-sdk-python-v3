# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAppWhitelistPolicyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'policy_name': 'str',
        'policy_type': 'str',
        'learning_status': 'str',
        'intercept': 'bool'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'policy_name': 'policy_name',
        'policy_type': 'policy_type',
        'learning_status': 'learning_status',
        'intercept': 'intercept'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, policy_name=None, policy_type=None, learning_status=None, intercept=None):
        r"""ListAppWhitelistPolicyRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param policy_name: 策略名称
        :type policy_name: str
        :param policy_type: **参数解释**： 进程白名单策略类型 **约束限制**: 不涉及 **取值范围**: - allow：允许指定/授权进程运行 - block：阻止潜在恶意软件运行  **默认取值**: 不涉及 
        :type policy_type: str
        :param learning_status: **参数解释**： 策略学习状态 **约束限制**: 不涉及 **取值范围**: - effecting：学习完成，策略生效 - learned：学习完成，待确认 - learning：学习中 - pause：暂停 - abnormal：学习异常  **默认取值**: 不涉及 
        :type learning_status: str
        :param intercept: **参数解释**： 是否开启阻断 **约束限制**: 不涉及 **取值范围**: - true：是 - false：否  **默认取值**: 不涉及 
        :type intercept: bool
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._policy_name = None
        self._policy_type = None
        self._learning_status = None
        self._intercept = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.offset = offset
        self.limit = limit
        if policy_name is not None:
            self.policy_name = policy_name
        if policy_type is not None:
            self.policy_type = policy_type
        if learning_status is not None:
            self.learning_status = learning_status
        if intercept is not None:
            self.intercept = intercept

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListAppWhitelistPolicyRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListAppWhitelistPolicyRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListAppWhitelistPolicyRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListAppWhitelistPolicyRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListAppWhitelistPolicyRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :return: The offset of this ListAppWhitelistPolicyRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAppWhitelistPolicyRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :param offset: The offset of this ListAppWhitelistPolicyRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListAppWhitelistPolicyRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListAppWhitelistPolicyRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAppWhitelistPolicyRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListAppWhitelistPolicyRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def policy_name(self):
        r"""Gets the policy_name of this ListAppWhitelistPolicyRequest.

        策略名称

        :return: The policy_name of this ListAppWhitelistPolicyRequest.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this ListAppWhitelistPolicyRequest.

        策略名称

        :param policy_name: The policy_name of this ListAppWhitelistPolicyRequest.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def policy_type(self):
        r"""Gets the policy_type of this ListAppWhitelistPolicyRequest.

        **参数解释**： 进程白名单策略类型 **约束限制**: 不涉及 **取值范围**: - allow：允许指定/授权进程运行 - block：阻止潜在恶意软件运行  **默认取值**: 不涉及 

        :return: The policy_type of this ListAppWhitelistPolicyRequest.
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        r"""Sets the policy_type of this ListAppWhitelistPolicyRequest.

        **参数解释**： 进程白名单策略类型 **约束限制**: 不涉及 **取值范围**: - allow：允许指定/授权进程运行 - block：阻止潜在恶意软件运行  **默认取值**: 不涉及 

        :param policy_type: The policy_type of this ListAppWhitelistPolicyRequest.
        :type policy_type: str
        """
        self._policy_type = policy_type

    @property
    def learning_status(self):
        r"""Gets the learning_status of this ListAppWhitelistPolicyRequest.

        **参数解释**： 策略学习状态 **约束限制**: 不涉及 **取值范围**: - effecting：学习完成，策略生效 - learned：学习完成，待确认 - learning：学习中 - pause：暂停 - abnormal：学习异常  **默认取值**: 不涉及 

        :return: The learning_status of this ListAppWhitelistPolicyRequest.
        :rtype: str
        """
        return self._learning_status

    @learning_status.setter
    def learning_status(self, learning_status):
        r"""Sets the learning_status of this ListAppWhitelistPolicyRequest.

        **参数解释**： 策略学习状态 **约束限制**: 不涉及 **取值范围**: - effecting：学习完成，策略生效 - learned：学习完成，待确认 - learning：学习中 - pause：暂停 - abnormal：学习异常  **默认取值**: 不涉及 

        :param learning_status: The learning_status of this ListAppWhitelistPolicyRequest.
        :type learning_status: str
        """
        self._learning_status = learning_status

    @property
    def intercept(self):
        r"""Gets the intercept of this ListAppWhitelistPolicyRequest.

        **参数解释**： 是否开启阻断 **约束限制**: 不涉及 **取值范围**: - true：是 - false：否  **默认取值**: 不涉及 

        :return: The intercept of this ListAppWhitelistPolicyRequest.
        :rtype: bool
        """
        return self._intercept

    @intercept.setter
    def intercept(self, intercept):
        r"""Sets the intercept of this ListAppWhitelistPolicyRequest.

        **参数解释**： 是否开启阻断 **约束限制**: 不涉及 **取值范围**: - true：是 - false：否  **默认取值**: 不涉及 

        :param intercept: The intercept of this ListAppWhitelistPolicyRequest.
        :type intercept: bool
        """
        self._intercept = intercept

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
        if not isinstance(other, ListAppWhitelistPolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
