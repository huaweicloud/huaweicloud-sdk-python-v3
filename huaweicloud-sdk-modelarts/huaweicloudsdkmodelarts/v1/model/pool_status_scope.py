# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoolStatusScope:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scope_type': 'str',
        'state': 'str'
    }

    attribute_map = {
        'scope_type': 'scopeType',
        'state': 'state'
    }

    def __init__(self, scope_type=None, state=None):
        r"""PoolStatusScope

        The model defined in huaweicloud sdk

        :param scope_type: **参数解释**：资源池的业务类型。 **取值范围**：可选值如下： - Train：训练任务。 - Infer：推理任务。 - Notebook：Notebook作业。
        :type scope_type: str
        :param state: **参数解释**：资源池业务类型状态。 **取值范围**：可选值如下： - Enabling：启动中。 - Enabled：已启动。 - Disabling：关闭中。 - Disabled：已关闭。
        :type state: str
        """
        
        

        self._scope_type = None
        self._state = None
        self.discriminator = None

        self.scope_type = scope_type
        self.state = state

    @property
    def scope_type(self):
        r"""Gets the scope_type of this PoolStatusScope.

        **参数解释**：资源池的业务类型。 **取值范围**：可选值如下： - Train：训练任务。 - Infer：推理任务。 - Notebook：Notebook作业。

        :return: The scope_type of this PoolStatusScope.
        :rtype: str
        """
        return self._scope_type

    @scope_type.setter
    def scope_type(self, scope_type):
        r"""Sets the scope_type of this PoolStatusScope.

        **参数解释**：资源池的业务类型。 **取值范围**：可选值如下： - Train：训练任务。 - Infer：推理任务。 - Notebook：Notebook作业。

        :param scope_type: The scope_type of this PoolStatusScope.
        :type scope_type: str
        """
        self._scope_type = scope_type

    @property
    def state(self):
        r"""Gets the state of this PoolStatusScope.

        **参数解释**：资源池业务类型状态。 **取值范围**：可选值如下： - Enabling：启动中。 - Enabled：已启动。 - Disabling：关闭中。 - Disabled：已关闭。

        :return: The state of this PoolStatusScope.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this PoolStatusScope.

        **参数解释**：资源池业务类型状态。 **取值范围**：可选值如下： - Enabling：启动中。 - Enabled：已启动。 - Disabling：关闭中。 - Disabled：已关闭。

        :param state: The state of this PoolStatusScope.
        :type state: str
        """
        self._state = state

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
        if not isinstance(other, PoolStatusScope):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
