# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRetentionPolicyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'algorithm': 'str',
        'enabled': 'bool',
        'rules': 'list[RetentionRule]',
        'trigger': 'TriggerConfig',
        'name': 'str'
    }

    attribute_map = {
        'algorithm': 'algorithm',
        'enabled': 'enabled',
        'rules': 'rules',
        'trigger': 'trigger',
        'name': 'name'
    }

    def __init__(self, algorithm=None, enabled=None, rules=None, trigger=None, name=None):
        r"""CreateRetentionPolicyRequestBody

        The model defined in huaweicloud sdk

        :param algorithm: 算法，目前只支持or
        :type algorithm: str
        :param enabled: 是否启用或者关闭所有retentionRules
        :type enabled: bool
        :param rules: 匹配规则，配置repo范围、tag范围以及作用规则
        :type rules: list[:class:`huaweicloudsdkswr.v2.RetentionRule`]
        :param trigger: 
        :type trigger: :class:`huaweicloudsdkswr.v2.TriggerConfig`
        :param name: 策略名称，由字母、汉字、数字、下划线（_）、中划线 (-)组成，1-256个字符。
        :type name: str
        """
        
        

        self._algorithm = None
        self._enabled = None
        self._rules = None
        self._trigger = None
        self._name = None
        self.discriminator = None

        self.algorithm = algorithm
        self.enabled = enabled
        self.rules = rules
        self.trigger = trigger
        self.name = name

    @property
    def algorithm(self):
        r"""Gets the algorithm of this CreateRetentionPolicyRequestBody.

        算法，目前只支持or

        :return: The algorithm of this CreateRetentionPolicyRequestBody.
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        r"""Sets the algorithm of this CreateRetentionPolicyRequestBody.

        算法，目前只支持or

        :param algorithm: The algorithm of this CreateRetentionPolicyRequestBody.
        :type algorithm: str
        """
        self._algorithm = algorithm

    @property
    def enabled(self):
        r"""Gets the enabled of this CreateRetentionPolicyRequestBody.

        是否启用或者关闭所有retentionRules

        :return: The enabled of this CreateRetentionPolicyRequestBody.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this CreateRetentionPolicyRequestBody.

        是否启用或者关闭所有retentionRules

        :param enabled: The enabled of this CreateRetentionPolicyRequestBody.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def rules(self):
        r"""Gets the rules of this CreateRetentionPolicyRequestBody.

        匹配规则，配置repo范围、tag范围以及作用规则

        :return: The rules of this CreateRetentionPolicyRequestBody.
        :rtype: list[:class:`huaweicloudsdkswr.v2.RetentionRule`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        r"""Sets the rules of this CreateRetentionPolicyRequestBody.

        匹配规则，配置repo范围、tag范围以及作用规则

        :param rules: The rules of this CreateRetentionPolicyRequestBody.
        :type rules: list[:class:`huaweicloudsdkswr.v2.RetentionRule`]
        """
        self._rules = rules

    @property
    def trigger(self):
        r"""Gets the trigger of this CreateRetentionPolicyRequestBody.

        :return: The trigger of this CreateRetentionPolicyRequestBody.
        :rtype: :class:`huaweicloudsdkswr.v2.TriggerConfig`
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        r"""Sets the trigger of this CreateRetentionPolicyRequestBody.

        :param trigger: The trigger of this CreateRetentionPolicyRequestBody.
        :type trigger: :class:`huaweicloudsdkswr.v2.TriggerConfig`
        """
        self._trigger = trigger

    @property
    def name(self):
        r"""Gets the name of this CreateRetentionPolicyRequestBody.

        策略名称，由字母、汉字、数字、下划线（_）、中划线 (-)组成，1-256个字符。

        :return: The name of this CreateRetentionPolicyRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateRetentionPolicyRequestBody.

        策略名称，由字母、汉字、数字、下划线（_）、中划线 (-)组成，1-256个字符。

        :param name: The name of this CreateRetentionPolicyRequestBody.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, CreateRetentionPolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
