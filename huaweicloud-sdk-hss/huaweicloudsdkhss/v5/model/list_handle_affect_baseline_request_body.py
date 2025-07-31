# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHandleAffectBaselineRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'handle_status': 'str',
        'host_id': 'str',
        'check_rule_list': 'list[ListHandleAffectBaselineRequestBodyCheckRuleList]'
    }

    attribute_map = {
        'action': 'action',
        'handle_status': 'handle_status',
        'host_id': 'host_id',
        'check_rule_list': 'check_rule_list'
    }

    def __init__(self, action=None, handle_status=None, host_id=None, check_rule_list=None):
        r"""ListHandleAffectBaselineRequestBody

        The model defined in huaweicloud sdk

        :param action: **参数解释** 基线检查执行的操作 **约束限制** 不涉及 **取值范围**   - add_to_whitelist: 加白名单 - ignore          : 忽略 - unignore        : 取消忽略 - fix             : 修复 - verify          : 验证 **默认取值** 不涉及
        :type action: str
        :param handle_status: **参数解释** 当前检查项的状态 **约束限制** 不涉及 **取值范围**   - unhandled : 未处理 - fix-failed: 修复失败 - fixing    : 修复中 - verifying : 验证中 - ignored   : 忽略 - safe      : 安全 **默认取值** 不涉及
        :type handle_status: str
        :param host_id: **参数解释** 主机id，没有该字段则代表该检查项影响的部分主机 **约束限制** 不涉及 **取值范围**   字符长度1-256位 **默认取值** 不涉及
        :type host_id: str
        :param check_rule_list: **参数解释** 需要进行操作的检查项列表 **约束限制** 列表范围0-200条
        :type check_rule_list: list[:class:`huaweicloudsdkhss.v5.ListHandleAffectBaselineRequestBodyCheckRuleList`]
        """
        
        

        self._action = None
        self._handle_status = None
        self._host_id = None
        self._check_rule_list = None
        self.discriminator = None

        self.action = action
        self.handle_status = handle_status
        if host_id is not None:
            self.host_id = host_id
        self.check_rule_list = check_rule_list

    @property
    def action(self):
        r"""Gets the action of this ListHandleAffectBaselineRequestBody.

        **参数解释** 基线检查执行的操作 **约束限制** 不涉及 **取值范围**   - add_to_whitelist: 加白名单 - ignore          : 忽略 - unignore        : 取消忽略 - fix             : 修复 - verify          : 验证 **默认取值** 不涉及

        :return: The action of this ListHandleAffectBaselineRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ListHandleAffectBaselineRequestBody.

        **参数解释** 基线检查执行的操作 **约束限制** 不涉及 **取值范围**   - add_to_whitelist: 加白名单 - ignore          : 忽略 - unignore        : 取消忽略 - fix             : 修复 - verify          : 验证 **默认取值** 不涉及

        :param action: The action of this ListHandleAffectBaselineRequestBody.
        :type action: str
        """
        self._action = action

    @property
    def handle_status(self):
        r"""Gets the handle_status of this ListHandleAffectBaselineRequestBody.

        **参数解释** 当前检查项的状态 **约束限制** 不涉及 **取值范围**   - unhandled : 未处理 - fix-failed: 修复失败 - fixing    : 修复中 - verifying : 验证中 - ignored   : 忽略 - safe      : 安全 **默认取值** 不涉及

        :return: The handle_status of this ListHandleAffectBaselineRequestBody.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        r"""Sets the handle_status of this ListHandleAffectBaselineRequestBody.

        **参数解释** 当前检查项的状态 **约束限制** 不涉及 **取值范围**   - unhandled : 未处理 - fix-failed: 修复失败 - fixing    : 修复中 - verifying : 验证中 - ignored   : 忽略 - safe      : 安全 **默认取值** 不涉及

        :param handle_status: The handle_status of this ListHandleAffectBaselineRequestBody.
        :type handle_status: str
        """
        self._handle_status = handle_status

    @property
    def host_id(self):
        r"""Gets the host_id of this ListHandleAffectBaselineRequestBody.

        **参数解释** 主机id，没有该字段则代表该检查项影响的部分主机 **约束限制** 不涉及 **取值范围**   字符长度1-256位 **默认取值** 不涉及

        :return: The host_id of this ListHandleAffectBaselineRequestBody.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListHandleAffectBaselineRequestBody.

        **参数解释** 主机id，没有该字段则代表该检查项影响的部分主机 **约束限制** 不涉及 **取值范围**   字符长度1-256位 **默认取值** 不涉及

        :param host_id: The host_id of this ListHandleAffectBaselineRequestBody.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def check_rule_list(self):
        r"""Gets the check_rule_list of this ListHandleAffectBaselineRequestBody.

        **参数解释** 需要进行操作的检查项列表 **约束限制** 列表范围0-200条

        :return: The check_rule_list of this ListHandleAffectBaselineRequestBody.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ListHandleAffectBaselineRequestBodyCheckRuleList`]
        """
        return self._check_rule_list

    @check_rule_list.setter
    def check_rule_list(self, check_rule_list):
        r"""Sets the check_rule_list of this ListHandleAffectBaselineRequestBody.

        **参数解释** 需要进行操作的检查项列表 **约束限制** 列表范围0-200条

        :param check_rule_list: The check_rule_list of this ListHandleAffectBaselineRequestBody.
        :type check_rule_list: list[:class:`huaweicloudsdkhss.v5.ListHandleAffectBaselineRequestBodyCheckRuleList`]
        """
        self._check_rule_list = check_rule_list

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
        if not isinstance(other, ListHandleAffectBaselineRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
