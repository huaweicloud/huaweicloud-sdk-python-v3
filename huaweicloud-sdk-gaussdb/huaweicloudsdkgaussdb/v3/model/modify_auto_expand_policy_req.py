# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyAutoExpandPolicyReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'switch_option': 'bool',
        'limit_size': 'int',
        'trigger_available_percent': 'int',
        'step_percent': 'int'
    }

    attribute_map = {
        'switch_option': 'switch_option',
        'limit_size': 'limit_size',
        'trigger_available_percent': 'trigger_available_percent',
        'step_percent': 'step_percent'
    }

    def __init__(self, switch_option=None, limit_size=None, trigger_available_percent=None, step_percent=None):
        r"""ModifyAutoExpandPolicyReq

        The model defined in huaweicloud sdk

        :param switch_option: **参数解释**：  自动扩容策略开关。  **取值范围**：  - true：表示开启。 - false：表示关闭。
        :type switch_option: bool
        :param limit_size: **参数解释**：  存储自动扩容上限，需要为10的倍数，单位GB。  **取值范围**：  10 - 最大容量上限。  示例：500
        :type limit_size: int
        :param trigger_available_percent: **参数解释**：  可用存储空间率。  **取值范围**：  - 10 - 15 - 20
        :type trigger_available_percent: int
        :param step_percent: **参数解释**：  扩容步长百分比。  **取值范围**:   5 - 50
        :type step_percent: int
        """
        
        

        self._switch_option = None
        self._limit_size = None
        self._trigger_available_percent = None
        self._step_percent = None
        self.discriminator = None

        if switch_option is not None:
            self.switch_option = switch_option
        if limit_size is not None:
            self.limit_size = limit_size
        if trigger_available_percent is not None:
            self.trigger_available_percent = trigger_available_percent
        if step_percent is not None:
            self.step_percent = step_percent

    @property
    def switch_option(self):
        r"""Gets the switch_option of this ModifyAutoExpandPolicyReq.

        **参数解释**：  自动扩容策略开关。  **取值范围**：  - true：表示开启。 - false：表示关闭。

        :return: The switch_option of this ModifyAutoExpandPolicyReq.
        :rtype: bool
        """
        return self._switch_option

    @switch_option.setter
    def switch_option(self, switch_option):
        r"""Sets the switch_option of this ModifyAutoExpandPolicyReq.

        **参数解释**：  自动扩容策略开关。  **取值范围**：  - true：表示开启。 - false：表示关闭。

        :param switch_option: The switch_option of this ModifyAutoExpandPolicyReq.
        :type switch_option: bool
        """
        self._switch_option = switch_option

    @property
    def limit_size(self):
        r"""Gets the limit_size of this ModifyAutoExpandPolicyReq.

        **参数解释**：  存储自动扩容上限，需要为10的倍数，单位GB。  **取值范围**：  10 - 最大容量上限。  示例：500

        :return: The limit_size of this ModifyAutoExpandPolicyReq.
        :rtype: int
        """
        return self._limit_size

    @limit_size.setter
    def limit_size(self, limit_size):
        r"""Sets the limit_size of this ModifyAutoExpandPolicyReq.

        **参数解释**：  存储自动扩容上限，需要为10的倍数，单位GB。  **取值范围**：  10 - 最大容量上限。  示例：500

        :param limit_size: The limit_size of this ModifyAutoExpandPolicyReq.
        :type limit_size: int
        """
        self._limit_size = limit_size

    @property
    def trigger_available_percent(self):
        r"""Gets the trigger_available_percent of this ModifyAutoExpandPolicyReq.

        **参数解释**：  可用存储空间率。  **取值范围**：  - 10 - 15 - 20

        :return: The trigger_available_percent of this ModifyAutoExpandPolicyReq.
        :rtype: int
        """
        return self._trigger_available_percent

    @trigger_available_percent.setter
    def trigger_available_percent(self, trigger_available_percent):
        r"""Sets the trigger_available_percent of this ModifyAutoExpandPolicyReq.

        **参数解释**：  可用存储空间率。  **取值范围**：  - 10 - 15 - 20

        :param trigger_available_percent: The trigger_available_percent of this ModifyAutoExpandPolicyReq.
        :type trigger_available_percent: int
        """
        self._trigger_available_percent = trigger_available_percent

    @property
    def step_percent(self):
        r"""Gets the step_percent of this ModifyAutoExpandPolicyReq.

        **参数解释**：  扩容步长百分比。  **取值范围**:   5 - 50

        :return: The step_percent of this ModifyAutoExpandPolicyReq.
        :rtype: int
        """
        return self._step_percent

    @step_percent.setter
    def step_percent(self, step_percent):
        r"""Sets the step_percent of this ModifyAutoExpandPolicyReq.

        **参数解释**：  扩容步长百分比。  **取值范围**:   5 - 50

        :param step_percent: The step_percent of this ModifyAutoExpandPolicyReq.
        :type step_percent: int
        """
        self._step_percent = step_percent

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
        if not isinstance(other, ModifyAutoExpandPolicyReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
