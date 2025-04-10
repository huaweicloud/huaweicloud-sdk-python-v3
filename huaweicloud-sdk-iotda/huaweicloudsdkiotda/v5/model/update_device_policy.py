# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDevicePolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_name': 'str',
        'statement': 'list[Statement]'
    }

    attribute_map = {
        'policy_name': 'policy_name',
        'statement': 'statement'
    }

    def __init__(self, policy_name=None, statement=None):
        r"""UpdateDevicePolicy

        The model defined in huaweicloud sdk

        :param policy_name: **参数说明**：策略名称。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type policy_name: str
        :param statement: **参数说明**：策略文档。
        :type statement: list[:class:`huaweicloudsdkiotda.v5.Statement`]
        """
        
        

        self._policy_name = None
        self._statement = None
        self.discriminator = None

        if policy_name is not None:
            self.policy_name = policy_name
        if statement is not None:
            self.statement = statement

    @property
    def policy_name(self):
        r"""Gets the policy_name of this UpdateDevicePolicy.

        **参数说明**：策略名称。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The policy_name of this UpdateDevicePolicy.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this UpdateDevicePolicy.

        **参数说明**：策略名称。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param policy_name: The policy_name of this UpdateDevicePolicy.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def statement(self):
        r"""Gets the statement of this UpdateDevicePolicy.

        **参数说明**：策略文档。

        :return: The statement of this UpdateDevicePolicy.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.Statement`]
        """
        return self._statement

    @statement.setter
    def statement(self, statement):
        r"""Sets the statement of this UpdateDevicePolicy.

        **参数说明**：策略文档。

        :param statement: The statement of this UpdateDevicePolicy.
        :type statement: list[:class:`huaweicloudsdkiotda.v5.Statement`]
        """
        self._statement = statement

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
        if not isinstance(other, UpdateDevicePolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
