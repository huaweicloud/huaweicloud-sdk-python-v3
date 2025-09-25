# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BaseOpsKeyViewRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'node_id': 'str',
        'component_id': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'node_id': 'node_id',
        'component_id': 'component_id'
    }

    def __init__(self, instance_id=None, node_id=None, component_id=None):
        r"""BaseOpsKeyViewRequestBody

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type instance_id: str
        :param node_id: **参数解释**： 节点ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type node_id: str
        :param component_id: **参数解释**： 组件ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type component_id: str
        """
        
        

        self._instance_id = None
        self._node_id = None
        self._component_id = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        self.node_id = node_id
        self.component_id = component_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this BaseOpsKeyViewRequestBody.

        **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The instance_id of this BaseOpsKeyViewRequestBody.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this BaseOpsKeyViewRequestBody.

        **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param instance_id: The instance_id of this BaseOpsKeyViewRequestBody.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def node_id(self):
        r"""Gets the node_id of this BaseOpsKeyViewRequestBody.

        **参数解释**： 节点ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The node_id of this BaseOpsKeyViewRequestBody.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this BaseOpsKeyViewRequestBody.

        **参数解释**： 节点ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param node_id: The node_id of this BaseOpsKeyViewRequestBody.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def component_id(self):
        r"""Gets the component_id of this BaseOpsKeyViewRequestBody.

        **参数解释**： 组件ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The component_id of this BaseOpsKeyViewRequestBody.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        r"""Sets the component_id of this BaseOpsKeyViewRequestBody.

        **参数解释**： 组件ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param component_id: The component_id of this BaseOpsKeyViewRequestBody.
        :type component_id: str
        """
        self._component_id = component_id

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
        if not isinstance(other, BaseOpsKeyViewRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
