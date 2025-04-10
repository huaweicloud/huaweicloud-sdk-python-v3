# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSmartLiveRuleCommandsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'rule_commands': 'list[RuleCommand]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'count': 'count',
        'rule_commands': 'rule_commands',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, count=None, rule_commands=None, x_request_id=None):
        r"""ListSmartLiveRuleCommandsResponse

        The model defined in huaweicloud sdk

        :param count: 数字人直播任务互动规则未确认命令总数。
        :type count: int
        :param rule_commands: 数字人互动规则命令列表。
        :type rule_commands: list[:class:`huaweicloudsdkmetastudio.v1.RuleCommand`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListSmartLiveRuleCommandsResponse, self).__init__()

        self._count = None
        self._rule_commands = None
        self._x_request_id = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if rule_commands is not None:
            self.rule_commands = rule_commands
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def count(self):
        r"""Gets the count of this ListSmartLiveRuleCommandsResponse.

        数字人直播任务互动规则未确认命令总数。

        :return: The count of this ListSmartLiveRuleCommandsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListSmartLiveRuleCommandsResponse.

        数字人直播任务互动规则未确认命令总数。

        :param count: The count of this ListSmartLiveRuleCommandsResponse.
        :type count: int
        """
        self._count = count

    @property
    def rule_commands(self):
        r"""Gets the rule_commands of this ListSmartLiveRuleCommandsResponse.

        数字人互动规则命令列表。

        :return: The rule_commands of this ListSmartLiveRuleCommandsResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.RuleCommand`]
        """
        return self._rule_commands

    @rule_commands.setter
    def rule_commands(self, rule_commands):
        r"""Sets the rule_commands of this ListSmartLiveRuleCommandsResponse.

        数字人互动规则命令列表。

        :param rule_commands: The rule_commands of this ListSmartLiveRuleCommandsResponse.
        :type rule_commands: list[:class:`huaweicloudsdkmetastudio.v1.RuleCommand`]
        """
        self._rule_commands = rule_commands

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListSmartLiveRuleCommandsResponse.

        :return: The x_request_id of this ListSmartLiveRuleCommandsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListSmartLiveRuleCommandsResponse.

        :param x_request_id: The x_request_id of this ListSmartLiveRuleCommandsResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListSmartLiveRuleCommandsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
