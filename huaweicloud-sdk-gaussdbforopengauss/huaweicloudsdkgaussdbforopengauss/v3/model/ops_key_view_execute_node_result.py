# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsKeyViewExecuteNodeResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'node_name': 'str',
        'role': 'str',
        'type': 'str',
        'distributed_id': 'str',
        'component_id': 'str',
        'detail': 'str'
    }

    attribute_map = {
        'node_id': 'node_id',
        'node_name': 'node_name',
        'role': 'role',
        'type': 'type',
        'distributed_id': 'distributed_id',
        'component_id': 'component_id',
        'detail': 'detail'
    }

    def __init__(self, node_id=None, node_name=None, role=None, type=None, distributed_id=None, component_id=None, detail=None):
        r"""OpsKeyViewExecuteNodeResult

        The model defined in huaweicloud sdk

        :param node_id: **参数解释**: 节点ID。 **取值范围**: 不涉及。
        :type node_id: str
        :param node_name: **参数解释**: 节点名称。 **取值范围**: 不涉及。
        :type node_name: str
        :param role: **参数解释**: 节点角色。 **取值范围**: - master：主节点。 - slave：备节点。 - secondary：日志节点。 - readreplica：只读节点。
        :type role: str
        :param type: **参数解释**: 节点类型。 **取值范围**: - CN：CN组件。 - DN：DN组件。
        :type type: str
        :param distributed_id: **参数解释**: 分布ID。 **取值范围**: 不涉及。
        :type distributed_id: str
        :param component_id: **参数解释**: 组件ID。 **取值范围**: 不涉及。
        :type component_id: str
        :param detail: **参数解释**: 描述信息。 **取值范围**: 不涉及。
        :type detail: str
        """
        
        

        self._node_id = None
        self._node_name = None
        self._role = None
        self._type = None
        self._distributed_id = None
        self._component_id = None
        self._detail = None
        self.discriminator = None

        if node_id is not None:
            self.node_id = node_id
        if node_name is not None:
            self.node_name = node_name
        if role is not None:
            self.role = role
        if type is not None:
            self.type = type
        if distributed_id is not None:
            self.distributed_id = distributed_id
        if component_id is not None:
            self.component_id = component_id
        if detail is not None:
            self.detail = detail

    @property
    def node_id(self):
        r"""Gets the node_id of this OpsKeyViewExecuteNodeResult.

        **参数解释**: 节点ID。 **取值范围**: 不涉及。

        :return: The node_id of this OpsKeyViewExecuteNodeResult.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this OpsKeyViewExecuteNodeResult.

        **参数解释**: 节点ID。 **取值范围**: 不涉及。

        :param node_id: The node_id of this OpsKeyViewExecuteNodeResult.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def node_name(self):
        r"""Gets the node_name of this OpsKeyViewExecuteNodeResult.

        **参数解释**: 节点名称。 **取值范围**: 不涉及。

        :return: The node_name of this OpsKeyViewExecuteNodeResult.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this OpsKeyViewExecuteNodeResult.

        **参数解释**: 节点名称。 **取值范围**: 不涉及。

        :param node_name: The node_name of this OpsKeyViewExecuteNodeResult.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def role(self):
        r"""Gets the role of this OpsKeyViewExecuteNodeResult.

        **参数解释**: 节点角色。 **取值范围**: - master：主节点。 - slave：备节点。 - secondary：日志节点。 - readreplica：只读节点。

        :return: The role of this OpsKeyViewExecuteNodeResult.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this OpsKeyViewExecuteNodeResult.

        **参数解释**: 节点角色。 **取值范围**: - master：主节点。 - slave：备节点。 - secondary：日志节点。 - readreplica：只读节点。

        :param role: The role of this OpsKeyViewExecuteNodeResult.
        :type role: str
        """
        self._role = role

    @property
    def type(self):
        r"""Gets the type of this OpsKeyViewExecuteNodeResult.

        **参数解释**: 节点类型。 **取值范围**: - CN：CN组件。 - DN：DN组件。

        :return: The type of this OpsKeyViewExecuteNodeResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this OpsKeyViewExecuteNodeResult.

        **参数解释**: 节点类型。 **取值范围**: - CN：CN组件。 - DN：DN组件。

        :param type: The type of this OpsKeyViewExecuteNodeResult.
        :type type: str
        """
        self._type = type

    @property
    def distributed_id(self):
        r"""Gets the distributed_id of this OpsKeyViewExecuteNodeResult.

        **参数解释**: 分布ID。 **取值范围**: 不涉及。

        :return: The distributed_id of this OpsKeyViewExecuteNodeResult.
        :rtype: str
        """
        return self._distributed_id

    @distributed_id.setter
    def distributed_id(self, distributed_id):
        r"""Sets the distributed_id of this OpsKeyViewExecuteNodeResult.

        **参数解释**: 分布ID。 **取值范围**: 不涉及。

        :param distributed_id: The distributed_id of this OpsKeyViewExecuteNodeResult.
        :type distributed_id: str
        """
        self._distributed_id = distributed_id

    @property
    def component_id(self):
        r"""Gets the component_id of this OpsKeyViewExecuteNodeResult.

        **参数解释**: 组件ID。 **取值范围**: 不涉及。

        :return: The component_id of this OpsKeyViewExecuteNodeResult.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        r"""Sets the component_id of this OpsKeyViewExecuteNodeResult.

        **参数解释**: 组件ID。 **取值范围**: 不涉及。

        :param component_id: The component_id of this OpsKeyViewExecuteNodeResult.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def detail(self):
        r"""Gets the detail of this OpsKeyViewExecuteNodeResult.

        **参数解释**: 描述信息。 **取值范围**: 不涉及。

        :return: The detail of this OpsKeyViewExecuteNodeResult.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        r"""Sets the detail of this OpsKeyViewExecuteNodeResult.

        **参数解释**: 描述信息。 **取值范围**: 不涉及。

        :param detail: The detail of this OpsKeyViewExecuteNodeResult.
        :type detail: str
        """
        self._detail = detail

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
        if not isinstance(other, OpsKeyViewExecuteNodeResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
