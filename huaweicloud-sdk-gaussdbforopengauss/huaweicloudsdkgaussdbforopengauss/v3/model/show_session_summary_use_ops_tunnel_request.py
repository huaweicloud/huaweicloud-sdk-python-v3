# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSessionSummaryUseOpsTunnelRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'instance_id': 'str',
        'node_id': 'str',
        'component_id': 'str',
        'use_ops_tunnel': 'bool'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'node_id': 'node_id',
        'component_id': 'component_id',
        'use_ops_tunnel': 'use_ops_tunnel'
    }

    def __init__(self, x_language=None, instance_id=None, node_id=None, component_id=None, use_ops_tunnel=None):
        r"""ShowSessionSummaryUseOpsTunnelRequest

        The model defined in huaweicloud sdk

        :param x_language: **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn - en-us  **默认取值**: en-us
        :type x_language: str
        :param instance_id: **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。
        :type instance_id: str
        :param node_id: **参数解释**: 节点ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type node_id: str
        :param component_id: **参数解释**: 组件ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type component_id: str
        :param use_ops_tunnel: **参数解释**: 是否走紧急通道。 **约束限制**: 不涉及。 **取值范围**: - true：走紧急通道 - false：不走紧急通道  **默认取值**: false。
        :type use_ops_tunnel: bool
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._node_id = None
        self._component_id = None
        self._use_ops_tunnel = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        if node_id is not None:
            self.node_id = node_id
        if component_id is not None:
            self.component_id = component_id
        self.use_ops_tunnel = use_ops_tunnel

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowSessionSummaryUseOpsTunnelRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn - en-us  **默认取值**: en-us

        :return: The x_language of this ShowSessionSummaryUseOpsTunnelRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowSessionSummaryUseOpsTunnelRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn - en-us  **默认取值**: en-us

        :param x_language: The x_language of this ShowSessionSummaryUseOpsTunnelRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowSessionSummaryUseOpsTunnelRequest.

        **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。

        :return: The instance_id of this ShowSessionSummaryUseOpsTunnelRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowSessionSummaryUseOpsTunnelRequest.

        **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。

        :param instance_id: The instance_id of this ShowSessionSummaryUseOpsTunnelRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def node_id(self):
        r"""Gets the node_id of this ShowSessionSummaryUseOpsTunnelRequest.

        **参数解释**: 节点ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The node_id of this ShowSessionSummaryUseOpsTunnelRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ShowSessionSummaryUseOpsTunnelRequest.

        **参数解释**: 节点ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param node_id: The node_id of this ShowSessionSummaryUseOpsTunnelRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def component_id(self):
        r"""Gets the component_id of this ShowSessionSummaryUseOpsTunnelRequest.

        **参数解释**: 组件ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The component_id of this ShowSessionSummaryUseOpsTunnelRequest.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        r"""Sets the component_id of this ShowSessionSummaryUseOpsTunnelRequest.

        **参数解释**: 组件ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param component_id: The component_id of this ShowSessionSummaryUseOpsTunnelRequest.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def use_ops_tunnel(self):
        r"""Gets the use_ops_tunnel of this ShowSessionSummaryUseOpsTunnelRequest.

        **参数解释**: 是否走紧急通道。 **约束限制**: 不涉及。 **取值范围**: - true：走紧急通道 - false：不走紧急通道  **默认取值**: false。

        :return: The use_ops_tunnel of this ShowSessionSummaryUseOpsTunnelRequest.
        :rtype: bool
        """
        return self._use_ops_tunnel

    @use_ops_tunnel.setter
    def use_ops_tunnel(self, use_ops_tunnel):
        r"""Sets the use_ops_tunnel of this ShowSessionSummaryUseOpsTunnelRequest.

        **参数解释**: 是否走紧急通道。 **约束限制**: 不涉及。 **取值范围**: - true：走紧急通道 - false：不走紧急通道  **默认取值**: false。

        :param use_ops_tunnel: The use_ops_tunnel of this ShowSessionSummaryUseOpsTunnelRequest.
        :type use_ops_tunnel: bool
        """
        self._use_ops_tunnel = use_ops_tunnel

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
        if not isinstance(other, ShowSessionSummaryUseOpsTunnelRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
