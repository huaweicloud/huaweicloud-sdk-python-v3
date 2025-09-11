# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExcuteSQLNodeInfoResult:

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
        'instance_id': 'str',
        'component_type': 'str'
    }

    attribute_map = {
        'node_id': 'node_id',
        'node_name': 'node_name',
        'role': 'role',
        'instance_id': 'instance_id',
        'component_type': 'component_type'
    }

    def __init__(self, node_id=None, node_name=None, role=None, instance_id=None, component_type=None):
        r"""ExcuteSQLNodeInfoResult

        The model defined in huaweicloud sdk

        :param node_id: **参数解释**: 节点ID。 **取值范围**: 不涉及。
        :type node_id: str
        :param node_name: **参数解释**: 节点名称。 **取值范围**: 不涉及。
        :type node_name: str
        :param role: **参数描述**: 节点角色。 **取值范围**: - master：主节点。 - slave：备节点。 - secondary：日志节点。 - readreplica：只读节点。 
        :type role: str
        :param instance_id: **参数解释**: 实例ID。 **取值范围**: 不涉及。
        :type instance_id: str
        :param component_type: **参数描述**: 组件类型。 **取值范围**: - CN：CN组件。 - DN：DN组件。 
        :type component_type: str
        """
        
        

        self._node_id = None
        self._node_name = None
        self._role = None
        self._instance_id = None
        self._component_type = None
        self.discriminator = None

        if node_id is not None:
            self.node_id = node_id
        if node_name is not None:
            self.node_name = node_name
        if role is not None:
            self.role = role
        if instance_id is not None:
            self.instance_id = instance_id
        if component_type is not None:
            self.component_type = component_type

    @property
    def node_id(self):
        r"""Gets the node_id of this ExcuteSQLNodeInfoResult.

        **参数解释**: 节点ID。 **取值范围**: 不涉及。

        :return: The node_id of this ExcuteSQLNodeInfoResult.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ExcuteSQLNodeInfoResult.

        **参数解释**: 节点ID。 **取值范围**: 不涉及。

        :param node_id: The node_id of this ExcuteSQLNodeInfoResult.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def node_name(self):
        r"""Gets the node_name of this ExcuteSQLNodeInfoResult.

        **参数解释**: 节点名称。 **取值范围**: 不涉及。

        :return: The node_name of this ExcuteSQLNodeInfoResult.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this ExcuteSQLNodeInfoResult.

        **参数解释**: 节点名称。 **取值范围**: 不涉及。

        :param node_name: The node_name of this ExcuteSQLNodeInfoResult.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def role(self):
        r"""Gets the role of this ExcuteSQLNodeInfoResult.

        **参数描述**: 节点角色。 **取值范围**: - master：主节点。 - slave：备节点。 - secondary：日志节点。 - readreplica：只读节点。 

        :return: The role of this ExcuteSQLNodeInfoResult.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this ExcuteSQLNodeInfoResult.

        **参数描述**: 节点角色。 **取值范围**: - master：主节点。 - slave：备节点。 - secondary：日志节点。 - readreplica：只读节点。 

        :param role: The role of this ExcuteSQLNodeInfoResult.
        :type role: str
        """
        self._role = role

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ExcuteSQLNodeInfoResult.

        **参数解释**: 实例ID。 **取值范围**: 不涉及。

        :return: The instance_id of this ExcuteSQLNodeInfoResult.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ExcuteSQLNodeInfoResult.

        **参数解释**: 实例ID。 **取值范围**: 不涉及。

        :param instance_id: The instance_id of this ExcuteSQLNodeInfoResult.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def component_type(self):
        r"""Gets the component_type of this ExcuteSQLNodeInfoResult.

        **参数描述**: 组件类型。 **取值范围**: - CN：CN组件。 - DN：DN组件。 

        :return: The component_type of this ExcuteSQLNodeInfoResult.
        :rtype: str
        """
        return self._component_type

    @component_type.setter
    def component_type(self, component_type):
        r"""Sets the component_type of this ExcuteSQLNodeInfoResult.

        **参数描述**: 组件类型。 **取值范围**: - CN：CN组件。 - DN：DN组件。 

        :param component_type: The component_type of this ExcuteSQLNodeInfoResult.
        :type component_type: str
        """
        self._component_type = component_type

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
        if not isinstance(other, ExcuteSQLNodeInfoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
