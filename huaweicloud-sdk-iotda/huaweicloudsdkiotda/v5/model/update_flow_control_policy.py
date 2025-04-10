# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateFlowControlPolicy:

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
        'description': 'str',
        'limit': 'int'
    }

    attribute_map = {
        'policy_name': 'policy_name',
        'description': 'description',
        'limit': 'limit'
    }

    def __init__(self, policy_name=None, description=None, limit=None):
        r"""UpdateFlowControlPolicy

        The model defined in huaweicloud sdk

        :param policy_name: **参数说明**：数据流转流控策略名称。 **取值范围**：长度不超过256，只允许中文、字母、数字、以及_?&#39;#().,&amp;%@!-等字符的组合。
        :type policy_name: str
        :param description: **参数说明**：用户自定义的数据流转流控策略描述。 **取值范围**：长度不超过256，只允许中文、字母、数字、以及_?&#39;#().,&amp;%@!-等字符的组合。
        :type description: str
        :param limit: **参数说明**：数据转发流控大小。单位为tps，取值范围为1~1000的整数，默认为1000.
        :type limit: int
        """
        
        

        self._policy_name = None
        self._description = None
        self._limit = None
        self.discriminator = None

        if policy_name is not None:
            self.policy_name = policy_name
        if description is not None:
            self.description = description
        if limit is not None:
            self.limit = limit

    @property
    def policy_name(self):
        r"""Gets the policy_name of this UpdateFlowControlPolicy.

        **参数说明**：数据流转流控策略名称。 **取值范围**：长度不超过256，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :return: The policy_name of this UpdateFlowControlPolicy.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this UpdateFlowControlPolicy.

        **参数说明**：数据流转流控策略名称。 **取值范围**：长度不超过256，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :param policy_name: The policy_name of this UpdateFlowControlPolicy.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def description(self):
        r"""Gets the description of this UpdateFlowControlPolicy.

        **参数说明**：用户自定义的数据流转流控策略描述。 **取值范围**：长度不超过256，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :return: The description of this UpdateFlowControlPolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateFlowControlPolicy.

        **参数说明**：用户自定义的数据流转流控策略描述。 **取值范围**：长度不超过256，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :param description: The description of this UpdateFlowControlPolicy.
        :type description: str
        """
        self._description = description

    @property
    def limit(self):
        r"""Gets the limit of this UpdateFlowControlPolicy.

        **参数说明**：数据转发流控大小。单位为tps，取值范围为1~1000的整数，默认为1000.

        :return: The limit of this UpdateFlowControlPolicy.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this UpdateFlowControlPolicy.

        **参数说明**：数据转发流控大小。单位为tps，取值范围为1~1000的整数，默认为1000.

        :param limit: The limit of this UpdateFlowControlPolicy.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, UpdateFlowControlPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
