# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventForensicInfoStackForensic:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attack_input_value': 'str',
        'app_stack': 'str',
        'chk_probe': 'int',
        'chk_rule': 'int',
        'plugin_name': 'int'
    }

    attribute_map = {
        'attack_input_value': 'attack_input_value',
        'app_stack': 'app_stack',
        'chk_probe': 'chk_probe',
        'chk_rule': 'chk_rule',
        'plugin_name': 'plugin_name'
    }

    def __init__(self, attack_input_value=None, app_stack=None, chk_probe=None, chk_rule=None, plugin_name=None):
        r"""EventForensicInfoStackForensic

        The model defined in huaweicloud sdk

        :param attack_input_value: **参数解释**： 攻击载荷 **取值范围**： 不涉及
        :type attack_input_value: str
        :param app_stack: **参数解释**： 堆栈信息 **取值范围**： 不涉及
        :type app_stack: str
        :param chk_probe: **参数解释**： 攻击探针 **取值范围**： 不涉及
        :type chk_probe: int
        :param chk_rule: **参数解释**： 特性规则 **取值范围**： 不涉及
        :type chk_rule: int
        :param plugin_name: **参数解释**： 检测规则 **取值范围**： 不涉及
        :type plugin_name: int
        """
        
        

        self._attack_input_value = None
        self._app_stack = None
        self._chk_probe = None
        self._chk_rule = None
        self._plugin_name = None
        self.discriminator = None

        if attack_input_value is not None:
            self.attack_input_value = attack_input_value
        if app_stack is not None:
            self.app_stack = app_stack
        if chk_probe is not None:
            self.chk_probe = chk_probe
        if chk_rule is not None:
            self.chk_rule = chk_rule
        if plugin_name is not None:
            self.plugin_name = plugin_name

    @property
    def attack_input_value(self):
        r"""Gets the attack_input_value of this EventForensicInfoStackForensic.

        **参数解释**： 攻击载荷 **取值范围**： 不涉及

        :return: The attack_input_value of this EventForensicInfoStackForensic.
        :rtype: str
        """
        return self._attack_input_value

    @attack_input_value.setter
    def attack_input_value(self, attack_input_value):
        r"""Sets the attack_input_value of this EventForensicInfoStackForensic.

        **参数解释**： 攻击载荷 **取值范围**： 不涉及

        :param attack_input_value: The attack_input_value of this EventForensicInfoStackForensic.
        :type attack_input_value: str
        """
        self._attack_input_value = attack_input_value

    @property
    def app_stack(self):
        r"""Gets the app_stack of this EventForensicInfoStackForensic.

        **参数解释**： 堆栈信息 **取值范围**： 不涉及

        :return: The app_stack of this EventForensicInfoStackForensic.
        :rtype: str
        """
        return self._app_stack

    @app_stack.setter
    def app_stack(self, app_stack):
        r"""Sets the app_stack of this EventForensicInfoStackForensic.

        **参数解释**： 堆栈信息 **取值范围**： 不涉及

        :param app_stack: The app_stack of this EventForensicInfoStackForensic.
        :type app_stack: str
        """
        self._app_stack = app_stack

    @property
    def chk_probe(self):
        r"""Gets the chk_probe of this EventForensicInfoStackForensic.

        **参数解释**： 攻击探针 **取值范围**： 不涉及

        :return: The chk_probe of this EventForensicInfoStackForensic.
        :rtype: int
        """
        return self._chk_probe

    @chk_probe.setter
    def chk_probe(self, chk_probe):
        r"""Sets the chk_probe of this EventForensicInfoStackForensic.

        **参数解释**： 攻击探针 **取值范围**： 不涉及

        :param chk_probe: The chk_probe of this EventForensicInfoStackForensic.
        :type chk_probe: int
        """
        self._chk_probe = chk_probe

    @property
    def chk_rule(self):
        r"""Gets the chk_rule of this EventForensicInfoStackForensic.

        **参数解释**： 特性规则 **取值范围**： 不涉及

        :return: The chk_rule of this EventForensicInfoStackForensic.
        :rtype: int
        """
        return self._chk_rule

    @chk_rule.setter
    def chk_rule(self, chk_rule):
        r"""Sets the chk_rule of this EventForensicInfoStackForensic.

        **参数解释**： 特性规则 **取值范围**： 不涉及

        :param chk_rule: The chk_rule of this EventForensicInfoStackForensic.
        :type chk_rule: int
        """
        self._chk_rule = chk_rule

    @property
    def plugin_name(self):
        r"""Gets the plugin_name of this EventForensicInfoStackForensic.

        **参数解释**： 检测规则 **取值范围**： 不涉及

        :return: The plugin_name of this EventForensicInfoStackForensic.
        :rtype: int
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        r"""Sets the plugin_name of this EventForensicInfoStackForensic.

        **参数解释**： 检测规则 **取值范围**： 不涉及

        :param plugin_name: The plugin_name of this EventForensicInfoStackForensic.
        :type plugin_name: int
        """
        self._plugin_name = plugin_name

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
        if not isinstance(other, EventForensicInfoStackForensic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
